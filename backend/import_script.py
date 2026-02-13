#!/usr/bin/env python
import os
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

import django
django.setup()

from apps.tours.models import Tour, EarlyBookingOffer

# Load data
with open('export_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Creating multi-destination tours...")
for tour_data in data['multi_tours']:
    slug = tour_data['slug']
    name = tour_data['name']

    if not Tour.objects.filter(slug=slug).exists():
        print(f'Creating {name}...')
        existing = Tour.objects.first()
        if existing:
            # Create tour using raw SQL to avoid model validation issues
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO tours_tour (
                        name, slug, short_description, description,
                        days, nights, price,
                        is_featured, is_best_seller, is_new, is_multi_destination,
                        category_id, is_published, created_at, updated_at,
                        currency, min_group_size, max_group_size,
                        average_rating, review_count, has_discount,
                        difficulty_level, featured_image, video_url,
                        meta_title, meta_description, meta_keywords,
                        departure_city, languages,
                        name_es, name_pt, short_description_es, short_description_pt,
                        description_es, description_pt
                    ) VALUES (
                        %s, %s, %s, %s,
                        %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, NOW(), NOW(),
                        'USD', 1, 20,
                        0, 0, false,
                        'moderate', 'tours/default.jpg', '',
                        %s, %s, '',
                        'Cairo', 'English',
                        '', '', '', '',
                        '', ''
                    )
                """, [
                    name, slug,
                    tour_data.get('short_description') or 'Multi-destination tour',
                    tour_data.get('description') or 'Explore multiple countries',
                    tour_data['days'], tour_data['nights'], tour_data['price'],
                    tour_data.get('is_featured', False),
                    tour_data.get('is_best_seller', False),
                    tour_data.get('is_new', False),
                    True,  # is_multi_destination
                    existing.category_id, True,
                    name,  # meta_title
                    tour_data.get('short_description') or 'Multi-destination tour'  # meta_description
                ])
            print(f'  Created {name}')
    else:
        t = Tour.objects.get(slug=slug)
        t.is_multi_destination = True
        t.save()
        print(f'Updated {name} - is_multi_destination=True')

print(f'\nTotal multi-destination tours: {Tour.objects.filter(is_multi_destination=True).count()}')
print(f'Total early booking offers: {EarlyBookingOffer.objects.count()}')
