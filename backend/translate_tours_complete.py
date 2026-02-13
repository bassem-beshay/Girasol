"""
Script to translate ALL Tour-related fields to Spanish and Portuguese.
"""
import os
import sys
import django
import time

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from deep_translator import GoogleTranslator


def translate_text(text, target_lang):
    """Translate text to target language with retry."""
    if not text or not text.strip():
        return ''

    max_retries = 3
    for attempt in range(max_retries):
        try:
            translator = GoogleTranslator(source='en', target=target_lang)
            if len(text) > 4500:
                parts = [text[i:i+4500] for i in range(0, len(text), 4500)]
                translated_parts = [translator.translate(part) for part in parts]
                return ''.join(translated_parts)
            return translator.translate(text)
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                print(f"    Error: {e}")
                return ''


def translate_field(obj, field_name, count_dict):
    """Translate a field to Spanish and Portuguese if empty."""
    en_value = getattr(obj, field_name, '') or ''
    es_field = f"{field_name}_es"
    pt_field = f"{field_name}_pt"
    es_value = getattr(obj, es_field, '') or ''
    pt_value = getattr(obj, pt_field, '') or ''

    changed = False

    if en_value and not es_value:
        print(f"    {field_name} -> ES...", end=' ', flush=True)
        translated = translate_text(en_value, 'es')
        if translated:
            setattr(obj, es_field, translated)
            changed = True
            count_dict['es'] += 1
            print("OK")
        else:
            print("FAILED")

    if en_value and not pt_value:
        print(f"    {field_name} -> PT...", end=' ', flush=True)
        translated = translate_text(en_value, 'pt')
        if translated:
            setattr(obj, pt_field, translated)
            changed = True
            count_dict['pt'] += 1
            print("OK")
        else:
            print("FAILED")

    return changed


