# -*- coding: utf-8 -*-
"""
Check all empty fields in all models.
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


def check_empty_fields(model, fields, name):
    """Check for empty fields."""
    print(f"\n{'='*60}")
    print(f" {name}")
    print('='*60)

    items = model.objects.all()
    total = items.count()

    if total == 0:
        print("  No records")
        return

    print(f"  Total: {total} records")

    for field in fields:
        empty_count = 0
        for item in items:
            value = getattr(item, field, None)
            if not value or (isinstance(value, str) and not value.strip()):
                empty_count += 1

        if empty_count > 0:
            print(f"  [!] {field}: {empty_count}/{total} empty")
        else:
            print(f"  [OK] {field}: all filled")


def main():
    print("\n" + "#"*60)
    print("# CHECKING EMPTY FIELDS")
    print("#"*60)

    # Tour Categories
    check_empty_fields(TourCategory, [
        'name', 'name_es', 'name_pt',
        'description', 'description_es', 'description_pt'
    ], 'Tour Categories')

    # Tour Types
    check_empty_fields(TourType, [
        'name', 'name_es', 'name_pt',
        'description', 'description_es', 'description_pt'
    ], 'Tour Types')

    # Tours
    check_empty_fields(Tour, [
        'name', 'name_es', 'name_pt',
        'short_description', 'short_description_es', 'short_description_pt',
        'description', 'description_es', 'description_pt'
    ], 'Tours')

    # Tour Images
    check_empty_fields(TourImage, [
        'caption', 'caption_es', 'caption_pt',
        'alt_text', 'alt_text_es', 'alt_text_pt'
    ], 'Tour Images')

    # Tour Highlights
    check_empty_fields(TourHighlight, [
        'title', 'title_es', 'title_pt',
        'description', 'description_es', 'description_pt'
    ], 'Tour Highlights')

    # Tour Itineraries
    check_empty_fields(TourItinerary, [
        'title', 'title_es', 'title_pt',
        'description', 'description_es', 'description_pt',
        'locations', 'locations_es', 'locations_pt',
        'meals_included', 'meals_included_es', 'meals_included_pt',
        'accommodation', 'accommodation_es', 'accommodation_pt'
    ], 'Tour Itineraries')

    # Tour Inclusions
    check_empty_fields(TourInclusion, [
        'item', 'item_es', 'item_pt'
    ], 'Tour Inclusions')

    # Early Booking
    check_empty_fields(EarlyBookingOffer, [
        'title', 'title_es', 'title_pt',
        'subtitle', 'subtitle_es', 'subtitle_pt',
        'description', 'description_es', 'description_pt',
        'badge_text', 'badge_text_es', 'badge_text_pt'
    ], 'Early Booking Offers')

    # Destinations
    check_empty_fields(Destination, [
        'name', 'name_es', 'name_pt',
        'tagline', 'tagline_es', 'tagline_pt',
        'description', 'description_es', 'description_pt'
    ], 'Destinations')

    # Destination Images
    check_empty_fields(DestinationImage, [
        'caption', 'caption_es', 'caption_pt',
        'alt_text', 'alt_text_es', 'alt_text_pt'
    ], 'Destination Images')

    # Activities
    check_empty_fields(Activity, [
        'name', 'name_es', 'name_pt',
        'description', 'description_es', 'description_pt'
    ], 'Activities')

    # Blog Categories
    check_empty_fields(BlogCategory, [
        'name', 'name_es', 'name_pt',
        'description', 'description_es', 'description_pt'
    ], 'Blog Categories')

    # Tags
    check_empty_fields(Tag, [
        'name', 'name_es', 'name_pt'
    ], 'Tags')

    # Posts
    check_empty_fields(Post, [
        'title', 'title_es', 'title_pt',
        'excerpt', 'excerpt_es', 'excerpt_pt',
        'content', 'content_es', 'content_pt'
    ], 'Blog Posts')

    # Reviews
    check_empty_fields(Review, [
        'title', 'title_es', 'title_pt',
        'content', 'content_es', 'content_pt'
    ], 'Reviews')

    # Testimonials
    check_empty_fields(Testimonial, [
        'quote', 'quote_es', 'quote_pt'
    ], 'Testimonials')

    # FAQs
    check_empty_fields(FAQ, [
        'question', 'question_es', 'question_pt',
        'answer', 'answer_es', 'answer_pt'
    ], 'FAQs')

    # Offices
    check_empty_fields(Office, [
        'name', 'name_es', 'name_pt',
        'city', 'city_es', 'city_pt',
        'address', 'address_es', 'address_pt',
        'working_hours', 'working_hours_es', 'working_hours_pt'
    ], 'Offices')

    # Statistics
    check_empty_fields(Statistic, [
        'label', 'label_es', 'label_pt',
        'description', 'description_es', 'description_pt'
    ], 'Statistics')

    print("\n")


if __name__ == '__main__':
    main()
