"""
Tour filters for API.
"""
import django_filters
from .models import Tour, TourType


class TourFilter(django_filters.FilterSet):
    """Filter set for tours."""

    destination = django_filters.CharFilter(
        field_name='destinations__slug',
        lookup_expr='exact'
    )
    category = django_filters.CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    tour_type = django_filters.CharFilter(
        field_name='tour_type__slug',
        lookup_expr='exact'
    )

    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    min_days = django_filters.NumberFilter(field_name='days', lookup_expr='gte')
    max_days = django_filters.NumberFilter(field_name='days', lookup_expr='lte')

    difficulty = django_filters.CharFilter(field_name='difficulty_level')

    is_featured = django_filters.BooleanFilter()
    is_best_seller = django_filters.BooleanFilter()
    is_multi_destination = django_filters.BooleanFilter()
    has_discount = django_filters.BooleanFilter()

    class Meta:
        model = Tour
        fields = [
            'destination', 'category', 'tour_type',
            'min_price', 'max_price', 'min_days', 'max_days',
            'difficulty', 'is_featured', 'is_best_seller', 'is_multi_destination', 'has_discount'
        ]
