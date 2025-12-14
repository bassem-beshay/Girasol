"""
Destination views for API.
"""
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Destination
from .serializers import DestinationListSerializer, DestinationDetailSerializer


class DestinationListView(generics.ListAPIView):
    """List all active destinations."""
    serializer_class = DestinationListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_featured', 'country', 'region']
    search_fields = ['name', 'description', 'tagline']
    ordering_fields = ['name', 'sort_order']
    ordering = ['sort_order']

    def get_queryset(self):
        return Destination.objects.filter(is_active=True)


class DestinationDetailView(generics.RetrieveAPIView):
    """Get destination details by slug."""
    serializer_class = DestinationDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Destination.objects.filter(is_active=True).prefetch_related(
            'images', 'activities'
        )


class FeaturedDestinationsView(generics.ListAPIView):
    """List featured destinations."""
    serializer_class = DestinationListSerializer

    def get_queryset(self):
        return Destination.objects.filter(is_active=True, is_featured=True)[:6]
