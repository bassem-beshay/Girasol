# -*- coding: utf-8 -*-
"""
Fill all remaining empty fields.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import TourType, TourItinerary
from apps.contact.models import Statistic


def fill_tour_types():
    """Fill empty Tour Type descriptions."""
    print("\nFilling Tour Type descriptions...")

    descriptions = {
        'Package Tour': {
            'en': 'Complete travel packages including accommodation, transfers, guided tours, and meals for a hassle-free vacation experience.',
            'es': 'Paquetes de viaje completos que incluyen alojamiento, traslados, tours guiados y comidas para unas vacaciones sin preocupaciones.',
            'pt': 'Pacotes de viagem completos que incluem hospedagem, transfers, passeios guiados e refeicoes para ferias sem preocupacoes.'
        },
        'Day Tour': {
            'en': 'Full-day excursions to explore major attractions and landmarks with expert guides, returning the same day.',
            'es': 'Excursiones de un dia completo para explorar las principales atracciones con guias expertos, regresando el mismo dia.',
            'pt': 'Passeios de um dia completo para explorar as principais atracoes com guias especializados, retornando no mesmo dia.'
        },
        'Group Tour': {
            'en': 'Budget-friendly tours with scheduled departures in groups, perfect for solo travelers and those seeking social experiences.',
            'es': 'Tours economicos con salidas programadas en grupo, perfectos para viajeros solos y quienes buscan experiencias sociales.',
            'pt': 'Tours economicos com saidas programadas em grupo, perfeitos para viajantes sozinhos e quem busca experiencias sociais.'
        },
    }

    for tt in TourType.objects.all():
        if not tt.description or not tt.description.strip():
            if tt.name in descriptions:
                tt.description = descriptions[tt.name]['en']
                tt.description_es = descriptions[tt.name]['es']
                tt.description_pt = descriptions[tt.name]['pt']
            else:
                tt.description = f'Explore Egypt with our {tt.name} options, designed for an unforgettable travel experience.'
                tt.description_es = f'Explora Egipto con nuestras opciones de {tt.name_es}, disenadas para una experiencia de viaje inolvidable.'
                tt.description_pt = f'Explore o Egito com nossas opcoes de {tt.name_pt}, projetadas para uma experiencia de viagem inesquecivel.'
            tt.save()
            print(f"  Filled: {tt.name}")


def fill_tour_itineraries():
    """Fill empty Tour Itinerary fields."""
    print("\nFilling Tour Itinerary empty fields...")

    for itin in TourItinerary.objects.all():
        updated = False

        if not itin.meals_included or not itin.meals_included.strip():
            itin.meals_included = 'Breakfast'
            itin.meals_included_es = 'Desayuno'
            itin.meals_included_pt = 'Cafe da manha'
            updated = True

        if not itin.accommodation or not itin.accommodation.strip():
            itin.accommodation = '4-5 Star Hotel'
            itin.accommodation_es = 'Hotel 4-5 Estrellas'
            itin.accommodation_pt = 'Hotel 4-5 Estrelas'
            updated = True

        if updated:
            itin.save()
            print(f"  Filled: Day {itin.day_number} - {itin.tour.name}")


def fill_statistics():
    """Fill empty Statistic descriptions."""
    print("\nFilling Statistic descriptions...")

    stat_descriptions = {
        'Years of Experience': {
            'en': 'Decades of expertise in Egyptian tourism',
            'es': 'Decadas de experiencia en turismo egipcio',
            'pt': 'Decadas de experiencia em turismo egipcio'
        },
        'Years Experience': {
            'en': 'Years of trusted travel expertise',
            'es': 'Anos de experiencia confiable en viajes',
            'pt': 'Anos de experiencia confiavel em viagens'
        },
        'Happy Travelers': {
            'en': 'Satisfied customers from around the world',
            'es': 'Clientes satisfechos de todo el mundo',
            'pt': 'Clientes satisfeitos de todo o mundo'
        },
        'Tours Completed': {
            'en': 'Successful tours delivered with excellence',
            'es': 'Tours exitosos realizados con excelencia',
            'pt': 'Tours bem-sucedidos realizados com excelencia'
        },
        'Destinations': {
            'en': 'Unique destinations across Egypt',
            'es': 'Destinos unicos en todo Egipto',
            'pt': 'Destinos unicos em todo o Egito'
        },
        'Expert Guides': {
            'en': 'Professional certified tour guides',
            'es': 'Guias turisticos profesionales certificados',
            'pt': 'Guias turisticos profissionais certificados'
        },
        'Customer Rating': {
            'en': 'Average rating from verified reviews',
            'es': 'Calificacion promedio de resenas verificadas',
            'pt': 'Classificacao media de avaliacoes verificadas'
        },
        'Countries Served': {
            'en': 'Welcoming travelers from across the globe',
            'es': 'Recibiendo viajeros de todo el mundo',
            'pt': 'Recebendo viajantes de todo o mundo'
        },
        'Local Offices': {
            'en': 'Offices across Egypt for local support',
            'es': 'Oficinas en todo Egipto para soporte local',
            'pt': 'Escritorios em todo o Egito para suporte local'
        },
    }

    for stat in Statistic.objects.all():
        if not stat.description or not stat.description.strip():
            if stat.label in stat_descriptions:
                stat.description = stat_descriptions[stat.label]['en']
                stat.description_es = stat_descriptions[stat.label]['es']
                stat.description_pt = stat_descriptions[stat.label]['pt']
            else:
                stat.description = f'Key metric for {stat.label}'
                stat.description_es = f'Metrica clave para {stat.label_es}'
                stat.description_pt = f'Metrica chave para {stat.label_pt}'
            stat.save()
            print(f"  Filled: {stat.label}")


def main():
    print("\n" + "#"*60)
    print("# FILLING EMPTY FIELDS")
    print("#"*60)

    fill_tour_types()
    fill_tour_itineraries()
    fill_statistics()

    print("\n" + "#"*60)
    print("# DONE!")
    print("#"*60 + "\n")


if __name__ == '__main__':
    main()
