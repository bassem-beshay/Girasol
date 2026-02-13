"""
Script to add seasonal pricing to all tours.
"""
import os
import sys
import django
from datetime import date
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import Tour, TourPricing


# Seasonal pricing configuration
SEASONS = [
    {
        'season_name': 'High Season',
        'season_name_es': 'Temporada Alta',
        'season_name_pt': 'Alta Temporada',
        'start_date': date(2025, 10, 1),
        'end_date': date(2026, 4, 30),
        'price_multiplier': Decimal('1.0'),  # Base price
        'single_supplement_pct': Decimal('0.25'),  # 25% extra for single room
    },
    {
        'season_name': 'Low Season',
        'season_name_es': 'Temporada Baja',
        'season_name_pt': 'Baixa Temporada',
        'start_date': date(2025, 6, 1),
        'end_date': date(2025, 8, 31),
        'price_multiplier': Decimal('0.85'),  # 15% discount
        'single_supplement_pct': Decimal('0.20'),  # 20% extra for single room
    },
    {
        'season_name': 'Shoulder Season',
        'season_name_es': 'Temporada Media',
        'season_name_pt': 'Meia Temporada',
        'start_date': date(2025, 5, 1),
        'end_date': date(2025, 5, 31),
        'price_multiplier': Decimal('0.92'),  # 8% discount
        'single_supplement_pct': Decimal('0.22'),  # 22% extra for single room
    },
    {
        'season_name': 'Shoulder Season',
        'season_name_es': 'Temporada Media',
        'season_name_pt': 'Meia Temporada',
        'start_date': date(2025, 9, 1),
        'end_date': date(2025, 9, 30),
        'price_multiplier': Decimal('0.92'),  # 8% discount
        'single_supplement_pct': Decimal('0.22'),  # 22% extra for single room
    },
]


def add_pricing_to_tours():
    """Add seasonal pricing to all tours."""
    tours = Tour.objects.all()
    total = tours.count()
    added = 0

    print("="*60)
    print("ADDING SEASONAL PRICING TO TOURS")
    print("="*60)

    for i, tour in enumerate(tours, 1):
        existing = tour.seasonal_pricing.count()
        print(f"\n[{i}/{total}] {tour.name[:50]}")

        if existing > 0:
            print(f"  Already has {existing} pricing entries, skipping...")
            continue

        base_price = tour.price or Decimal('0')
        if base_price == 0:
            print(f"  No base price set, skipping...")
            continue

        # Add seasonal pricing
        for season in SEASONS:
            season_price = base_price * season['price_multiplier']
            single_supp = base_price * season['single_supplement_pct']

            TourPricing.objects.create(
                tour=tour,
                season_name=season['season_name'],
                season_name_es=season['season_name_es'],
                season_name_pt=season['season_name_pt'],
                start_date=season['start_date'],
                end_date=season['end_date'],
                price_per_person=season_price.quantize(Decimal('0.01')),
                single_supplement=single_supp.quantize(Decimal('0.01')),
            )

        print(f"  Added {len(SEASONS)} seasonal prices")
        added += 1

    print(f"\n{'='*60}")
    print(f"COMPLETED! Added pricing to {added} tours")
    print(f"Total pricing entries created: {added * len(SEASONS)}")
    print("="*60)


if __name__ == '__main__':
    add_pricing_to_tours()
