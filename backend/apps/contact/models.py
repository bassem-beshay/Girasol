"""
Contact models for Girasol Tours.
"""
from django.db import models
from apps.core.models import TimeStampedModel


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
    """Newsletter subscribers."""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    # Preferences
    interests = models.CharField(max_length=200, blank=True)  # Comma-separated

    # Source
    source = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email


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
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)

    # Location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Hours
    working_hours = models.CharField(max_length=200, blank=True)

    is_headquarters = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'
        ordering = ['-is_headquarters', 'sort_order']

    def __str__(self):
        return f"{self.name} - {self.city}"
