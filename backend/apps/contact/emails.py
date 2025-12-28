"""
Email sending utilities for Newsletter and Contact.
"""
import logging
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

logger = logging.getLogger(__name__)


def get_frontend_url():
    """Get the frontend URL from settings."""
    return getattr(settings, 'FRONTEND_URL', 'https://girasoltours.com')


def send_confirmation_email(subscriber):
    """
    Send confirmation email to new subscriber.

    Args:
        subscriber: Newsletter model instance

    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        frontend_url = get_frontend_url()
        confirm_url = f"{frontend_url}/newsletter/confirm/{subscriber.confirmation_token}"

        context = {
            'email': subscriber.email,
            'name': subscriber.name or 'there',
            'confirm_url': confirm_url,
            'company_name': 'Girasol Tours',
            'company_email': settings.DEFAULT_FROM_EMAIL,
        }

        subject = 'Confirm Your Subscription - Girasol Tours'

        # Render HTML template
        html_message = render_to_string('emails/newsletter_confirm.html', context)
        plain_message = strip_tags(html_message)

        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscriber.email],
            html_message=html_message,
            fail_silently=False,
        )

        logger.info(f"Confirmation email sent to {subscriber.email}")
        return True

    except Exception as e:
        logger.error(f"Failed to send confirmation email to {subscriber.email}: {str(e)}")
        return False


def send_welcome_email(subscriber):
    """
    Send welcome email after subscription is confirmed.

    Args:
        subscriber: Newsletter model instance

    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        frontend_url = get_frontend_url()
        unsubscribe_url = f"{frontend_url}/newsletter/unsubscribe/{subscriber.unsubscribe_token}"

        context = {
            'email': subscriber.email,
            'name': subscriber.name or 'there',
            'unsubscribe_url': unsubscribe_url,
            'website_url': frontend_url,
            'tours_url': f"{frontend_url}/tours",
            'company_name': 'Girasol Tours',
        }

        subject = 'Welcome to Girasol Tours Newsletter!'

        # Render HTML template
        html_message = render_to_string('emails/newsletter_welcome.html', context)
        plain_message = strip_tags(html_message)

        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscriber.email],
            html_message=html_message,
            fail_silently=False,
        )

        logger.info(f"Welcome email sent to {subscriber.email}")
        return True

    except Exception as e:
        logger.error(f"Failed to send welcome email to {subscriber.email}: {str(e)}")
        return False


def send_unsubscribe_confirmation_email(subscriber):
    """
    Send confirmation email after unsubscription.

    Args:
        subscriber: Newsletter model instance

    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        frontend_url = get_frontend_url()
        resubscribe_url = f"{frontend_url}/newsletter"

        context = {
            'email': subscriber.email,
            'name': subscriber.name or 'there',
            'resubscribe_url': resubscribe_url,
            'company_name': 'Girasol Tours',
        }

        subject = "You've been unsubscribed - Girasol Tours"

        # Render HTML template
        html_message = render_to_string('emails/newsletter_unsubscribe.html', context)
        plain_message = strip_tags(html_message)

        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscriber.email],
            html_message=html_message,
            fail_silently=False,
        )

        logger.info(f"Unsubscribe confirmation email sent to {subscriber.email}")
        return True

    except Exception as e:
        logger.error(f"Failed to send unsubscribe email to {subscriber.email}: {str(e)}")
        return False


def send_newsletter_campaign(subject, html_content, subscribers_queryset):
    """
    Send newsletter campaign to multiple subscribers.

    Args:
        subject: Email subject
        html_content: HTML content of the newsletter
        subscribers_queryset: QuerySet of Newsletter subscribers

    Returns:
        dict: Statistics about sent emails
    """
    stats = {
        'total': subscribers_queryset.count(),
        'sent': 0,
        'failed': 0,
        'emails': []
    }

    frontend_url = get_frontend_url()

    for subscriber in subscribers_queryset.filter(is_active=True, is_confirmed=True):
        try:
            # Add unsubscribe link to each email
            unsubscribe_url = f"{frontend_url}/newsletter/unsubscribe/{subscriber.unsubscribe_token}"
            personalized_content = html_content.replace(
                '{{unsubscribe_url}}',
                unsubscribe_url
            )

            plain_message = strip_tags(personalized_content)

            send_mail(
                subject=subject,
                message=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                html_message=personalized_content,
                fail_silently=False,
            )

            # Update subscriber stats
            from django.utils import timezone
            subscriber.emails_sent += 1
            subscriber.last_email_sent_at = timezone.now()
            subscriber.save(update_fields=['emails_sent', 'last_email_sent_at'])

            stats['sent'] += 1
            stats['emails'].append({'email': subscriber.email, 'status': 'sent'})
            logger.info(f"Newsletter sent to {subscriber.email}")

        except Exception as e:
            stats['failed'] += 1
            stats['emails'].append({'email': subscriber.email, 'status': 'failed', 'error': str(e)})
            logger.error(f"Failed to send newsletter to {subscriber.email}: {str(e)}")

    logger.info(f"Newsletter campaign completed: {stats['sent']} sent, {stats['failed']} failed")
    return stats
