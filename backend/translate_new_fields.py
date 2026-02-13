"""
Script to translate empty Spanish and Portuguese fields for SEO and travel info.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from deep_translator import GoogleTranslator


def translate_text(text, target_lang):
    """Translate text to target language."""
    if not text or not text.strip():
        return ''
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        # Handle long text by splitting
        if len(text) > 4500:
            parts = [text[i:i+4500] for i in range(0, len(text), 4500)]
            translated_parts = [translator.translate(part) for part in parts]
            return ''.join(translated_parts)
        return translator.translate(text)
    except Exception as e:
        print(f"  Error translating: {e}")
        return ''


def translate_model_fields(model, fields_to_translate):
    """Translate fields for a model."""
    model_name = model.__name__
    print(f"\n{'='*60}")
    print(f"Translating {model_name}")
    print('='*60)

    objects = model.objects.all()
    total = objects.count()
    updated = 0

    for i, obj in enumerate(objects, 1):
        obj_name = getattr(obj, 'name', None) or getattr(obj, 'title', None) or str(obj.pk)
        print(f"\n[{i}/{total}] {obj_name}")

        changed = False
        for field in fields_to_translate:
            en_field = field
            es_field = f"{field}_es"
            pt_field = f"{field}_pt"

            en_value = getattr(obj, en_field, '') or ''
            es_value = getattr(obj, es_field, '') or ''
            pt_value = getattr(obj, pt_field, '') or ''

            # Translate to Spanish if empty
            if en_value and not es_value:
                print(f"  Translating {en_field} -> Spanish...")
                translated = translate_text(en_value, 'es')
                if translated:
                    setattr(obj, es_field, translated)
                    changed = True
                    print(f"    Done!")

            # Translate to Portuguese if empty
            if en_value and not pt_value:
                print(f"  Translating {en_field} -> Portuguese...")
                translated = translate_text(en_value, 'pt')
                if translated:
                    setattr(obj, pt_field, translated)
                    changed = True
                    print(f"    Done!")

        if changed:
            obj.save()
            updated += 1
            print(f"  Saved!")

    print(f"\nUpdated {updated}/{total} {model_name} objects")
    return updated


def main():
    print("="*60)
    print("TRANSLATING NEW FIELDS TO SPANISH AND PORTUGUESE")
    print("="*60)

    # Import models
    from apps.destinations.models import Destination
    from apps.tours.models import Tour
    from apps.blog.models import Post

    total_updated = 0

    # Translate Destination fields
    destination_fields = [
        'best_time_to_visit',
        'getting_there',
        'climate_info',
        'meta_title',
        'meta_description',
        'meta_keywords'
    ]
    total_updated += translate_model_fields(Destination, destination_fields)

    # Translate Tour SEO fields
    tour_fields = [
        'meta_title',
        'meta_description',
        'meta_keywords'
    ]
    total_updated += translate_model_fields(Tour, tour_fields)

    # Translate Post SEO fields
    post_fields = [
        'meta_title',
        'meta_description',
        'meta_keywords'
    ]
    total_updated += translate_model_fields(Post, post_fields)

    print("\n" + "="*60)
    print(f"COMPLETED! Total objects updated: {total_updated}")
    print("="*60)


if __name__ == '__main__':
    main()
