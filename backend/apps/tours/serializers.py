"""
Tour serializers for API.
"""
from rest_framework import serializers
from .models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourDeparture, TourFAQ
)
from apps.destinations.serializers import DestinationListSerializer


class TourCategorySerializer(serializers.ModelSerializer):
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


class TourTypeSerializer(serializers.ModelSerializer):
    tour_count = serializers.SerializerMethodField()

    class Meta:
        model = TourType
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'description', 'icon', 'tour_count'
        ]

    def get_tour_count(self, obj):
        return obj.tours.filter(is_published=True).count()


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = ['id', 'image', 'caption', 'alt_text']


class TourHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourHighlight
        fields = ['id', 'title', 'description', 'icon']


class TourItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourItinerary
        fields = [
            'id', 'day_number', 'title', 'description',
            'locations', 'meals_included', 'accommodation', 'image'
        ]


class TourInclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourInclusion
        fields = ['id', 'item', 'is_included']


class TourPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPricing
        fields = ['id', 'season_name', 'start_date', 'end_date', 'price_per_person', 'single_supplement']


class TourDepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDeparture
        fields = [
            'id', 'departure_date', 'return_date', 'price',
            'available_spots', 'is_guaranteed', 'status'
        ]


class TourFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourFAQ
        fields = ['id', 'question', 'answer']


class TourListSerializer(serializers.ModelSerializer):
    """Serializer for tour listing (minimal data)."""
    category = TourCategorySerializer(read_only=True)
    tour_type = TourTypeSerializer(read_only=True)
    duration_display = serializers.CharField(read_only=True)
    discounted_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    destination_names = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'short_description', 'short_description_es', 'short_description_pt',
            'featured_image', 'category', 'tour_type', 'days', 'nights', 'duration_display',
            'price', 'discounted_price', 'currency', 'has_discount', 'discount_percentage',
            'discount_start_date', 'discount_end_date',
            'is_featured', 'is_best_seller', 'is_new',
            'average_rating', 'review_count', 'difficulty_level',
            'destination_names', 'max_group_size'
        ]

    def get_destination_names(self, obj):
        return list(obj.destinations.values_list('name', flat=True))


class TourDetailSerializer(serializers.ModelSerializer):
    """Serializer for full tour details."""
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

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'short_description', 'short_description_es', 'short_description_pt',
            'description', 'description_es', 'description_pt',
            'featured_image', 'video_url',
            'category', 'tour_type', 'destinations',
            'days', 'nights', 'duration_display', 'departure_city',
            'price', 'price_single_supplement', 'child_price', 'currency',
            'discounted_price', 'has_discount', 'discount_percentage',
            'discount_start_date', 'discount_end_date',
            'min_group_size', 'max_group_size',
            'is_featured', 'is_best_seller', 'is_new',
            'average_rating', 'review_count', 'difficulty_level', 'languages',
            'images', 'highlights', 'itinerary', 'inclusions',
            'seasonal_pricing', 'departures', 'faqs',
            'meta_title', 'meta_description',
            'created_at', 'updated_at'
        ]


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
