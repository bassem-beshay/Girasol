"""
Review serializers for API.
"""
from rest_framework import serializers
from apps.core.serializers import MultiLanguageSerializerMixin
from .models import Review, ReviewImage, Testimonial


class ReviewImageSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['caption']

    class Meta:
        model = ReviewImage
        fields = ['id', 'image', 'caption', 'caption_es', 'caption_pt']


class ReviewSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['title', 'content']
    images = ReviewImageSerializer(many=True, read_only=True)
    tour_name = serializers.CharField(source='tour.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'reviewer_name', 'reviewer_country', 'reviewer_avatar',
            'tour', 'tour_name', 'rating',
            'title', 'title_es', 'title_pt',
            'content', 'content_es', 'content_pt',
            'travel_date', 'is_verified', 'images',
            'admin_response', 'admin_response_at', 'created_at'
        ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), required=False, write_only=True
    )

    class Meta:
        model = Review
        fields = [
            'tour', 'booking', 'reviewer_name', 'reviewer_country',
            'rating', 'title', 'content', 'travel_date', 'images'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
            # Auto-verify if user has a completed booking
            if validated_data.get('booking'):
                validated_data['is_verified'] = True

        review = Review.objects.create(**validated_data)

        for image in images_data:
            ReviewImage.objects.create(review=review, image=image)

        return review


class TestimonialSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    TRANSLATABLE_FIELDS = ['quote']
    tour_name = serializers.CharField(source='tour.name', read_only=True)

    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'country', 'avatar',
            'quote', 'quote_es', 'quote_pt',
            'rating', 'tour', 'tour_name'
        ]
