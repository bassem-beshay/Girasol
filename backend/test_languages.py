"""
Test script to verify multilingual API responses.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.test import RequestFactory
from rest_framework.request import Request

# Import serializers
from apps.destinations.serializers import DestinationListSerializer, DestinationDetailSerializer
from apps.tours.serializers import TourListSerializer, TourDetailSerializer, TourCategorySerializer
from apps.blog.serializers import PostListSerializer, CategorySerializer as BlogCategorySerializer
from apps.contact.serializers import FAQSerializer, StatisticSerializer

# Import models
from apps.destinations.models import Destination
from apps.tours.models import Tour, TourCategory
from apps.blog.models import Post, Category as BlogCategory
from apps.contact.models import FAQ, Statistic


def create_request_with_language(language):
    """Create a mock request with Accept-Language header."""
    factory = RequestFactory()
    request = factory.get('/')
    request.META['HTTP_ACCEPT_LANGUAGE'] = language
    return Request(request)


def test_model(model_class, serializer_class, name_field='name', languages=['en', 'es', 'pt']):
    """Test a model with its serializer across all languages."""
    print(f"\n{'='*60}")
    print(f"Testing: {model_class.__name__}")
    print('='*60)

    items = model_class.objects.all()[:2]

    if not items:
        print(f"  [!] No {model_class.__name__} found in database")
        return False

    all_ok = True

    for item in items:
        print(f"\n  Item: {getattr(item, name_field, str(item))}")
        print(f"  {'-'*50}")

        results = {}
        for lang in languages:
            request = create_request_with_language(lang)
            serializer = serializer_class(item, context={'request': request})
            data = serializer.data

            # Get the name field value
            value = data.get(name_field, 'N/A')
            results[lang] = value
            print(f"    [{lang.upper()}] {name_field}: {value[:60]}..." if len(str(value)) > 60 else f"    [{lang.upper()}] {name_field}: {value}")

        # Check if translations are different (they should be for most items)
        unique_values = set(str(v) for v in results.values() if v)
        if len(unique_values) == 1:
            print(f"    [!] WARNING: All languages have same value - translations may be missing")
            all_ok = False
        elif len(unique_values) < 3:
            missing = [l for l, v in results.items() if not v or v == results.get('en')]
            if missing and 'en' not in missing:
                print(f"    [!] WARNING: Missing translations for: {missing}")

    return all_ok


def check_database_translations():
    """Check if translations exist in database."""
    print("\n" + "="*60)
    print("DATABASE TRANSLATION CHECK")
    print("="*60)

    checks = [
        ('Destination', Destination, ['name_es', 'name_pt', 'description_es', 'description_pt']),
        ('Tour', Tour, ['name_es', 'name_pt', 'description_es', 'description_pt']),
        ('TourCategory', TourCategory, ['name_es', 'name_pt', 'description_es', 'description_pt']),
        ('BlogCategory', BlogCategory, ['name_es', 'name_pt']),
        ('Post', Post, ['title_es', 'title_pt', 'content_es', 'content_pt']),
        ('FAQ', FAQ, ['question_es', 'question_pt', 'answer_es', 'answer_pt']),
        ('Statistic', Statistic, ['label_es', 'label_pt']),
    ]

    all_ok = True

    for name, model, fields in checks:
        total = model.objects.count()
        if total == 0:
            print(f"\n  {name}: No records found")
            continue

        print(f"\n  {name} ({total} records):")

        for field in fields:
            # Count non-empty translations
            filled = model.objects.exclude(**{field: ''}).exclude(**{f'{field}__isnull': True}).count()
            percentage = (filled / total) * 100 if total > 0 else 0

            status = "[OK]" if percentage >= 80 else "[!!]" if percentage < 50 else "[!]"
            print(f"    {status} {field}: {filled}/{total} ({percentage:.0f}%)")

            if percentage < 50:
                all_ok = False

    return all_ok


def main():
    print("\n" + "#"*60)
    print("# MULTILINGUAL API TEST")
    print("#"*60)

    # First check database
    db_ok = check_database_translations()

    # Test each serializer
    print("\n" + "#"*60)
    print("# SERIALIZER OUTPUT TEST")
    print("#"*60)

    tests = [
        (Destination, DestinationListSerializer, 'name'),
        (Tour, TourListSerializer, 'name'),
        (TourCategory, TourCategorySerializer, 'name'),
        (BlogCategory, BlogCategorySerializer, 'name'),
        (Post, PostListSerializer, 'title'),
        (FAQ, FAQSerializer, 'question'),
        (Statistic, StatisticSerializer, 'label'),
    ]

    serializer_ok = True
    for model, serializer, field in tests:
        if not test_model(model, serializer, field):
            serializer_ok = False

    # Summary
    print("\n" + "#"*60)
    print("# SUMMARY")
    print("#"*60)

    if db_ok and serializer_ok:
        print("\n  [OK] All translations are working correctly!")
    else:
        if not db_ok:
            print("\n  [!!] Some database translations are missing")
        if not serializer_ok:
            print("\n  [!!] Some serializers may have issues")
        print("\n  Run the seed script to add missing translations:")
        print("  python seed_multilingual_data.py")

    print()


if __name__ == '__main__':
    main()
