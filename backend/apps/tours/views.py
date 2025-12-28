"""
Tour views for API.
"""
from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch
from django.utils import timezone
from .models import Tour, TourCategory, TourDeparture, EarlyBookingOffer
from .serializers import (
    TourListSerializer, TourDetailSerializer, TourCategorySerializer,
    TourDepartureSerializer, EarlyBookingOfferSerializer, EarlyBookingOfferListSerializer
)
from .filters import TourFilter


class TourListView(generics.ListAPIView):
    """List all published tours with filtering."""
    serializer_class = TourListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TourFilter
    search_fields = ['name', 'short_description', 'description', 'destinations__name']
    ordering_fields = ['price', 'days', 'average_rating', 'created_at', 'name']
    ordering = ['-is_featured', '-is_best_seller', '-created_at']

    def get_queryset(self):
        return Tour.objects.filter(is_published=True).select_related(
            'category', 'tour_type'
        ).prefetch_related('destinations')


class TourDetailView(generics.RetrieveAPIView):
    """Get full tour details by slug."""
    serializer_class = TourDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Tour.objects.filter(is_published=True).select_related(
            'category'
        ).prefetch_related(
            'destinations',
            'images',
            'highlights',
            'itinerary',
            'inclusions',
            'seasonal_pricing',
            Prefetch(
                'departures',
                queryset=TourDeparture.objects.filter(status__in=['available', 'limited'])
            ),
            'faqs'
        )


class FeaturedToursView(generics.ListAPIView):
    """List featured tours for homepage."""
    serializer_class = TourListSerializer

    def get_queryset(self):
        return Tour.objects.filter(
            is_published=True,
            is_featured=True
        ).select_related('category', 'tour_type').prefetch_related('destinations')[:8]


class PopularToursView(generics.ListAPIView):
    """List popular/best-selling tours."""
    serializer_class = TourListSerializer

    def get_queryset(self):
        return Tour.objects.filter(
            is_published=True,
            is_best_seller=True
        ).select_related('category', 'tour_type').prefetch_related('destinations')[:8]


class MultiDestinationToursView(generics.ListAPIView):
    """List multi-destination tours (e.g., Egypt & Jordan, Egypt & Dubai)."""
    serializer_class = TourListSerializer

    def get_queryset(self):
        return Tour.objects.filter(
            is_published=True,
            is_multi_destination=True
        ).select_related('category', 'tour_type').prefetch_related('destinations')[:6]


class TourCategoryListView(generics.ListAPIView):
    """List all active tour categories."""
    serializer_class = TourCategorySerializer

    def get_queryset(self):
        return TourCategory.objects.filter(is_active=True)


class ToursByDestinationView(generics.ListAPIView):
    """List tours for a specific destination."""
    serializer_class = TourListSerializer

    def get_queryset(self):
        destination_slug = self.kwargs.get('destination_slug')
        return Tour.objects.filter(
            is_published=True,
            destinations__slug=destination_slug
        ).select_related('category').prefetch_related('destinations')


class ToursByCategoryView(generics.ListAPIView):
    """List tours for a specific category."""
    serializer_class = TourListSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        return Tour.objects.filter(
            is_published=True,
            category__slug=category_slug
        ).select_related('category').prefetch_related('destinations')


class RelatedToursView(generics.ListAPIView):
    """Get related tours based on current tour."""
    serializer_class = TourListSerializer

    def get_queryset(self):
        tour_slug = self.kwargs.get('slug')
        try:
            tour = Tour.objects.get(slug=tour_slug)
            destination_ids = tour.destinations.values_list('id', flat=True)

            return Tour.objects.filter(
                is_published=True,
                destinations__in=destination_ids
            ).exclude(slug=tour_slug).distinct().select_related(
                'category'
            ).prefetch_related('destinations')[:4]
        except Tour.DoesNotExist:
            return Tour.objects.none()


class TourDeparturesView(generics.ListAPIView):
    """Get available departures for a tour."""
    serializer_class = TourDepartureSerializer

    def get_queryset(self):
        tour_slug = self.kwargs.get('slug')
        return TourDeparture.objects.filter(
            tour__slug=tour_slug,
            status__in=['available', 'limited']
        ).order_by('departure_date')


class TourSearchView(APIView):
    """Advanced tour search endpoint."""

    def get(self, request):
        queryset = Tour.objects.filter(is_published=True)

        # Apply filters
        search = request.query_params.get('q')
        if search:
            queryset = queryset.filter(
                models.Q(name__icontains=search) |
                models.Q(short_description__icontains=search) |
                models.Q(destinations__name__icontains=search)
            ).distinct()

        # Serialize and return
        serializer = TourListSerializer(queryset[:20], many=True)
        return Response(serializer.data)


# ============================================================================
# Early Booking Offers (الحجز المبكر)
# ============================================================================

class EarlyBookingOfferListView(generics.ListAPIView):
    """
    List all active early booking offers.
    عرض كل عروض الحجز المبكر النشطة
    """
    serializer_class = EarlyBookingOfferListSerializer

    def get_queryset(self):
        now = timezone.now()
        return EarlyBookingOffer.objects.filter(
            is_active=True,
            offer_start_date__lte=now,
            offer_end_date__gte=now
        ).prefetch_related('tours')


class EarlyBookingOfferDetailView(generics.RetrieveAPIView):
    """
    Get single early booking offer with full details.
    تفاصيل عرض الحجز المبكر
    """
    serializer_class = EarlyBookingOfferSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return EarlyBookingOffer.objects.filter(
            is_active=True
        ).prefetch_related('tours')


class FeaturedEarlyBookingView(generics.ListAPIView):
    """
    Get featured early booking offers for homepage.
    عروض الحجز المبكر المميزة للصفحة الرئيسية
    """
    serializer_class = EarlyBookingOfferSerializer

    def get_queryset(self):
        now = timezone.now()
        return EarlyBookingOffer.objects.filter(
            is_active=True,
            is_featured=True,
            offer_start_date__lte=now,
            offer_end_date__gte=now
        ).prefetch_related('tours')[:3]


class EarlyBookingCountdownView(APIView):
    """
    Get countdown timer data for early booking offers.
    بيانات العد التنازلي لعروض الحجز المبكر
    """

    def get(self, request, pk=None):
        try:
            if pk:
                offer = EarlyBookingOffer.objects.get(pk=pk, is_active=True)
            else:
                # Get the first featured active offer
                now = timezone.now()
                offer = EarlyBookingOffer.objects.filter(
                    is_active=True,
                    is_featured=True,
                    offer_start_date__lte=now,
                    offer_end_date__gte=now
                ).first()

            if not offer:
                return Response({'error': 'No active offer found'}, status=status.HTTP_404_NOT_FOUND)

            return Response({
                'id': offer.id,
                'title': offer.title,
                'discount_percentage': offer.discount_percentage,
                'offer_end_date': offer.offer_end_date.isoformat(),
                'is_currently_active': offer.is_currently_active,
                'days_remaining': offer.days_remaining,
                'hours_remaining': offer.hours_remaining,
                'minutes_remaining': offer.minutes_remaining,
                'seconds_remaining': offer.seconds_remaining,
            })
        except EarlyBookingOffer.DoesNotExist:
            return Response({'error': 'Offer not found'}, status=status.HTTP_404_NOT_FOUND)
