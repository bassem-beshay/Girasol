# -*- coding: utf-8 -*-
"""
Show sample translations from the database.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import TourCategory, TourType, TourHighlight, TourInclusion
from apps.destinations.models import Destination, Activity
from apps.blog.models import Tag
from apps.contact.models import Office, Statistic


def show_samples():
    print("\n" + "="*70)
    print(" SAMPLE TRANSLATIONS")
    print("="*70)

    # Tour Categories
    print("\n--- TOUR CATEGORIES ---")
    for cat in TourCategory.objects.all()[:3]:
        print(f"\n  EN: {cat.name}")
        print(f"  ES: {cat.name_es}")
        print(f"  PT: {cat.name_pt}")
        if cat.description_es:
            print(f"  Desc ES: {cat.description_es[:60]}...")

    # Tour Types
    print("\n\n--- TOUR TYPES ---")
    for tt in TourType.objects.all()[:3]:
        print(f"\n  EN: {tt.name}")
        print(f"  ES: {tt.name_es}")
        print(f"  PT: {tt.name_pt}")
        if tt.description_es:
            print(f"  Desc ES: {tt.description_es[:60]}...")

    # Destinations
    print("\n\n--- DESTINATIONS ---")
    for dest in Destination.objects.all()[:3]:
        print(f"\n  EN: {dest.name}")
        print(f"  ES: {dest.name_es}")
        print(f"  PT: {dest.name_pt}")
        if dest.tagline_es:
            print(f"  Tagline ES: {dest.tagline_es}")
            print(f"  Tagline PT: {dest.tagline_pt}")

    # Activities
    print("\n\n--- ACTIVITIES ---")
    for act in Activity.objects.all()[:3]:
        print(f"\n  EN: {act.name}")
        print(f"  ES: {act.name_es}")
        print(f"  PT: {act.name_pt}")

    # Tour Highlights
    print("\n\n--- TOUR HIGHLIGHTS ---")
    for hl in TourHighlight.objects.all()[:3]:
        print(f"\n  EN: {hl.title}")
        print(f"  ES: {hl.title_es}")
        print(f"  PT: {hl.title_pt}")

    # Tour Inclusions
    print("\n\n--- TOUR INCLUSIONS ---")
    for inc in TourInclusion.objects.all()[:5]:
        print(f"\n  EN: {inc.item}")
        print(f"  ES: {inc.item_es}")
        print(f"  PT: {inc.item_pt}")

    # Tags
    print("\n\n--- TAGS ---")
    for tag in Tag.objects.all()[:5]:
        print(f"  {tag.name} -> ES: {tag.name_es}, PT: {tag.name_pt}")

    # Offices
    print("\n\n--- OFFICES ---")
    for office in Office.objects.all()[:2]:
        print(f"\n  EN: {office.name}")
        print(f"  ES: {office.name_es}")
        print(f"  PT: {office.name_pt}")
        if office.working_hours_es:
            print(f"  Hours ES: {office.working_hours_es}")
            print(f"  Hours PT: {office.working_hours_pt}")

    # Statistics
    print("\n\n--- STATISTICS ---")
    for stat in Statistic.objects.all()[:3]:
        print(f"\n  EN: {stat.label}")
        print(f"  ES: {stat.label_es}")
        print(f"  PT: {stat.label_pt}")

    print("\n" + "="*70)


if __name__ == '__main__':
    show_samples()
