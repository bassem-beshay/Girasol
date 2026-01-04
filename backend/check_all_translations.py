"""
Check all translation fields across all models.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourFAQ, EarlyBookingOffer
)
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.blog.models import Category as BlogCategory, Tag, Post
from apps.reviews.models import Review, ReviewImage, Testimonial
from apps.contact.models import FAQ, Office, Statistic


def check_model_translations(model_class, fields_to_check, model_name):
    """Check translation coverage for a model."""
    print(f"\n{'='*60}")
    print(f" {model_name}")
    print('='*60)

    items = model_class.objects.all()
    total = items.count()

    if total == 0:
        print(f"  No records found")
        return [], 0

    print(f"  Total records: {total}")

    missing_translations = []

    for item in items:
        item_name = str(item)[:50]
        item_missing = []

        for field in fields_to_check:
            en_value = getattr(item, field, '')
            es_value = getattr(item, f'{field}_es', '')
            pt_value = getattr(item, f'{field}_pt', '')

            # If English has value but translations are missing
            if en_value and en_value.strip():
                if not es_value or not es_value.strip():
                    item_missing.append(f'{field}_es')
                if not pt_value or not pt_value.strip():
                    item_missing.append(f'{field}_pt')

        if item_missing:
            missing_translations.append({
                'id': item.id,
                'name': item_name,
                'missing': item_missing
            })

    if missing_translations:
        print(f"\n  [!] Missing translations:")
        for item in missing_translations[:5]:  # Show first 5
            print(f"      ID {item['id']}: {item['name']}")
            print(f"         Missing: {', '.join(item['missing'])}")
        if len(missing_translations) > 5:
            print(f"      ... and {len(missing_translations) - 5} more")
    else:
        print(f"  [OK] All translations complete!")

    return missing_translations, total


def main():
    print("\n" + "#"*60)
    print("# COMPLETE TRANSLATION CHECK")
    print("#"*60)

    all_missing = {}
    total_records = 0
    total_missing = 0

    # Check all models
    checks = [
        (TourCategory, ['name', 'description'], 'Tour Categories'),
        (TourType, ['name', 'description'], 'Tour Types'),
        (Tour, ['name', 'short_description', 'description'], 'Tours'),
        (TourImage, ['caption', 'alt_text'], 'Tour Images'),
        (TourHighlight, ['title', 'description'], 'Tour Highlights'),
        (TourItinerary, ['title', 'description', 'locations', 'meals_included', 'accommodation'], 'Tour Itineraries'),
        (TourInclusion, ['item'], 'Tour Inclusions'),
        (TourPricing, ['season_name'], 'Tour Pricing'),
        (TourFAQ, ['question', 'answer'], 'Tour FAQs'),
        (EarlyBookingOffer, ['title', 'subtitle', 'description', 'terms_conditions', 'cancellation_policy', 'badge_text'], 'Early Booking Offers'),
        (Destination, ['name', 'tagline', 'description'], 'Destinations'),
        (DestinationImage, ['caption', 'alt_text'], 'Destination Images'),
        (Activity, ['name', 'description'], 'Activities'),
        (BlogCategory, ['name', 'description'], 'Blog Categories'),
        (Tag, ['name'], 'Blog Tags'),
        (Post, ['title', 'excerpt', 'content', 'featured_image_alt'], 'Blog Posts'),
        (Review, ['title', 'content'], 'Reviews'),
        (ReviewImage, ['caption'], 'Review Images'),
        (Testimonial, ['quote'], 'Testimonials'),
        (FAQ, ['question', 'answer'], 'FAQs'),
        (Office, ['name', 'city', 'address', 'working_hours'], 'Offices'),
        (Statistic, ['label', 'description'], 'Statistics'),
    ]

    for model, fields, name in checks:
        missing, count = check_model_translations(model, fields, name)
        if missing:
            all_missing[name] = missing
        total_records += count
        total_missing += len(missing)

    # Summary
    print("\n" + "#"*60)
    print("# SUMMARY")
    print("#"*60)

    print(f"\n  Total records checked: {total_records}")
    print(f"  Records with missing translations: {total_missing}")

    if all_missing:
        print(f"\n  Models needing updates:")
        for model_name, items in all_missing.items():
            print(f"    - {model_name}: {len(items)} records")
    else:
        print(f"\n  [OK] All translations are complete!")

    print()
    return all_missing


if __name__ == '__main__':
    missing = main()
