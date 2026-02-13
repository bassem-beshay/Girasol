"""
Script to add departure dates to all tours.
"""
import os
import sys
import django
from datetime import date, timedelta
from decimal import Decimal
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import Tour, TourDeparture


def add_departures_to_tours():
    """Add departure dates to all tours."""
    tours = Tour.objects.all()
    total = tours.count()
    added = 0

    print("="*60)
    print("ADDING DEPARTURE DATES TO TOURS")
    print("="*60)

    # Base date - start from next month
    today = date.today()
    base_date = date(today.year, today.month + 1 if today.month < 12 else 1, 1)
    if today.month == 12:
        base_date = date(today.year + 1, 1, 1)

    for i, tour in enumerate(tours, 1):
        existing = tour.departures.count()
        print(f"\n[{i}/{total}] {tour.name[:50]}")

        if existing > 0:
            print(f"  Already has {existing} departures, skipping...")
            continue

        tour_days = tour.days or 7
        base_price = float(tour.price) if tour.price else 1000

        # Generate 8-12 departure dates over the next 12 months
        num_departures = random.randint(8, 12)
        departure_dates = []

        # Spread departures across the year
        for month_offset in range(12):
            if len(departure_dates) >= num_departures:
                break

            month_date = base_date + timedelta(days=month_offset * 30)

            # Add 1-2 departures per month
            departures_this_month = random.randint(1, 2) if month_offset < 6 else 1

            for j in range(departures_this_month):
                if len(departure_dates) >= num_departures:
                    break

                # Random day in the month (1-28 to be safe)
                day = random.randint(1, 28)
                dep_date = date(month_date.year, month_date.month, day)

                # Skip if date is in the past
                if dep_date <= today:
                    continue

                departure_dates.append(dep_date)

        # Sort dates
        departure_dates.sort()

        # Create departure entries
        for dep_date in departure_dates:
            return_date = dep_date + timedelta(days=tour_days - 1)

            # Vary price slightly (+/- 10%)
            price_variation = random.uniform(0.9, 1.1)
            dep_price = Decimal(str(round(base_price * price_variation, 2)))

            # Random available spots (5-20)
            spots = random.randint(5, 20)

            # Some departures are guaranteed (30% chance)
            guaranteed = random.random() < 0.3

            # Status: mostly available, some almost full
            if spots <= 5:
                status = 'almost_full'
            else:
                status = 'available'

            TourDeparture.objects.create(
                tour=tour,
                departure_date=dep_date,
                return_date=return_date,
                price=dep_price,
                available_spots=spots,
                is_guaranteed=guaranteed,
                status=status,
            )

        print(f"  Added {len(departure_dates)} departures")
        added += 1

    print(f"\n{'='*60}")
    print(f"COMPLETED! Added departures to {added} tours")
    print("="*60)


if __name__ == '__main__':
    add_departures_to_tours()
