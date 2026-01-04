"""
Test API language switching.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.test import RequestFactory
from rest_framework.request import Request

from apps.tours.serializers import TourListSerializer
from apps.destinations.serializers import DestinationListSerializer
from apps.blog.serializers import PostListSerializer
from apps.contact.serializers import FAQSerializer, StatisticSerializer

from apps.tours.models import Tour
from apps.destinations.models import Destination
from apps.blog.models import Post
from apps.contact.models import FAQ, Statistic


def create_request(language):
    factory = RequestFactory()
    request = factory.get('/')
    request.META['HTTP_ACCEPT_LANGUAGE'] = language
    return Request(request)


def test_serializer(model_class, serializer_class, name_field, label):
    print(f"\n{'='*60}")
    print(f"Testing: {label}")
    print('='*60)

    item = model_class.objects.first()
    if not item:
        print("  No data found")
        return

    print(f"  Original (EN): {getattr(item, name_field)}")
    print(f"  Spanish (ES): {getattr(item, name_field + '_es', 'N/A')}")
    print(f"  Portuguese (PT): {getattr(item, name_field + '_pt', 'N/A')}")

    print(f"\n  API Response Test:")

    for lang in ['en', 'es', 'pt']:
        request = create_request(lang)
        serializer = serializer_class(item, context={'request': request})
        data = serializer.data

        value = data.get(name_field, 'N/A')
        # Truncate if too long
        if len(str(value)) > 50:
            value = str(value)[:50] + '...'

        # Check if language suffixes are removed
        has_suffixes = name_field + '_es' in data or name_field + '_pt' in data

        print(f"    [{lang.upper()}] {name_field}: {value}")
        if has_suffixes:
            print(f"         [WARNING] Language suffixes still in response!")
        else:
            print(f"         [OK] Language suffixes removed")


def main():
    print("\n" + "#"*60)
    print("# API LANGUAGE SWITCHING TEST")
    print("#"*60)

    test_serializer(Tour, TourListSerializer, 'name', 'Tours')
    test_serializer(Destination, DestinationListSerializer, 'name', 'Destinations')
    test_serializer(Post, PostListSerializer, 'title', 'Blog Posts')
    test_serializer(FAQ, FAQSerializer, 'question', 'FAQs')
    test_serializer(Statistic, StatisticSerializer, 'label', 'Statistics')

    print("\n" + "#"*60)
    print("# TEST COMPLETE")
    print("#"*60 + "\n")


if __name__ == '__main__':
    main()
