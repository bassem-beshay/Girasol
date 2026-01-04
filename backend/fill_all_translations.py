# -*- coding: utf-8 -*-
"""
Fill all missing translations for all models.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourFAQ, EarlyBookingOffer
)
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.blog.models import Category as BlogCategory, Tag, Post
from apps.reviews.models import Review, ReviewImage, Testimonial
from apps.contact.models import FAQ, Office, Statistic

# Translation dictionaries for common terms
COMMON_TRANSLATIONS = {
    # Tour Types
    'Multi-Day Package': {'es': 'Paquete de Varios Dias', 'pt': 'Pacote de Varios Dias'},
    'Day Trip': {'es': 'Excursion de un Dia', 'pt': 'Passeio de um Dia'},
    'Multi Destination': {'es': 'Multi Destino', 'pt': 'Multi Destino'},
    'Nile Cruise': {'es': 'Crucero por el Nilo', 'pt': 'Cruzeiro pelo Nilo'},
    'Private Tour': {'es': 'Tour Privado', 'pt': 'Tour Privado'},
    'Group Tour': {'es': 'Tour en Grupo', 'pt': 'Tour em Grupo'},
    'Adventure': {'es': 'Aventura', 'pt': 'Aventura'},
    'Cultural': {'es': 'Cultural', 'pt': 'Cultural'},
    'Beach': {'es': 'Playa', 'pt': 'Praia'},
    'Desert': {'es': 'Desierto', 'pt': 'Deserto'},

    # Common words
    'Expert Guides': {'es': 'Guias Expertos', 'pt': 'Guias Especializados'},
    'Professional Guide': {'es': 'Guia Profesional', 'pt': 'Guia Profissional'},
    'Small Groups': {'es': 'Grupos Pequenos', 'pt': 'Grupos Pequenos'},
    'Luxury Experience': {'es': 'Experiencia de Lujo', 'pt': 'Experiencia de Luxo'},
    'All Inclusive': {'es': 'Todo Incluido', 'pt': 'Tudo Incluido'},
    'Premium Service': {'es': 'Servicio Premium', 'pt': 'Servico Premium'},
    'Airport Transfer': {'es': 'Traslado al Aeropuerto', 'pt': 'Transfer do Aeroporto'},
    'Hotel Pickup': {'es': 'Recogida en Hotel', 'pt': 'Busca no Hotel'},

    # Meals
    'Breakfast': {'es': 'Desayuno', 'pt': 'Cafe da Manha'},
    'Lunch': {'es': 'Almuerzo', 'pt': 'Almoco'},
    'Dinner': {'es': 'Cena', 'pt': 'Jantar'},
    'Breakfast, Lunch': {'es': 'Desayuno, Almuerzo', 'pt': 'Cafe da Manha, Almoco'},
    'Breakfast, Lunch, Dinner': {'es': 'Desayuno, Almuerzo, Cena', 'pt': 'Cafe da Manha, Almoco, Jantar'},
    'Breakfast, Dinner': {'es': 'Desayuno, Cena', 'pt': 'Cafe da Manha, Jantar'},

    # Cities
    'Cairo': {'es': 'El Cairo', 'pt': 'Cairo'},
    'Luxor': {'es': 'Luxor', 'pt': 'Luxor'},
    'Aswan': {'es': 'Asuan', 'pt': 'Aswan'},
    'Alexandria': {'es': 'Alejandria', 'pt': 'Alexandria'},
    'Sharm El Sheikh': {'es': 'Sharm El Sheikh', 'pt': 'Sharm El Sheikh'},
    'Hurghada': {'es': 'Hurghada', 'pt': 'Hurghada'},
    'Giza': {'es': 'Guiza', 'pt': 'Gize'},

    # Tags
    'History': {'es': 'Historia', 'pt': 'Historia'},
    'Culture': {'es': 'Cultura', 'pt': 'Cultura'},
    'Diving': {'es': 'Buceo', 'pt': 'Mergulho'},
    'Temples': {'es': 'Templos', 'pt': 'Templos'},
    'Pyramids': {'es': 'Piramides', 'pt': 'Piramides'},
    'Museum': {'es': 'Museo', 'pt': 'Museu'},
    'Nile': {'es': 'Nilo', 'pt': 'Nilo'},
    'Red Sea': {'es': 'Mar Rojo', 'pt': 'Mar Vermelho'},
    'Ancient': {'es': 'Antiguo', 'pt': 'Antigo'},
    'Pharaonic': {'es': 'Faraonico', 'pt': 'Faraonico'},
}

def translate_text(text, lang):
    """Translate text to Spanish or Portuguese."""
    if not text:
        return ''

    # Check if exact match exists
    if text in COMMON_TRANSLATIONS:
        return COMMON_TRANSLATIONS[text][lang]

    # Try to translate word by word for simple texts
    result = text
    for en, trans in COMMON_TRANSLATIONS.items():
        if en.lower() in result.lower():
            result = result.replace(en, trans[lang])

    # If still same, create basic translation
    if result == text:
        if lang == 'es':
            return f"{text} (ES)"
        else:
            return f"{text} (PT)"

    return result


def generate_description_translation(text, lang):
    """Generate description translation."""
    if not text:
        return ''

    # Basic translations for descriptions
    if lang == 'es':
        replacements = {
            'Explore': 'Explora',
            'Visit': 'Visita',
            'Discover': 'Descubre',
            'Experience': 'Experimenta',
            'Enjoy': 'Disfruta',
            'includes': 'incluye',
            'features': 'cuenta con',
            'with': 'con',
            'and': 'y',
            'the': 'el/la',
            'tour': 'tour',
            'trip': 'viaje',
            'day': 'dia',
            'night': 'noche',
            'hotel': 'hotel',
            'transfer': 'traslado',
            'guide': 'guia',
            'meal': 'comida',
            'breakfast': 'desayuno',
            'lunch': 'almuerzo',
            'dinner': 'cena',
            'ancient': 'antiguo',
            'temple': 'templo',
            'pyramid': 'piramide',
            'museum': 'museo',
            'river': 'rio',
            'desert': 'desierto',
            'beach': 'playa',
            'sea': 'mar',
            'city': 'ciudad',
            'professional': 'profesional',
            'expert': 'experto',
            'luxury': 'lujo',
            'comfortable': 'comodo',
            'air-conditioned': 'con aire acondicionado',
            'private': 'privado',
            'group': 'grupo',
            'small': 'pequeno',
        }
    else:  # Portuguese
        replacements = {
            'Explore': 'Explore',
            'Visit': 'Visite',
            'Discover': 'Descubra',
            'Experience': 'Experimente',
            'Enjoy': 'Aproveite',
            'includes': 'inclui',
            'features': 'apresenta',
            'with': 'com',
            'and': 'e',
            'the': 'o/a',
            'tour': 'tour',
            'trip': 'viagem',
            'day': 'dia',
            'night': 'noite',
            'hotel': 'hotel',
            'transfer': 'transfer',
            'guide': 'guia',
            'meal': 'refeicao',
            'breakfast': 'cafe da manha',
            'lunch': 'almoco',
            'dinner': 'jantar',
            'ancient': 'antigo',
            'temple': 'templo',
            'pyramid': 'piramide',
            'museum': 'museu',
            'river': 'rio',
            'desert': 'deserto',
            'beach': 'praia',
            'sea': 'mar',
            'city': 'cidade',
            'professional': 'profissional',
            'expert': 'especialista',
            'luxury': 'luxo',
            'comfortable': 'confortavel',
            'air-conditioned': 'com ar condicionado',
            'private': 'privado',
            'group': 'grupo',
            'small': 'pequeno',
        }

    result = text
    for en, trans in replacements.items():
        result = result.replace(en, trans)
        result = result.replace(en.lower(), trans.lower())
        result = result.replace(en.upper(), trans.upper())
        result = result.replace(en.capitalize(), trans.capitalize())

    return result


def fill_tour_type_translations():
    """Fill TourType translations."""
    print("\nFilling TourType translations...")

    descriptions = {
        'Multi-Day Package': {
            'es': 'Paquetes de varios dias con alojamiento, traslados y tours guiados incluidos.',
            'pt': 'Pacotes de varios dias com hospedagem, transfers e passeios guiados incluidos.'
        },
        'Day Trip': {
            'es': 'Excursiones de un dia para explorar destinos cercanos.',
            'pt': 'Passeios de um dia para explorar destinos proximos.'
        },
        'Multi Destination': {
            'es': 'Tours que combinan multiples paises en un solo viaje.',
            'pt': 'Tours que combinam multiplos paises em uma unica viagem.'
        },
        'Nile Cruise': {
            'es': 'Cruceros de lujo por el Rio Nilo con todas las comodidades.',
            'pt': 'Cruzeiros de luxo pelo Rio Nilo com todas as comodidades.'
        },
        'Private Tour': {
            'es': 'Tours privados personalizados segun sus preferencias.',
            'pt': 'Tours privados personalizados de acordo com suas preferencias.'
        },
        'Group Tour': {
            'es': 'Tours en grupo con guias expertos y precios accesibles.',
            'pt': 'Tours em grupo com guias especializados e precos acessiveis.'
        },
        'Shore Excursion': {
            'es': 'Excursiones en tierra para pasajeros de cruceros.',
            'pt': 'Excursoes em terra para passageiros de cruzeiros.'
        },
    }

    for tour_type in TourType.objects.all():
        updated = False
        name = tour_type.name

        # Name translations
        if not tour_type.name_es:
            tour_type.name_es = translate_text(name, 'es')
            updated = True
        if not tour_type.name_pt:
            tour_type.name_pt = translate_text(name, 'pt')
            updated = True

        # Description translations
        if tour_type.description:
            if not tour_type.description_es:
                if name in descriptions:
                    tour_type.description_es = descriptions[name]['es']
                else:
                    tour_type.description_es = generate_description_translation(tour_type.description, 'es')
                updated = True
            if not tour_type.description_pt:
                if name in descriptions:
                    tour_type.description_pt = descriptions[name]['pt']
                else:
                    tour_type.description_pt = generate_description_translation(tour_type.description, 'pt')
                updated = True

        if updated:
            tour_type.save()
            print(f"  Updated: {name}")


def fill_tour_image_translations():
    """Fill TourImage translations."""
    print("\nFilling TourImage translations...")

    for img in TourImage.objects.all():
        updated = False

        if img.caption:
            if not img.caption_es:
                img.caption_es = generate_description_translation(img.caption, 'es')
                updated = True
            if not img.caption_pt:
                img.caption_pt = generate_description_translation(img.caption, 'pt')
                updated = True

        if img.alt_text:
            if not img.alt_text_es:
                img.alt_text_es = generate_description_translation(img.alt_text, 'es')
                updated = True
            if not img.alt_text_pt:
                img.alt_text_pt = generate_description_translation(img.alt_text, 'pt')
                updated = True

        if updated:
            img.save()

    print(f"  Updated {TourImage.objects.count()} tour images")


def fill_tour_highlight_translations():
    """Fill TourHighlight translations."""
    print("\nFilling TourHighlight translations...")

    highlight_translations = {
        'Expert Guides': {'es': 'Guias Expertos', 'pt': 'Guias Especializados'},
        'Small Groups': {'es': 'Grupos Pequenos', 'pt': 'Grupos Pequenos'},
        'Luxury Transport': {'es': 'Transporte de Lujo', 'pt': 'Transporte de Luxo'},
        'All Inclusive': {'es': 'Todo Incluido', 'pt': 'Tudo Incluido'},
        'Premium Hotels': {'es': 'Hoteles Premium', 'pt': 'Hoteis Premium'},
        'Local Experience': {'es': 'Experiencia Local', 'pt': 'Experiencia Local'},
        'Unique Access': {'es': 'Acceso Exclusivo', 'pt': 'Acesso Exclusivo'},
        'Flexible Schedule': {'es': 'Horario Flexible', 'pt': 'Horario Flexivel'},
        'Family Friendly': {'es': 'Ideal para Familias', 'pt': 'Ideal para Familias'},
        'Adventure Activities': {'es': 'Actividades de Aventura', 'pt': 'Atividades de Aventura'},
    }

    for highlight in TourHighlight.objects.all():
        updated = False

        # Title
        if highlight.title:
            if not highlight.title_es:
                if highlight.title in highlight_translations:
                    highlight.title_es = highlight_translations[highlight.title]['es']
                else:
                    highlight.title_es = generate_description_translation(highlight.title, 'es')
                updated = True
            if not highlight.title_pt:
                if highlight.title in highlight_translations:
                    highlight.title_pt = highlight_translations[highlight.title]['pt']
                else:
                    highlight.title_pt = generate_description_translation(highlight.title, 'pt')
                updated = True

        # Description
        if highlight.description:
            if not highlight.description_es:
                highlight.description_es = generate_description_translation(highlight.description, 'es')
                updated = True
            if not highlight.description_pt:
                highlight.description_pt = generate_description_translation(highlight.description, 'pt')
                updated = True

        if updated:
            highlight.save()

    print(f"  Updated {TourHighlight.objects.count()} tour highlights")


def fill_tour_itinerary_translations():
    """Fill TourItinerary translations."""
    print("\nFilling TourItinerary translations...")

    for itinerary in TourItinerary.objects.all():
        updated = False

        if itinerary.title and not itinerary.title_es:
            itinerary.title_es = generate_description_translation(itinerary.title, 'es')
            updated = True
        if itinerary.title and not itinerary.title_pt:
            itinerary.title_pt = generate_description_translation(itinerary.title, 'pt')
            updated = True

        if itinerary.description and not itinerary.description_es:
            itinerary.description_es = generate_description_translation(itinerary.description, 'es')
            updated = True
        if itinerary.description and not itinerary.description_pt:
            itinerary.description_pt = generate_description_translation(itinerary.description, 'pt')
            updated = True

        if itinerary.locations and not itinerary.locations_es:
            itinerary.locations_es = generate_description_translation(itinerary.locations, 'es')
            updated = True
        if itinerary.locations and not itinerary.locations_pt:
            itinerary.locations_pt = generate_description_translation(itinerary.locations, 'pt')
            updated = True

        if itinerary.meals_included and not itinerary.meals_included_es:
            itinerary.meals_included_es = translate_text(itinerary.meals_included, 'es')
            updated = True
        if itinerary.meals_included and not itinerary.meals_included_pt:
            itinerary.meals_included_pt = translate_text(itinerary.meals_included, 'pt')
            updated = True

        if itinerary.accommodation and not itinerary.accommodation_es:
            itinerary.accommodation_es = generate_description_translation(itinerary.accommodation, 'es')
            updated = True
        if itinerary.accommodation and not itinerary.accommodation_pt:
            itinerary.accommodation_pt = generate_description_translation(itinerary.accommodation, 'pt')
            updated = True

        if updated:
            itinerary.save()

    print(f"  Updated {TourItinerary.objects.count()} tour itineraries")


def fill_tour_inclusion_translations():
    """Fill TourInclusion translations."""
    print("\nFilling TourInclusion translations...")

    inclusions_translations = {
        'Hotel accommodations': {'es': 'Alojamiento en hotel', 'pt': 'Hospedagem em hotel'},
        'Airport transfers': {'es': 'Traslados al aeropuerto', 'pt': 'Transfers do aeroporto'},
        'All meals': {'es': 'Todas las comidas', 'pt': 'Todas as refeicoes'},
        'Professional guide': {'es': 'Guia profesional', 'pt': 'Guia profissional'},
        'Entrance fees': {'es': 'Entradas incluidas', 'pt': 'Ingressos incluidos'},
        'Air-conditioned vehicle': {'es': 'Vehiculo con aire acondicionado', 'pt': 'Veiculo com ar condicionado'},
        'Bottled water': {'es': 'Agua embotellada', 'pt': 'Agua engarrafada'},
        'Tips and gratuities': {'es': 'Propinas', 'pt': 'Gorjetas'},
        'Personal expenses': {'es': 'Gastos personales', 'pt': 'Despesas pessoais'},
        'Travel insurance': {'es': 'Seguro de viaje', 'pt': 'Seguro de viagem'},
        'International flights': {'es': 'Vuelos internacionales', 'pt': 'Voos internacionais'},
        'Domestic flights': {'es': 'Vuelos domesticos', 'pt': 'Voos domesticos'},
        'Visa fees': {'es': 'Tasas de visa', 'pt': 'Taxas de visto'},
    }

    for inclusion in TourInclusion.objects.all():
        updated = False

        if inclusion.item:
            if not inclusion.item_es:
                # Check for exact match first
                matched = False
                for en, trans in inclusions_translations.items():
                    if en.lower() in inclusion.item.lower():
                        inclusion.item_es = inclusion.item.replace(en, trans['es'])
                        matched = True
                        break
                if not matched:
                    inclusion.item_es = generate_description_translation(inclusion.item, 'es')
                updated = True

            if not inclusion.item_pt:
                matched = False
                for en, trans in inclusions_translations.items():
                    if en.lower() in inclusion.item.lower():
                        inclusion.item_pt = inclusion.item.replace(en, trans['pt'])
                        matched = True
                        break
                if not matched:
                    inclusion.item_pt = generate_description_translation(inclusion.item, 'pt')
                updated = True

        if updated:
            inclusion.save()

    print(f"  Updated {TourInclusion.objects.count()} tour inclusions")


def fill_early_booking_translations():
    """Fill EarlyBookingOffer translations."""
    print("\nFilling EarlyBookingOffer translations...")

    for offer in EarlyBookingOffer.objects.all():
        updated = False

        if offer.title and not offer.title_es:
            offer.title_es = offer.title.replace('Early Bird', 'Reserva Anticipada').replace('Early Booking', 'Reserva Anticipada').replace('Special', 'Especial').replace('Discount', 'Descuento')
            updated = True
        if offer.title and not offer.title_pt:
            offer.title_pt = offer.title.replace('Early Bird', 'Reserva Antecipada').replace('Early Booking', 'Reserva Antecipada').replace('Special', 'Especial').replace('Discount', 'Desconto')
            updated = True

        if offer.subtitle and not offer.subtitle_es:
            offer.subtitle_es = generate_description_translation(offer.subtitle, 'es')
            updated = True
        if offer.subtitle and not offer.subtitle_pt:
            offer.subtitle_pt = generate_description_translation(offer.subtitle, 'pt')
            updated = True

        if offer.description and not offer.description_es:
            offer.description_es = generate_description_translation(offer.description, 'es')
            updated = True
        if offer.description and not offer.description_pt:
            offer.description_pt = generate_description_translation(offer.description, 'pt')
            updated = True

        if offer.terms_conditions and not offer.terms_conditions_es:
            offer.terms_conditions_es = generate_description_translation(offer.terms_conditions, 'es')
            updated = True
        if offer.terms_conditions and not offer.terms_conditions_pt:
            offer.terms_conditions_pt = generate_description_translation(offer.terms_conditions, 'pt')
            updated = True

        if offer.cancellation_policy and not offer.cancellation_policy_es:
            offer.cancellation_policy_es = generate_description_translation(offer.cancellation_policy, 'es')
            updated = True
        if offer.cancellation_policy and not offer.cancellation_policy_pt:
            offer.cancellation_policy_pt = generate_description_translation(offer.cancellation_policy, 'pt')
            updated = True

        if offer.badge_text and not offer.badge_text_es:
            offer.badge_text_es = offer.badge_text.replace('Early Bird', 'Anticipado').replace('Special', 'Especial').replace('Limited', 'Limitado')
            updated = True
        if offer.badge_text and not offer.badge_text_pt:
            offer.badge_text_pt = offer.badge_text.replace('Early Bird', 'Antecipado').replace('Special', 'Especial').replace('Limited', 'Limitado')
            updated = True

        if updated:
            offer.save()
            print(f"  Updated: {offer.title}")


def fill_destination_image_translations():
    """Fill DestinationImage translations."""
    print("\nFilling DestinationImage translations...")

    for img in DestinationImage.objects.all():
        updated = False

        if img.caption and not img.caption_es:
            img.caption_es = generate_description_translation(img.caption, 'es')
            updated = True
        if img.caption and not img.caption_pt:
            img.caption_pt = generate_description_translation(img.caption, 'pt')
            updated = True

        if img.alt_text and not img.alt_text_es:
            img.alt_text_es = generate_description_translation(img.alt_text, 'es')
            updated = True
        if img.alt_text and not img.alt_text_pt:
            img.alt_text_pt = generate_description_translation(img.alt_text, 'pt')
            updated = True

        if updated:
            img.save()

    print(f"  Updated {DestinationImage.objects.count()} destination images")


def fill_activity_translations():
    """Fill Activity translations."""
    print("\nFilling Activity translations...")

    for activity in Activity.objects.all():
        updated = False

        if activity.name and not activity.name_es:
            activity.name_es = generate_description_translation(activity.name, 'es')
            updated = True
        if activity.name and not activity.name_pt:
            activity.name_pt = generate_description_translation(activity.name, 'pt')
            updated = True

        if activity.description and not activity.description_es:
            activity.description_es = generate_description_translation(activity.description, 'es')
            updated = True
        if activity.description and not activity.description_pt:
            activity.description_pt = generate_description_translation(activity.description, 'pt')
            updated = True

        if updated:
            activity.save()

    print(f"  Updated {Activity.objects.count()} activities")


def fill_tag_translations():
    """Fill Tag translations."""
    print("\nFilling Tag translations...")

    tag_translations = {
        'Beach': {'es': 'Playa', 'pt': 'Praia'},
        'Cairo': {'es': 'El Cairo', 'pt': 'Cairo'},
        'Culture': {'es': 'Cultura', 'pt': 'Cultura'},
        'Desert': {'es': 'Desierto', 'pt': 'Deserto'},
        'Diving': {'es': 'Buceo', 'pt': 'Mergulho'},
        'History': {'es': 'Historia', 'pt': 'Historia'},
        'Luxor': {'es': 'Luxor', 'pt': 'Luxor'},
        'Nile': {'es': 'Nilo', 'pt': 'Nilo'},
        'Pyramids': {'es': 'Piramides', 'pt': 'Piramides'},
        'Temple': {'es': 'Templo', 'pt': 'Templo'},
        'Temples': {'es': 'Templos', 'pt': 'Templos'},
        'Ancient': {'es': 'Antiguo', 'pt': 'Antigo'},
        'Egypt': {'es': 'Egipto', 'pt': 'Egito'},
        'Travel': {'es': 'Viaje', 'pt': 'Viagem'},
        'Tips': {'es': 'Consejos', 'pt': 'Dicas'},
        'Adventure': {'es': 'Aventura', 'pt': 'Aventura'},
        'Photography': {'es': 'Fotografia', 'pt': 'Fotografia'},
        'Food': {'es': 'Gastronomia', 'pt': 'Gastronomia'},
    }

    for tag in Tag.objects.all():
        updated = False

        if tag.name:
            if not tag.name_es:
                if tag.name in tag_translations:
                    tag.name_es = tag_translations[tag.name]['es']
                else:
                    tag.name_es = tag.name
                updated = True
            if not tag.name_pt:
                if tag.name in tag_translations:
                    tag.name_pt = tag_translations[tag.name]['pt']
                else:
                    tag.name_pt = tag.name
                updated = True

        if updated:
            tag.save()
            print(f"  Updated: {tag.name}")


def fill_review_translations():
    """Fill Review translations."""
    print("\nFilling Review translations...")

    for review in Review.objects.all():
        updated = False

        if review.title and not review.title_es:
            review.title_es = generate_description_translation(review.title, 'es')
            updated = True
        if review.title and not review.title_pt:
            review.title_pt = generate_description_translation(review.title, 'pt')
            updated = True

        if review.content and not review.content_es:
            review.content_es = generate_description_translation(review.content, 'es')
            updated = True
        if review.content and not review.content_pt:
            review.content_pt = generate_description_translation(review.content, 'pt')
            updated = True

        if updated:
            review.save()

    print(f"  Updated {Review.objects.count()} reviews")


def fill_review_image_translations():
    """Fill ReviewImage translations."""
    print("\nFilling ReviewImage translations...")

    for img in ReviewImage.objects.all():
        updated = False

        if img.caption and not img.caption_es:
            img.caption_es = generate_description_translation(img.caption, 'es')
            updated = True
        if img.caption and not img.caption_pt:
            img.caption_pt = generate_description_translation(img.caption, 'pt')
            updated = True

        if updated:
            img.save()

    print(f"  Updated {ReviewImage.objects.count()} review images")


def fill_testimonial_translations():
    """Fill Testimonial translations."""
    print("\nFilling Testimonial translations...")

    for testimonial in Testimonial.objects.all():
        updated = False

        if testimonial.quote and not testimonial.quote_es:
            testimonial.quote_es = generate_description_translation(testimonial.quote, 'es')
            updated = True
        if testimonial.quote and not testimonial.quote_pt:
            testimonial.quote_pt = generate_description_translation(testimonial.quote, 'pt')
            updated = True

        if updated:
            testimonial.save()

    print(f"  Updated {Testimonial.objects.count()} testimonials")


def fill_office_translations():
    """Fill Office translations."""
    print("\nFilling Office translations...")

    for office in Office.objects.all():
        updated = False

        if office.name and not office.name_es:
            office.name_es = office.name.replace('Office', 'Oficina').replace('Headquarters', 'Sede Central')
            updated = True
        if office.name and not office.name_pt:
            office.name_pt = office.name.replace('Office', 'Escritorio').replace('Headquarters', 'Sede')
            updated = True

        if office.city and not office.city_es:
            office.city_es = translate_text(office.city, 'es')
            updated = True
        if office.city and not office.city_pt:
            office.city_pt = translate_text(office.city, 'pt')
            updated = True

        if office.address and not office.address_es:
            office.address_es = office.address
            updated = True
        if office.address and not office.address_pt:
            office.address_pt = office.address
            updated = True

        if office.working_hours and not office.working_hours_es:
            office.working_hours_es = office.working_hours.replace('Monday', 'Lunes').replace('Friday', 'Viernes').replace('Saturday', 'Sabado').replace('Sunday', 'Domingo').replace('to', 'a')
            updated = True
        if office.working_hours and not office.working_hours_pt:
            office.working_hours_pt = office.working_hours.replace('Monday', 'Segunda').replace('Friday', 'Sexta').replace('Saturday', 'Sabado').replace('Sunday', 'Domingo').replace('to', 'a')
            updated = True

        if updated:
            office.save()
            print(f"  Updated: {office.name}")


def fill_statistic_translations():
    """Fill Statistic translations."""
    print("\nFilling Statistic translations...")

    for stat in Statistic.objects.all():
        updated = False

        if stat.description and not stat.description_es:
            stat.description_es = generate_description_translation(stat.description, 'es')
            updated = True
        if stat.description and not stat.description_pt:
            stat.description_pt = generate_description_translation(stat.description, 'pt')
            updated = True

        if updated:
            stat.save()

    print(f"  Updated {Statistic.objects.count()} statistics")


def main():
    print("\n" + "#"*60)
    print("# FILLING ALL MISSING TRANSLATIONS")
    print("#"*60)

    fill_tour_type_translations()
    fill_tour_image_translations()
    fill_tour_highlight_translations()
    fill_tour_itinerary_translations()
    fill_tour_inclusion_translations()
    fill_early_booking_translations()
    fill_destination_image_translations()
    fill_activity_translations()
    fill_tag_translations()
    fill_review_translations()
    fill_review_image_translations()
    fill_testimonial_translations()
    fill_office_translations()
    fill_statistic_translations()

    print("\n" + "#"*60)
    print("# DONE!")
    print("#"*60 + "\n")


if __name__ == '__main__':
    main()
