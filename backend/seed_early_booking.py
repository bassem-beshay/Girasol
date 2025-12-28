"""
Seed Early Booking Offers data.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.utils import timezone
from datetime import timedelta
from apps.tours.models import EarlyBookingOffer, Tour

def seed_early_booking():
    # Get some tours to add to the offer
    tours = list(Tour.objects.filter(is_published=True)[:5])
    print(f'Found {len(tours)} tours')

    # Create Early Booking Offer 1 - Summer 2025
    offer1, created = EarlyBookingOffer.objects.get_or_create(
        title='Summer 2025 Early Bird',
        defaults={
            'title_ar': 'عرض الصيف 2025 - احجز مبكراً',
            'subtitle': 'Save Up to 20% on Early Bookings',
            'subtitle_ar': 'وفر حتى 20% عند الحجز المبكر',
            'description': 'Book your dream Egyptian adventure now and enjoy exclusive discounts on our most popular packages. Don\'t miss this opportunity to explore the land of pharaohs!',
            'description_ar': 'احجز مغامرتك المصرية الآن واستمتع بخصومات حصرية على أشهر باقاتنا. لا تفوت هذه الفرصة لاستكشاف أرض الفراعنة!',
            'discount_percentage': 20,
            'min_days_advance': 90,
            'offer_start_date': timezone.now(),
            'offer_end_date': timezone.now() + timedelta(days=30),
            'travel_start_date': (timezone.now() + timedelta(days=90)).date(),
            'travel_end_date': (timezone.now() + timedelta(days=180)).date(),
            'benefits': [
                'Lower prices - Save up to 20%',
                'Better room selection',
                'Guaranteed availability',
                'Flexible payment plans',
                'Free cancellation up to 30 days before'
            ],
            'terms_conditions': 'Offer valid for bookings made at least 90 days before travel date. Cannot be combined with other offers.',
            'cancellation_policy': 'Free cancellation up to 30 days before departure. 50% refund 15-29 days before. No refund within 14 days.',
            'badge_text': 'Early Bird',
            'background_color': '#2563eb',
            'is_active': True,
            'is_featured': True,
            'sort_order': 1
        }
    )
    if created:
        offer1.tours.set(tours[:3])
        print('Created: Summer 2025 Early Bird')
    else:
        print('Already exists: Summer 2025 Early Bird')

    # Create Early Booking Offer 2 - Winter Special
    offer2, created = EarlyBookingOffer.objects.get_or_create(
        title='Winter Escape Special',
        defaults={
            'title_ar': 'عرض الشتاء الخاص',
            'subtitle': 'Book Now for Winter Adventures - 15% OFF',
            'subtitle_ar': 'احجز الآن لمغامرات الشتاء - خصم 15%',
            'description': 'Escape the cold and discover Egypt\'s warm winter sun. Perfect weather for exploring ancient wonders!',
            'description_ar': 'اهرب من البرد واكتشف دفء شمس مصر الشتوية. طقس مثالي لاستكشاف العجائب القديمة!',
            'discount_percentage': 15,
            'min_days_advance': 60,
            'offer_start_date': timezone.now(),
            'offer_end_date': timezone.now() + timedelta(days=45),
            'travel_start_date': (timezone.now() + timedelta(days=60)).date(),
            'travel_end_date': (timezone.now() + timedelta(days=150)).date(),
            'benefits': [
                'Save 15% on all packages',
                'Perfect weather for sightseeing',
                'Less crowded attractions',
                'Priority booking for Nile cruises'
            ],
            'terms_conditions': 'Minimum 60 days advance booking required.',
            'cancellation_policy': 'Free cancellation up to 21 days before departure.',
            'badge_text': 'Winter Deal',
            'background_color': '#059669',
            'is_active': True,
            'is_featured': True,
            'sort_order': 2
        }
    )
    if created:
        offer2.tours.set(tours[1:4])
        print('Created: Winter Escape Special')
    else:
        print('Already exists: Winter Escape Special')

    # Create Early Booking Offer 3 - Family Package
    offer3, created = EarlyBookingOffer.objects.get_or_create(
        title='Family Adventure Discount',
        defaults={
            'title_ar': 'خصم رحلات العائلة',
            'subtitle': 'Plan Ahead for Family Fun - Save 25%',
            'subtitle_ar': 'خطط مسبقاً لمتعة العائلة - وفر 25%',
            'description': 'The perfect opportunity to plan your family vacation to Egypt. Kids will love the pyramids and mummies!',
            'description_ar': 'الفرصة المثالية لتخطيط إجازة عائلتك في مصر. سيحب الأطفال الأهرامات والمومياوات!',
            'discount_percentage': 25,
            'min_days_advance': 120,
            'offer_start_date': timezone.now(),
            'offer_end_date': timezone.now() + timedelta(days=60),
            'travel_start_date': (timezone.now() + timedelta(days=120)).date(),
            'travel_end_date': (timezone.now() + timedelta(days=240)).date(),
            'benefits': [
                'Biggest discount - 25% OFF',
                'Kids under 12 stay free',
                'Family-friendly activities included',
                'Private guides for families',
                'Flexible itinerary adjustments'
            ],
            'terms_conditions': 'Must book at least 4 months in advance. Minimum 2 adults required.',
            'cancellation_policy': 'Full refund up to 45 days before. 75% refund 30-44 days before.',
            'badge_text': 'Family Deal',
            'background_color': '#dc2626',
            'is_active': True,
            'is_featured': False,
            'sort_order': 3
        }
    )
    if created:
        offer3.tours.set(tours)
        print('Created: Family Adventure Discount')
    else:
        print('Already exists: Family Adventure Discount')

    print('\n=== Early Booking Offers Summary ===')
    for offer in EarlyBookingOffer.objects.all():
        print(f'{offer.title}: {offer.discount_percentage}% OFF - {offer.tours.count()} tours - Active: {offer.is_currently_active}')
        print(f'  Countdown: {offer.days_remaining}d {offer.hours_remaining}h {offer.minutes_remaining}m')

if __name__ == '__main__':
    seed_early_booking()
