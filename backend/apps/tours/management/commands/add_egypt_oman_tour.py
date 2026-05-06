"""
Management command to add "Eternal Empires: Egypt & Oman" tour.
"""
from django.core.management.base import BaseCommand
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourDeparture
)
from apps.destinations.models import Destination
from datetime import date


class Command(BaseCommand):
    help = 'Add Eternal Empires: Egypt & Oman 15-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Eternal Empires: Egypt & Oman tour...')

        # Get or create category
        category, _ = TourCategory.objects.get_or_create(
            slug='multi-country-tours',
            defaults={
                'name': 'Multi-Country Tours',
                'name_es': 'Tours Multi-País',
                'name_pt': 'Tours Multi-País',
            }
        )

        tour_type, _ = TourType.objects.get_or_create(
            slug='multi-country-tour',
            defaults={
                'name': 'Multi-Country Tour',
                'name_es': 'Tour Multi-País',
                'name_pt': 'Tour Multi-País',
            }
        )

        # Ensure Oman destinations exist
        oman_dests = [
            {
                'name': 'Muscat', 'name_es': 'Mascate', 'name_pt': 'Mascate',
                'slug': 'muscat',
                'country': 'Oman',
                'description': 'The capital of Oman, where dramatic mountains meet turquoise waters.',
                'description_es': 'La capital de Omán, donde montañas dramáticas se encuentran con aguas turquesa.',
                'description_pt': 'A capital de Omã, onde montanhas dramáticas encontram águas turquesa.',
            },
            {
                'name': 'Nizwa', 'name_es': 'Nizwa', 'name_pt': 'Nizwa',
                'slug': 'nizwa',
                'country': 'Oman',
                'description': 'The ancient capital of Oman and its spiritual and cultural heart.',
                'description_es': 'La antigua capital de Omán y su corazón espiritual y cultural.',
                'description_pt': 'A antiga capital de Omã e seu coração espiritual e cultural.',
            },
            {
                'name': 'Wahiba Sands', 'name_es': 'Arenas de Wahiba', 'name_pt': 'Areias de Wahiba',
                'slug': 'wahiba-sands',
                'country': 'Oman',
                'description': 'A vast sea of golden dunes stretching as far as the eye can see.',
                'description_es': 'Un vasto mar de dunas doradas que se extiende hasta donde alcanza la vista.',
                'description_pt': 'Um vasto mar de dunas douradas que se estende até onde a vista alcança.',
            },
        ]

        for d in oman_dests:
            slug = d.pop('slug')
            Destination.objects.get_or_create(slug=slug, defaults=d)

        # Create the tour
        tour, created = Tour.objects.update_or_create(
            slug='eternal-empires-egypt-oman-15-days',
            defaults={
                'name': 'Eternal Empires: Egypt & Oman – 15 Days',
                'name_es': 'Imperios Eternos: Egipto y Omán – 15 Días',
                'name_pt': 'Impérios Eternos: Egito e Omã – 15 Dias',
                'short_description': 'Two fabulous destinations in one package. Egypt and Oman – a rich, different and unforgettable experience. On one side, the Pyramids, the Nile and the pharaohs. On the other, golden deserts, hidden valleys and the warmest Arabian hospitality. Two civilizations, one unforgettable journey.',
                'short_description_es': 'Dos destinos fabulosos en un solo paquete. Egipto y Omán – una experiencia rica, diferente y memorable. De un lado, las Pirámides, el Nilo y los faraones. Del otro, desiertos dorados, valles escondidos y la más cálida hospitalidad árabe. Dos civilizaciones, un viaje inolvidable.',
                'short_description_pt': 'Dois destinos fabulosos em um só pacote. Egito e Omã – uma experiência rica, diferente e marcante. De um lado, as Pirâmides, o Nilo e os faraós. Do outro, desertos dourados, vales escondidos e a hospitalidade árabe mais acolhedora. Duas civilizações, uma viagem inesquecível.',
                'description': """Discover two ancient civilizations in one extraordinary journey. Begin in Egypt exploring the Pyramids of Giza, the Grand Egyptian Museum, and sail the Nile on a 5★ cruise from Luxor to Aswan. Then fly to Oman to experience the Sultan Qaboos Grand Mosque, the turquoise pools of Wadi Bani Khalid, a night under the stars in the Wahiba Sands desert, and the historic forts of Nizwa.

**Season:** Winter (October 01 – April 30)

**Night Distribution:**
- 08 Nights in Egypt 🇪🇬 (Cairo 5★ Hotels + Nile Cruise 5★ Full Board)
- 06 Nights in Oman 🇴🇲 (4★ Hotels + 1 night Bedouin Desert Camp)

**Includes:**
- 02 domestic flights in Egypt ✈️: Cairo → Luxor / Aswan → Cairo
- All airport transfers included

**Meal Plan:**
- Daily breakfast at all hotels
- Lunch at local restaurants on tour days
- Full board during Nile cruise (4 nights)
- Dinner during desert camp night

**Tour Format:**
Small group tours with personalized attention.

**Accommodation:**
- Cairo: 5★ Hotels
- Nile Cruise: 5★ (Full Board)
- Muscat & Nizwa: 4★ Hotels
- Wahiba Sands: Bedouin Desert Camp""",
                'description_es': """Descubra dos civilizaciones antiguas en un solo viaje extraordinario. Comience en Egipto explorando las Pirámides de Guiza, el Gran Museo Egipcio, y navegue por el Nilo en un crucero 5★ de Luxor a Asuán. Luego vuele a Omán para experimentar la Mezquita del Sultán Qaboos, las piscinas turquesa de Wadi Bani Khalid, una noche bajo las estrellas en el desierto de Wahiba Sands, y los históricos fuertes de Nizwa.

**Temporada:** Invierno (01 de octubre al 30 de abril)

**Distribución de Noches:**
- 08 Noches en Egipto 🇪🇬 (El Cairo: hoteles 5★ + Crucero por el Nilo: 5★ pensión completa)
- 06 Noches en Omán 🇴🇲 (Hoteles 4★ + 1 noche en campamento beduino)

**Incluye:**
- 02 vuelos internos en Egipto ✈️: El Cairo → Luxor / Asuán → El Cairo
- Todos los traslados aeroportuarios incluidos

**Régimen de Alimentación:**
- Desayuno diario en todos los hoteles
- Almuerzos en restaurantes locales los días de tour
- Pensión completa durante el crucero por el Nilo (4 noches)
- Cena durante la noche en el desierto

**Formato de las Excursiones:**
Tours en grupos pequeños con atención personalizada.

**Alojamiento:**
- El Cairo: Hoteles 5★
- Crucero por el Nilo: 5★ (Pensión Completa)
- Mascate y Nizwa: Hoteles 4★
- Arenas de Wahiba: Campamento Beduino""",
                'description_pt': """Descubra duas civilizações antigas em uma jornada extraordinária. Comece no Egito explorando as Pirâmides de Gizé, o Grande Museu Egípcio, e navegue pelo Nilo em um cruzeiro 5★ de Luxor a Aswan. Em seguida, voe para Omã para conhecer a Mesquita do Sultão Qaboos, as piscinas turquesa de Wadi Bani Khalid, uma noite sob as estrelas no deserto de Wahiba Sands, e os fortes históricos de Nizwa.

**Temporada:** Inverno (01 de outubro a 30 de abril)

**Distribuição das Hospedagens:**
- 08 Noites no Egito 🇪🇬 (Cairo: hotéis 5★ + Cruzeiro pelo Nilo: 5★ pensão completa)
- 06 Noites em Omã 🇴🇲 (Hotéis 4★ + 1 noite em acampamento beduíno)

**Inclui:**
- 02 voos domésticos no Egito ✈️: Cairo → Luxor / Aswan → Cairo
- Todos os traslados aeroportuários incluídos

**Regime de Refeições:**
- Café da manhã diário em todos os hotéis
- Almoços em restaurantes locais nos dias de passeio
- Pensão completa durante o cruzeiro pelo Nilo (4 noites)
- Jantar durante a noite no deserto

**Formato dos Passeios:**
Tours em grupos pequenos com atenção personalizada.

**Hospedagem:**
- Cairo: Hotéis 5★
- Cruzeiro pelo Nilo: 5★ (Pensão Completa)
- Mascate e Nizwa: Hotéis 4★
- Areias de Wahiba: Acampamento Beduíno""",
                'category': category,
                'tour_type': tour_type,
                'days': 15,
                'nights': 14,
                'price': 3200.00,
                'currency': 'USD',
                'min_group_size': 2,
                'max_group_size': 12,
                'is_featured': True,
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
        dest_slugs = ['cairo', 'luxor', 'aswan', 'muscat', 'nizwa', 'wahiba-sands']
        for slug in dest_slugs:
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

        # ===== HIGHLIGHTS =====
        highlights_data = [
            {
                'title': 'Two Fabulous Destinations',
                'title_es': 'Dos Destinos Fabulosos',
                'title_pt': 'Dois Destinos Fabulosos',
                'description': 'Egypt and Oman in one package. A rich, different and unforgettable experience. On one side, the Pyramids, the Nile and the pharaohs. On the other, golden deserts, hidden valleys and the warmest Arabian hospitality. Two civilizations, one unforgettable journey.',
                'description_es': 'Egipto y Omán en un solo paquete. Una experiencia rica, diferente y memorable. De un lado, las Pirámides, el Nilo y los faraones. Del otro, desiertos dorados, valles escondidos y la más cálida hospitalidad árabe. Dos civilizaciones, un viaje inolvidable.',
                'description_pt': 'Egito e Omã em um só pacote. Uma experiência rica, diferente e marcante. De um lado, as Pirâmides, o Nilo e os faraós. Do outro, desertos dourados, vales escondidos e a hospitalidade árabe mais acolhedora. Duas civilizações, uma viagem inesquecível.',
            },
            {
                'title': 'Comfortable Accommodation',
                'title_es': 'Alojamiento Confortable',
                'title_pt': 'Hospedagem Confortável',
                'description': 'Egypt: 5★ hotels in Cairo + 5★ Nile Cruise (full board). Oman: 4★ hotels + 1 night in a Bedouin desert camp in Wahiba Sands.',
                'description_es': 'Egipto: Hoteles 5★ en El Cairo + Crucero 5★ por el Nilo (pensión completa). Omán: Hoteles 4★ + 1 noche en campamento beduino en las Arenas de Wahiba.',
                'description_pt': 'Egito: Hotéis 5★ no Cairo + Cruzeiro 5★ no Nilo (pensão completa). Omã: Hotéis 4★ + 1 noite em acampamento beduíno no deserto.',
            },
            {
                'title': 'Nile Cruise (4 Nights)',
                'title_es': 'Crucero por el Nilo (4 Noches)',
                'title_pt': 'Cruzeiro pelo Nilo (4 Noites)',
                'description': 'Sail between Luxor and Aswan aboard a 5★ cruise with full board. Stops in Edfu, Kom Ombo and Aswan.',
                'description_es': 'Navegue entre Luxor y Asuán a bordo de un crucero 5★ con pensión completa. Paradas en Edfú, Kom Ombo y Asuán.',
                'description_pt': 'Navegue entre Luxor e Aswan a bordo de um cruzeiro 5★ com pensão completa. Paradas em Edfu, Kom Ombo e Aswan.',
            },
            {
                'title': 'Specialized Guides',
                'title_es': 'Guías Especializados',
                'title_pt': 'Guias Especializados',
                'description': 'Egypt: English-speaking guide. Oman: English-speaking guide (subject to availability). 24/7 local assistance.',
                'description_es': 'Egipto: Guía de habla española. Omán: Guía de habla española o inglesa (según disponibilidad). Asistencia local 24/7.',
                'description_pt': 'Egito: Guia de língua portuguesa. Omã: Guia de língua espanhola ou portuguesa (conforme disponibilidade). Assistência local 24/7.',
            },
            {
                'title': 'Treasures of Egypt',
                'title_es': 'Tesoros de Egipto',
                'title_pt': 'Tesouros do Egito',
                'description': 'Giza Pyramids, Sphinx, Grand Egyptian Museum (GEM), Valley of the Kings, Hatshepsut Temple, Karnak, Luxor, Edfu, Kom Ombo, Philae and a felucca ride.',
                'description_es': 'Pirámides de Guiza, Esfinge, Gran Museo Egipcio (GEM), Valle de los Reyes, Templo de Hatshepsut, Karnak, Luxor, Edfú, Kom Ombo, Filae y paseo en faluca.',
                'description_pt': 'Pirâmides de Gizé, Esfinge, Grande Museu Egípcio (GEM), Vale dos Reis, Templo de Hatshepsut, Karnak, Luxor, Edfu, Kom Ombo, Filas e passeio de feluca.',
            },
            {
                'title': 'Authentic Experiences in Oman',
                'title_es': 'Experiencias Auténticas en Omán',
                'title_pt': 'Experiências Autênticas em Omã',
                'description': 'Sultan Qaboos Grand Mosque, Wadi Bani Khalid, overnight in the Wahiba Sands desert, Nizwa Fort, Jabreen Castle, Bahla (UNESCO) and Muttrah Souq.',
                'description_es': 'Mezquita del Sultán Qaboos, Wadi Bani Khalid, noche en el desierto de Wahiba Sands, Fuerte de Nizwa, Castillo de Jabreen, Bahla (UNESCO) y Zoco de Muttrah.',
                'description_pt': 'Mesquita do Sultão Qaboos, Wadi Bani Khalid, noite no deserto de Wahiba Sands, Forte de Nizwa, Castelo de Jabreen, Bahla (UNESCO) e Zoco de Muttrah.',
            },
            {
                'title': 'Complete Logistics',
                'title_es': 'Logística Completa',
                'title_pt': 'Logística Completa',
                'description': '2 domestic flights in Egypt (Cairo → Luxor / Aswan → Cairo). All airport transfers included.',
                'description_es': '2 vuelos domésticos en Egipto (El Cairo → Luxor / Asuán → El Cairo). Todos los traslados aeroportuarios incluidos.',
                'description_pt': '2 voos domésticos no Egito (Cairo → Luxor / Aswan → Cairo). Todos os traslados aeroportuários incluídos.',
            },
            {
                'title': 'Entrance Fees Included',
                'title_es': 'Entradas Incluidas',
                'title_pt': 'Ingressos Incluídos',
                'description': 'All entry fees to temples, museums, archaeological sites and monuments mentioned in the itinerary.',
                'description_es': 'Todas las entradas a templos, museos, sitios arqueológicos y monumentos mencionados en el itinerario.',
                'description_pt': 'Todas as entradas para templos, museus, sítios arqueológicos e monumentos do roteiro.',
            },
            {
                'title': 'Modern Transportation',
                'title_es': 'Transporte Moderno',
                'title_pt': 'Transporte Moderno',
                'description': 'Air-conditioned vehicles (coach/van/4x4 in Oman) + airport transfers.',
                'description_es': 'Vehículos con aire acondicionado (autocar/furgoneta/4x4 en Omán) + traslados aeroportuarios.',
                'description_pt': 'Veículos com ar-condicionado (ônibus/van/4x4 em Omã) + traslados aeroportuários.',
            },
            {
                'title': 'Planned Meals',
                'title_es': 'Alimentación Planificada',
                'title_pt': 'Alimentação Planejada',
                'description': 'Daily breakfast, lunches at local restaurants, full board on the cruise, dinner in the desert + 1 bottle of water/person/day during tours and transfers.',
                'description_es': 'Desayuno diario, almuerzos en restaurantes locales, pensión completa en el crucero, cena en el desierto + 1 botella de agua/persona/día durante tours y traslados.',
                'description_pt': 'Café da manhã diário, almoços em restaurantes locais, pensão completa no cruzeiro, jantar no deserto + 1 garrafa de água/pessoa/dia.',
            },
        ]

        for i, h in enumerate(highlights_data):
            TourHighlight.objects.create(tour=tour, sort_order=i, **h)

        # ===== ITINERARY =====
        itinerary_data = [
            {
                'day_number': 1,
                'title': 'Arrival in Cairo',
                'title_es': 'Llegada a El Cairo',
                'title_pt': 'Chegada ao Cairo',
                'description': 'Arrival at Cairo International Airport according to your own flight schedule. (International flight not included). Reception by our local agency representative to assist with entry formalities. Transfer to your hotel. Check-in. Overnight in Cairo.\n\n🕒 Note: Hotel check-in opens from 15:00 onwards.',
                'description_es': 'Llegada al Aeropuerto Internacional de El Cairo según su propio vuelo. (Vuelo internacional no incluido). Recepción por nuestro representante de la agencia para asistir con las formalidades de entrada. Traslado al hotel. Check-in. Noche en El Cairo.\n\n🕒 Nota: El check-in en el hotel abre a partir de las 15:00 horas.',
                'description_pt': 'Chegada ao Aeroporto Internacional do Cairo conforme seu próprio voo. (Voo internacional não incluído). Recepção por nosso representante local para auxiliar nas formalidades de entrada. Transfer para seu hotel. Check-in. Pernoite no Cairo.\n\n🕒 Nota: O check-in no hotel abre a partir das 15:00.',
                'locations': 'Cairo',
                'meals_included': '',
                'accommodation': '5★ Hotel in Cairo',
                'accommodation_es': 'Hotel 5★ en El Cairo',
                'accommodation_pt': 'Hotel 5★ no Cairo',
            },
            {
                'day_number': 2,
                'title': 'Cairo – Giza Pyramids & Grand Egyptian Museum',
                'title_es': 'El Cairo – Pirámides de Guiza y Gran Museo Egipcio',
                'title_pt': 'Cairo – Pirâmides de Gizé e Grande Museu Egípcio',
                'description': 'Breakfast at the hotel. Depart with your private guide to visit the Giza Plateau, home to the last surviving wonder of the ancient world.\n\nThe Great Pyramids of Giza – Towering monuments built as eternal royal tombs for Pharaohs Cheops (Khufu), Chephren (Khafre), and Mycerinus (Menkaure). The Great Pyramid of Cheops, the largest, originally rose to 146 meters and held the title of the tallest man-made structure on Earth for over 3,800 years.\n\nThe Great Sphinx – A mythical creature with the body of a lion and the face of a pharaoh, believed to represent King Chephren. Carved from a single ridge of limestone, the Sphinx has guarded the Giza Plateau for over 4,500 years as a symbol of strength and wisdom.\n\nThe Valley Temple of King Chephren – A remarkably preserved structure made of massive granite blocks, where the pharaoh\'s body was prepared for mummification before being transported to the pyramid.\n\nLunch at a local restaurant. (Drinks are not included).\n\nThen, proceed to the Grand Egyptian Museum (GEM) – A stunning architectural masterpiece partially opened at the foot of the Giza Plateau. The museum houses over 50,000 genuine artifacts, including the complete, never-before-seen collection of King Tutankhamun\'s treasures. With its state-of-the-art galleries, immersive multimedia exhibits, and a breathtaking panoramic view of the Pyramids from its glass façade, GEM offers an unforgettable journey through 7,000 years of ancient Egyptian civilization.\n\nReturn to the hotel. (Dinner not included). Overnight in Cairo.',
                'description_es': 'Desayuno en el hotel. Salida con su guía privado para visitar la Meseta de Guiza, hogar de la última maravilla del mundo antiguo.\n\nLas Grandes Pirámides de Guiza – Monumentos imponentes construidos como tumbas eternas para los faraones Keops (Jufu), Kefrén (Jafra) y Micerinos (Menkaure). La Gran Pirámide de Keops, la más grande, alcanzaba originalmente los 146 metros y fue la estructura más alta del mundo durante más de 3800 años.\n\nLa Gran Esfinge – Criatura mítica con cuerpo de león y rostro de faraón, que representa al rey Kefrén. Tallada en una sola cresta de piedra caliza, ha custodiado la meseta durante más de 4500 años.\n\nEl Templo del Valle del Rey Kefrén – Estructura notablemente conservada de enormes bloques de granito, donde se preparaba el cuerpo del faraón para la momificación.\n\nComida en un restaurante local. (Las bebidas no están incluidas).\n\nLuego, visite el Gran Museo Egipcio (GEM) – Una obra maestra arquitectónica parcialmente inaugurada al pie de la meseta de Guiza. Alberga más de 50,000 artefactos auténticos, incluyendo la colección completa e inédita de los tesoros del rey Tutankamón. Regreso al hotel. (Cena no incluida). Noche en El Cairo.',
                'description_pt': 'Café da manhã no hotel. Saída com seu guia particular para visitar o Planalto de Gizé, lar da última maravilha do mundo antigo.\n\nAs Grandes Pirâmides de Gizé – Monumentos imponentes construídos como tumbas eternas para os faraós Quéops (Khufu), Quéfren (Khafre) e Miquerinos (Menkaure). A Grande Pirâmide de Quéops, a maior, originalmente atingia 146 metros e foi a estrutura mais alta do mundo por mais de 3.800 anos.\n\nA Grande Esfinge – Criatura mítica com corpo de leão e rosto de faraó, acreditada como representando o rei Quéfren. Esculpida em uma única crista de calcário, a Esfinge guarda o planalto há mais de 4.500 anos.\n\nO Templo do Vale do Rei Quéfren – Estrutura notavelmente preservada feita de enormes blocos de granito, onde o corpo do faraó era preparado para a mumificação.\n\nAlmoço em restaurante local. (Bebidas não incluídas).\n\nEm seguida, visite o Grande Museu Egípcio (GEM) – Uma obra-prima arquitetônica parcialmente inaugurada aos pés do Planalto de Gizé. O museu abriga mais de 50.000 artefatos genuínos, incluindo a coleção completa e nunca antes vista dos tesouros do rei Tutancâmon. Retorno ao hotel. (Jantar não incluído). Noite no Cairo.',
                'locations': 'Cairo, Giza',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': '5★ Hotel in Cairo',
            },
            {
                'day_number': 3,
                'title': 'Cairo to Luxor – Nile Cruise Embarkation',
                'title_es': 'El Cairo a Luxor – Embarque en el Crucero por el Nilo',
                'title_pt': 'Cairo para Luxor – Embarque no Cruzeiro pelo Nilo',
                'description': 'Breakfast. Transfer to Cairo Airport for your domestic flight to Luxor – the ancient city of Thebes, once the glittering capital of the New Kingdom. Arrival and transfer to your 5★ Nile Cruise. Welcome drink on board.\n\nAfter lunch, visit:\n\nThe Temple of Karnak – The largest religious complex ever built, covering over 200 acres. A magnificent open-air museum of pylons, obelisks, chapels, and the legendary Hypostyle Hall with its 134 towering columns, Karnak was the spiritual heart of Egypt, dedicated to the sun god Amon-Ra.\n\nThe Temple of Luxor – Majestically located on the east bank of the Nile, this elegant temple was largely built by Pharaoh Amenhotep III and later expanded by Ramses II. Lit up at night, the temple is connected to Karnak by the famous Avenue of the Sphinxes, a 2.7 km processional path. Dinner and overnight on board in Luxor.',
                'description_es': 'Desayuno. Traslado al aeropuerto de El Cairo para su vuelo doméstico a Luxor – la antigua Tebas, capital del Imperio Nuevo. Llegada y traslado a su crucero 5★ por el Nilo. Bebida de bienvenida a bordo.\n\nDespués del almuerzo, visite:\n\nEl Templo de Karnak – El complejo religioso más grande jamás construido, con más de 200 acres. Corazón espiritual de Egipto, dedicado al dios sol Amón-Ra.\n\nEl Templo de Luxor – Elegante templo construido por Amenhotep III y expandido por Ramsés II. Conectado a Karnak por la famosa Avenida de las Esfinges. Cena y noche a bordo en Luxor.',
                'description_pt': 'Café da manhã. Transfer para o Aeroporto do Cairo para seu voo doméstico para Luxor – a antiga Tebas, outrora a capital reluzente do Império Novo. Chegada e transfer para seu cruzeiro 5★ pelo Nilo. Bebida de boas-vindas a bordo.\n\nApós o almoço, visite:\n\nO Templo de Karnak – O maior complexo religioso já construído, cobrindo mais de 200 acres. Coração espiritual do Egito, dedicado ao deus sol Amon-Rá.\n\nO Templo de Luxor – Localizado majestosamente na margem leste do Nilo, este elegante templo foi construído pelo faraó Amenhotep III e expandido por Ramsés II. Conectado a Karnak pela famosa Avenida das Esfinges. Jantar e noite a bordo em Luxor.',
                'locations': 'Cairo, Luxor',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': '5★ Nile Cruise',
            },
            {
                'day_number': 4,
                'title': 'Luxor West Bank – Sailing to Esna',
                'title_es': 'Luxor – Orilla Occidental – Navegación a Esná',
                'title_pt': 'Luxor – Margem Ocidental – Navegação para Esna',
                'description': 'Early morning, cross to the West Bank of Luxor, the ancient necropolis of Thebes:\n\nThe Valley of the Kings – A vast royal burial ground hidden within the Theban hills, where Egypt\'s mighty New Kingdom pharaohs, including Tutankhamun, Ramses the Great, and Seti I, were laid to rest in lavishly decorated tombs carved deep into the limestone. Visit three impressive royal tombs (tomb of Tutankhamun not included).\n\nThe Temple of Queen Hatshepsut – A breathtaking terraced sanctuary carved into the cliffs of Deir el-Bahari. Dedicated to Egypt\'s most famous female pharaoh, this architectural marvel blends harmoniously with the surrounding mountains, celebrating the queen\'s divine birth and successful reign.\n\nThe Colossi of Memnon – Two gigantic stone statues, each over 18 meters tall, that once guarded the entrance of Pharaoh Amenhotep III\'s mortuary temple. For centuries, the northern statue was famous for producing a mysterious musical sound at dawn. Return to the boat. Sail to Esna. Cross the Esna Lock. Continue sailing to Edfu. Dinner and overnight on board.',
                'description_es': 'Muy temprano, cruce a la Orilla Occidental de Luxor, la antigua necrópolis de Tebas:\n\nEl Valle de los Reyes – Extenso cementerio real donde descansan los faraones del Imperio Nuevo. Visita de tres tumbas reales (tumba de Tutankamón no incluida).\n\nEl Templo de la Reina Hatshepsut – Santuario en terrazas tallado en los acantilados de Deir el-Bahari, dedicado a la famosa faraona.\n\nLos Colosos de Memnón – Dos estatuas gigantes de más de 18 metros de altura que custodiaban el templo de Amenhotep III.\n\nRegreso al barco. Navegación a Esná. Cruce de la esclusa. Continuación a Edfú. Cena y noche a bordo.',
                'description_pt': 'Logo cedo, cruze para a Margem Ocidental de Luxor, a antiga necrópole de Tebas:\n\nO Vale dos Reis – Extenso cemitério real escondido nas colinas tebanas, onde os poderosos faraós do Império Novo foram sepultados em tumbas ricamente decoradas. Visite três tumbas reais (tumba de Tutancâmon não incluída).\n\nO Templo da Rainha Hatshepsut – Santuário em terraços esculpido nos penhascos de Deir el-Bahari, dedicado à mais famosa faraó do Egito.\n\nOs Colossos de Memnon – Duas estátuas gigantes de pedra, cada uma com mais de 18 metros de altura, que outrora guardavam a entrada do templo mortuário do faraó Amenhotep III.\n\nRetorno ao barco. Navegue para Esna. Cruze a eclusa de Esna. Continue navegando para Edfu. Jantar e noite a bordo.',
                'locations': 'Luxor, Esna, Edfu',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': '5★ Nile Cruise',
            },
            {
                'day_number': 5,
                'title': 'Edfu – Kom Ombo – Aswan',
                'title_es': 'Edfú – Kom Ombo – Asuán',
                'title_pt': 'Edfu – Kom Ombo – Aswan',
                'description': 'Breakfast on board.\n\nTemple of Horus in Edfu – The best-preserved temple in all of Egypt, buried under desert sand for centuries until its rediscovery. Dedicated to the falcon-headed god Horus, this Ptolemaic masterpiece offers an almost intact glimpse of ancient religious life, with towering pylons, a majestic hypostyle hall, and a granite shrine still housing the ceremonial barque of the god.\n\nSail to Kom Ombo.\n\nTemple of Kom Ombo – A unique double temple dedicated equally to two triads of deities: Sobek, the fearsome crocodile god of fertility and creation, and Haroeris (Horus the Elder), the solar warrior god. Perfectly symmetrical, the temple also contains fascinating reliefs depicting ancient surgical instruments.\n\nContinue sailing to Aswan. Dinner and overnight on board.',
                'description_es': 'Desayuno a bordo.\n\nTemplo de Horus en Edfú – El templo mejor conservado de Egipto, dedicado al dios halcón Horus. Navegación a Kom Ombo.\n\nTemplo de Kom Ombo – Un doble templo único dedicado a Sobek (dios cocodrilo) y Haroeris (Horus el Viejo). Continuación a Asuán. Cena y noche a bordo.',
                'description_pt': 'Café da manhã a bordo.\n\nTemplo de Hórus em Edfu – O templo mais bem preservado de todo o Egito, dedicado ao deus falcão Hórus.\n\nNavegue para Kom Ombo.\n\nTemplo de Kom Ombo – Um templo duplo único dedicado a Sobek (deus crocodilo) e Haroeris (Hórus, o Velho). Continue navegando para Aswan. Jantar e noite a bordo.',
                'locations': 'Edfu, Kom Ombo, Aswan',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': '5★ Nile Cruise',
            },
            {
                'day_number': 6,
                'title': 'Aswan – High Dam – Philae Temple – Felucca Ride',
                'title_es': 'Asuán – Presa Alta – Templo de Filae – Paseo en Faluca',
                'title_pt': 'Aswan – Barragem Alta – Templo de Filas – Passeio de Feluca',
                'description': 'Breakfast on board.\n\nThe High Dam – A modern engineering marvel completed in 1971, controlling the Nile\'s annual floods, generating hydroelectric power, and creating Lake Nasser – one of the world\'s largest artificial reservoirs, stretching over 500 kilometers into Sudan.\n\nThe Unfinished Obelisk – Lying abandoned in an ancient granite quarry, this massive obelisk would have been the largest ever erected, measuring 42 meters and weighing nearly 1,200 tons. Its cracks reveal the fascinating techniques used by ancient stoneworkers.\n\nPhilae Temple (Temple of Isis) – Rescued from the rising waters of Lake Nasser and meticulously relocated to the island of Agilkia, this romantic and graceful temple complex was the last bastion of ancient Egyptian religion. Dedicated to the goddess Isis, mother of Horus, it blends Egyptian, Greek, and Roman architectural styles in stunning harmony.\n\nAfternoon: Sail on a traditional Felucca – a graceful wooden sailboat unchanged for millennia – gliding through the emerald waters of the Nile around Elephantine Island and the Botanical Garden. Dinner and overnight on board.',
                'description_es': 'Desayuno a bordo.\n\nLa Presa Alta – Obra maestra de la ingeniería moderna, controla las inundaciones del Nilo y crea el lago Nasser.\n\nEl Obelisco Inacabado – Abandonado en una antigua cantera de granito, habría sido el obelisco más grande jamás erigido.\n\nTemplo de Filae (Templo de Isis) – Rescatado de las aguas del lago Nasser y reubicado en la isla de Agilkia. Último bastión de la religión del antiguo Egipto.\n\nTarde: Paseo en una Faluca tradicional – un velero de madera inalterado durante milenios. Cena y noche a bordo.',
                'description_pt': 'Café da manhã a bordo.\n\nA Barragem Alta – Uma maravilha da engenharia moderna concluída em 1971, controla as cheias do Nilo e cria o Lago Nasser.\n\nO Obelisco Inacabado – Abandonado em uma antiga pedreira de granito, teria sido o maior obelisco já erguido.\n\nTemplo de Filas (Templo de Ísis) – Resgatado das águas do Lago Nasser e realocado para a Ilha de Agilkia. Último bastião da religião do antigo Egito.\n\nTarde: Passeio em uma Feluca tradicional – um veleiro de madeira inalterado por milênios. Jantar e noite a bordo.',
                'locations': 'Aswan',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': '5★ Nile Cruise',
            },
            {
                'day_number': 7,
                'title': 'Aswan – Flight to Cairo',
                'title_es': 'Asuán – El Cairo (Vuelo a El Cairo incluido)',
                'title_pt': 'Aswan – Voo para o Cairo',
                'description': 'Disembarkation after breakfast. Transfer to Aswan Airport for your flight to Cairo. Arrival. Transfer to your hotel. Overnight in Cairo.\n\n🔵 Optional: Abu Simbel – Overland transfer to Abu Simbel (260 km), home to the two magnificent temples of Abu Simbel, a UNESCO World Heritage Site. Visit the breathtaking temple of Ramses II and the temple of Nefertari. Overland return to Aswan (260 km). Included: Transfers, entrance fees, and local guide. Please contact us for details and pricing.',
                'description_es': 'Desembarque tras el desayuno. Traslado al aeropuerto de Asuán para su vuelo a El Cairo. Llegada y traslado al hotel. Noche en El Cairo.\n\n🔵 Opcional – Abu Simbel: Traslado terrestre a Abu Simbel (260 km), hogar de los dos magníficos templos de Abu Simbel, Patrimonio de la UNESCO. Visita al templo de Ramsés II y al templo de Nefertari. Regreso terrestre a Asuán (260 km). Incluye: Traslados, entradas y guía local. Consúltenos para detalles y precios.',
                'description_pt': 'Desembarque após o café da manhã. Transfer para o Aeroporto de Aswan para seu voo para Cairo. Chegada. Transfer para seu hotel. Pernoite no Cairo.\n\n🔵 Opcional – Abu Simbel: Transfer terrestre para Abu Simbel (260 km), lar dos dois magníficos templos de Abu Simbel, Patrimônio da Humanidade pela UNESCO. Visita ao templo de Ramsés II e ao templo de Nefertari. Retorno terrestre a Aswan (260 km). Inclui: Transfers, ingressos e guia local. Consulte-nos para detalhes e preços.',
                'locations': 'Aswan, Cairo',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': '5★ Hotel in Cairo',
            },
            {
                'day_number': 8,
                'title': 'Cairo – Coptic Cairo & Citadel',
                'title_es': 'El Cairo – El Cairo Copto y Ciudadela de Saladino',
                'title_pt': 'Cairo – Cairo Copta e Cidadela de Saladino',
                'description': 'Breakfast. Depart to visit Coptic Cairo, one of the most sacred and historic areas of the city, where Christianity took root in Egypt during the Roman era. Explore three remarkable churches:\n\nThe Hanging Church (Al-Muallaqa) – Suspended above the gatehouse of the Roman Fortress of Babylon, this iconic basilica dates back to the 3rd century. Its wooden roof is designed to resemble Noah\'s Ark, and its interior glows with exquisite marble columns and intricate icons of the Virgin Mary.\n\nThe Church of St. Sergius and Bacchus (Abu Serga) – Built over an ancient crypt where the Holy Family – Joseph, Mary, and the infant Jesus – is believed to have rested during their flight into Egypt. A place of profound devotion and quiet spirituality, this church is one of the oldest in Cairo.\n\nThe Basilica of St. Barbara – A beautiful early Christian church dedicated to the martyred saint Barbara. Known for its fine marble columns, rare icons, and serene courtyard, the basilica reflects the rich artistic and spiritual heritage of Egypt\'s Coptic community.\n\nLunch at a local restaurant. (Drinks are not included).\n\nContinue to the Citadel of Saladin – A magnificent medieval fortress built in the 12th century by the legendary Muslim leader Saladin to protect Cairo from the Crusaders. Inside, visit the breathtaking Mohamed Ali Mosque (The Alabaster Mosque), with its stunning Ottoman silhouette, soaring twin minarets, massive central dome, and an interior glittering with alabaster and gilded decorations. From its courtyard, enjoy panoramic views of all Cairo – from the minarets of Old Cairo to the distant Pyramids.\n\nReturn to the hotel. (Dinner not included). Overnight in Cairo.',
                'description_es': 'Desayuno. Salida a visitar El Cairo Copto, una de las zonas más sagradas de la ciudad. Explore tres iglesias notables:\n\nLa Iglesia Colgante (Al-Muallaqa) – Construida sobre la puerta de la Fortaleza Romana de Babilonia.\n\nLa Iglesia de San Sergio y San Baco (Abu Serga) – Construida sobre una cripta donde la Sagrada Familia descansó durante su huida a Egipto.\n\nLa Basílica de Santa Bárbara – Dedicada a la mártir Santa Bárbara, con hermosas columnas de mármol e iconos.\n\nComida en un restaurante local. (Las bebidas no están incluidas).\n\nContinúe a la Ciudadela de Saladino – Fortaleza medieval construida en el siglo XII. En su interior, visite la Mezquita de Mohamed Alí (Mezquita de Alabastro), con impresionantes vistas de todo El Cairo. Regreso al hotel. (Cena no incluida) Noche en El Cairo.',
                'description_pt': 'Café da manhã. Saída para visitar o Cairo Copta, uma das áreas mais sagradas e históricas da cidade. Explore três igrejas notáveis:\n\nIgreja Suspensa (Al-Muallaqa) – Suspensa sobre o portal da Fortaleza Romana da Babilônia, esta basílica data do século III.\n\nIgreja de São Sérgio e São Baco (Abu Serga) – Construída sobre uma cripta antiga onde a Sagrada Família – José, Maria e o menino Jesus – teria descansado durante sua fuga para o Egito.\n\nBasílica de Santa Bárbara – Bela igreja cristã primitiva dedicada à mártir Santa Bárbara, conhecida por suas colunas de mármore e ícones raros.\n\nAlmoço em restaurante local. (Bebidas não incluídas).\n\nContinue para a Cidadela de Saladino – Fortaleza medieval construída no século XII pelo lendário líder muçulmano Saladino. Dentro dela, visite a deslumbrante Mesquita de Mohamed Ali (Mesquita de Alabastro), com vistas panorâmicas de todo o Cairo. Retorno ao hotel. (Jantar não incluído). Noite no Cairo.',
                'locations': 'Cairo',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': '5★ Hotel in Cairo',
            },
            {
                'day_number': 9,
                'title': 'Cairo – Muscat, Oman (Flight to Muscat is not included)',
                'title_es': 'El Cairo – Vuelo a Mascate, Omán',
                'title_pt': 'Cairo – Voo para Mascate, Omã',
                'description': 'Breakfast. Transfer to Cairo Airport. Departure flight to Muscat, Oman. (Flight to Muscat is not included). Arrival. Meet and assist by our local representative. Transfer to your hotel.\n\nOvernight in Muscat. (Dinner not included).\n\n🕒 Note: Hotel check-in opens from 15:00 onwards.',
                'description_es': 'Desayuno. Traslado al aeropuerto de El Cairo. Vuelo a Mascate, Omán. (vuelo de El Cairo a Mascate no está incluido). Llegada. Recepción y asistencia por nuestro representante local. Traslado a su hotel 4★. Noche en Mascate. (Cena no incluida)\n\n🕒 Nota: El check-in en el hotel abre a partir de las 15:00 horas.',
                'description_pt': 'Café da manhã. Transfer para o Aeroporto do Cairo. Voo para Mascate, Omã. Chegada. Recepção e assistência pelo nosso representante local. Transfer para seu hotel 4★.\n\nNoite em Mascate. (Jantar não incluído)\n\n🕒 Nota: O check-in no hotel abre a partir das 15:00.',
                'locations': 'Cairo, Muscat',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': '4★ Hotel in Muscat',
            },
            {
                'day_number': 10,
                'title': 'Muscat City Tour',
                'title_es': 'Tour por la Ciudad de Mascate',
                'title_pt': 'City Tour em Mascate',
                'description': 'Breakfast.\n\nSultan Qaboos Grand Mosque – A breathtaking architectural masterpiece of modern Oman, the mosque dazzles with its hand-woven Persian carpet (the second largest in the world), a magnificent Swarovski crystal chandelier, and pure white marble courtyards.\n\nCruise trip – Glide along the coast of Muscat, admiring the dramatic meeting of rugged mountains, turquoise waters, and the city\'s striking skyline.\n\nLunch at a local restaurant.\n\nAfternoon: Visit Bait Al Zubair Museum – A fascinating private museum showcasing Omani heritage through jewelry, weapons, costumes, and household artifacts. Then explore Old Muscat, framed by the 16th-century Portuguese forts Jalali and Mirani, and wander through the historic Muttrah Souq – a labyrinth of narrow alleyways filled with the scent of frankincense, silver, textiles, and perfumes.\n\nReturn to the hotel. (Dinner not included). Overnight in Muscat.',
                'description_es': 'Desayuno.\n\nMezquita del Sultán Qaboos – Obra maestra de la Omán moderna, con su alfombra persa tejida a mano (la segunda más grande del mundo) y una espectacular lámpara de cristal Swarovski.\n\nPaseo en barco – Navegue por la costa de Mascate.\n\nComida en un restaurante local.\n\nTarde: Visita al Museo Bait Al Zubair, la ciudad antigua de Mascate, los fuertes Jalali y Mirani del siglo XVI, y el histórico zoco de Muttrah. Regreso al hotel. (Cena no incluida) Noche en Mascate.',
                'description_pt': 'Café da manhã.\n\nMesquita do Sultão Qaboos – Uma obra-prima arquitetônica da Omã moderna, com seu tapete persa tecido à mão (o segundo maior do mundo), um magnífico lustre de cristal Swarovski e pátios de mármore branco.\n\nPasseio de barco – Deslize pela costa de Mascate, admirando o encontro dramático de montanhas escarpadas, águas turquesa e o horizonte da cidade.\n\nAlmoço em restaurante local.\n\nTarde: Visite o Museu Bait Al Zubair, a cidade antiga de Mascate, os fortes portugueses Jalali e Mirani do século XVI, e o histórico Souq de Muttrah – um labirinto de vielas estreitas com aroma de incenso, prata, têxteis e perfumes.\n\nRetorno ao hotel. (Jantar não incluído). Noite em Mascate.',
                'locations': 'Muscat',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': '4★ Hotel in Muscat',
            },
            {
                'day_number': 11,
                'title': 'Muscat – Ibra – Wahiba Sands (Desert Night)',
                'title_es': 'Mascate – Ibra – Arenas de Wahiba (Noche en el Desierto)',
                'title_pt': 'Mascate – Ibra – Areias de Wahiba (Noite no Deserto)',
                'description': 'Breakfast. Depart by 4x4 vehicle into the interior of Oman.\n\nWadi Bani Khalid – A lush, palm-fringed valley with crystal-clear turquoise pools nestled between dramatic Rocky Mountains. A perfect spot to enjoy nature\'s beauty.\n\nPicnic lunch on the road.\n\nContinue into the Wahiba Sands – a vast sea of golden dunes stretching as far as the eye can see. Arrive at a traditional Bedouin desert camp. Experience the silence, the stunning sunset over the dunes, and the hospitality of the desert. Dinner and overnight in the desert camp.',
                'description_es': 'Desayuno. Salida en vehículo 4x4 hacia el interior de Omán.\n\nWadi Bani Khalid – Valle verde con piscinas de agua turquesa entre montañas rocosas.\n\nComida de picnic en ruta.\n\nContinuación a las Arenas de Wahiba – mar de dunas doradas. Llegada a un campamento beduino. Cena y noche en el campamento del desierto.',
                'description_pt': 'Café da manhã. Saída em veículo 4x4 para o interior de Omã.\n\nWadi Bani Khalid – Um vale verdejante e cheio de palmeiras, com piscinas de água turquesa cristalina aninhadas entre montanhas rochosas.\n\nPiquenique na estrada.\n\nContinue para as Areias de Wahiba – um vasto mar de dunas douradas que se estende até onde a vista alcança. Chegada a um acampamento beduíno tradicional. Jantar e noite no acampamento no deserto.',
                'locations': 'Muscat, Wadi Bani Khalid, Wahiba Sands',
                'locations_es': 'Mascate, Wadi Bani Khalid, Arenas de Wahiba',
                'locations_pt': 'Mascate, Wadi Bani Khalid, Areias de Wahiba',
                'meals_included': 'Breakfast, Lunch, Dinner',
                'meals_included_es': 'Desayuno, Almuerzo, Cena',
                'meals_included_pt': 'Café da manhã, Almoço, Jantar',
                'accommodation': 'Bedouin Desert Camp',
                'accommodation_es': 'Campamento Beduino',
                'accommodation_pt': 'Acampamento Beduíno',
            },
            {
                'day_number': 12,
                'title': 'Wahiba Sands – Al Hamra – Nizwa',
                'title_es': 'Arenas de Wahiba – Al Hamra – Nizwa',
                'title_pt': 'Areias de Wahiba – Al Hamra – Nizwa',
                'description': 'Breakfast at the camp. Depart through the desert.\n\nAl Hamra – A town famous for its ancient mud-brick houses (some over 400 years old) that seem frozen in time. Visit Bait Al Safa, a traditional Omani house lovingly restored and turned into a museum showcasing daily life, dates, coffee, and handicrafts.\n\nLunch on the road.\n\nAfternoon arrival in Nizwa, once the capital of Oman and still its spiritual and cultural heart. Overnight at your hotel in Nizwa. (Dinner not included)',
                'description_es': 'Desayuno en el campamento.\n\nAl Hamra – Pueblo con casas de adobe de más de 400 años. Visita a Bait Al Safa, museo de la vida tradicional.\n\nComida en ruta.\n\nLlegada a Nizwa, antigua capital de Omán. Noche en su hotel 4★ en Nizwa. (Cena no incluida)',
                'description_pt': 'Café da manhã no acampamento. Partida através do deserto.\n\nAl Hamra – Cidade famosa por suas antigas casas de tijolos de barro (algumas com mais de 400 anos). Visite Bait Al Safa, uma casa tradicional omanense transformada em museu.\n\nAlmoço na estrada.\n\nChegada à tarde em Nizwa, antiga capital de Omã e ainda seu coração espiritual e cultural. Noite em seu hotel 4★ em Nizwa. (Jantar não incluído).',
                'locations': 'Wahiba Sands, Al Hamra, Nizwa',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': '4★ Hotel in Nizwa',
            },
            {
                'day_number': 13,
                'title': 'Nizwa – Cattle Market – Forts – Bahla – Muscat',
                'title_es': 'Nizwa – Mercado de Ganado – Fortalezas – Bahla – Mascate',
                'title_pt': 'Nizwa – Mercado de Gado – Fortes – Bahla – Mascate',
                'description': 'Early morning: Experience the famous Nizwa Cattle Market – a lively, authentic spectacle where locals gather to trade goats, sheep, cows, and even camels. The atmosphere is raw, energetic, and deeply traditional. Return to the hotel for breakfast.\n\nNizwa Fort – A 17th-century fortress with a massive circular cannon tower, one of the most impressive military monuments in Oman. Climb to the top for panoramic views of the date palm plantations and the Hajar Mountains.\n\nNizwa Souq – Famous for its silver jewelry (especially the iconic Khanjar dagger), copper coffee pots, and handcrafted goods.\n\nJabreen Castle – Perhaps the most beautiful castle in Oman, built in the late 17th century. It served as a center for learning, featuring exquisite painted ceilings, hidden rooms, and intricate woodwork.\n\nLunch at a local restaurant.\n\nBahla – A UNESCO World Heritage site, surrounded by a 12-kilometer fortified wall. The town is famous for its traditional pottery, still made by hand using ancient techniques.\n\nContinue to Barka and Rustaq, the ancient capital of Oman, before returning to Muscat. (Dinner not included). Overnight in Muscat.',
                'description_es': 'Muy temprano: Experimente el famoso mercado de ganado de Nizwa.\n\nRegreso al hotel para el desayuno.\n\nFuerte de Nizwa – Fortaleza del siglo XVII con una enorme torre circular.\n\nZoco de Nizwa – Famoso por su joyería de plata y dagas khanjar.\n\nCastillo de Jabreen – El castillo más hermoso de Omán, con techos pintados y tallas intrincadas.\n\nComida en un restaurante local.\n\nBahla – Patrimonio de la UNESCO, famosa por su cerámica tradicional y su muralla fortificada de 12 km.\n\nContinuación a Barka y Rustaq antes de regresar a Mascate. (Cena no incluida) Noche en Mascate.',
                'description_pt': 'Logo cedo: Experimente o famoso Mercado de Gado de Nizwa – um espetáculo autêntico e animado onde os locais se reúnem para negociar cabras, ovelhas, vacas e até camelos.\n\nRetorno ao hotel para o café da manhã.\n\nForte de Nizwa – Fortaleza do século XVII com uma enorme torre de canhão circular. Suba até o topo para vistas panorâmicas.\n\nSouq de Nizwa – Famoso por suas joias de prata (especialmente a adaga Khanjar), cafeteiras de cobre e artesanato.\n\nCastelo de Jabreen – Talvez o castelo mais bonito de Omã, construído no final do século XVII, com tetos pintados e entalhes intrincados.\n\nAlmoço em restaurante local.\n\nBahla – Patrimônio da UNESCO, cercada por uma muralha fortificada de 12 quilômetros, famosa por sua cerâmica tradicional.\n\nContinue para Barka e Rustaq, a antiga capital de Omã, antes de retornar a Mascate. (Jantar não incluído). Noite em Mascate.',
                'locations': 'Nizwa, Bahla, Barka, Rustaq, Muscat',
                'meals_included': 'Breakfast, Lunch',
                'meals_included_es': 'Desayuno, Almuerzo',
                'meals_included_pt': 'Café da manhã, Almoço',
                'accommodation': '4★ Hotel in Muscat',
            },
            {
                'day_number': 14,
                'title': 'Muscat – Free Day / Optional Activities',
                'title_es': 'Mascate – Día Libre / Actividades Opcionales',
                'title_pt': 'Mascate – Dia Livre / Atividades Opcionais',
                'description': 'Breakfast at the hotel. Free day at leisure to explore Muscat independently, relax at a beach club, or shop for souvenirs.\n\nOptional tours available upon request (e.g., dhow cruise with dolphin watching, full-day excursion to Wadi Shab & Bimmah Sinkhole, or a half-day to the stunning Shangri-La area).\n\n(Dinner not included). Overnight in Muscat.',
                'description_es': 'Desayuno en el hotel. Día libre para explorar Mascate de forma independiente, relajarse o comprar recuerdos.\n\nExcursiones opcionales disponibles bajo petición.\n\n(Cena no incluida) Noche en Mascate.',
                'description_pt': 'Café da manhã no hotel. Dia livre para explorar Mascate de forma independente, relaxar em um clube de praia ou comprar souvenirs.\n\nPasseios opcionais disponíveis mediante solicitação (ex.: cruzeiro em dhow com observação de golfinhos, excursão de dia completo para Wadi Shab e Bimmah Sinkhole).\n\n(Jantar não incluído). Noite em Mascate.',
                'locations': 'Muscat',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': '4★ Hotel in Muscat',
            },
            {
                'day_number': 15,
                'title': 'Muscat – Departure',
                'title_es': 'Mascate – Salida',
                'title_pt': 'Mascate – Partida',
                'description': 'Breakfast at the hotel. Check-out. Transfer to Muscat International Airport for your international flight back home.\n\nEnd of services.',
                'description_es': 'Desayuno en el hotel. Check-out. Traslado al Aeropuerto Internacional de Mascate para su vuelo internacional de regreso a casa.\n\nFin de los servicios. ✈️',
                'description_pt': 'Café da manhã no hotel. Check-out. Transfer para o Aeroporto Internacional de Mascate para seu voo internacional de volta para casa.\n\nFim dos serviços.',
                'locations': 'Muscat',
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Café da manhã',
                'accommodation': '',
            },
        ]

        for i, it in enumerate(itinerary_data):
            TourItinerary.objects.create(tour=tour, sort_order=i, **it)

        # ===== INCLUSIONS =====
        inclusions = [
            ('14 nights accommodation (15 days/14 nights): Egypt: 8 nights – Cairo: 5★ hotels + Nile Cruise: 5★ (4 nights full board). Oman: 6 nights – 4★ hotels + 1 night in Bedouin desert camp (Wahiba Sands)', '14 noches de alojamiento (15 días/14 noches): Egipto: 8 noches – El Cairo: hoteles 5★ + Crucero por el Nilo: 5★ (4 noches pensión completa). Omán: 6 noches – hoteles 4★ + 1 noche en campamento beduino (Arenas de Wahiba).', '14 noites de acomodação (15 dias/14 noites): Egito: 8 noites – Cairo: hotéis 5★ + Cruzeiro pelo Nilo: 5★ (4 noites pensão completa). Omã: 6 noites – hotéis 4★ + 1 noite em acampamento beduíno (Areias de Wahiba).', True),
            ('Daily breakfast at all hotels', 'Desayuno diario en todos los hoteles', 'Café da manhã diário em todos os hotéis', True),
            ('Lunch at local restaurants on tour days', 'Almuerzos en restaurantes locales los días de tour (bebidas no incluidas)', 'Almoços em restaurantes locais nos dias de passeio (bebidas não incluídas)', True),
            ('Full board during Nile cruise (12 meals, drinks not included)', 'Pensión completa durante el crucero por el Nilo (12 comidas, bebidas no incluidas)', 'Pensão completa durante o cruzeiro pelo Nilo (12 refeições, bebidas não incluídas)', True),
            ('Dinner during desert camp', 'Cena durante la noche en el desierto', 'Jantar durante a noite no deserto', True),
            ('Domestic flights: Cairo → Luxor / Aswan → Cairo (Economy Class)', 'Vuelos domésticos: El Cairo → Luxor / Asuán → El Cairo (clase turista)', 'Voos domésticos: Cairo → Luxor / Aswan → Cairo (classe econômica)', True),
            ('All airport transfers', 'Todos los traslados aeroportuarios', 'Todos os transfers aeroportuários', True),
            ('All ground transport: air-conditioned coach/van/4x4', 'Todo el transporte terrestre en vehículos con aire acondicionado (autocar/furgoneta/4x4)', 'Todo o transporte terrestre em veículos com ar condicionado (ônibus/van/4x4)', True),
            ('All entrance fees to sites, temples, museums & monuments', 'Todas las entradas a sitios, templos, museos y monumentos', 'Todas as entradas em sítios, templos, museus e monumentos', True),
            ('Giza Pyramids, Sphinx, Valley Temple & Grand Egyptian Museum (GEM)', 'Pirámides de Guiza, Esfinge, Templo del Valle y Gran Museo Egipcio (GEM)', 'Pirâmides de Gizé, Esfinge, Templo do Vale e Grande Museu Egípcio (GEM)', True),
            ('Karnak Temple, Luxor Temple, Valley of the Kings (3 tombs), Hatshepsut Temple, Colossi of Memnon', 'Templo de Karnak, Templo de Luxor, Valle de los Reyes (3 tumbas), Templo de Hatshepsut, Colosos de Memnón', 'Templo de Karnak, Templo de Luxor, Vale dos Reis (3 tumbas), Templo de Hatshepsut, Colossos de Memnon', True),
            ('Edfu Temple, Kom Ombo Temple, High Dam, Unfinished Obelisk, Philae Temple', 'Templo de Edfú, Templo de Kom Ombo, Presa Alta, Obelisco Inacabado, Templo de Filae', 'Templo de Edfu, Templo de Kom Ombo, Barragem Alta, Obelisco Inacabado, Templo de Filas', True),
            ('Felucca ride in Aswan', 'Paseo en faluca en Asuán', 'Passeio de feluca em Aswan', True),
            ('Coptic Cairo: Hanging Church, St. Sergius Church, St. Barbara Basilica', 'El Cairo Copto: Iglesia Colgante, Iglesia de San Sergio, Basílica de Santa Bárbara', 'Cairo Copta: Igreja Suspensa, Igreja de São Sérgio, Basílica de Santa Bárbara', True),
            ('Citadel of Saladin & Mohamed Ali Mosque (Alabaster Mosque)', 'Ciudadela de Saladino y Mezquita de Mohamed Alí (Mezquita de Alabastro)', 'Cidadela de Saladino e Mesquita de Mohamed Ali (Mesquita de Alabastro)', True),
            ('Muscat City Tour: Sultan Qaboos Grand Mosque, Bait Al Zubair Museum, Muttrah Souq, Old Muscat', 'Tour por Mascate: Mezquita del Sultán Qaboos, Museo Bait Al Zubair, Zoco de Muttrah, Mascate Antigua', 'City Tour em Mascate: Mesquita do Sultão Qaboos, Museu Bait Al Zubair, Souq de Muttrah, Mascate Antiga', True),
            ('Wadi Bani Khalid & Wahiba Sands desert experience', 'Wadi Bani Khalid y experiencia en el desierto de Wahiba Sands', 'Wadi Bani Khalid e experiência no deserto de Wahiba Sands', True),
            ('Al Hamra (Bait Al Safa Museum), Nizwa Fort & Souq, Jabreen Castle, Bahla (UNESCO)', 'Al Hamra (Museo Bait Al Safa), Fuerte y Zoco de Nizwa, Castillo de Jabreen, Bahla (UNESCO)', 'Al Hamra (Museu Bait Al Safa), Forte e Souq de Nizwa, Castelo de Jabreen, Bahla (UNESCO)', True),
            ('Expert local guides in Egypt and Oman (English-speaking guides)', 'Guías profesionales: Egipto: guía de español. Omán: guía de habla española o inglés (según disponibilidad)', 'Guias especializados: Egito: guia de língua portuguesa e em Omã: guia de língua espanhola ou portuguesa (conforme disponibilidade)', True),
            ('All hotel taxes & service charges', 'Todos los impuestos y cargos de servicio hoteleros', 'Todos os impostos e taxas de serviço hoteleiros', True),
            ('24/7 local assistance', 'Asistencia local 24/7', 'Assistência local 24/7', True),
            ('1 bottle of water/person/day during tours & transfers', '1 botella de agua/persona/día durante tours y traslados', '1 garrafa de água/pessoa/dia durante passeios', True),
            # EXCLUSIONS
            ('International flights: home → Cairo / Muscat → home', 'Vuelos internacionales: origen → El Cairo / Mascate → origen', 'Voos internacionais: origem → Cairo / Mascate → origem', False),
            ('Optional tours: Abu Simbel and Oman activities (dhow, dolphins, Wadi Shab, etc.)', 'Excursiones opcionales: Abu Simbel y actividades en Omán (dhow, delfines, Wadi Shab, etc.)', 'Passeios opcionais: Abu Simbel e atividades em Omã (dhow, golfinhos, Wadi Shab, etc.)', False),
            ('Egyptian visa (on arrival – Ask us for more information)', 'Visa egipcia (a la llegada – Consúltenos para más información)', 'Visto egípcio (na chegada – Consulte-nos para mais informações)', False),
            ('Travel insurance (highly recommended)', 'Seguro de viaje (muy recomendado)', 'Seguro de viagem (altamente recomendado)', False),
            ('Tips & gratuities for: tour guides, drivers, cruise crew, hotel staff, restaurant staff, airport porters', 'Propinas para: guías, conductores, personal del crucero, personal del hotel, restaurantes, porteros', 'Gorjetas para: guias, motoristas, tripulação do cruzeiro, funcionários de hotéis, restaurantes, carregadores', False),
            ('Personal expenses: beverages, laundry, phone calls, internet, souvenirs, room service, mini-bar', 'Gastos personales: bebidas, lavandería, llamadas, internet, souvenirs, servicio de habitación, mini-bar', 'Despesas pessoais: bebidas, lavanderia, chamadas telefônicas, internet, souvenirs, serviço de quarto, mini-bar', False),
            ('Special area entries: Tutankhamun tomb or the Great Pyramid inner chamber', 'Entradas a áreas especiales: tumba de Tutankamón o cámara interior de la Gran Pirámide', 'Entradas em áreas especiais: tumba de Tutancâmon ou câmara interna da Grande Pirâmide', False),
            ('Any services not clearly stated as included', 'Cualquier servicio no indicado explícitamente como incluido', 'Quaisquer serviços não explicitamente indicados como incluídos', False),
        ]

        for i, (en, es, pt, is_inc) in enumerate(inclusions):
            TourInclusion.objects.create(
                tour=tour, item=en, item_es=es, item_pt=pt,
                is_included=is_inc, sort_order=i
            )

        self.stdout.write(self.style.SUCCESS(
            f'Tour "Eternal Empires: Egypt & Oman" {"created" if created else "updated"} successfully!'
        ))
        self.stdout.write(self.style.SUCCESS(f'Tour ID: {tour.id}, Slug: {tour.slug}'))
