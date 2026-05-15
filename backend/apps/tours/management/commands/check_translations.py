"""
Check all translatable fields across all content models.
Reports empty ES/PT fields and optionally fills them with '.' placeholder.
"""
from django.core.management.base import BaseCommand
from apps.tours.models import (
    Tour, TourCategory, TourType, TourImage, TourHighlight,
    TourItinerary, TourInclusion, TourPricing, TourFAQ, EarlyBookingOffer,
)
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.blog.models import Post, Category as BlogCategory, Tag
from apps.reviews.models import Review, ReviewImage, Testimonial
from apps.contact.models import FAQ, Office, Statistic


# Define all models and their translatable fields
MODELS_CONFIG = [
    (Tour, ['name', 'short_description', 'description', 'focus_keyphrase', 'semantic_keywords', 'lsi_keywords', 'long_tail_phrases']),
    (TourCategory, ['name', 'description']),
    (TourType, ['name', 'description']),
    (TourImage, ['caption', 'alt_text']),
    (TourHighlight, ['title', 'description']),
    (TourItinerary, ['title', 'description', 'locations', 'meals_included', 'accommodation']),
    (TourInclusion, ['item']),
    (TourPricing, ['season_name']),
    (TourFAQ, ['question', 'answer']),
    (EarlyBookingOffer, ['title', 'subtitle', 'description', 'terms_conditions', 'cancellation_policy', 'badge_text']),
    (Destination, ['name', 'tagline', 'description', 'best_time_to_visit', 'getting_there', 'climate_info', 'focus_keyphrase', 'semantic_keywords', 'lsi_keywords', 'long_tail_phrases']),
    (DestinationImage, ['caption', 'alt_text']),
    (Activity, ['name', 'description']),
    (BlogCategory, ['name', 'description']),
    (Tag, ['name']),
    (Post, ['title', 'excerpt', 'content', 'focus_keyphrase', 'semantic_keywords', 'lsi_keywords', 'long_tail_phrases']),
    (Review, ['title', 'content']),
    (ReviewImage, ['caption']),
    (Testimonial, ['quote']),
    (FAQ, ['question', 'answer']),
    (Office, ['name', 'city', 'address', 'working_hours']),
    (Statistic, ['label', 'description']),
]

LANGUAGES = ['es', 'pt']


class Command(BaseCommand):
    help = 'Check and optionally fill empty translation fields'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fill',
            action='store_true',
            help='Fill empty fields with "." placeholder',
        )

    def handle(self, *args, **options):
        fill = options['fill']
        total_empty = 0
        total_filled = 0

        for model_class, fields in MODELS_CONFIG:
            model_name = model_class.__name__
            objects = model_class.objects.all()
            count = objects.count()

            if count == 0:
                continue

            model_empty = 0

            for obj in objects:
                obj_label = str(obj)[:60]
                obj_changed = False

                for field in fields:
                    # Check if the English field has content
                    en_value = getattr(obj, field, None)
                    if not en_value:
                        continue  # Skip if English is also empty

                    for lang in LANGUAGES:
                        lang_field = f'{field}_{lang}'
                        if not hasattr(obj, lang_field):
                            continue

                        value = getattr(obj, lang_field, None)
                        if not value or (isinstance(value, str) and not value.strip()):
                            total_empty += 1
                            model_empty += 1

                            if fill:
                                setattr(obj, lang_field, '.')
                                obj_changed = True
                                total_filled += 1

                if obj_changed:
                    obj.save()

            if model_empty > 0:
                self.stdout.write(
                    self.style.WARNING(f'  {model_name}: {model_empty} empty fields ({count} objects)')
                )

        self.stdout.write('')
        self.stdout.write(self.style.ERROR(f'Total empty translation fields: {total_empty}'))

        if fill:
            self.stdout.write(self.style.SUCCESS(f'Filled {total_filled} fields with "."'))
        else:
            self.stdout.write(self.style.NOTICE('Run with --fill to fill empty fields with "." placeholder'))
