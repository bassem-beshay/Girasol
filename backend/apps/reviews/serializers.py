"""
Review serializers for API.
"""
from rest_framework import serializers
from .models import Review, ReviewImage, Testimonial


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['id', 'image', 'caption']


class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)
    tour_name = serializers.CharField(source='tour.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'reviewer_name', 'reviewer_country', 'reviewer_avatar',
            'tour', 'tour_name', 'rating', 'title', 'content',
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


class TestimonialSerializer(serializers.ModelSerializer):
    tour_name = serializers.CharField(source='tour.name', read_only=True)

    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'country', 'avatar', 'quote',
            'rating', 'tour', 'tour_name'
        ]
