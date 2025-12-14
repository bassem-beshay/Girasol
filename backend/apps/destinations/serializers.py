"""
Destination serializers for API.
"""
from rest_framework import serializers
from .models import Destination, DestinationImage, Activity


class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = ['id', 'image', 'caption', 'alt_text']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'image', 'price_from', 'price_to', 'duration']


class DestinationListSerializer(serializers.ModelSerializer):
    tour_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug', 'tagline', 'tagline_es', 'tagline_pt',
            'featured_image', 'country', 'region', 'is_featured', 'tour_count'
        ]


class DestinationDetailSerializer(serializers.ModelSerializer):
    images = DestinationImageSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)
    tour_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'tagline', 'tagline_es', 'tagline_pt',
            'description', 'description_es', 'description_pt',
            'featured_image', 'banner_image', 'video_url',
            'country', 'region', 'latitude', 'longitude',
            'best_time_to_visit', 'getting_there', 'climate_info',
            'is_featured', 'tour_count', 'images', 'activities',
            'meta_title', 'meta_description'
        ]
