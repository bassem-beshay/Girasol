"""
Update all existing records with missing translations.
This script adds Spanish and Portuguese translations to records that only have English.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.destinations.models import Destination
from apps.tours.models import Tour, TourCategory, TourType
from apps.blog.models import Post, Category as BlogCategory
from apps.contact.models import FAQ, Statistic


# Translation dictionaries for common tourism terms
DESTINATION_TRANSLATIONS = {
    'Cairo': {'es': 'El Cairo', 'pt': 'Cairo'},
    'Luxor': {'es': 'Luxor', 'pt': 'Luxor'},
    'Aswan': {'es': 'Asuan', 'pt': 'Assua'},
    'Hurghada': {'es': 'Hurghada', 'pt': 'Hurghada'},
    'Sharm El Sheikh': {'es': 'Sharm El Sheikh', 'pt': 'Sharm El Sheikh'},
    'Alexandria': {'es': 'Alejandria', 'pt': 'Alexandria'},
    'Dahab': {'es': 'Dahab', 'pt': 'Dahab'},
    'Siwa Oasis': {'es': 'Oasis de Siwa', 'pt': 'Oasis de Siwa'},
}

# Generic translation templates
TOUR_NAME_TEMPLATES = {
    'Day Tour': {'es': 'Tour de un Dia', 'pt': 'Tour de um Dia'},
    'Package': {'es': 'Paquete', 'pt': 'Pacote'},
    'Cruise': {'es': 'Crucero', 'pt': 'Cruzeiro'},
    'Safari': {'es': 'Safari', 'pt': 'Safari'},
    'Adventure': {'es': 'Aventura', 'pt': 'Aventura'},
    'Tour': {'es': 'Tour', 'pt': 'Tour'},
    'Trip': {'es': 'Viaje', 'pt': 'Viagem'},
    'Excursion': {'es': 'Excursion', 'pt': 'Excursao'},
    'Egypt': {'es': 'Egipto', 'pt': 'Egito'},
    'Nile': {'es': 'Nilo', 'pt': 'Nilo'},
    'Pyramids': {'es': 'Piramides', 'pt': 'Piramides'},
    'Desert': {'es': 'Desierto', 'pt': 'Deserto'},
    'Red Sea': {'es': 'Mar Rojo', 'pt': 'Mar Vermelho'},
    'Beach': {'es': 'Playa', 'pt': 'Praia'},
    'Diving': {'es': 'Buceo', 'pt': 'Mergulho'},
    'Snorkeling': {'es': 'Snorkel', 'pt': 'Snorkeling'},
    'Historical': {'es': 'Historico', 'pt': 'Historico'},
    'Cultural': {'es': 'Cultural', 'pt': 'Cultural'},
    'Private': {'es': 'Privado', 'pt': 'Privado'},
    'Group': {'es': 'Grupo', 'pt': 'Grupo'},
    'Luxury': {'es': 'Lujo', 'pt': 'Luxo'},
    'Budget': {'es': 'Economico', 'pt': 'Economico'},
    'Classic': {'es': 'Clasico', 'pt': 'Classico'},
    'Ancient': {'es': 'Antiguo', 'pt': 'Antigo'},
    'Modern': {'es': 'Moderno', 'pt': 'Moderno'},
    'Best': {'es': 'Mejor', 'pt': 'Melhor'},
    'Ultimate': {'es': 'Definitivo', 'pt': 'Definitivo'},
    'Explore': {'es': 'Explorar', 'pt': 'Explorar'},
    'Discover': {'es': 'Descubrir', 'pt': 'Descobrir'},
    'Experience': {'es': 'Experiencia', 'pt': 'Experiencia'},
    'Jordan': {'es': 'Jordania', 'pt': 'Jordania'},
    'Dubai': {'es': 'Dubai', 'pt': 'Dubai'},
}

CATEGORY_TRANSLATIONS = {
    'Cultural & Historical': {'es': 'Cultural e Historico', 'pt': 'Cultural e Historico'},
    'Adventure & Safari': {'es': 'Aventura y Safari', 'pt': 'Aventura e Safari'},
    'Beach & Diving': {'es': 'Playa y Buceo', 'pt': 'Praia e Mergulho'},
    'Nile Cruises': {'es': 'Cruceros por el Nilo', 'pt': 'Cruzeiros no Nilo'},
    'Family Friendly': {'es': 'Familiar', 'pt': 'Familiar'},
    'Luxury': {'es': 'Lujo', 'pt': 'Luxo'},
    'Religious & Spiritual': {'es': 'Religioso y Espiritual', 'pt': 'Religioso e Espiritual'},
    'Wellness & Relaxation': {'es': 'Bienestar y Relajacion', 'pt': 'Bem-estar e Relaxamento'},
    'Day Tours': {'es': 'Tours de un Dia', 'pt': 'Tours de um Dia'},
    'Multi-Day Tours': {'es': 'Tours de Varios Dias', 'pt': 'Tours de Varios Dias'},
    'Shore Excursions': {'es': 'Excursiones en Puerto', 'pt': 'Excursoes em Porto'},
    'Private Tours': {'es': 'Tours Privados', 'pt': 'Tours Privados'},
    'Group Tours': {'es': 'Tours en Grupo', 'pt': 'Tours em Grupo'},
    'Honeymoon': {'es': 'Luna de Miel', 'pt': 'Lua de Mel'},
    'Travel Tips': {'es': 'Consejos de Viaje', 'pt': 'Dicas de Viagem'},
    'Ancient History': {'es': 'Historia Antigua', 'pt': 'Historia Antiga'},
    'Culture & Traditions': {'es': 'Cultura y Tradiciones', 'pt': 'Cultura e Tradicoes'},
    'Food & Cuisine': {'es': 'Gastronomia', 'pt': 'Gastronomia'},
    'Adventure': {'es': 'Aventura', 'pt': 'Aventura'},
}

TOUR_TYPE_TRANSLATIONS = {
    'Multi-Day Package': {'es': 'Paquete de Varios Dias', 'pt': 'Pacote de Varios Dias'},
    'Day Trip': {'es': 'Excursion de un Dia', 'pt': 'Passeio de um Dia'},
    'Nile Cruise': {'es': 'Crucero por el Nilo', 'pt': 'Cruzeiro no Nilo'},
    'Private Tour': {'es': 'Tour Privado', 'pt': 'Tour Privado'},
    'Small Group': {'es': 'Grupo Pequeno', 'pt': 'Grupo Pequeno'},
    'Shore Excursion': {'es': 'Excursion en Puerto', 'pt': 'Excursao em Porto'},
}


def translate_text(text, translations_dict):
    """Simple word-by-word translation using dictionary."""
    if not text:
        return {'es': '', 'pt': ''}

    # Check if exact match exists
    if text in translations_dict:
        return translations_dict[text]

    # Try word-by-word translation
    es_words = []
    pt_words = []

    for word in text.split():
        clean_word = word.strip('.,!?:;')
        if clean_word in translations_dict:
            es_words.append(translations_dict[clean_word]['es'])
            pt_words.append(translations_dict[clean_word]['pt'])
        else:
            es_words.append(word)
            pt_words.append(word)

    return {
        'es': ' '.join(es_words),
        'pt': ' '.join(pt_words)
    }


def update_destinations():
    """Update destinations with missing translations."""
    print("\n[*] Updating Destinations...")
    updated = 0

    for dest in Destination.objects.all():
        changed = False

        # Name translations
        if not dest.name_es and dest.name in DESTINATION_TRANSLATIONS:
            dest.name_es = DESTINATION_TRANSLATIONS[dest.name]['es']
            changed = True
        if not dest.name_pt and dest.name in DESTINATION_TRANSLATIONS:
            dest.name_pt = DESTINATION_TRANSLATIONS[dest.name]['pt']
            changed = True

        # If no specific translation, use same name (for proper nouns)
        if not dest.name_es:
            dest.name_es = dest.name
            changed = True
        if not dest.name_pt:
            dest.name_pt = dest.name
            changed = True

        # Tagline - simple approach
        if dest.tagline and not dest.tagline_es:
            trans = translate_text(dest.tagline, TOUR_NAME_TEMPLATES)
            dest.tagline_es = trans['es']
            changed = True
        if dest.tagline and not dest.tagline_pt:
            trans = translate_text(dest.tagline, TOUR_NAME_TEMPLATES)
            dest.tagline_pt = trans['pt']
            changed = True

        # Description - copy if no translation (better than empty)
        if dest.description and not dest.description_es:
            dest.description_es = dest.description  # Fallback to English
            changed = True
        if dest.description and not dest.description_pt:
            dest.description_pt = dest.description  # Fallback to English
            changed = True

        if changed:
            dest.save()
            updated += 1
            print(f"    [+] Updated: {dest.name}")

    print(f"    Total updated: {updated}")


def update_tour_categories():
    """Update tour categories with missing translations."""
    print("\n[*] Updating Tour Categories...")
    updated = 0

    for cat in TourCategory.objects.all():
        changed = False

        if cat.name in CATEGORY_TRANSLATIONS:
            if not cat.name_es:
                cat.name_es = CATEGORY_TRANSLATIONS[cat.name]['es']
                changed = True
            if not cat.name_pt:
                cat.name_pt = CATEGORY_TRANSLATIONS[cat.name]['pt']
                changed = True
        else:
            trans = translate_text(cat.name, TOUR_NAME_TEMPLATES)
            if not cat.name_es:
                cat.name_es = trans['es']
                changed = True
            if not cat.name_pt:
                cat.name_pt = trans['pt']
                changed = True

        # Description
        if cat.description and not cat.description_es:
            cat.description_es = cat.description
            changed = True
        if cat.description and not cat.description_pt:
            cat.description_pt = cat.description
            changed = True

        if changed:
            cat.save()
            updated += 1
            print(f"    [+] Updated: {cat.name}")

    print(f"    Total updated: {updated}")


def update_tour_types():
    """Update tour types with missing translations."""
    print("\n[*] Updating Tour Types...")
    updated = 0

    for tt in TourType.objects.all():
        changed = False

        if tt.name in TOUR_TYPE_TRANSLATIONS:
            if not tt.name_es:
                tt.name_es = TOUR_TYPE_TRANSLATIONS[tt.name]['es']
                changed = True
            if not tt.name_pt:
                tt.name_pt = TOUR_TYPE_TRANSLATIONS[tt.name]['pt']
                changed = True
        else:
            trans = translate_text(tt.name, TOUR_NAME_TEMPLATES)
            if not tt.name_es:
                tt.name_es = trans['es']
                changed = True
            if not tt.name_pt:
                tt.name_pt = trans['pt']
                changed = True

        if changed:
            tt.save()
            updated += 1
            print(f"    [+] Updated: {tt.name}")

    print(f"    Total updated: {updated}")


def update_tours():
    """Update tours with missing translations."""
    print("\n[*] Updating Tours...")
    updated = 0

    for tour in Tour.objects.all():
        changed = False

        # Name translation
        trans = translate_text(tour.name, TOUR_NAME_TEMPLATES)
        if not tour.name_es:
            tour.name_es = trans['es']
            changed = True
        if not tour.name_pt:
            tour.name_pt = trans['pt']
            changed = True

        # Short description
        if tour.short_description and not tour.short_description_es:
            tour.short_description_es = tour.short_description
            changed = True
        if tour.short_description and not tour.short_description_pt:
            tour.short_description_pt = tour.short_description
            changed = True

        # Description
        if tour.description and not tour.description_es:
            tour.description_es = tour.description
            changed = True
        if tour.description and not tour.description_pt:
            tour.description_pt = tour.description
            changed = True

        if changed:
            tour.save()
            updated += 1
            print(f"    [+] Updated: {tour.name}")

    print(f"    Total updated: {updated}")


def update_blog_categories():
    """Update blog categories with missing translations."""
    print("\n[*] Updating Blog Categories...")
    updated = 0

    for cat in BlogCategory.objects.all():
        changed = False

        if cat.name in CATEGORY_TRANSLATIONS:
            if not cat.name_es:
                cat.name_es = CATEGORY_TRANSLATIONS[cat.name]['es']
                changed = True
            if not cat.name_pt:
                cat.name_pt = CATEGORY_TRANSLATIONS[cat.name]['pt']
                changed = True
        else:
            trans = translate_text(cat.name, TOUR_NAME_TEMPLATES)
            if not cat.name_es:
                cat.name_es = trans['es']
                changed = True
            if not cat.name_pt:
                cat.name_pt = trans['pt']
                changed = True

        # Description
        if cat.description and not cat.description_es:
            cat.description_es = cat.description
            changed = True
        if cat.description and not cat.description_pt:
            cat.description_pt = cat.description
            changed = True

        if changed:
            cat.save()
            updated += 1
            print(f"    [+] Updated: {cat.name}")

    print(f"    Total updated: {updated}")


def update_blog_posts():
    """Update blog posts with missing translations."""
    print("\n[*] Updating Blog Posts...")
    updated = 0

    for post in Post.objects.all():
        changed = False

        # Title
        if post.title and not post.title_es:
            post.title_es = post.title
            changed = True
        if post.title and not post.title_pt:
            post.title_pt = post.title
            changed = True

        # Excerpt
        if post.excerpt and not post.excerpt_es:
            post.excerpt_es = post.excerpt
            changed = True
        if post.excerpt and not post.excerpt_pt:
            post.excerpt_pt = post.excerpt
            changed = True

        # Content
        if post.content and not post.content_es:
            post.content_es = post.content
            changed = True
        if post.content and not post.content_pt:
            post.content_pt = post.content
            changed = True

        if changed:
            post.save()
            updated += 1
            print(f"    [+] Updated: {post.title[:50]}...")

    print(f"    Total updated: {updated}")


def update_faqs():
    """Update FAQs with missing translations."""
    print("\n[*] Updating FAQs...")
    updated = 0

    for faq in FAQ.objects.all():
        changed = False

        # Question
        if faq.question and not faq.question_es:
            faq.question_es = faq.question
            changed = True
        if faq.question and not faq.question_pt:
            faq.question_pt = faq.question
            changed = True

        # Answer
        if faq.answer and not faq.answer_es:
            faq.answer_es = faq.answer
            changed = True
        if faq.answer and not faq.answer_pt:
            faq.answer_pt = faq.answer
            changed = True

        if changed:
            faq.save()
            updated += 1
            print(f"    [+] Updated: {faq.question[:50]}...")

    print(f"    Total updated: {updated}")


def update_statistics():
    """Update statistics with missing translations."""
    print("\n[*] Updating Statistics...")
    updated = 0

    STAT_TRANSLATIONS = {
        'Years of Experience': {'es': 'Anos de Experiencia', 'pt': 'Anos de Experiencia'},
        'Happy Travelers': {'es': 'Viajeros Felices', 'pt': 'Viajantes Felizes'},
        'Satisfaction Rate': {'es': 'Tasa de Satisfaccion', 'pt': 'Taxa de Satisfacao'},
        'Tour Packages': {'es': 'Paquetes de Tours', 'pt': 'Pacotes de Tours'},
        'Average Rating': {'es': 'Calificacion Promedio', 'pt': 'Avaliacao Media'},
        'Local Offices': {'es': 'Oficinas Locales', 'pt': 'Escritorios Locais'},
        'Countries': {'es': 'Paises', 'pt': 'Paises'},
        'Tours': {'es': 'Tours', 'pt': 'Tours'},
        'Destinations': {'es': 'Destinos', 'pt': 'Destinos'},
    }

    for stat in Statistic.objects.all():
        changed = False

        if stat.label in STAT_TRANSLATIONS:
            if not stat.label_es:
                stat.label_es = STAT_TRANSLATIONS[stat.label]['es']
                changed = True
            if not stat.label_pt:
                stat.label_pt = STAT_TRANSLATIONS[stat.label]['pt']
                changed = True
        else:
            if not stat.label_es:
                stat.label_es = stat.label
                changed = True
            if not stat.label_pt:
                stat.label_pt = stat.label
                changed = True

        if changed:
            stat.save()
            updated += 1
            print(f"    [+] Updated: {stat.label}")

    print(f"    Total updated: {updated}")


def main():
    print("\n" + "="*60)
    print("UPDATE MISSING TRANSLATIONS")
    print("="*60)

    update_destinations()
    update_tour_categories()
    update_tour_types()
    update_tours()
    update_blog_categories()
    update_blog_posts()
    update_faqs()
    update_statistics()

    print("\n" + "="*60)
    print("DONE! All missing translations have been filled.")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
