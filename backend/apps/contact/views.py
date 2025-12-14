"""
Contact views for API.
"""
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Inquiry, Newsletter, FAQ, Office
from .serializers import (
    InquirySerializer, NewsletterSerializer, FAQSerializer, OfficeSerializer
)


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
    """Subscribe to newsletter."""
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'Thank you for subscribing to our newsletter!'
        }, status=status.HTTP_201_CREATED)


class NewsletterUnsubscribeView(APIView):
    """Unsubscribe from newsletter."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            newsletter = Newsletter.objects.get(email=email)
            newsletter.is_active = False
            newsletter.unsubscribed_at = timezone.now()
            newsletter.save()
            return Response({'message': 'You have been unsubscribed successfully'})
        except Newsletter.DoesNotExist:
            return Response(
                {'error': 'Email not found'},
                status=status.HTTP_404_NOT_FOUND
            )


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
