"""
Destination models for Girasol Tours.
"""
from django.db import models
from apps.core.models import TimeStampedModel, SluggedModel, SEOModel, SortableModel


class Destination(TimeStampedModel, SluggedModel, SEOModel, SortableModel):
    """Travel destination (city/region)."""

    name = models.CharField(max_length=100)
    name_es = models.CharField('Name (Spanish)', max_length=100, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=100, blank=True)
    tagline = models.CharField(max_length=200, blank=True)
    tagline_es = models.CharField('Tagline (Spanish)', max_length=200, blank=True)
    tagline_pt = models.CharField('Tagline (Portuguese)', max_length=200, blank=True)
    description = models.TextField()
    description_es = models.TextField('Description (Spanish)', blank=True)
    description_pt = models.TextField('Description (Portuguese)', blank=True)

    # Media
    featured_image = models.ImageField(upload_to='destinations/')
    banner_image = models.ImageField(upload_to='destinations/banners/', null=True, blank=True)
    video_url = models.URLField(blank=True)

    # Location
    country = models.CharField(max_length=100, default='Egypt')
    region = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Info
    best_time_to_visit = models.TextField(blank=True)
    getting_there = models.TextField(blank=True)
    climate_info = models.TextField(blank=True)

    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name

    def get_slug_source(self):
        return self.name

    @property
    def tour_count(self):
        return self.tours.filter(is_published=True).count()


class DestinationImage(TimeStampedModel, SortableModel):
    """Gallery images for destinations."""

    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='destinations/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Destination Image'
        verbose_name_plural = 'Destination Images'
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.destination.name} - Image {self.pk}"


class Activity(TimeStampedModel, SortableModel):
    """Activities available in a destination."""

    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name='activities'
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/activities/', null=True, blank=True)
    price_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=50, blank=True, help_text='e.g., 2 hours, Full day')

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.name} - {self.destination.name}"
