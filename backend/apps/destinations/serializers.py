"""
Destination serializers for API.
"""
from rest_framework import serializers
from apps.core.serializers import MultiLanguageSerializerMixin
from .models import Destination, DestinationImage, Activity


class DestinationImageSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['caption', 'alt_text', 'title', 'description']

    class Meta:
        model = DestinationImage
        fields = [
            'id', 'image', 'caption', 'caption_es', 'caption_pt',
            'alt_text', 'alt_text_es', 'alt_text_pt',
            'title', 'title_es', 'title_pt',
            'description', 'description_es', 'description_pt',
        ]


class ActivitySerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['name', 'description', 'image_alt', 'image_title', 'image_caption', 'image_description']

    class Meta:
        model = Activity
        fields = [
            'id', 'name', 'name_es', 'name_pt',
            'description', 'description_es', 'description_pt',
            'image', 'price_from', 'price_to', 'duration',
            'image_alt', 'image_alt_es', 'image_alt_pt',
            'image_title', 'image_title_es', 'image_title_pt',
            'image_caption', 'image_caption_es', 'image_caption_pt',
            'image_description', 'image_description_es', 'image_description_pt',
        ]


class DestinationListSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['name', 'tagline', 'image_alt', 'image_title', 'image_caption', 'image_description']
    tour_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug', 'tagline', 'tagline_es', 'tagline_pt',
            'featured_image', 'country', 'region', 'is_featured', 'tour_count',
            'image_alt', 'image_alt_es', 'image_alt_pt',
            'image_title', 'image_title_es', 'image_title_pt',
            'image_caption', 'image_caption_es', 'image_caption_pt',
            'image_description', 'image_description_es', 'image_description_pt',
        ]


class DestinationDetailSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = [
        'name', 'tagline', 'description',
        'image_alt', 'image_title', 'image_caption', 'image_description',
        'best_time_to_visit', 'getting_there', 'climate_info',
        'meta_title', 'meta_description',
        'focus_keyphrase', 'semantic_keywords', 'lsi_keywords', 'long_tail_phrases',
    ]
    images = DestinationImageSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)
    tour_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'tagline', 'tagline_es', 'tagline_pt',
            'description', 'description_es', 'description_pt',
            'featured_image',
            'image_alt', 'image_alt_es', 'image_alt_pt',
            'image_title', 'image_title_es', 'image_title_pt',
            'image_caption', 'image_caption_es', 'image_caption_pt',
            'image_description', 'image_description_es', 'image_description_pt',
            'country', 'region', 'latitude', 'longitude',
            'best_time_to_visit', 'best_time_to_visit_es', 'best_time_to_visit_pt',
            'getting_there', 'getting_there_es', 'getting_there_pt',
            'climate_info', 'climate_info_es', 'climate_info_pt',
            'is_featured', 'tour_count', 'images', 'activities',
            'meta_title', 'meta_description',
            'focus_keyphrase', 'semantic_keywords', 'lsi_keywords', 'long_tail_phrases'
        ]
