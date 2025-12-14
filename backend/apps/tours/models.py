"""
Tour models for Girasol Tours.
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.core.models import TimeStampedModel, SluggedModel, SEOModel, SortableModel, PublishableModel


class TourCategory(TimeStampedModel, SluggedModel, SortableModel):
    """Category for tours (Cultural, Adventure, Beach, etc.)."""

    name = models.CharField(max_length=100)
    name_es = models.CharField('Name (Spanish)', max_length=100, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=100, blank=True)
    description = models.TextField(blank=True)
    description_es = models.TextField('Description (Spanish)', blank=True)
    description_pt = models.TextField('Description (Portuguese)', blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Icon class name')
    image = models.ImageField(upload_to='tours/categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tour Category'
        verbose_name_plural = 'Tour Categories'
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name

    def get_slug_source(self):
        return self.name


class TourType(TimeStampedModel, SluggedModel, SortableModel):
    """Types of tours (Package, Day Tour, Nile Cruise, etc.)."""

    name = models.CharField(max_length=100)
    name_es = models.CharField('Name (Spanish)', max_length=100, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=100, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Icon class name')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tour Type'
        verbose_name_plural = 'Tour Types'
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name

    def get_slug_source(self):
        return self.name


class Tour(TimeStampedModel, SluggedModel, SEOModel, PublishableModel):
    """Main tour/package model."""

    # Basic info
    name = models.CharField(max_length=200)
    name_es = models.CharField('Name (Spanish)', max_length=200, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=200, blank=True)
    short_description = models.CharField(max_length=300)
    short_description_es = models.CharField('Short Description (Spanish)', max_length=300, blank=True)
    short_description_pt = models.CharField('Short Description (Portuguese)', max_length=300, blank=True)
    description = models.TextField()
    description_es = models.TextField('Description (Spanish)', blank=True)
    description_pt = models.TextField('Description (Portuguese)', blank=True)

    # Classification
    category = models.ForeignKey(
        TourCategory, on_delete=models.SET_NULL, null=True, related_name='tours'
    )
    tour_type = models.ForeignKey(
        TourType, on_delete=models.SET_NULL, null=True, related_name='tours'
    )
    destinations = models.ManyToManyField(
        'destinations.Destination', related_name='tours'
    )

    # Duration
    days = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    nights = models.PositiveIntegerField(default=0)

    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_single_supplement = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    child_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD')

    # Group info
    min_group_size = models.PositiveIntegerField(default=1)
    max_group_size = models.PositiveIntegerField(default=20)

    # Media
    featured_image = models.ImageField(upload_to='tours/')
    video_url = models.URLField(blank=True)

    # Features
    is_featured = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    has_discount = models.BooleanField(default=False)
    discount_percentage = models.PositiveIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    discount_start_date = models.DateTimeField(
        'Discount Start Date', null=True, blank=True,
        help_text='When the discount offer starts'
    )
    discount_end_date = models.DateTimeField(
        'Discount End Date', null=True, blank=True,
        help_text='When the discount offer ends'
    )

    # Rating
    average_rating = models.DecimalField(
        max_digits=2, decimal_places=1, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    review_count = models.PositiveIntegerField(default=0)

    # Difficulty/Physical
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('easy', 'Easy'),
            ('moderate', 'Moderate'),
            ('challenging', 'Challenging'),
        ],
        default='easy'
    )

    # Additional
    departure_city = models.CharField(max_length=100, default='Cairo')
    languages = models.CharField(max_length=200, default='English', help_text='Comma-separated languages')

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.name

    def get_slug_source(self):
        return self.name

    @property
    def duration_display(self):
        if self.nights:
            return f"{self.days}D/{self.nights}N"
        return f"{self.days} Days"

    @property
    def discounted_price(self):
        if self.has_discount and self.discount_percentage:
            return self.price * (100 - self.discount_percentage) / 100
        return self.price


class TourImage(TimeStampedModel, SortableModel):
    """Gallery images for tours."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tours/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Tour Image'
        verbose_name_plural = 'Tour Images'
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.tour.name} - Image {self.pk}"


class TourHighlight(TimeStampedModel, SortableModel):
    """Key highlights of a tour."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='highlights')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Tour Highlight'
        verbose_name_plural = 'Tour Highlights'
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.tour.name} - {self.title}"


class TourItinerary(TimeStampedModel, SortableModel):
    """Day-by-day itinerary for a tour."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='itinerary')
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    locations = models.CharField(max_length=300, blank=True)
    meals_included = models.CharField(
        max_length=50, blank=True,
        help_text='e.g., Breakfast, Lunch, Dinner'
    )
    accommodation = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='tours/itinerary/', null=True, blank=True)

    class Meta:
        verbose_name = 'Tour Itinerary'
        verbose_name_plural = 'Tour Itineraries'
        ordering = ['day_number']

    def __str__(self):
        return f"{self.tour.name} - Day {self.day_number}"


class TourInclusion(TimeStampedModel, SortableModel):
    """What's included in the tour."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='inclusions')
    item = models.CharField(max_length=200)
    is_included = models.BooleanField(default=True)  # True = Included, False = Excluded

    class Meta:
        verbose_name = 'Tour Inclusion'
        verbose_name_plural = 'Tour Inclusions'
        ordering = ['-is_included', 'sort_order']

    def __str__(self):
        status = "Included" if self.is_included else "Excluded"
        return f"{self.tour.name} - {self.item} ({status})"


class TourPricing(TimeStampedModel):
    """Seasonal pricing for tours."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='seasonal_pricing')
    season_name = models.CharField(max_length=50)  # e.g., Low Season, High Season
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    single_supplement = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Tour Pricing'
        verbose_name_plural = 'Tour Pricing'
        ordering = ['start_date']

    def __str__(self):
        return f"{self.tour.name} - {self.season_name}"


class TourDeparture(TimeStampedModel):
    """Scheduled departure dates for tours."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='departures')
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_spots = models.PositiveIntegerField()
    is_guaranteed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('limited', 'Limited Spots'),
            ('sold_out', 'Sold Out'),
            ('cancelled', 'Cancelled'),
        ],
        default='available'
    )

    class Meta:
        verbose_name = 'Tour Departure'
        verbose_name_plural = 'Tour Departures'
        ordering = ['departure_date']

    def __str__(self):
        return f"{self.tour.name} - {self.departure_date}"


class TourFAQ(TimeStampedModel, SortableModel):
    """FAQs specific to a tour."""

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=300)
    answer = models.TextField()

    class Meta:
        verbose_name = 'Tour FAQ'
        verbose_name_plural = 'Tour FAQs'
        ordering = ['sort_order']

    def __str__(self):
        return f"{self.tour.name} - {self.question[:50]}"


