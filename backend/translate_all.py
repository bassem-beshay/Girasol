"""
Translation script for all dynamic content.
Translates all empty _es and _pt fields from English.
"""
import os
import sys
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from deep_translator import GoogleTranslator
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.tours.models import (
    Tour, TourCategory, TourType, TourImage, TourHighlight,
    TourItinerary, TourInclusion, TourPricing, TourFAQ, EarlyBookingOffer
)
from apps.blog.models import Post, Category as BlogCategory, Tag


def translate_text(text, target_lang):
    """Translate text to target language."""
    if not text or text.strip() == '':
        return ''
    try:
        # Split long text into chunks if needed (Google Translate limit is ~5000 chars)
        if len(text) > 4500:
            chunks = []
            current_chunk = ""
            sentences = text.split('. ')
            for sentence in sentences:
                if len(current_chunk) + len(sentence) < 4500:
                    current_chunk += sentence + '. '
                else:
                    if current_chunk:
                        chunks.append(current_chunk)
                    current_chunk = sentence + '. '
            if current_chunk:
                chunks.append(current_chunk)

            translated_chunks = []
            for chunk in chunks:
                translated = GoogleTranslator(source='en', target=target_lang).translate(chunk)
                translated_chunks.append(translated)
                time.sleep(0.3)  # Rate limiting
            return ' '.join(translated_chunks)
        else:
            result = GoogleTranslator(source='en', target=target_lang).translate(text)
            time.sleep(0.2)  # Rate limiting
            return result
    except Exception as e:
        print(f"  Error translating: {e}")
        return text  # Return original if translation fails


def needs_translation(original, translated):
    """Check if field needs translation (empty or same as original)."""
    if not translated or translated.strip() == '':
        return True
    if translated.strip() == original.strip():
        return True
    return False


def translate_model_fields(model_class, field_mapping, model_name):
    """
    Translate fields for a model.
    field_mapping: dict of {source_field: (es_field, pt_field)}
    """
    print(f"\n{'='*50}")
    print(f"Translating {model_name}...")
    print(f"{'='*50}")

    objects = model_class.objects.all()
    total = objects.count()
    translated_count = 0

    for idx, obj in enumerate(objects, 1):
        changed = False
        obj_name = getattr(obj, 'name', None) or getattr(obj, 'title', None) or getattr(obj, 'item', None) or str(obj.pk)
        if len(str(obj_name)) > 40:
            obj_name = str(obj_name)[:40] + "..."

        for source_field, (es_field, pt_field) in field_mapping.items():
            source_value = getattr(obj, source_field, '')
            if not source_value:
                continue

            # Translate to Spanish
            current_es = getattr(obj, es_field, '')
            if needs_translation(source_value, current_es):
                print(f"  [{idx}/{total}] {obj_name} - Translating {source_field} to ES...")
                translated_es = translate_text(source_value, 'es')
                setattr(obj, es_field, translated_es)
                changed = True

            # Translate to Portuguese
            current_pt = getattr(obj, pt_field, '')
            if needs_translation(source_value, current_pt):
                print(f"  [{idx}/{total}] {obj_name} - Translating {source_field} to PT...")
                translated_pt = translate_text(source_value, 'pt')
                setattr(obj, pt_field, translated_pt)
                changed = True

        if changed:
            obj.save()
            translated_count += 1

    print(f"Completed {model_name}: {translated_count}/{total} objects updated")
    return translated_count


