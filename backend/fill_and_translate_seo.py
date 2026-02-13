"""
Script to fill SEO fields in English and translate to Spanish/Portuguese.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from deep_translator import GoogleTranslator


def translate_text(text, target_lang, max_length=None):
    """Translate text to target language."""
    if not text or not text.strip():
        return ''
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        if len(text) > 4500:
            parts = [text[i:i+4500] for i in range(0, len(text), 4500)]
            translated_parts = [translator.translate(part) for part in parts]
            result = ''.join(translated_parts)
        else:
            result = translator.translate(text)

        # Truncate if max_length specified
        if max_length and len(result) > max_length:
            result = result[:max_length-3] + '...'
        return result
    except Exception as e:
        print(f"  Error translating: {e}")
        return ''


def truncate(text, max_length):
    """Truncate text to max length."""
    if not text:
        return ''
    text = text.strip()
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + '...'


def generate_keywords(name, category=None, destinations=None):
    """Generate keywords from name and related data."""
    keywords = []

    # Add words from name
    words = name.replace('-', ' ').replace(':', ' ').split()
    keywords.extend([w.lower() for w in words if len(w) > 3])

    # Add category
    if category:
        keywords.append(category.lower())

    # Add destinations
    if destinations:
        for dest in destinations[:3]:
            keywords.append(dest.lower())

    # Add common tourism keywords
    keywords.extend(['egypt', 'tour', 'travel'])

    # Remove duplicates and join
    seen = set()
    unique = []
    for k in keywords:
        if k not in seen:
            seen.add(k)
            unique.append(k)

    return ', '.join(unique[:10])


def fill_tour_seo():
    """Fill SEO fields for Tours."""
    from apps.tours.models import Tour

    print("\n" + "="*60)
    print("FILLING SEO FOR TOURS")
    print("="*60)

    tours = Tour.objects.all()
    total = tours.count()
    updated = 0

    for i, tour in enumerate(tours, 1):
        print(f"\n[{i}/{total}] {tour.name}")
        changed = False

        # Generate meta_title if empty
        if not tour.meta_title:
            tour.meta_title = truncate(f"{tour.name} | Girasol Tours Egypt", 70)
            changed = True
            print(f"  Generated meta_title: {tour.meta_title}")

        # Generate meta_description if empty
        if not tour.meta_description:
            desc = tour.short_description or tour.description
            tour.meta_description = truncate(desc, 160)
            changed = True
            print(f"  Generated meta_description")

        # Generate meta_keywords if empty
        if not tour.meta_keywords:
            destinations = [d.name for d in tour.destinations.all()]
            category = tour.category.name if tour.category else None
            tour.meta_keywords = generate_keywords(tour.name, category, destinations)
            changed = True
            print(f"  Generated meta_keywords: {tour.meta_keywords}")

        # Translate to Spanish
        if tour.meta_title and not tour.meta_title_es:
            print(f"  Translating meta_title -> Spanish...")
            tour.meta_title_es = translate_text(tour.meta_title, 'es', 70)

        if tour.meta_description and not tour.meta_description_es:
            print(f"  Translating meta_description -> Spanish...")
            tour.meta_description_es = translate_text(tour.meta_description, 'es', 160)

        if tour.meta_keywords and not tour.meta_keywords_es:
            print(f"  Translating meta_keywords -> Spanish...")
            tour.meta_keywords_es = translate_text(tour.meta_keywords, 'es', 255)

        # Translate to Portuguese
        if tour.meta_title and not tour.meta_title_pt:
            print(f"  Translating meta_title -> Portuguese...")
            tour.meta_title_pt = translate_text(tour.meta_title, 'pt', 70)

        if tour.meta_description and not tour.meta_description_pt:
            print(f"  Translating meta_description -> Portuguese...")
            tour.meta_description_pt = translate_text(tour.meta_description, 'pt', 160)

        if tour.meta_keywords and not tour.meta_keywords_pt:
            print(f"  Translating meta_keywords -> Portuguese...")
            tour.meta_keywords_pt = translate_text(tour.meta_keywords, 'pt', 255)

        if changed or tour.meta_title_es or tour.meta_title_pt:
            tour.save()
            updated += 1
            print(f"  Saved!")

    print(f"\nUpdated {updated}/{total} Tours")
    return updated


def fill_post_seo():
    """Fill SEO fields for Posts."""
    from apps.blog.models import Post

    print("\n" + "="*60)
    print("FILLING SEO FOR POSTS")
    print("="*60)

    posts = Post.objects.all()
    total = posts.count()
    updated = 0

    for i, post in enumerate(posts, 1):
        print(f"\n[{i}/{total}] {post.title}")
        changed = False

        # Generate meta_title if empty
        if not post.meta_title:
            post.meta_title = truncate(f"{post.title} | Girasol Tours Blog", 70)
            changed = True
            print(f"  Generated meta_title")

        # Generate meta_description if empty
        if not post.meta_description:
            desc = post.excerpt or post.content
            post.meta_description = truncate(desc, 160)
            changed = True
            print(f"  Generated meta_description")

        # Generate meta_keywords if empty
        if not post.meta_keywords:
            category = post.category.name if post.category else None
            tags = [t.name for t in post.tags.all()]
            keywords = []
            if category:
                keywords.append(category.lower())
            keywords.extend([t.lower() for t in tags])
            words = post.title.replace('-', ' ').replace(':', ' ').split()
            keywords.extend([w.lower() for w in words if len(w) > 3])
            keywords.extend(['egypt', 'travel', 'blog'])

            seen = set()
            unique = []
            for k in keywords:
                if k not in seen:
                    seen.add(k)
                    unique.append(k)

            post.meta_keywords = ', '.join(unique[:10])
            changed = True
            print(f"  Generated meta_keywords: {post.meta_keywords}")

        # Translate to Spanish
        if post.meta_title and not post.meta_title_es:
            print(f"  Translating meta_title -> Spanish...")
            post.meta_title_es = translate_text(post.meta_title, 'es', 70)

        if post.meta_description and not post.meta_description_es:
            print(f"  Translating meta_description -> Spanish...")
            post.meta_description_es = translate_text(post.meta_description, 'es', 160)

        if post.meta_keywords and not post.meta_keywords_es:
            print(f"  Translating meta_keywords -> Spanish...")
            post.meta_keywords_es = translate_text(post.meta_keywords, 'es', 255)

        # Translate to Portuguese
        if post.meta_title and not post.meta_title_pt:
            print(f"  Translating meta_title -> Portuguese...")
            post.meta_title_pt = translate_text(post.meta_title, 'pt', 70)

        if post.meta_description and not post.meta_description_pt:
            print(f"  Translating meta_description -> Portuguese...")
            post.meta_description_pt = translate_text(post.meta_description, 'pt', 160)

        if post.meta_keywords and not post.meta_keywords_pt:
            print(f"  Translating meta_keywords -> Portuguese...")
            post.meta_keywords_pt = translate_text(post.meta_keywords, 'pt', 255)

        if changed or post.meta_title_es or post.meta_title_pt:
            post.save()
            updated += 1
            print(f"  Saved!")

    print(f"\nUpdated {updated}/{total} Posts")
    return updated


def fill_destination_seo():
    """Fill SEO fields for Destinations."""
    from apps.destinations.models import Destination

    print("\n" + "="*60)
    print("FILLING SEO FOR DESTINATIONS")
    print("="*60)

    destinations = Destination.objects.all()
    total = destinations.count()
    updated = 0

    for i, dest in enumerate(destinations, 1):
        print(f"\n[{i}/{total}] {dest.name}")
        changed = False

        # Generate meta_title if empty
        if not dest.meta_title:
            dest.meta_title = truncate(f"{dest.name} Tours & Travel | Girasol Tours", 70)
            changed = True
            print(f"  Generated meta_title")

        # Generate meta_description if empty
        if not dest.meta_description:
            tagline = dest.tagline or ''
            desc = dest.description or ''
            combined = f"{tagline} {desc}".strip()
            dest.meta_description = truncate(combined, 160)
            changed = True
            print(f"  Generated meta_description")

        # Generate meta_keywords if empty
        if not dest.meta_keywords:
            keywords = [dest.name.lower(), dest.country.lower() if dest.country else '']
            if dest.region:
                keywords.append(dest.region.lower())
            keywords.extend(['tours', 'travel', 'vacation', 'holiday'])
            keywords = [k for k in keywords if k]
            dest.meta_keywords = ', '.join(keywords[:10])
            changed = True
            print(f"  Generated meta_keywords: {dest.meta_keywords}")

        # Translate to Spanish
        if dest.meta_title and not dest.meta_title_es:
            print(f"  Translating meta_title -> Spanish...")
            dest.meta_title_es = translate_text(dest.meta_title, 'es', 70)

        if dest.meta_description and not dest.meta_description_es:
            print(f"  Translating meta_description -> Spanish...")
            dest.meta_description_es = translate_text(dest.meta_description, 'es', 160)

        if dest.meta_keywords and not dest.meta_keywords_es:
            print(f"  Translating meta_keywords -> Spanish...")
            dest.meta_keywords_es = translate_text(dest.meta_keywords, 'es', 255)

        # Translate to Portuguese
        if dest.meta_title and not dest.meta_title_pt:
            print(f"  Translating meta_title -> Portuguese...")
            dest.meta_title_pt = translate_text(dest.meta_title, 'pt', 70)

        if dest.meta_description and not dest.meta_description_pt:
            print(f"  Translating meta_description -> Portuguese...")
            dest.meta_description_pt = translate_text(dest.meta_description, 'pt', 160)

        if dest.meta_keywords and not dest.meta_keywords_pt:
            print(f"  Translating meta_keywords -> Portuguese...")
            dest.meta_keywords_pt = translate_text(dest.meta_keywords, 'pt', 255)

        if changed or dest.meta_title_es or dest.meta_title_pt:
            dest.save()
            updated += 1
            print(f"  Saved!")

    print(f"\nUpdated {updated}/{total} Destinations")
    return updated


def main():
    print("="*60)
    print("FILLING AND TRANSLATING SEO FIELDS")
    print("="*60)

    total = 0
    total += fill_destination_seo()
    total += fill_tour_seo()
    total += fill_post_seo()

    print("\n" + "="*60)
    print(f"COMPLETED! Total objects updated: {total}")
    print("="*60)


if __name__ == '__main__':
    main()