def translate_tours():
    """Translate Tour main fields."""
    from apps.tours.models import Tour

    print("\n" + "="*60)
    print("TRANSLATING TOURS")
    print("="*60)

    tours = Tour.objects.all()
    total = tours.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, tour in enumerate(tours, 1):
        print(f"\n[{i}/{total}] {tour.name[:50]}")
        changed = False

        changed |= translate_field(tour, 'name', count)
        changed |= translate_field(tour, 'short_description', count)
        changed |= translate_field(tour, 'description', count)

        if changed:
            tour.save()
            updated += 1

    print(f"\nTours: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_highlights():
    """Translate TourHighlight fields."""
    from apps.tours.models import TourHighlight

    print("\n" + "="*60)
    print("TRANSLATING TOUR HIGHLIGHTS")
    print("="*60)

    highlights = TourHighlight.objects.select_related('tour').all()
    total = highlights.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, h in enumerate(highlights, 1):
        print(f"\n[{i}/{total}] {h.tour.name[:30]} - {h.title[:30]}")
        changed = False

        changed |= translate_field(h, 'title', count)
        changed |= translate_field(h, 'description', count)

        if changed:
            h.save()
            updated += 1

    print(f"\nHighlights: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_itineraries():
    """Translate TourItinerary fields."""
    from apps.tours.models import TourItinerary

    print("\n" + "="*60)
    print("TRANSLATING TOUR ITINERARIES")
    print("="*60)

    itineraries = TourItinerary.objects.select_related('tour').all()
    total = itineraries.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, it in enumerate(itineraries, 1):
        print(f"\n[{i}/{total}] {it.tour.name[:30]} - Day {it.day_number}")
        changed = False

        changed |= translate_field(it, 'title', count)
        changed |= translate_field(it, 'description', count)
        changed |= translate_field(it, 'locations', count)
        changed |= translate_field(it, 'meals_included', count)
        changed |= translate_field(it, 'accommodation', count)

        if changed:
            it.save()
            updated += 1

    print(f"\nItineraries: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_inclusions():
    """Translate TourInclusion fields."""
    from apps.tours.models import TourInclusion

    print("\n" + "="*60)
    print("TRANSLATING TOUR INCLUSIONS")
    print("="*60)

    inclusions = TourInclusion.objects.select_related('tour').all()
    total = inclusions.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, inc in enumerate(inclusions, 1):
        item_preview = (inc.item or '')[:40]
        print(f"\n[{i}/{total}] {item_preview}")
        changed = False

        changed |= translate_field(inc, 'item', count)

        if changed:
            inc.save()
            updated += 1

    print(f"\nInclusions: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_pricing():
    """Translate TourPricing fields."""
    from apps.tours.models import TourPricing

    print("\n" + "="*60)
    print("TRANSLATING TOUR PRICING")
    print("="*60)

    pricings = TourPricing.objects.select_related('tour').all()
    total = pricings.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, p in enumerate(pricings, 1):
        print(f"\n[{i}/{total}] {p.season_name}")
        changed = False

        changed |= translate_field(p, 'season_name', count)

        if changed:
            p.save()
            updated += 1

    print(f"\nPricing: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_faqs():
    """Translate TourFAQ fields."""
    from apps.tours.models import TourFAQ

    print("\n" + "="*60)
    print("TRANSLATING TOUR FAQS")
    print("="*60)

    faqs = TourFAQ.objects.select_related('tour').all()
    total = faqs.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, f in enumerate(faqs, 1):
        print(f"\n[{i}/{total}] {f.question[:50]}")
        changed = False

        changed |= translate_field(f, 'question', count)
        changed |= translate_field(f, 'answer', count)

        if changed:
            f.save()
            updated += 1

    print(f"\nFAQs: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_images():
    """Translate TourImage fields."""
    from apps.tours.models import TourImage

    print("\n" + "="*60)
    print("TRANSLATING TOUR IMAGES")
    print("="*60)

    images = TourImage.objects.select_related('tour').all()
    total = images.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, img in enumerate(images, 1):
        caption = (img.caption or img.alt_text or 'No caption')[:40]
        print(f"\n[{i}/{total}] {caption}")
        changed = False

        changed |= translate_field(img, 'caption', count)
        changed |= translate_field(img, 'alt_text', count)

        if changed:
            img.save()
            updated += 1

    print(f"\nImages: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_early_booking_offers():
    """Translate EarlyBookingOffer fields."""
    from apps.tours.models import EarlyBookingOffer

    print("\n" + "="*60)
    print("TRANSLATING EARLY BOOKING OFFERS")
    print("="*60)

    offers = EarlyBookingOffer.objects.all()
    total = offers.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, o in enumerate(offers, 1):
        print(f"\n[{i}/{total}] {o.title}")
        changed = False

        changed |= translate_field(o, 'title', count)
        changed |= translate_field(o, 'subtitle', count)
        changed |= translate_field(o, 'description', count)
        changed |= translate_field(o, 'terms_conditions', count)
        changed |= translate_field(o, 'cancellation_policy', count)
        changed |= translate_field(o, 'badge_text', count)

        if changed:
            o.save()
            updated += 1

    print(f"\nOffers: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_categories():
    """Translate TourCategory fields."""
    from apps.tours.models import TourCategory

    print("\n" + "="*60)
    print("TRANSLATING TOUR CATEGORIES")
    print("="*60)

    categories = TourCategory.objects.all()
    total = categories.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, cat in enumerate(categories, 1):
        print(f"\n[{i}/{total}] {cat.name}")
        changed = False

        changed |= translate_field(cat, 'name', count)
        changed |= translate_field(cat, 'description', count)

        if changed:
            cat.save()
            updated += 1

    print(f"\nCategories: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def translate_tour_types():
    """Translate TourType fields."""
    from apps.tours.models import TourType

    print("\n" + "="*60)
    print("TRANSLATING TOUR TYPES")
    print("="*60)

    types = TourType.objects.all()
    total = types.count()
    updated = 0
    count = {'es': 0, 'pt': 0}

    for i, t in enumerate(types, 1):
        print(f"\n[{i}/{total}] {t.name}")
        changed = False

        changed |= translate_field(t, 'name', count)
        changed |= translate_field(t, 'description', count)

        if changed:
            t.save()
            updated += 1

    print(f"\nTypes: Updated {updated}/{total} | ES: {count['es']} | PT: {count['pt']}")
    return updated


def main():
    print("="*60)
    print("COMPLETE TOUR TRANSLATION SCRIPT")
    print("="*60)

    total = 0

    total += translate_tour_categories()
    total += translate_tour_types()
    total += translate_tours()
    total += translate_tour_highlights()
    total += translate_tour_itineraries()
    total += translate_tour_inclusions()
    total += translate_tour_pricing()
    total += translate_tour_faqs()
    total += translate_tour_images()
    total += translate_early_booking_offers()

    print("\n" + "="*60)
    print(f"COMPLETED! Total records updated: {total}")
    print("="*60)


if __name__ == '__main__':
    main()
