"""
Update Early Booking Offer badges
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tours.models import EarlyBookingOffer

# Update badges for each offer
badge_updates = {
    'Summer 2025 Early Bird': 'Summer Deal',
    'Winter Escape Special': 'Winter Deal',
    'Family Adventure Discount': 'Family Deal',
}

for title, badge in badge_updates.items():
    updated = EarlyBookingOffer.objects.filter(title__icontains=title.split()[0]).update(badge_text=badge)
    if updated:
        print(f"✓ Updated '{title}' → badge: '{badge}'")
    else:
        print(f"✗ Not found: '{title}'")

print("\nDone! Badge texts updated.")
