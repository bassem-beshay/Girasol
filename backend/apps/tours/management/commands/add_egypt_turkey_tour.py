"""
Management command to add "Treasures of Egypt and Turkey" tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourDeparture
)
from apps.destinations.models import Destination
from datetime import date


class Command(BaseCommand):
    help = 'Add Treasures of Egypt and Turkey 14-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Treasures of Egypt and Turkey tour...')

        # Get or create category and type
        category, _ = TourCategory.objects.get_or_create(
            slug='classic-egypt-tours',
            defaults={'name': 'Classic Egypt Tours', 'name_es': 'Tours Clásicos de Egipto', 'name_pt': 'Tours Clássicos do Egito'}
        )

        tour_type, _ = TourType.objects.get_or_create(
            slug='multi-day-package',
            defaults={'name': 'Multi-Day Package', 'name_es': 'Paquete Multi-Día', 'name_pt': 'Pacote Multi-Dias'}
        )

        # Create the tour
        tour, created = Tour.objects.update_or_create(
            slug='treasures-of-egypt-and-turkey-14-days',
            defaults={
                'name': 'Treasures of Egypt and Turkey',
                'name_es': 'Tesoros de Egipto y Turquía',
                'name_pt': 'Tesouros do Egito e Turquia',
                'short_description': 'Live an Epic 14-Day Journey: Egypt, Cappadocia, and Istanbul! Explore pharaonic wonders, imperial Istanbul, and fairy-tale Cappadocia.',
                'short_description_es': '¡Vive un Viaje Épico de 14 Días: Egipto, Capadocia e Istambul! Explora maravillas faraónicas, la imperial Estambul y la Capadocia de cuento de hadas.',
                'short_description_pt': 'Embarque em uma Jornada Épica de 14 Dias: Egito, Capadócia e Istambul! Explore maravilhas faraônicas, a imperial Istambul e a Capadócia de contos de fadas.',
                'description': '''Begin by exploring the pharaonic wonders of Egypt in Cairo, Giza, Luxor, and Aswan. Then, fly to discover Istanbul, the city of glory, straddling two continents, and end by uncovering the fairy-tale landscapes of Cappadocia, with its natural charms and underground cities. A unique trip that blends history and culture into an unforgettable experience!

**Night Distribution:**
- 09 Nights in Egypt 🇪🇬
- 02 Nights in Istanbul 🇹🇷
- 02 Nights in Cappadocia 🇹🇷

**Includes:**
- 02 domestic flights in Egypt ✈️: Cairo → Luxor and Aswan → Cairo
- 01 domestic flight in Turkey ✈️: Istanbul → Nevsehir (Cappadocia)

**Meal Plan:**
- Cairo: Breakfast + Lunch on tour days
- Nile Cruise: Full Board on board 🚢
- Istanbul: Breakfast + Half Board on tour days

**Tour Format:**
Small group tours and excursions with up to 12 people.

**Accommodation:** Comfort & Good Selection – 4★ Hotels + 5★ Nile Cruise
- Cairo: Azal Pyramids Hotel or similar – 4★ Superior
- Nile Cruise: M/S Solaris Cruise or similar – 5★
- Istanbul: Mina Hotel or similar – 4★
- Cappadocia: Ascension Cave Suites or similar – Cave Hotel ☀️''',
                'description_es': '''Comienza explorando las maravillas faraónicas de Egipto en El Cairo, Guiza, Luxor y Asuán. Luego, vuela a descubrir Estambul, la ciudad de la gloria, puente entre dos continentes, y termina descubriendo los paisajes de cuento de hadas de Capadocia, con sus encantos naturales y ciudades subterráneas. ¡Un viaje único que une historia y cultura en una experiencia inolvidable!

**Distribución de Noches:**
- 09 Noches en Egipto 🇪🇬
- 02 Noches en Estambul 🇹🇷
- 02 Noches en Capadocia 🇹🇷

**Incluye:**
- 02 vuelos internos en Egipto ✈️: El Cairo → Luxor y Asuán → El Cairo
- 01 vuelo interno en Turquía ✈️: Estambul → Nevsehir (Capadocia)

**Régimen de Alimentación:**
- El Cairo: Desayuno + Almuerzo en los días de excursión
- Crucero en el Nilo: Pensión Completa a bordo 🚢
- Estambul: Desayuno + Media Pensión en los días de excursión

**Formato de las Excursiones:**
Excursiones y tours en grupos pequeños de hasta 12 personas.

**Alojamiento:** Confort y Buena Selección – Hoteles de 4★ + Crucero en el Nilo 5★
- El Cairo: Azal Pyramids Hotel o similar – 4★ Superior
- Crucero en el Nilo: M/S Solaris Cruise o similar – 5★
- Estambul: Mina Hotel o similar – 4★
- Capadocia: Ascension Cave Suites o similar – Hotel tipo cueva ☀️''',
                'description_pt': '''Inicie sua aventura desvendando as grandiosas maravilhas faraónicas do Egito, passando por Cairo, Gizé, Luxor e Assuã. Em seguida, siga de avião para desbravar Istambul, a esplendorosa metrópole que é ponte entre dois continentes, e finalize descobrindo os cenários surrealistas e de conto de fadas da Capadócia, com suas formações naturais encantadoras e misteriosas cidades subterrâneas. Uma viagem singular que entrelaça história milenar e cultura vibrante em uma experiência verdadeiramente inesquecível!

**Distribuição das Hospedagens:**
- 09 Noites no Egito 🇪🇬
- 02 Noites em Istambul 🇹🇷
- 02 Noites na Capadócia 🇹🇷

**Inclui:**
- 02 voos domésticos no Egito ✈️: Trecho Cairo → Luxor e Assuan → Cairo
- 01 voo interno na Turquia ✈️: Trecho Istambul → Nevshir (Capadócia)

**Regime de Refeições Incluídas:**
- Cairo: Café da manhã + Almoço nos dias de passeio
- Cruzeiro no Nilo: Pensão Completa a bordo 🚢
- Istambul: Café da manhã + Meia Pensão nos dias de passeio

**Formato dos Passeios e Visitas:**
Passeios e excursões realizados em grupos reduzidos, com no máximo 12 viajantes.

**Hospedagem:** Conforto e Seleção Criteriosa – Hotéis Categoria 4★ + Cruzeiro no Nilo 5★
- Cairo: Azal Pyramids Hotel ou similar – 4★ Superior
- Cruzeiro no Nilo: M/S Solaris Cruise ou similar – 5★
- Istambul: Mina Hotel ou similar – 4★
- Capadócia: Ascension Cave Suites ou similar – Hotel Caverna ☀️''',
                'category': category,
                'tour_type': tour_type,
                'days': 14,
                'nights': 13,
                'price': 2584.00,
                'currency': 'USD',
                'min_group_size': 2,
                'max_group_size': 12,
                'is_featured': False,
                'is_best_seller': False,
                'is_new': True,
                'is_multi_destination': True,
                'difficulty_level': 'moderate',
                'departure_city': 'Cairo',
                'languages': 'English, Spanish, Portuguese',
                'is_published': True,
            }
        )

        # Add destinations
        destination_slugs = ['cairo', 'luxor', 'aswan', 'istanbul', 'cappadocia']
        for slug in destination_slugs:
            try:
                dest = Destination.objects.get(slug=slug)
                tour.destinations.add(dest)
            except Destination.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Destination {slug} not found'))

        # Clear existing related data if updating
        if not created:
            tour.itinerary.all().delete()
            tour.inclusions.all().delete()
            tour.highlights.all().delete()
            tour.departures.all().delete()

        # Add Highlights
        highlights_data = [
            {
                'title': 'Complete and Exclusive Itinerary',
                'title_es': 'Itinerario Completo y Exclusivo',
                'title_pt': 'Roteiro Abrangente e Meticuloso',
                'description': 'Experience the best of Egypt and Istanbul and Cappadocia in one trip!',
                'description_es': '¡Vive lo mejor de Egipto y Estambul y Capadocia en un solo viaje!',
                'description_pt': 'Viva o ápice do Egito e da Turquia em uma única jornada!',
            },
            {
                'title': 'Nile Cruise with Full Board',
                'title_es': 'Crucero en el Nilo con Pensión Completa',
                'title_pt': 'Cruzeiro no Nilo com Pensão Completa',
                'description': 'Enjoy 4 nights on a 5-Star Cruise between Luxor and Aswan with full board.',
                'description_es': 'Disfruta de 4 noches en un Crucero de 5 Estrellas entre Luxor y Asuán con pensión completa.',
                'description_pt': 'Desfrute de 4 pernoites em um luxuoso cruzeiro de 5 Estrelas no trajeto Luxor-Assuão.',
            },
            {
                'title': 'Simplified Logistics with Included Internal Flights',
                'title_es': 'Logística Simplificada con Vuelos Internos Incluidos',
                'title_pt': 'Logística Facilitada com Voos Domésticos Inclusos',
                'description': '3 domestic flights included: Cairo/Luxor, Aswan/Cairo, Istanbul/Cappadocia.',
                'description_es': '3 vuelos domésticos incluidos: El Cairo/Luxor, Asuán/El Cairo, Estambul/Capadocia.',
                'description_pt': '3 voos domésticos inclusos: Cairo/Luxor, Assuã/Cairo, Istambul/Capadócia.',
            },
            {
                'title': 'Carefully Planned Meals',
                'title_es': 'Alimentación Cuidadosamente Planeada',
                'title_pt': 'Plano de Refeições Elaborado com Cuidado',
                'description': 'Breakfast included at all accommodations + half board on tour days + full board on cruise.',
                'description_es': 'Desayuno incluido en todos los alojamientos + media pensión en los días de excursión + pensión completa en el crucero.',
                'description_pt': 'Café da manhã incluso em todas as hospedagens + meia pensão nos dias de passeio + pensão completa no cruzeiro.',
            },
            {
                'title': 'Personalized Experience in Small Groups',
                'title_es': 'Experiencia Personalizada en Grupos Pequeños',
                'title_pt': 'Vivência Personalizada em Grupos Pequenos',
                'description': 'All tours conducted in small groups (max 12), ensuring personalized attention.',
                'description_es': 'Todos los tours se realizan en grupos pequeños (máx. 12), garantizando atención personalizada.',
                'description_pt': 'Todas as visitas são feitas em grupos de tamanho reduzido (máx. 12).',
            },
            {
                'title': 'Cave Hotel Experience in Cappadocia',
                'title_es': 'Experiencia en Hotel Cueva en Capadocia',
                'title_pt': 'Experiência em Hotel Caverna na Capadócia',
                'description': 'Stay in a unique cave-style hotel in Cappadocia for an authentic experience.',
                'description_es': 'Alójate en un hotel tipo cueva único en Capadocia para una experiencia auténtica.',
                'description_pt': 'Hospede-se em um hotel tipo caverna único na Capadócia para uma experiência autêntica.',
            },
        ]

        for i, h in enumerate(highlights_data):
            TourHighlight.objects.create(tour=tour, sort_order=i, **h)

        # Add Itinerary
        itinerary_data = [
            {
                'day_number': 1,
                'title': 'Arrival – Cairo',
                'title_es': 'Llegada – El Cairo',
                'title_pt': 'Chegada – Cairo',
                'description': 'Arrival at Cairo airport according to your own flight. Meet and assist by representative with entry formalities. Transfer to the hotel. Check-in.',
                'description_es': 'Llegada al aeropuerto de El Cairo según su propio vuelo. Recepción por nuestro representante para facilitar los trámites de entrada. Traslado al hotel. Check-in.',
                'description_pt': 'Chegada ao aeroporto do Cairo conforme seu voo próprio. Recepção por nosso representante para auxiliar nas formalidades de entrada. Transfer para o hotel. Check-in.',
                'locations': 'Cairo',
                'meals_included': '',
                'accommodation': 'Azal Pyramids Hotel or similar 4★',
            },
            {
                'day_number': 2,
                'title': 'Cairo – Saqqara',
                'title_es': 'El Cairo – Saqqara',
                'title_pt': 'Cairo – Saqqara',
                'description': 'Visit Saqqara and the King Djoser Complex, the first group of buildings entirely made of stone in human history. See the Step Pyramid built by architect Imhotep, the Heb Sed Court, and visit two Mastabas of ancient nobles. Lunch at a local restaurant.',
                'description_es': 'Visita a Saqqara y el complejo del rey Djoser, el primer grupo de edificios construidos enteramente en piedra en la historia de la humanidad. Vea la Pirámide Escalonada construida por el arquitecto Imhotep, el Patio Heb Sed, y visite dos Mastabas de antiguos nobles. Almuerzo en restaurante local.',
                'description_pt': 'Visite Saqqara e o complexo do Rei Djoser, o primeiro conjunto arquitetônico totalmente edificado em pedra na história da humanidade. Veja a Pirâmide de Degraus erguida pelo arquiteto Imhotep, o Pátio Heb Sed, e visite duas Mastabas de nobres da antiguidade. Almoço em restaurante local.',
                'locations': 'Cairo, Saqqara',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': 'Azal Pyramids Hotel or similar 4★',
            },
            {
                'day_number': 3,
                'title': 'Giza Pyramids and Sphinx – Egyptian Museum',
                'title_es': 'Pirámides de Guiza y la Esfinge – Museo Egipcio',
                'title_pt': 'Pirâmides de Gizé e a Esfinge – Museu Egípcio',
                'description': 'Visit Giza Complex to see Egypt\'s three great pyramids: Cheops, Khafre, and Menkaure. Continue to the panoramic area, Valley Temple of King Khafre and the Sphinx. Visit a Papyrus Gallery. Lunch at a local restaurant. Visit the Egyptian Museum in Tahrir Square.',
                'description_es': 'Visita al Complejo de Guiza para ver las tres grandes pirámides de Egipto: Keops, Kefrén y Micerinos. Continúe al área panorámica, el Templo del Valle del Rey Kefrén y la Esfinge. Visite una Galería de Papiros. Almuerzo en restaurante local. Visite el Museo Egipcio en la Plaza Tahrir.',
                'description_pt': 'Visite o Complexo de Gizé para ver as três grandiosas pirâmides: Quéops, Quéfren e Miquerinos. Continue até o platô panorâmico, o Templo do Vale do Rei Quéfren e a Esfinge. Visite uma galeria de papiros. Almoço em restaurante local. Visite o Museu Egípcio na Praça Tahrir.',
                'locations': 'Giza, Cairo',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': 'Azal Pyramids Hotel or similar 4★',
            },
            {
                'day_number': 4,
                'title': 'Cairo – Free Day',
                'title_es': 'El Cairo – Día Libre',
                'title_pt': 'Cairo – Dia Livre',
                'description': 'Free day for rest or suggested optional tours. Optional: National Museum of Egyptian Civilization + Coptic Christian Cairo + Islamic Cairo with Lunch.',
                'description_es': 'Día libre para descanso o excursiones opcionales sugeridas. Opcional: Museo Nacional de la Civilización Egipcia + El Cairo Copto Cristiano + El Cairo Islámico con Almuerzo.',
                'description_pt': 'Dia livre para descanso ou participação em passeios opcionais sugeridos. Opcional: Museu Nacional da Civilização Egípcia + Cairo Copta + Cairo Islâmico com Almoço.',
                'locations': 'Cairo',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': 'Azal Pyramids Hotel or similar 4★',
            },
            {
                'day_number': 5,
                'title': 'Cairo – Luxor (Flight) – Karnak Temple – Nile Cruise',
                'title_es': 'El Cairo – Luxor (Vuelo) – Templo de Karnak – Crucero en el Nilo',
                'title_pt': 'Cairo – Luxor (Voo) – Templo de Karnak – Cruzeiro no Nilo',
                'description': 'Domestic flight to Luxor. Visit the fabulous Temple of Karnak, one of the largest and oldest temples in the world. Check-in on the 5★ Nile Cruise for 4 nights with Full Board. At sunset, visit the magnificent Luxor Temple.',
                'description_es': 'Vuelo doméstico a Luxor. Visite el fabuloso Templo de Karnak, uno de los templos más grandes y antiguos del mundo. Check-in en el Crucero 5★ en el Nilo por 4 noches con Pensión Completa. Al atardecer, visite el magnífico Templo de Luxor.',
                'description_pt': 'Voo doméstico para Luxor. Visite o fabuloso Templo de Karnak, um dos maiores e mais antigos templos do mundo. Check-in no Cruzeiro 5★ no Nilo por 4 noites com Pensão Completa. Ao pôr do sol, visite o magnífico Templo de Luxor.',
                'locations': 'Cairo, Luxor',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': 'M/S Solaris Cruise or similar 5★',
            },
            {
                'day_number': 6,
                'title': 'Luxor – Esna – Edfu (Nile Cruise)',
                'title_es': 'Luxor – Esna – Edfu (Crucero en el Nilo)',
                'title_pt': 'Luxor – Esna – Edfu (Cruzeiro no Nilo)',
                'description': 'Visit the Valley of the Kings (3 royal tombs), the Two Colossi of Memnon, and the Temple of Queen Hatshepsut. Navigation through Esna Lock to Edfu. Optional: Hot Air Balloon Ride at sunrise.',
                'description_es': 'Visite el Valle de los Reyes (3 tumbas reales), los dos Colosos de Memnón y el Templo de la Reina Hatshepsut. Navegación por la esclusa de Esna hasta Edfu. Opcional: Paseo en Globo Aerostático al amanecer.',
                'description_pt': 'Visite o Vale dos Reis (3 túmulos reais), os dois Colossos de Mêmnon e o Templo da Rainha Hatshepsut. Navegação pela eclusa de Esna até Edfu. Opcional: Passeio de Balão ao nascer do sol.',
                'locations': 'Luxor, Esna, Edfu',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': 'M/S Solaris Cruise or similar 5★',
            },
            {
                'day_number': 7,
                'title': 'Edfu – Kom Ombo – Aswan (Nile Cruise)',
                'title_es': 'Edfu – Kom Ombo – Asuán (Crucero en el Nilo)',
                'title_pt': 'Edfu – Kom Ombo – Assuã (Cruzeiro no Nilo)',
                'description': 'Visit the Temple of Horus in Edfu, one of the best-preserved temples in Egypt. Navigation to Kom Ombo. Visit the Temple of Kom Ombo, the only temple consecrated to two triads of deities. Navigation to Aswan.',
                'description_es': 'Visite el Templo de Horus en Edfu, uno de los templos mejor conservados de Egipto. Navegación a Kom Ombo. Visite el Templo de Kom Ombo, el único templo consagrado a dos tríadas de deidades. Navegación a Asuán.',
                'description_pt': 'Visite o Templo de Hórus em Edfu, um dos mais bem conservados templos do Egito. Navegação até Kom Ombo. Visite o Templo de Kom Ombo, o único templo consagrado a duas tríades de divindades. Navegação até Assuã.',
                'locations': 'Edfu, Kom Ombo, Aswan',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': 'M/S Solaris Cruise or similar 5★',
            },
            {
                'day_number': 8,
                'title': 'Aswan – Philae Island – Felucca Ride',
                'title_es': 'Asuán – Isla de File – Paseo en Faluca',
                'title_pt': 'Assuã – Ilha de Filae – Passeio de Feluca',
                'description': 'Visit the Unfinished Obelisk and Aswan High Dam. Visit Philae Island and the famous Temple of Isis. Afternoon Felucca Ride (traditional sailboat) on the Nile River.',
                'description_es': 'Visite el Obelisco Inacabado y la Gran Presa de Asuán. Visite la Isla de File y el famoso Templo de Isis. Por la tarde, Paseo en Faluca (barco de vela típico) en el río Nilo.',
                'description_pt': 'Visite o Obelisco Inacabado e a Grande Barragem de Assuã. Visite a Ilha de Filae e o famoso Templo de Ísis. À tarde, Passeio de Feluca (barco típico a vela) pelo Rio Nilo.',
                'locations': 'Aswan, Philae Island',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': 'M/S Solaris Cruise or similar 5★',
            },
            {
                'day_number': 9,
                'title': 'Aswan – Cairo (Flight)',
                'title_es': 'Asuán – El Cairo (Vuelo)',
                'title_pt': 'Assuã – Cairo (Voo)',
                'description': 'Check out from cruise. Domestic flight to Cairo. Transfer to hotel. Optional: Visit Abu Simbel temples before flying to Cairo.',
                'description_es': 'Check-out del crucero. Vuelo doméstico a El Cairo. Traslado al hotel. Opcional: Visita a los templos de Abu Simbel antes de volar a El Cairo.',
                'description_pt': 'Check-out do cruzeiro. Voo doméstico para Cairo. Transfer para o hotel. Opcional: Visita aos templos de Abu Simbel antes de voar para Cairo.',
                'locations': 'Aswan, Cairo',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': 'Azal Pyramids Hotel or similar 4★',
            },
            {
                'day_number': 10,
                'title': 'Cairo – Istanbul (Turkey)',
                'title_es': 'El Cairo – Estambul (Turquía)',
                'title_pt': 'Cairo – Istambul (Turquia)',
                'description': 'Transfer to Cairo airport for international flight to Istanbul, Turkey (flight not included). Arrival in Istanbul. Transfer to hotel.',
                'description_es': 'Traslado al aeropuerto de El Cairo para vuelo internacional a Estambul, Turquía (vuelo no incluido). Llegada a Estambul. Traslado al hotel.',
                'description_pt': 'Transfer para o aeroporto do Cairo para voo internacional para Istambul, Turquia (voo não incluso). Chegada a Istambul. Transfer para o hotel.',
                'locations': 'Cairo, Istanbul',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': 'Mina Hotel or similar 4★',
            },
            {
                'day_number': 11,
                'title': 'Istanbul – City Tour – Grand Bazaar',
                'title_es': 'Estambul – City Tour – Gran Bazar',
                'title_pt': 'Istambul – City Tour – Grande Bazar',
                'description': 'City Tour in Istanbul: Hippodrome, Blue Mosque (17th century masterpiece), Hagia Sophia (UNESCO World Heritage), and Grand Bazaar with about 4000 shops.',
                'description_es': 'City Tour en Estambul: Hipódromo, Mezquita Azul (obra maestra del siglo XVII), Santa Sofía (Patrimonio de la Humanidad UNESCO) y Gran Bazar con unas 4000 tiendas.',
                'description_pt': 'City Tour em Istambul: Hipódromo, Mesquita Azul (obra-prima do século XVII), Hagia Sophia (Patrimônio Mundial UNESCO) e Grande Bazar com cerca de 4000 lojas.',
                'locations': 'Istanbul',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': 'Mina Hotel or similar 4★',
            },
            {
                'day_number': 12,
                'title': 'Istanbul – Bosphorus Cruise – Cappadocia (Flight)',
                'title_es': 'Estambul – Crucero por el Bósforo – Capadocia (Vuelo)',
                'title_pt': 'Istambul – Passeio pelo Bósforo – Capadócia (Voo)',
                'description': 'Bosphorus Boat Tour (1h45min). Transfer to Istanbul Airport for domestic flight to Cappadocia (Nevsehir). Transfer to cave hotel.',
                'description_es': 'Paseo en Barco por el Bósforo (1h45min). Traslado al Aeropuerto de Estambul para vuelo doméstico a Capadocia (Nevsehir). Traslado al hotel cueva.',
                'description_pt': 'Passeio de Barco pelo Bósforo (1h45min). Transfer para o Aeroporto de Istambul para voo doméstico para Capadócia (Nevsehir). Transfer para o hotel caverna.',
                'locations': 'Istanbul, Cappadocia',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': 'Ascension Cave Suites or similar',
            },
            {
                'day_number': 13,
                'title': 'Cappadocia – Full Day Tours',
                'title_es': 'Capadocia – Excursiones de Día Completo',
                'title_pt': 'Capadócia – Passeios de Dia Inteiro',
                'description': 'Visit cave houses of Uchisar, Pigeon Valley, Fairy Chimneys, Pashabagi (Monk\'s Valley), Avanos pottery city, Dervent Valley (Rose Valley), and famous fairy chimneys of Urgup. Watch sunset at Rose Valley. Optional: Hot Air Balloon at sunrise, Whirling Dervish show at night.',
                'description_es': 'Visite las casas cueva de Uchisar, Valle de las Palomas, Chimeneas de las Hadas, Pashabagi (Valle de los Monjes), ciudad de cerámica Avanos, Valle de Dervent (Valle de las Rosas) y las famosas chimeneas de hadas de Ürgüp. Vea el atardecer en el Valle de las Rosas. Opcional: Globo Aerostático al amanecer, espectáculo de Derviches Giróvagos por la noche.',
                'description_pt': 'Visite as casas caverna de Uçhisar, Vale dos Pombos, Chaminés de Fadas, Paşabağı (Vale dos Monges), cidade de cerâmica Avanos, Vale Dervent (Vale das Rosas) e as famosas chaminés de fadas de Ürgüp. Assista ao pôr do sol no Vale das Rosas. Opcional: Voo de Balão ao nascer do sol, espetáculo dos Dervixes Rodopiantes à noite.',
                'locations': 'Cappadocia',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': 'Ascension Cave Suites or similar',
            },
            {
                'day_number': 14,
                'title': 'Cappadocia – Departure',
                'title_es': 'Capadocia – Salida',
                'title_pt': 'Capadócia – Partida',
                'description': 'Transfer to Nevsehir airport for your international return flight (flight not included).',
                'description_es': 'Traslado al aeropuerto de Nevsehir para su vuelo internacional de regreso (vuelo no incluido).',
                'description_pt': 'Transfer para o aeroporto de Nevşehir para seu voo internacional de retorno (voo não incluso).',
                'locations': 'Cappadocia',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': '',
            },
        ]

        for item in itinerary_data:
            TourItinerary.objects.create(tour=tour, sort_order=item['day_number'], **item)

        # Add Inclusions
        inclusions_data = [
            # Included items
            {'item': '5 nights accommodation in Cairo in a 4-star hotel with breakfast', 'item_es': '5 noches de alojamiento en El Cairo en hotel 4 estrellas con desayuno', 'item_pt': 'Hospedagem no Cairo por 5 noites em hotel categoria 4 estrelas com café da manhã', 'is_included': True},
            {'item': '4 nights Nile Cruise, 5-star Deluxe, Full Board (12 meals)', 'item_es': 'Crucero en el Nilo de 4 noches, 5 estrellas Lujo, Pensión Completa (12 comidas)', 'item_pt': 'Cruzeiro no Nilo por 4 noites, 5 estrelas Luxo, Pensão Completa (12 refeições)', 'is_included': True},
            {'item': '2 nights accommodation in Istanbul, Turkey', 'item_es': '2 noches de alojamiento en Estambul, Turquía', 'item_pt': 'Estadia em Istambul, Turquia, por 2 noites', 'is_included': True},
            {'item': '2 nights accommodation in Cappadocia, Turkey (cave hotel)', 'item_es': '2 noches de alojamiento en Capadocia, Turquía (hotel cueva)', 'item_pt': 'Estadia na Capadócia, Turquia, por 2 noites (hotel caverna)', 'is_included': True},
            {'item': '3 Domestic Flights: Cairo/Luxor, Aswan/Cairo, Istanbul/Cappadocia', 'item_es': '3 Vuelos Domésticos: El Cairo/Luxor, Asuán/El Cairo, Estambul/Capadocia', 'item_pt': '3 Voos domésticos: Cairo/Luxor, Assuã/Cairo, Istambul/Capadócia', 'is_included': True},
            {'item': '4 Lunches at local restaurants during tours', 'item_es': '4 Almuerzos en restaurantes locales durante las excursiones', 'item_pt': '4 Almoços em restaurantes locais durante os passeios', 'is_included': True},
            {'item': 'All transfers in Egypt and Turkey according to itinerary', 'item_es': 'Todos los traslados en Egipto y Turquía según el itinerario', 'item_pt': 'Todos os traslados no Egito e na Turquia conforme o roteiro', 'is_included': True},
            {'item': 'Expert English/Spanish/Portuguese speaking guide in Egypt and Turkey', 'item_es': 'Guía oficial que habla español en Egipto y Turquía', 'item_pt': 'Guia oficial falando português ou espanhol no Egito e Turquia', 'is_included': True},
            {'item': 'Entrance tickets to all sites mentioned in itinerary', 'item_es': 'Entradas a todos los sitios mencionados en el itinerario', 'item_pt': 'Ingressos para todos os sítios mencionados no programa', 'is_included': True},
            {'item': 'Hotel taxes, service charges, and tour fees', 'item_es': 'Impuestos hoteleros, cargos por servicio y tasas de tours', 'item_pt': 'Todos os impostos e taxas hoteleiras', 'is_included': True},
            {'item': 'Meet & Assist at Egyptian airports', 'item_es': 'Servicios de recepción y asistencia en aeropuertos de Egipto', 'item_pt': 'Serviço de recepção e assistência nos aeroportos do Egito', 'is_included': True},
            {'item': 'Technical support from operations team', 'item_es': 'Soporte técnico del equipo de operaciones', 'item_pt': 'Suporte técnico e operacional da equipe especializada', 'is_included': True},
            # Excluded items
            {'item': 'International flights: Brazil/Cairo, Cairo/Istanbul, Cappadocia/Brazil', 'item_es': 'Pasajes aéreos internacionales: Brasil/El Cairo, El Cairo/Estambul, Capadocia/Brasil', 'item_pt': 'Passagens aéreas internacionais: Brasil/Cairo, Cairo/Istambul, Capadócia/Brasil', 'is_included': False},
            {'item': 'Optional tours and personal extras (beverages, laundry, phone calls)', 'item_es': 'Excursiones opcionales y extras personales (bebidas, lavandería, llamadas)', 'item_pt': 'Passeios opcionais e extras pessoais (bebidas, lavanderia, telefonemas)', 'is_included': False},
            {'item': 'Egyptian Entry Visa (can be obtained on arrival)', 'item_es': 'Visa de entrada a Egipto (puede obtenerse a la llegada)', 'item_pt': 'Visto de entrada no Egito (pode ser obtido na chegada)', 'is_included': False},
            {'item': 'Tips for drivers and guides', 'item_es': 'Propinas para conductores y guías', 'item_pt': 'Gorjetas para motoristas e guias', 'is_included': False},
            {'item': 'Personal baggage overweight expenses', 'item_es': 'Gastos por exceso de equipaje personal', 'item_pt': 'Despesas de excesso de bagagem pessoal', 'is_included': False},
            {'item': 'Travel Insurance', 'item_es': 'Seguro de viaje', 'item_pt': 'Seguro viagem internacional', 'is_included': False},
        ]

        for i, inc in enumerate(inclusions_data):
            TourInclusion.objects.create(tour=tour, sort_order=i, **inc)

        # Add Departure Dates
        departure_dates = [
            # October 2025
            {'departure_date': date(2025, 10, 5), 'return_date': date(2025, 10, 18)},
            {'departure_date': date(2025, 10, 12), 'return_date': date(2025, 10, 25)},
            {'departure_date': date(2025, 10, 19), 'return_date': date(2025, 11, 1)},
            # November 2025
            {'departure_date': date(2025, 11, 2), 'return_date': date(2025, 11, 15)},
            {'departure_date': date(2025, 11, 9), 'return_date': date(2025, 11, 22)},
            {'departure_date': date(2025, 11, 16), 'return_date': date(2025, 11, 29)},
            # December 2025
            {'departure_date': date(2025, 12, 7), 'return_date': date(2025, 12, 20)},
            # January 2026
            {'departure_date': date(2026, 1, 4), 'return_date': date(2026, 1, 17)},
            {'departure_date': date(2026, 1, 18), 'return_date': date(2026, 1, 31)},
            # February 2026
            {'departure_date': date(2026, 2, 8), 'return_date': date(2026, 2, 21)},
            {'departure_date': date(2026, 2, 15), 'return_date': date(2026, 2, 28)},
            # March 2026
            {'departure_date': date(2026, 3, 8), 'return_date': date(2026, 3, 21)},
            {'departure_date': date(2026, 3, 15), 'return_date': date(2026, 3, 28)},
            # April 2026
            {'departure_date': date(2026, 4, 5), 'return_date': date(2026, 4, 18)},  # Easter period +15%
            {'departure_date': date(2026, 4, 12), 'return_date': date(2026, 4, 25)},
            # May 2026
            {'departure_date': date(2026, 5, 3), 'return_date': date(2026, 5, 16)},
            {'departure_date': date(2026, 5, 10), 'return_date': date(2026, 5, 23)},
            {'departure_date': date(2026, 5, 17), 'return_date': date(2026, 5, 30)},  # Easter period +15%
        ]

        for dep in departure_dates:
            TourDeparture.objects.create(
                tour=tour,
                departure_date=dep['departure_date'],
                return_date=dep['return_date'],
                available_spots=12,
                is_guaranteed=True,
                status='available'
            )

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(f'{action} tour: {tour.name}'))
        self.stdout.write(self.style.SUCCESS(f'Added {len(highlights_data)} highlights'))
        self.stdout.write(self.style.SUCCESS(f'Added {len(itinerary_data)} itinerary days'))
        self.stdout.write(self.style.SUCCESS(f'Added {len(inclusions_data)} inclusions'))
        self.stdout.write(self.style.SUCCESS(f'Added {len(departure_dates)} departure dates'))
