"""
Review models for Girasol Tours.
"""
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.core.models import TimeStampedModel


class Review(TimeStampedModel):
    """Customer review for tours."""

    # Relations
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='reviews'
    )
    tour = models.ForeignKey(
        'tours.Tour', on_delete=models.CASCADE, related_name='reviews'
    )

    # Reviewer info (for display or non-logged users)
    reviewer_name = models.CharField(max_length=100)
    reviewer_country = models.CharField(max_length=100, blank=True)
    reviewer_avatar = models.ImageField(
        upload_to='reviews/avatars/', null=True, blank=True
    )

    # Rating
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # Content
    title = models.CharField(max_length=200, blank=True)
    title_es = models.CharField('Title (Spanish)', max_length=200, blank=True)
    title_pt = models.CharField('Title (Portuguese)', max_length=200, blank=True)
    content = models.TextField()
    content_es = models.TextField('Content (Spanish)', blank=True)
    content_pt = models.TextField('Content (Portuguese)', blank=True)

    # Travel date
    travel_date = models.DateField(null=True, blank=True)

    # Status
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    # Admin response
    admin_response = models.TextField(blank=True)
    admin_response_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.reviewer_name} - {self.tour.name} ({self.rating}★)"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update tour's average rating
        self.update_tour_rating()

    def update_tour_rating(self):
        from django.db.models import Avg
        tour = self.tour
        reviews = tour.reviews.filter(is_approved=True)
        avg = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        tour.average_rating = round(avg, 1)
        tour.review_count = reviews.count()
        tour.save(update_fields=['average_rating', 'review_count'])


class ReviewImage(TimeStampedModel):
    """Images attached to reviews."""

    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='reviews/images/')
    caption = models.CharField(max_length=200, blank=True)
    caption_es = models.CharField('Caption (Spanish)', max_length=200, blank=True)
    caption_pt = models.CharField('Caption (Portuguese)', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Review Image'
        verbose_name_plural = 'Review Images'

    def __str__(self):
        return f"Image for review {self.review.id}"


class Testimonial(TimeStampedModel):
    """Featured testimonials for homepage/marketing."""

    # Customer info
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    # Content
    quote = models.TextField()
    quote_es = models.TextField('Quote (Spanish)', blank=True)
    quote_pt = models.TextField('Quote (Portuguese)', blank=True)
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # Related tour (optional)
    tour = models.ForeignKey(
        'tours.Tour', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='testimonials'
    )

    # Display settings
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['sort_order', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.country}"
