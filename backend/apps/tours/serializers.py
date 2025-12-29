"""
Tour serializers for API.
"""
from rest_framework import serializers
from apps.core.serializers import MultiLanguageSerializerMixin
from .models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourDeparture, TourFAQ, EarlyBookingOffer
)
from apps.destinations.serializers import DestinationListSerializer


class TourCategorySerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['name', 'description']
    tour_count = serializers.SerializerMethodField()

    class Meta:
        model = TourCategory
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'description', 'description_es', 'description_pt',
            'icon', 'image', 'tour_count'
        ]

    def get_tour_count(self, obj):
        return obj.tours.filter(is_published=True).count()


class TourTypeSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['name', 'description']
    tour_count = serializers.SerializerMethodField()

    class Meta:
        model = TourType
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'description', 'description_es', 'description_pt',
            'icon', 'tour_count'
        ]

    def get_tour_count(self, obj):
        return obj.tours.filter(is_published=True).count()


class TourImageSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['caption', 'alt_text']

    class Meta:
        model = TourImage
        fields = ['id', 'image', 'caption', 'caption_es', 'caption_pt', 'alt_text', 'alt_text_es', 'alt_text_pt']


class TourHighlightSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['title', 'description']

    class Meta:
        model = TourHighlight
        fields = ['id', 'title', 'title_es', 'title_pt', 'description', 'description_es', 'description_pt', 'icon']


class TourItinerarySerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['title', 'description', 'locations', 'meals_included', 'accommodation']

    class Meta:
        model = TourItinerary
        fields = [
            'id', 'day_number',
            'title', 'title_es', 'title_pt',
            'description', 'description_es', 'description_pt',
            'locations', 'locations_es', 'locations_pt',
            'meals_included', 'meals_included_es', 'meals_included_pt',
            'accommodation', 'accommodation_es', 'accommodation_pt',
            'image'
        ]


class TourInclusionSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['item']

    class Meta:
        model = TourInclusion
        fields = ['id', 'item', 'item_es', 'item_pt', 'is_included']


class TourPricingSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['season_name']

    class Meta:
        model = TourPricing
        fields = ['id', 'season_name', 'season_name_es', 'season_name_pt', 'start_date', 'end_date', 'price_per_person', 'single_supplement']


class TourDepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDeparture
        fields = [
            'id', 'departure_date', 'return_date', 'price',
            'available_spots', 'is_guaranteed', 'status'
        ]


class TourFAQSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['question', 'answer']

    class Meta:
        model = TourFAQ
        fields = ['id', 'question', 'question_es', 'question_pt', 'answer', 'answer_es', 'answer_pt']


class TourListSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for tour listing (minimal data)."""
    TRANSLATABLE_FIELDS = ['name', 'short_description']
    category = TourCategorySerializer(read_only=True)
    tour_type = TourTypeSerializer(read_only=True)
    duration_display = serializers.CharField(read_only=True)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    destination_names = serializers.SerializerMethodField()
    highlights = serializers.SerializerMethodField()

    # Early Booking fields
    is_early_booking = serializers.SerializerMethodField()
    early_booking_discount = serializers.SerializerMethodField()
    early_booking_price = serializers.SerializerMethodField()
    early_booking_badge = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'short_description', 'short_description_es', 'short_description_pt',
            'featured_image', 'category', 'tour_type', 'days', 'nights', 'duration_display',
            'price', 'discounted_price', 'currency', 'has_discount', 'discount_percentage',
            'discount_start_date', 'discount_end_date',
            'is_featured', 'is_best_seller', 'is_new', 'is_multi_destination',
            'average_rating', 'review_count', 'difficulty_level',
            'destination_names', 'max_group_size', 'highlights',
            # Early Booking fields
            'is_early_booking', 'early_booking_discount', 'early_booking_price', 'early_booking_badge'
        ]

    def get_destination_names(self, obj):
        return list(obj.destinations.values_list('name', flat=True))

    def get_highlights(self, obj):
        return list(obj.highlights.values_list('title', flat=True)[:3])

    def _get_active_early_booking(self, obj):
        """Get the active early booking offer for this tour."""
        from django.utils import timezone
        now = timezone.now()
        return obj.early_booking_offers.filter(
            is_active=True,
            offer_start_date__lte=now,
            offer_end_date__gte=now
        ).order_by('-discount_percentage').first()

    def get_is_early_booking(self, obj):
        """Check if tour is part of any active early booking offer."""
        return self._get_active_early_booking(obj) is not None

    def get_early_booking_discount(self, obj):
        """Get the early booking discount percentage."""
        offer = self._get_active_early_booking(obj)
        return offer.discount_percentage if offer else None

    def get_early_booking_price(self, obj):
        """Calculate the early booking price."""
        offer = self._get_active_early_booking(obj)
        if offer:
            return round(float(obj.price) * (100 - offer.discount_percentage) / 100, 2)
        return None

    def get_early_booking_badge(self, obj):
        """Get the badge text for early booking."""
        offer = self._get_active_early_booking(obj)
        return offer.badge_text if offer else None


class TourDetailSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """Serializer for full tour details."""
    TRANSLATABLE_FIELDS = ['name', 'short_description', 'description']
    category = TourCategorySerializer(read_only=True)
    tour_type = TourTypeSerializer(read_only=True)
    destinations = DestinationListSerializer(many=True, read_only=True)
    images = TourImageSerializer(many=True, read_only=True)
    highlights = TourHighlightSerializer(many=True, read_only=True)
    itinerary = TourItinerarySerializer(many=True, read_only=True)
    inclusions = TourInclusionSerializer(many=True, read_only=True)
    seasonal_pricing = TourPricingSerializer(many=True, read_only=True)
    departures = TourDepartureSerializer(many=True, read_only=True)
    faqs = TourFAQSerializer(many=True, read_only=True)
    duration_display = serializers.CharField(read_only=True)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    destination_names = serializers.SerializerMethodField()

    # Early Booking fields
    is_early_booking = serializers.SerializerMethodField()
    early_booking_discount = serializers.SerializerMethodField()
    early_booking_price = serializers.SerializerMethodField()
    early_booking_badge = serializers.SerializerMethodField()
    early_booking_end_date = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'short_description', 'short_description_es', 'short_description_pt',
            'description', 'description_es', 'description_pt',
            'featured_image', 'video_url',
            'category', 'tour_type', 'destinations', 'destination_names',
            'days', 'nights', 'duration_display', 'departure_city',
            'price', 'price_single_supplement', 'child_price', 'currency',
            'discounted_price', 'has_discount', 'discount_percentage',
            'discount_start_date', 'discount_end_date',
            'min_group_size', 'max_group_size',
            'is_featured', 'is_best_seller', 'is_new', 'is_multi_destination',
            'average_rating', 'review_count', 'difficulty_level', 'languages',
            'images', 'highlights', 'itinerary', 'inclusions',
            'seasonal_pricing', 'departures', 'faqs',
            'meta_title', 'meta_description',
            'created_at', 'updated_at',
            # Early Booking fields
            'is_early_booking', 'early_booking_discount', 'early_booking_price',
            'early_booking_badge', 'early_booking_end_date'
        ]

    def get_destination_names(self, obj):
        return list(obj.destinations.values_list('name', flat=True))

    def _get_active_early_booking(self, obj):
        """Get the active early booking offer for this tour."""
        from django.utils import timezone
        now = timezone.now()
        return obj.early_booking_offers.filter(
            is_active=True,
            offer_start_date__lte=now,
            offer_end_date__gte=now
        ).order_by('-discount_percentage').first()

    def get_is_early_booking(self, obj):
        """Check if tour is part of any active early booking offer."""
        return self._get_active_early_booking(obj) is not None

    def get_early_booking_discount(self, obj):
        """Get the early booking discount percentage."""
        offer = self._get_active_early_booking(obj)
        return offer.discount_percentage if offer else None

    def get_early_booking_price(self, obj):
        """Calculate the early booking price."""
        offer = self._get_active_early_booking(obj)
        if offer:
            return round(float(obj.price) * (100 - offer.discount_percentage) / 100, 2)
        return None

    def get_early_booking_badge(self, obj):
        """Get the badge text for early booking."""
        offer = self._get_active_early_booking(obj)
        return offer.badge_text if offer else None

    def get_early_booking_end_date(self, obj):
        """Get the end date of the early booking offer."""
        offer = self._get_active_early_booking(obj)
        return offer.offer_end_date.isoformat() if offer else None


class TourSearchSerializer(serializers.Serializer):
    """Serializer for tour search/filter parameters."""
    destination = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    tour_type = serializers.CharField(required=False)
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    min_days = serializers.IntegerField(required=False)
    max_days = serializers.IntegerField(required=False)
    difficulty = serializers.CharField(required=False)
    search = serializers.CharField(required=False)


class EarlyBookingTourSerializer(serializers.ModelSerializer):
    """Minimal tour info for Early Booking offers."""
    duration_display = serializers.CharField(read_only=True)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'slug', 'featured_image',
            'days', 'nights', 'duration_display',
            'price', 'discounted_price', 'currency',
            'average_rating', 'review_count'
        ]


class EarlyBookingOfferSerializer(serializers.ModelSerializer):
    """
    Serializer for Early Booking Offers.
    الحجز المبكر - عروض خاصة للحجز المسبق
    """
    tours = EarlyBookingTourSerializer(many=True, read_only=True)
    is_currently_active = serializers.BooleanField(read_only=True)
    days_remaining = serializers.IntegerField(read_only=True)
    hours_remaining = serializers.IntegerField(read_only=True)
    minutes_remaining = serializers.IntegerField(read_only=True)
    seconds_remaining = serializers.IntegerField(read_only=True)

    # Calculate early booking price for each tour
    tours_with_early_price = serializers.SerializerMethodField()

    class Meta:
        model = EarlyBookingOffer
        fields = [
            'id', 'title', 'title_es', 'title_pt',
            'subtitle', 'subtitle_es', 'subtitle_pt',
            'description', 'description_es', 'description_pt',
            'discount_percentage', 'min_days_advance',
            'offer_start_date', 'offer_end_date',
            'travel_start_date', 'travel_end_date',
            'tours', 'tours_with_early_price',
            'benefits',
            'terms_conditions', 'terms_conditions_es', 'terms_conditions_pt',
            'cancellation_policy', 'cancellation_policy_es', 'cancellation_policy_pt',
            'badge_text', 'badge_text_es', 'badge_text_pt',
            'banner_image', 'background_color',
            'is_currently_active', 'is_featured',
            'days_remaining', 'hours_remaining', 'minutes_remaining', 'seconds_remaining'
        ]

    def get_tours_with_early_price(self, obj):
        """Get tours with calculated early booking prices."""
        tours_data = []
        for tour in obj.tours.filter(is_published=True):
            early_price = float(tour.price) * (100 - obj.discount_percentage) / 100
            tours_data.append({
                'id': tour.id,
                'name': tour.name,
                'slug': tour.slug,
                'featured_image': tour.featured_image.url if tour.featured_image else None,
                'days': tour.days,
                'nights': tour.nights,
                'duration_display': tour.duration_display,
                'original_price': float(tour.price),
                'early_booking_price': round(early_price, 2),
                'discount_percentage': obj.discount_percentage,
                'currency': tour.currency,
                'average_rating': float(tour.average_rating),
                'review_count': tour.review_count,
            })
        return tours_data


class EarlyBookingOfferListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing early booking offers."""
    is_currently_active = serializers.BooleanField(read_only=True)
    days_remaining = serializers.IntegerField(read_only=True)
    tour_count = serializers.SerializerMethodField()

    class Meta:
        model = EarlyBookingOffer
        fields = [
            'id', 'title', 'subtitle', 'discount_percentage',
            'offer_end_date', 'badge_text', 'banner_image', 'background_color',
            'is_currently_active', 'is_featured', 'days_remaining', 'tour_count'
        ]

    def get_tour_count(self, obj):
        return obj.tours.filter(is_published=True).count()
