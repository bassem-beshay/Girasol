"""
Celery tasks for Newsletter and Contact emails.
"""
import logging
from celery import shared_task
from django.utils import timezone

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_confirmation_email_task(self, subscriber_id):
    """
    Async task to send confirmation email.

    Args:
        subscriber_id: ID of the Newsletter subscriber

    Returns:
        dict: Result of the operation
    """
    from .models import Newsletter
    from .emails import send_confirmation_email

    try:
        subscriber = Newsletter.objects.get(id=subscriber_id)

        if subscriber.is_confirmed:
            logger.info(f"Subscriber {subscriber.email} already confirmed, skipping")
            return {'status': 'skipped', 'reason': 'already_confirmed'}

        success = send_confirmation_email(subscriber)

        if success:
            subscriber.confirmation_sent_at = timezone.now()
            subscriber.save(update_fields=['confirmation_sent_at'])
            return {'status': 'success', 'email': subscriber.email}
        else:
            raise Exception("Email sending failed")

    except Newsletter.DoesNotExist:
        logger.error(f"Subscriber with id {subscriber_id} not found")
        return {'status': 'error', 'reason': 'subscriber_not_found'}

    except Exception as e:
        logger.error(f"Error sending confirmation email: {str(e)}")
        # Retry the task
        try:
            self.retry(exc=e)
        except self.MaxRetriesExceededError:
            logger.error(f"Max retries exceeded for subscriber {subscriber_id}")
            return {'status': 'error', 'reason': 'max_retries_exceeded'}


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_welcome_email_task(self, subscriber_id):
    """
    Async task to send welcome email after confirmation.

    Args:
        subscriber_id: ID of the Newsletter subscriber

    Returns:
        dict: Result of the operation
    """
    from .models import Newsletter
    from .emails import send_welcome_email

    try:
        subscriber = Newsletter.objects.get(id=subscriber_id)

        if not subscriber.is_confirmed:
            logger.warning(f"Subscriber {subscriber.email} not confirmed, skipping welcome email")
            return {'status': 'skipped', 'reason': 'not_confirmed'}

        success = send_welcome_email(subscriber)

        if success:
            return {'status': 'success', 'email': subscriber.email}
        else:
            raise Exception("Email sending failed")

    except Newsletter.DoesNotExist:
        logger.error(f"Subscriber with id {subscriber_id} not found")
        return {'status': 'error', 'reason': 'subscriber_not_found'}

    except Exception as e:
        logger.error(f"Error sending welcome email: {str(e)}")
        try:
            self.retry(exc=e)
        except self.MaxRetriesExceededError:
            logger.error(f"Max retries exceeded for welcome email to subscriber {subscriber_id}")
            return {'status': 'error', 'reason': 'max_retries_exceeded'}


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_unsubscribe_confirmation_task(self, subscriber_id):
    """
    Async task to send unsubscribe confirmation email.

    Args:
        subscriber_id: ID of the Newsletter subscriber

    Returns:
        dict: Result of the operation
    """
    from .models import Newsletter
    from .emails import send_unsubscribe_confirmation_email

    try:
        subscriber = Newsletter.objects.get(id=subscriber_id)

        success = send_unsubscribe_confirmation_email(subscriber)

        if success:
            return {'status': 'success', 'email': subscriber.email}
        else:
            raise Exception("Email sending failed")

    except Newsletter.DoesNotExist:
        logger.error(f"Subscriber with id {subscriber_id} not found")
        return {'status': 'error', 'reason': 'subscriber_not_found'}

    except Exception as e:
        logger.error(f"Error sending unsubscribe email: {str(e)}")
        try:
            self.retry(exc=e)
        except self.MaxRetriesExceededError:
            logger.error(f"Max retries exceeded for unsubscribe email to subscriber {subscriber_id}")
            return {'status': 'error', 'reason': 'max_retries_exceeded'}


@shared_task
def send_newsletter_campaign_task(subject, html_content):
    """
    Async task to send newsletter campaign to all active subscribers.

    Args:
        subject: Email subject
        html_content: HTML content of the newsletter

    Returns:
        dict: Statistics about sent emails
    """
    from .models import Newsletter
    from .emails import send_newsletter_campaign

    subscribers = Newsletter.objects.filter(is_active=True, is_confirmed=True)
    stats = send_newsletter_campaign(subject, html_content, subscribers)

    logger.info(f"Newsletter campaign task completed: {stats}")
    return stats


@shared_task
def cleanup_unconfirmed_subscribers(days=7):
    """
    Clean up subscribers who haven't confirmed after X days.

    Args:
        days: Number of days after which to delete unconfirmed subscribers

    Returns:
        dict: Number of deleted subscribers
    """
    from .models import Newsletter
    from datetime import timedelta

    cutoff_date = timezone.now() - timedelta(days=days)

    # Get unconfirmed subscribers older than cutoff
    unconfirmed = Newsletter.objects.filter(
        is_confirmed=False,
        created_at__lt=cutoff_date
    )

    count = unconfirmed.count()
    emails = list(unconfirmed.values_list('email', flat=True))

    unconfirmed.delete()

    logger.info(f"Cleaned up {count} unconfirmed subscribers: {emails}")

    return {
        'deleted_count': count,
        'emails': emails
    }


@shared_task
def resend_confirmation_to_pending(hours=24):
    """
    Resend confirmation email to subscribers who haven't confirmed.

    Args:
        hours: Only resend to those who subscribed more than X hours ago

    Returns:
        dict: Statistics
    """
    from .models import Newsletter
    from datetime import timedelta

    cutoff_time = timezone.now() - timedelta(hours=hours)

    # Get pending subscribers
    pending = Newsletter.objects.filter(
        is_confirmed=False,
        confirmation_sent_at__lt=cutoff_time,
        is_active=True
    )

    resent = 0
    for subscriber in pending:
        send_confirmation_email_task.delay(subscriber.id)
        resent += 1

    logger.info(f"Queued {resent} confirmation email resends")

    return {'resent': resent}
