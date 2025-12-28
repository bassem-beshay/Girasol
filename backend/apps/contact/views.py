"""
Contact views for API.
"""
import logging
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Inquiry, Newsletter, FAQ, Office, Statistic
from .serializers import (
    InquirySerializer, NewsletterSerializer, FAQSerializer, OfficeSerializer, StatisticSerializer
)
from .tasks import send_confirmation_email_task, send_welcome_email_task, send_unsubscribe_confirmation_task

logger = logging.getLogger(__name__)


class NewsletterThrottle(AnonRateThrottle):
    """Custom throttle for newsletter subscription - 5 requests per hour."""
    rate = '5/hour'


class InquiryCreateView(generics.CreateAPIView):
    """Submit a contact inquiry."""
    serializer_class = InquirySerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inquiry = serializer.save()

        # TODO: Send email notification to admin
        # TODO: Send confirmation email to user

        return Response({
            'message': 'Thank you for your inquiry. We will get back to you soon!',
            'inquiry_id': inquiry.id
        }, status=status.HTTP_201_CREATED)


class NewsletterSubscribeView(generics.CreateAPIView):
    """
    Subscribe to newsletter with Double Opt-In.

    Flow:
    1. User submits email
    2. Email saved with is_confirmed=False
    3. Confirmation email sent via Celery
    4. User clicks link to confirm
    """
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [NewsletterThrottle]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', '').lower().strip()

        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if already subscribed and confirmed
        existing = Newsletter.objects.filter(email=email).first()

        if existing:
            if existing.is_confirmed and existing.is_active:
                return Response({
                    'message': 'You are already subscribed to our newsletter!',
                    'status': 'already_subscribed'
                }, status=status.HTTP_200_OK)

            elif existing.is_confirmed and not existing.is_active:
                # Reactivate subscription
                existing.is_active = True
                existing.unsubscribed_at = None
                existing.save(update_fields=['is_active', 'unsubscribed_at'])

                logger.info(f"Newsletter reactivated for {email}")

                return Response({
                    'message': 'Welcome back! Your subscription has been reactivated.',
                    'status': 'reactivated'
                }, status=status.HTTP_200_OK)

            else:
                # Not confirmed yet, resend confirmation
                send_confirmation_email_task.delay(existing.id)

                logger.info(f"Confirmation email resent to {email}")

                return Response({
                    'message': 'Please check your email to confirm your subscription.',
                    'status': 'confirmation_resent'
                }, status=status.HTTP_200_OK)

        # New subscription
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscriber = serializer.save()

        # Send confirmation email via Celery (async)
        send_confirmation_email_task.delay(subscriber.id)

        logger.info(f"New newsletter subscription: {email}")

        return Response({
            'message': 'Please check your email to confirm your subscription.',
            'status': 'pending_confirmation'
        }, status=status.HTTP_201_CREATED)


class NewsletterConfirmView(APIView):
    """
    Confirm newsletter subscription via token.

    GET /api/contact/newsletter/confirm/<token>/
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, token):
        try:
            subscriber = Newsletter.objects.get(confirmation_token=token)

            if subscriber.is_confirmed:
                return Response({
                    'message': 'Your subscription was already confirmed.',
                    'status': 'already_confirmed'
                }, status=status.HTTP_200_OK)

            # Confirm subscription
            subscriber.is_confirmed = True
            subscriber.confirmed_at = timezone.now()
            subscriber.is_active = True
            subscriber.save(update_fields=['is_confirmed', 'confirmed_at', 'is_active'])

            # Send welcome email via Celery
            send_welcome_email_task.delay(subscriber.id)

            logger.info(f"Newsletter confirmed for {subscriber.email}")

            return Response({
                'message': 'Thank you! Your subscription has been confirmed.',
                'status': 'confirmed',
                'email': subscriber.email
            }, status=status.HTTP_200_OK)

        except Newsletter.DoesNotExist:
            logger.warning(f"Invalid confirmation token: {token}")
            return Response(
                {'error': 'Invalid or expired confirmation link.'},
                status=status.HTTP_404_NOT_FOUND
            )


class NewsletterUnsubscribeView(APIView):
    """
    Unsubscribe from newsletter.

    Two methods:
    1. POST with email (legacy)
    2. GET with token (one-click from email)
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, token=None):
        """One-click unsubscribe via token in email."""
        if not token:
            return Response(
                {'error': 'Unsubscribe token is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            subscriber = Newsletter.objects.get(unsubscribe_token=token)

            if not subscriber.is_active:
                return Response({
                    'message': 'You are already unsubscribed.',
                    'status': 'already_unsubscribed'
                }, status=status.HTTP_200_OK)

            subscriber.is_active = False
            subscriber.unsubscribed_at = timezone.now()
            subscriber.save(update_fields=['is_active', 'unsubscribed_at'])

            # Send unsubscribe confirmation email
            send_unsubscribe_confirmation_task.delay(subscriber.id)

            logger.info(f"Newsletter unsubscribed: {subscriber.email}")

            return Response({
                'message': 'You have been successfully unsubscribed.',
                'status': 'unsubscribed',
                'email': subscriber.email
            }, status=status.HTTP_200_OK)

        except Newsletter.DoesNotExist:
            logger.warning(f"Invalid unsubscribe token: {token}")
            return Response(
                {'error': 'Invalid unsubscribe link.'},
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        """Legacy unsubscribe via email address."""
        email = request.data.get('email', '').lower().strip()

        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            subscriber = Newsletter.objects.get(email=email)

            if not subscriber.is_active:
                return Response({
                    'message': 'You are already unsubscribed.',
                    'status': 'already_unsubscribed'
                }, status=status.HTTP_200_OK)

            subscriber.is_active = False
            subscriber.unsubscribed_at = timezone.now()
            subscriber.save(update_fields=['is_active', 'unsubscribed_at'])

            # Send unsubscribe confirmation
            send_unsubscribe_confirmation_task.delay(subscriber.id)

            logger.info(f"Newsletter unsubscribed via email: {email}")

            return Response({
                'message': 'You have been successfully unsubscribed.',
                'status': 'unsubscribed'
            }, status=status.HTTP_200_OK)

        except Newsletter.DoesNotExist:
            return Response(
                {'error': 'Email not found in our newsletter list.'},
                status=status.HTTP_404_NOT_FOUND
            )


class NewsletterStatusView(APIView):
    """Check newsletter subscription status."""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        email = request.query_params.get('email', '').lower().strip()

        if not email:
            return Response(
                {'error': 'Email parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            subscriber = Newsletter.objects.get(email=email)

            return Response({
                'email': subscriber.email,
                'is_subscribed': subscriber.is_active and subscriber.is_confirmed,
                'is_confirmed': subscriber.is_confirmed,
                'is_active': subscriber.is_active,
                'subscribed_at': subscriber.subscribed_at,
            }, status=status.HTTP_200_OK)

        except Newsletter.DoesNotExist:
            return Response({
                'email': email,
                'is_subscribed': False,
                'is_confirmed': False,
                'is_active': False,
            }, status=status.HTTP_200_OK)


class FAQListView(generics.ListAPIView):
    """List all FAQs."""
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = FAQ.objects.filter(is_active=True)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset


class OfficeListView(generics.ListAPIView):
    """List all offices."""
    serializer_class = OfficeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Office.objects.filter(is_active=True)


class StatisticListView(generics.ListAPIView):
    """List all statistics for homepage."""
    serializer_class = StatisticSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Statistic.objects.filter(is_active=True)
