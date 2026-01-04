"""
Contact models for Girasol Tours.
"""
import uuid
import logging
from django.db import models
from apps.core.models import TimeStampedModel

logger = logging.getLogger(__name__)


class InquiryType(models.TextChoices):
    GENERAL = 'general', 'General Inquiry'
    TOUR = 'tour', 'Tour Inquiry'
    BOOKING = 'booking', 'Booking Question'
    CUSTOM = 'custom', 'Custom Trip Request'
    COMPLAINT = 'complaint', 'Complaint'
    PARTNERSHIP = 'partnership', 'Partnership'
    OTHER = 'other', 'Other'


class InquiryStatus(models.TextChoices):
    NEW = 'new', 'New'
    IN_PROGRESS = 'in_progress', 'In Progress'
    RESPONDED = 'responded', 'Responded'
    CLOSED = 'closed', 'Closed'


class Inquiry(TimeStampedModel):
    """Contact form submissions and inquiries."""

    # Contact info
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    # Inquiry details
    inquiry_type = models.CharField(
        max_length=20, choices=InquiryType.choices, default=InquiryType.GENERAL
    )
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()

    # Related tour (optional)
    tour = models.ForeignKey(
        'tours.Tour', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='inquiries'
    )

    # Travel preferences
    travel_date = models.DateField(null=True, blank=True)
    travelers = models.PositiveIntegerField(null=True, blank=True)
    budget = models.CharField(max_length=50, blank=True)

    # Status
    status = models.CharField(
        max_length=20, choices=InquiryStatus.choices, default=InquiryStatus.NEW
    )

    # Admin handling
    assigned_to = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='assigned_inquiries'
    )
    internal_notes = models.TextField(blank=True)

    # Source tracking
    source = models.CharField(max_length=50, blank=True)  # e.g., website, whatsapp, email
    utm_source = models.CharField(max_length=100, blank=True)
    utm_medium = models.CharField(max_length=100, blank=True)
    utm_campaign = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.inquiry_type} ({self.created_at.date()})"


class InquiryResponse(TimeStampedModel):
    """Responses to inquiries."""

    inquiry = models.ForeignKey(
        Inquiry, on_delete=models.CASCADE, related_name='responses'
    )
    responder = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True
    )
    message = models.TextField()
    is_internal = models.BooleanField(default=False)  # Internal note vs actual response

    class Meta:
        verbose_name = 'Inquiry Response'
        verbose_name_plural = 'Inquiry Responses'
        ordering = ['created_at']

    def __str__(self):
        return f"Response to {self.inquiry.name}"


class Newsletter(TimeStampedModel):
    """Newsletter subscribers with double opt-in support."""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    # Double Opt-In fields
    confirmation_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    confirmation_sent_at = models.DateTimeField(null=True, blank=True)

    # Unsubscribe token (for one-click unsubscribe in emails)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    # Preferences
    interests = models.CharField(max_length=200, blank=True)  # Comma-separated

    # Source
    source = models.CharField(max_length=50, blank=True)

    # Email tracking
    emails_sent = models.PositiveIntegerField(default=0)
    last_email_sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
        ordering = ['-subscribed_at']

    def __str__(self):
        status = "Confirmed" if self.is_confirmed else "Pending"
        return f"{self.email} ({status})"

    def regenerate_tokens(self):
        """Regenerate confirmation and unsubscribe tokens."""
        self.confirmation_token = uuid.uuid4()
        self.unsubscribe_token = uuid.uuid4()
        self.save(update_fields=['confirmation_token', 'unsubscribe_token'])
        logger.info(f"Tokens regenerated for {self.email}")


class NewsletterCampaign(TimeStampedModel):
    """Newsletter campaigns to send to subscribers."""

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('sending', 'Sending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]

    title = models.CharField(max_length=200, help_text="Internal title for this campaign")
    subject = models.CharField(max_length=200, help_text="Email subject line")
    preview_text = models.CharField(max_length=200, blank=True, help_text="Preview text shown in inbox")

    # Content
    content = models.TextField(help_text="Email content (HTML supported)")

    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    # Scheduling
    scheduled_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    # Stats
    recipients_count = models.PositiveIntegerField(default=0)
    sent_count = models.PositiveIntegerField(default=0)
    failed_count = models.PositiveIntegerField(default=0)

    # Created by
    created_by = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='newsletter_campaigns'
    )

    class Meta:
        verbose_name = 'Newsletter Campaign'
        verbose_name_plural = 'Newsletter Campaigns'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.status})"

    def get_active_subscribers(self):
        """Get all active and confirmed subscribers."""
        return Newsletter.objects.filter(is_active=True, is_confirmed=True)


class FAQ(TimeStampedModel):
    """Frequently asked questions."""

    question = models.CharField(max_length=300)
    question_es = models.CharField('Question (Spanish)', max_length=300, blank=True)
    question_pt = models.CharField('Question (Portuguese)', max_length=300, blank=True)
    answer = models.TextField()
    answer_es = models.TextField('Answer (Spanish)', blank=True)
    answer_pt = models.TextField('Answer (Portuguese)', blank=True)

    category = models.CharField(
        max_length=50,
        choices=[
            ('booking', 'Booking & Payments'),
            ('travel', 'Travel & Visa'),
            ('accommodation', 'Accommodations'),
            ('tours', 'Tours & Services'),
            ('general', 'General'),
        ],
        default='general'
    )

    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['category', 'sort_order']

    def __str__(self):
        return self.question[:50]


class Office(TimeStampedModel):
    """Company office locations."""

    name = models.CharField(max_length=100)
    name_es = models.CharField('Name (Spanish)', max_length=100, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=100, blank=True)
    city = models.CharField(max_length=100)
    city_es = models.CharField('City (Spanish)', max_length=100, blank=True)
    city_pt = models.CharField('City (Portuguese)', max_length=100, blank=True)
    address = models.TextField()
    address_es = models.TextField('Address (Spanish)', blank=True)
    address_pt = models.TextField('Address (Portuguese)', blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)

    # Location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Hours
    working_hours = models.CharField(max_length=200, blank=True)
    working_hours_es = models.CharField('Working Hours (Spanish)', max_length=200, blank=True)
    working_hours_pt = models.CharField('Working Hours (Portuguese)', max_length=200, blank=True)

    is_headquarters = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'
        ordering = ['-is_headquarters', 'sort_order']

    def __str__(self):
        return f"{self.name} - {self.city}"


class Statistic(TimeStampedModel):
    """Company statistics for homepage display."""

    ICON_CHOICES = [
        ('clock', 'Clock - Years Experience'),
        ('users', 'Users - Happy Travelers'),
        ('map-pin', 'Map Pin - Local Offices'),
        ('globe', 'Globe - Countries Partners'),
        ('award', 'Award - Awards'),
        ('star', 'Star - Rating'),
        ('heart', 'Heart - Satisfaction'),
        ('shield', 'Shield - Certified'),
    ]

    value = models.CharField(max_length=50, help_text="e.g., 25+, 50,000+, 6")
    label = models.CharField(max_length=100, help_text="e.g., Years Experience")
    label_es = models.CharField('Label (Spanish)', max_length=100, blank=True)
    label_pt = models.CharField('Label (Portuguese)', max_length=100, blank=True)
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='star')
    description = models.CharField(max_length=200, blank=True, help_text="Optional description")
    description_es = models.CharField('Description (Spanish)', max_length=200, blank=True)
    description_pt = models.CharField('Description (Portuguese)', max_length=200, blank=True)

    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistics'
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.value} - {self.label}"