def main():
    print("\n" + "="*60)
    print("   GIRASOL TOURS - TRANSLATION SCRIPT")
    print("   Translating all content to Spanish & Portuguese")
    print("="*60)

    total_translated = 0

    # 1. Destinations
    total_translated += translate_model_fields(
        Destination,
        {
            'name': ('name_es', 'name_pt'),
            'tagline': ('tagline_es', 'tagline_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Destinations"
    )

    # 2. Destination Images
    total_translated += translate_model_fields(
        DestinationImage,
        {
            'caption': ('caption_es', 'caption_pt'),
            'alt_text': ('alt_text_es', 'alt_text_pt'),
        },
        "Destination Images"
    )

    # 3. Activities
    total_translated += translate_model_fields(
        Activity,
        {
            'name': ('name_es', 'name_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Activities"
    )

    # 4. Tour Categories
    total_translated += translate_model_fields(
        TourCategory,
        {
            'name': ('name_es', 'name_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Tour Categories"
    )

    # 5. Tour Types
    total_translated += translate_model_fields(
        TourType,
        {
            'name': ('name_es', 'name_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Tour Types"
    )

    # 6. Tours
    total_translated += translate_model_fields(
        Tour,
        {
            'name': ('name_es', 'name_pt'),
            'short_description': ('short_description_es', 'short_description_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Tours"
    )

    # 7. Tour Images
    total_translated += translate_model_fields(
        TourImage,
        {
            'caption': ('caption_es', 'caption_pt'),
            'alt_text': ('alt_text_es', 'alt_text_pt'),
        },
        "Tour Images"
    )

    # 8. Tour Highlights
    total_translated += translate_model_fields(
        TourHighlight,
        {
            'title': ('title_es', 'title_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Tour Highlights"
    )

    # 9. Tour Itinerary
    total_translated += translate_model_fields(
        TourItinerary,
        {
            'title': ('title_es', 'title_pt'),
            'description': ('description_es', 'description_pt'),
            'locations': ('locations_es', 'locations_pt'),
            'meals_included': ('meals_included_es', 'meals_included_pt'),
            'accommodation': ('accommodation_es', 'accommodation_pt'),
        },
        "Tour Itinerary"
    )

    # 10. Tour Inclusions
    total_translated += translate_model_fields(
        TourInclusion,
        {
            'item': ('item_es', 'item_pt'),
        },
        "Tour Inclusions"
    )

    # 11. Tour Pricing
    total_translated += translate_model_fields(
        TourPricing,
        {
            'season_name': ('season_name_es', 'season_name_pt'),
        },
        "Tour Pricing"
    )

    # 12. Tour FAQs
    total_translated += translate_model_fields(
        TourFAQ,
        {
            'question': ('question_es', 'question_pt'),
            'answer': ('answer_es', 'answer_pt'),
        },
        "Tour FAQs"
    )

    # 13. Early Booking Offers
    total_translated += translate_model_fields(
        EarlyBookingOffer,
        {
            'title': ('title_es', 'title_pt'),
            'subtitle': ('subtitle_es', 'subtitle_pt'),
            'description': ('description_es', 'description_pt'),
            'badge_text': ('badge_text_es', 'badge_text_pt'),
            'terms_conditions': ('terms_conditions_es', 'terms_conditions_pt'),
            'cancellation_policy': ('cancellation_policy_es', 'cancellation_policy_pt'),
        },
        "Early Booking Offers"
    )

    # 14. Blog Categories
    total_translated += translate_model_fields(
        BlogCategory,
        {
            'name': ('name_es', 'name_pt'),
            'description': ('description_es', 'description_pt'),
        },
        "Blog Categories"
    )

    # 15. Blog Tags
    total_translated += translate_model_fields(
        Tag,
        {
            'name': ('name_es', 'name_pt'),
        },
        "Blog Tags"
    )

    # 16. Blog Posts
    total_translated += translate_model_fields(
        Post,
        {
            'title': ('title_es', 'title_pt'),
            'excerpt': ('excerpt_es', 'excerpt_pt'),
            'content': ('content_es', 'content_pt'),
            'featured_image_alt': ('featured_image_alt_es', 'featured_image_alt_pt'),
        },
        "Blog Posts"
    )

    print("\n" + "="*60)
    print(f"   TRANSLATION COMPLETE!")
    print(f"   Total objects updated: {total_translated}")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
