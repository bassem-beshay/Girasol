"""
Review views for API.
"""
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review, Testimonial
from .serializers import (
    ReviewSerializer, ReviewCreateSerializer, TestimonialSerializer
)


class ReviewListView(generics.ListAPIView):
    """List approved reviews."""
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['tour', 'rating', 'is_verified', 'is_featured']
    ordering_fields = ['created_at', 'rating']
    ordering = ['-created_at']

    def get_queryset(self):
        return Review.objects.filter(is_approved=True).select_related('tour')


class TourReviewsView(generics.ListAPIView):
    """List reviews for a specific tour."""
    serializer_class = ReviewSerializer

    def get_queryset(self):
        tour_slug = self.kwargs.get('tour_slug')
        return Review.objects.filter(
            tour__slug=tour_slug, is_approved=True
        ).select_related('tour').prefetch_related('images')


class ReviewCreateView(generics.CreateAPIView):
    """Create a new review."""
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.AllowAny]


class FeaturedReviewsView(generics.ListAPIView):
    """List featured reviews for homepage."""
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(
            is_approved=True, is_featured=True
        ).select_related('tour')[:6]


class TestimonialListView(generics.ListAPIView):
    """List active testimonials."""
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True)
