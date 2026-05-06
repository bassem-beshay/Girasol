"""
Management command to add "Nile Splendor – Summer Offer 8 Days" tour.
"""
from django.core.management.base import BaseCommand
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourPricing
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Nile Splendor – Summer Offer 8 Days tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Nile Splendor – Summer Offer tour...')

        # Get or create category
        category, _ = TourCategory.objects.get_or_create(
            slug='nile-cruises',
            defaults={
                'name': 'Nile Cruises',
                'name_es': 'Cruceros por el Nilo',
                'name_pt': 'Cruzeiros pelo Nilo',
            }
        )

        tour_type, _ = TourType.objects.get_or_create(
            slug='classic-tour',
            defaults={
                'name': 'Classic Tour',
                'name_es': 'Tour Clásico',
                'name_pt': 'Tour Clássico',
            }
        )

        # Build justified text helper
        def j(text):
            """Wrap text in justify-aligned paragraph for CKEditor."""
            return f'<p style="text-align: justify;">{text}</p>'

        # Create the tour
        tour, created = Tour.objects.update_or_create(
            slug='nile-splendor-summer-offer-8-days',
            defaults={
                'name': 'Nile Splendor – Summer Offer 8 Days',
                'name_es': 'Esplendor del Nilo – Oferta de Verano 8 Días',
                'name_pt': 'Esplendor do Nilo – Oferta de Verão 8 Dias / 7 Noites',
                'short_description': 'Discover the timeless wonders of Egypt on this 8-day journey. Explore the Pyramids of Giza, the Grand Egyptian Museum, and sail the Nile on a 5-star cruise from Luxor to Aswan visiting ancient temples, royal tombs, and iconic monuments.',
                'short_description_es': 'Descubra las maravillas eternas de Egipto en este viaje de 8 días. Explore las Pirámides de Guiza, el Gran Museo Egipcio, y navegue por el Nilo en un crucero 5 estrellas de Luxor a Asuán visitando templos antiguos, tumbas reales y monumentos icónicos.',
                'short_description_pt': 'Descubra as maravilhas eternas do Egito nesta jornada de 8 dias. Explore as Pirâmides de Gizé, o Grande Museu Egípcio, e navegue pelo Nilo em um cruzeiro 5 estrelas de Luxor a Aswan visitando templos antigos, tumbas reais e monumentos icônicos.',
                'description': '<p style="text-align: justify;">Discover the timeless wonders of Egypt on this unforgettable 8-day summer journey. Begin in Cairo with the legendary Pyramids of Giza, the Great Sphinx, and the stunning Grand Egyptian Museum. Then fly to Luxor and embark on a luxurious 5\u2605 Nile Cruise, sailing to Aswan through the heartland of ancient civilization.</p>'
                    + '<p style="text-align: justify;"><strong>Season:</strong> Summer</p>'
                    + '<p style="text-align: justify;"><strong>Night Distribution:</strong></p>'
                    + '<ul><li>3 Nights in Cairo \U0001f1ea\U0001f1ec (Azal Pyramids Hotel or similar 4\u2605)</li>'
                    + '<li>4 Nights on Nile Cruise (M/S Paradise or similar 5\u2605 \u2013 Full Board)</li></ul>'
                    + '<p style="text-align: justify;"><strong>Meal Plan:</strong></p>'
                    + '<ul><li>Daily breakfast at Cairo hotel</li>'
                    + '<li>Full board during Nile cruise (12 meals \u2013 beverages not included)</li></ul>'
                    + '<p style="text-align: justify;"><strong>Accommodation:</strong></p>'
                    + '<ul><li>Cairo: Azal Pyramids Hotel or similar 4\u2605</li>'
                    + '<li>Nile Cruise: M/S Paradise or similar 5\u2605 (Full Board)</li></ul>',
                'description_es': '<p style="text-align: justify;">Descubra las maravillas eternas de Egipto en este inolvidable viaje de verano de 8 d\u00edas. Comience en El Cairo con las legendarias Pir\u00e1mides de Guiza, la Gran Esfinge y el impresionante Gran Museo Egipcio. Luego vuele a Luxor y embarque en un lujoso crucero 5\u2605 por el Nilo, navegando hasta Asu\u00e1n a trav\u00e9s del coraz\u00f3n de la civilizaci\u00f3n antigua.</p>'
                    + '<p style="text-align: justify;"><strong>Temporada:</strong> Verano</p>'
                    + '<p style="text-align: justify;"><strong>Distribuci\u00f3n de Noches:</strong></p>'
                    + '<ul><li>3 Noches en El Cairo \U0001f1ea\U0001f1ec (Azal Pyramids Hotel o similar 4\u2605)</li>'
                    + '<li>4 Noches en Crucero por el Nilo (M/S Paradise o similar 5\u2605 \u2013 Pensi\u00f3n Completa)</li></ul>'
                    + '<p style="text-align: justify;"><strong>R\u00e9gimen de Alimentaci\u00f3n:</strong></p>'
                    + '<ul><li>Desayuno diario en el hotel de El Cairo</li>'
                    + '<li>Pensi\u00f3n completa durante el crucero por el Nilo (12 comidas \u2013 bebidas no incluidas)</li></ul>'
                    + '<p style="text-align: justify;"><strong>Alojamiento:</strong></p>'
                    + '<ul><li>El Cairo: Azal Pyramids Hotel o similar 4\u2605</li>'
                    + '<li>Crucero por el Nilo: M/S Paradise o similar 5\u2605 (Pensi\u00f3n Completa)</li></ul>',
                'description_pt': '<p style="text-align: justify;">Descubra as maravilhas eternas do Egito nesta inesquec\u00edvel jornada de ver\u00e3o de 8 dias. Comece no Cairo com as lend\u00e1rias Pir\u00e2mides de Giz\u00e9, a Grande Esfinge e o deslumbrante Grande Museu Eg\u00edpcio. Em seguida, voe para Luxor e embarque em um luxuoso cruzeiro 5\u2605 pelo Nilo, navegando at\u00e9 Aswan pelo cora\u00e7\u00e3o da civiliza\u00e7\u00e3o antiga.</p>'
                    + '<p style="text-align: justify;"><strong>Temporada:</strong> Ver\u00e3o</p>'
                    + '<p style="text-align: justify;"><strong>Distribui\u00e7\u00e3o das Hospedagens:</strong></p>'
                    + '<ul><li>3 Noites no Cairo \U0001f1ea\U0001f1ec (Azal Pyramids Hotel ou similar 4\u2605)</li>'
                    + '<li>4 Noites em Cruzeiro pelo Nilo (M/S Paradise ou similar 5\u2605 \u2013 Pens\u00e3o Completa)</li></ul>'
                    + '<p style="text-align: justify;"><strong>Regime de Refei\u00e7\u00f5es:</strong></p>'
                    + '<ul><li>Caf\u00e9 da manh\u00e3 di\u00e1rio no hotel do Cairo</li>'
                    + '<li>Pens\u00e3o completa durante o cruzeiro pelo Nilo (12 refei\u00e7\u00f5es \u2013 bebidas n\u00e3o inclu\u00eddas)</li></ul>'
                    + '<p style="text-align: justify;"><strong>Hospedagem:</strong></p>'
                    + '<ul><li>Cairo: Azal Pyramids Hotel ou similar 4\u2605</li>'
                    + '<li>Cruzeiro pelo Nilo: M/S Paradise ou similar 5\u2605 (Pens\u00e3o Completa)</li></ul>',
                'category': category,
                'tour_type': tour_type,
                'days': 8,
                'nights': 7,
                'price': 1077.00,
                'price_single_supplement': 630.00,
                'child_price': 570.00,
                'currency': 'USD',
                'min_group_size': 2,
                'max_group_size': 15,
                'is_featured': True,
                'is_best_seller': False,
                'is_new': True,
                'is_multi_destination': False,
                'difficulty_level': 'easy',
                'departure_city': 'Cairo',
                'languages': 'English, Spanish, Portuguese',
                'is_published': True,
            }
        )

        # Add destinations
        dest_slugs = ['cairo', 'luxor', 'aswan']
        for slug in dest_slugs:
            try:
                dest = Destination.objects.get(slug=slug)
                tour.destinations.add(dest)
            except Destination.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Destination {slug} not found'))

        # ===== HIGHLIGHTS =====
        tour.highlights.all().delete()

        highlights_data = [
            {
                'title': 'Premium Nile Cruise (4 Nights)',
                'title_es': 'Crucero Premium por el Nilo (4 Noches)',
                'title_pt': 'Cruzeiro Premium pelo Nilo (4 Noites)',
                'description': j('Sail between Luxor and Aswan aboard a 5\u2605 cruise with full board. A unique experience in the \u201ccradle of civilization,\u201d with stops in Edfu, Kom Ombo and Aswan. All meals on board included.'),
                'description_es': j('Navegue entre Luxor y Asu\u00e1n a bordo de un crucero 5\u2605 con pensi\u00f3n completa. Una experiencia \u00fanica en la \u201ccuna de la civilizaci\u00f3n\u201d, con paradas en Edf\u00fa, Kom Ombo y Asu\u00e1n. Todas las comidas a bordo incluidas.'),
                'description_pt': j('Navegue entre Luxor e Aswan a bordo de um cruzeiro 5\u2605 com pens\u00e3o completa. Uma experi\u00eancia \u00fanica no \u201cber\u00e7o da civiliza\u00e7\u00e3o\u201d, com paradas em Edfu, Kom Ombo e Aswan. Todas as refei\u00e7\u00f5es a bordo inclu\u00eddas.'),
                'icon': 'ship',
            },
            {
                'title': 'Comfortable Accommodation & Specialized Guides',
                'title_es': 'Alojamiento Confortable y Gu\u00edas Especializados',
                'title_pt': 'Hospedagem Confort\u00e1vel e Guias Especializados',
                'description': j('Cairo: 4\u2605 hotel (Azal Pyramids or similar) with breakfast. Cruise: 5\u2605 with full board (12 meals). Guides: Official English-speaking Egyptologists throughout the itinerary.'),
                'description_es': j('El Cairo: Hotel 4\u2605 (Azal Pyramids o similar) con desayuno. Crucero: 5\u2605 con pensi\u00f3n completa (12 comidas). Gu\u00edas: Egipt\u00f3logos oficiales de habla inglesa durante todo el itinerario.'),
                'description_pt': j('Cairo: Hotel 4\u2605 (Azal Pyramids ou similar) com caf\u00e9 da manh\u00e3. Cruzeiro: 5\u2605 com pens\u00e3o completa (12 refei\u00e7\u00f5es). Guias: Egipt\u00f3logos oficiais de l\u00edngua inglesa durante todo o roteiro.'),
                'icon': 'hotel',
            },
            {
                'title': 'Pyramids of Giza & The Great Sphinx',
                'title_es': 'Pir\u00e1mides de Guiza y la Gran Esfinge',
                'title_pt': 'Pir\u00e2mides de Giz\u00e9 e a Grande Esfinge',
                'description': j('Visit the Giza Plateau, home to the last surviving wonder of the ancient world. The three great pyramids (Cheops, Chephren and Mycerinus) and the majestic Sphinx guard over 4,500 years of history.'),
                'description_es': j('Visite la Meseta de Guiza, hogar de la \u00faltima maravilla del mundo antiguo. Las tres grandes pir\u00e1mides (Keops, Kefr\u00e9n y Micerinos) y la majestuosa Esfinge custodian m\u00e1s de 4.500 a\u00f1os de historia.'),
                'description_pt': j('Visite o Planalto de Giz\u00e9, lar da \u00faltima maravilha do mundo antigo. As tr\u00eas grandes pir\u00e2mides (Qu\u00e9ops, Qu\u00e9fren e Miquerinos) e a majestosa Esfinge guardam mais de 4.500 anos de hist\u00f3ria.'),
                'icon': 'pyramid',
            },
            {
                'title': 'Grand Egyptian Museum (GEM)',
                'title_es': 'Gran Museo Egipcio (GEM)',
                'title_pt': 'Grande Museu Eg\u00edpcio (GEM)',
                'description': j('Egypt\u2019s newest treasure. Located at the foot of the Pyramids, the GEM houses over 50,000 artifacts, including the complete, never-before-seen collection of King Tutankhamun.'),
                'description_es': j('El tesoro m\u00e1s nuevo de Egipto. Ubicado al pie de las Pir\u00e1mides, el GEM alberga m\u00e1s de 50.000 artefactos, incluyendo la colecci\u00f3n completa e in\u00e9dita del rey Tutankam\u00f3n.'),
                'description_pt': j('O mais novo tesouro do Egito. Localizado aos p\u00e9s das Pir\u00e2mides, o GEM abriga mais de 50.000 artefatos, incluindo a cole\u00e7\u00e3o completa e nunca antes vista do rei Tutanc\u00e2mon.'),
                'icon': 'museum',
            },
            {
                'title': 'Valley of the Kings & Hatshepsut Temple',
                'title_es': 'Valle de los Reyes y Templo de Hatshepsut',
                'title_pt': 'Vale dos Reis e Templo de Hatshepsut',
                'description': j('Explore the ancient necropolis of Thebes on the west bank of Luxor. Includes 3 royal tombs, the imposing Colossi of Memnon, and the terraced temple of Egypt\u2019s only female pharaoh, Hatshepsut.'),
                'description_es': j('Explore la antigua necr\u00f3polis de Tebas en la orilla occidental de Luxor. Incluye 3 tumbas reales, los imponentes Colosos de Memn\u00f3n y el templo en terrazas de la \u00fanica faraona mujer de Egipto, Hatshepsut.'),
                'description_pt': j('Explore a antiga necr\u00f3pole de Tebas na margem oeste de Luxor. Inclui 3 tumbas reais, os imponentes Colossos de Memnon e o templo terra\u00e7o da \u00fanica fara\u00f3 mulher do Egito, Hatshepsut.'),
                'icon': 'crown',
            },
            {
                'title': 'Karnak & Luxor Temples',
                'title_es': 'Templos de Karnak y Luxor',
                'title_pt': 'Templos de Karnak e Luxor',
                'description': j('Karnak is the largest religious complex ever built, with its legendary Hypostyle Hall of 134 columns. Luxor, connected by 2.7 km of Sphinxes, is one of the most elegant and well-preserved temples in the country.'),
                'description_es': j('Karnak es el complejo religioso m\u00e1s grande jam\u00e1s construido, con su legendaria sala hip\u00f3stila de 134 columnas. Luxor, conectado por 2,7 km de Esfinges, es uno de los templos m\u00e1s elegantes y mejor conservados del pa\u00eds.'),
                'description_pt': j('Karnak \u00e9 o maior complexo religioso j\u00e1 constru\u00eddo, com sua lend\u00e1ria sala hipostila de 134 colunas. Luxor, conectado por 2,7 km de Esfinges, \u00e9 um dos templos mais elegantes e bem preservados do pa\u00eds.'),
                'icon': 'columns',
            },
            {
                'title': 'Edfu & Kom Ombo Temples',
                'title_es': 'Templos de Edf\u00fa y Kom Ombo',
                'title_pt': 'Templos de Edfu e Kom Ombo',
                'description': j('Edfu is the best-preserved temple in Egypt, dedicated to the falcon god Horus. Kom Ombo is a unique double temple, dedicated to Sobek (crocodile god) and Haroeris, featuring reliefs of ancient surgical instruments.'),
                'description_es': j('Edf\u00fa es el templo mejor conservado de Egipto, dedicado al dios halc\u00f3n Horus. Kom Ombo es un doble templo \u00fanico, dedicado a Sobek (dios cocodrilo) y Haroeris, con relieves de antiguos instrumentos quir\u00fargicos.'),
                'description_pt': j('Edfu \u00e9 o templo mais bem preservado do Egito, dedicado ao deus falc\u00e3o H\u00f3rus. Kom Ombo \u00e9 um templo duplo \u00fanico, dedicado a Sobek (deus crocodilo) e Haroeris, com relevos de instrumentos cir\u00fargicos antigos.'),
                'icon': 'temple',
            },
            {
                'title': 'Aswan: High Dam, Philae Temple & Felucca',
                'title_es': 'Asu\u00e1n: Presa Alta, Templo de Filae y Faluca',
                'title_pt': 'Assu\u00e3: Barragem Alta, Templo de Filas e Feluca',
                'description': j('The High Dam, Egypt\u2019s greatest modern engineering work. The Temple of Philae, dedicated to the goddess Isis, rescued from the waters. And a relaxing felucca ride, the traditional Nile sailboat.'),
                'description_es': j('La Presa Alta, la mayor obra de ingenier\u00eda moderna de Egipto. El Templo de Filae, dedicado a la diosa Isis, rescatado de las aguas. Y un relajante paseo en faluca, el tradicional velero del Nilo.'),
                'description_pt': j('A Barragem Alta, a maior obra de engenharia moderna do Egito. O Templo de Filas, dedicado \u00e0 deusa \u00cdsis, resgatado das \u00e1guas. E um relaxante passeio de feluca, o tradicional barco \u00e0 vela do Nilo.'),
                'icon': 'water',
            },
        ]

        for i, h in enumerate(highlights_data):
            TourHighlight.objects.create(tour=tour, sort_order=i, **h)

        # ===== ITINERARY =====
        tour.itinerary.all().delete()

        itinerary_data = [
            {
                'day_number': 1,
                'title': 'Arrival in Cairo',
                'title_es': 'Llegada a El Cairo',
                'title_pt': 'Chegada ao Cairo',
                'description': j('Upon your arrival at Cairo International Airport, you will be welcomed by our representative and assisted with entry formalities. Then, enjoy a private transfer to your hotel, where we will help you with a smooth check-in.')
                    + j('Cairo \u2013 The bustling capital of Egypt, Cairo is a vibrant metropolis where ancient history meets modern life. Known as \u201cThe City of a Thousand Minarets,\u201d it is the gateway to the legendary Pyramids of Giza and the timeless Nile River.')
                    + j('Overnight in Cairo.'),
                'description_es': j('A su llegada al Aeropuerto Internacional de El Cairo, ser\u00e1 recibido por nuestro representante y asistido con las formalidades de entrada. Luego, disfrute de un traslado privado a su hotel, donde le ayudaremos con un check-in sin problemas.')
                    + j('El Cairo \u2013 La bulliciosa capital de Egipto, El Cairo es una metr\u00f3polis vibrante donde la historia antigua se encuentra con la vida moderna. Conocida como \u201cLa Ciudad de los Mil Minaretes\u201d, es la puerta de entrada a las legendarias Pir\u00e1mides de Guiza y al eterno R\u00edo Nilo.')
                    + j('Noche en El Cairo.'),
                'description_pt': j('Ao chegar ao Aeroporto Internacional do Cairo, voc\u00ea ser\u00e1 recebido pelo nosso representante e auxiliado com as formalidades de entrada. Em seguida, desfrute de um transfer privado para seu hotel, onde o ajudaremos com um check-in tranquilo.')
                    + j('Cairo \u2013 A agitada capital do Egito, Cairo \u00e9 uma metr\u00f3pole vibrante onde a hist\u00f3ria antiga encontra a vida moderna. Conhecida como \u201cA Cidade dos Mil Minaretes\u201d, \u00e9 a porta de entrada para as lend\u00e1rias Pir\u00e2mides de Giz\u00e9 e o eterno Rio Nilo.')
                    + j('Pernoite no Cairo.'),
                'meals_included': '\u2013',
                'accommodation': 'Azal Pyramids Hotel or similar 4\u2605',
                'accommodation_es': 'Azal Pyramids Hotel o similar 4\u2605',
                'accommodation_pt': 'Azal Pyramids Hotel ou similar 4\u2605',
                'locations': 'Cairo',
            },
            {
                'day_number': 2,
                'title': 'Giza Pyramids & Grand Egyptian Museum',
                'title_es': 'Pir\u00e1mides de Guiza y Gran Museo Egipcio',
                'title_pt': 'Pir\u00e2mides de Giz\u00e9 e Grande Museu Eg\u00edpcio',
                'description': j('After breakfast, head to the Giza Plateau to explore the majestic Pyramids of Cheops (Khufu), Chephren (Khafre), and Mycerinus (Menkaure). These towering monuments have stood for over 4,500 years as the last surviving wonder of the ancient world. Then, marvel at the legendary Great Sphinx, a mythical creature with the body of a lion and the face of a pharaoh, guardian of the Giza necropolis.')
                    + j('After your visit, there will be a stop at a local restaurant for lunch (not included \u2013 at your own expense). In the afternoon, continue to the Grand Egyptian Museum (GEM) \u2013 a stunning architectural masterpiece at the foot of the Giza Plateau. The museum houses over 50,000 genuine artifacts, including the complete collection of King Tutankhamun\u2019s treasures. Return to your hotel in the late afternoon.')
                    + j('Overnight in Cairo.'),
                'description_es': j('Despu\u00e9s del desayuno, dir\u00edjase a la Meseta de Guiza para explorar las majestuosas Pir\u00e1mides de Keops (Jufu), Kefr\u00e9n (Jafra) y Micerinos (Menkaure). Estos imponentes monumentos han permanecido durante m\u00e1s de 4.500 a\u00f1os como la \u00faltima maravilla del mundo antiguo. Luego, marav\u00edllese ante la legendaria Gran Esfinge, una criatura m\u00edtica con cuerpo de le\u00f3n y rostro de fara\u00f3n, guardiana de la necr\u00f3polis de Guiza.')
                    + j('Despu\u00e9s de la visita, habr\u00e1 una parada en un restaurante local para almorzar (no incluido \u2013 por cuenta propia). Por la tarde, contin\u00fae al Gran Museo Egipcio (GEM) \u2013 una impresionante obra maestra arquitect\u00f3nica al pie de la Meseta de Guiza. El museo alberga m\u00e1s de 50.000 artefactos genuinos, incluyendo la colecci\u00f3n completa del rey Tutankam\u00f3n. Regreso a su hotel a \u00faltima hora de la tarde.')
                    + j('Noche en El Cairo.'),
                'description_pt': j('Ap\u00f3s o caf\u00e9 da manh\u00e3, dirija-se ao Planalto de Giz\u00e9 para explorar as majestosas Pir\u00e2mides de Qu\u00e9ops (Khufu), Qu\u00e9fren (Khafre) e Miquerinos (Menkaure). Estes monumentos imponentes permanecem h\u00e1 mais de 4.500 anos como a \u00faltima maravilha do mundo antigo. Em seguida, maravilhe-se com a lend\u00e1ria Grande Esfinge, uma criatura m\u00edtica com corpo de le\u00e3o e rosto de fara\u00f3, guardi\u00e3 da necr\u00f3pole de Giz\u00e9.')
                    + j('Ap\u00f3s a visita, haver\u00e1 uma parada em um restaurante local para almo\u00e7o (n\u00e3o inclu\u00eddo \u2013 por sua conta). \u00c0 tarde, continue para o Grande Museu Eg\u00edpcio (GEM) \u2013 uma deslumbrante obra-prima arquitet\u00f4nica aos p\u00e9s do Planalto de Giz\u00e9. O museu abriga mais de 50.000 artefatos genu\u00ednos, incluindo a cole\u00e7\u00e3o completa do rei Tutanc\u00e2mon. Retorno ao seu hotel no final da tarde.')
                    + j('Pernoite no Cairo.'),
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Caf\u00e9 da manh\u00e3',
                'accommodation': 'Azal Pyramids Hotel or similar 4\u2605',
                'accommodation_es': 'Azal Pyramids Hotel o similar 4\u2605',
                'accommodation_pt': 'Azal Pyramids Hotel ou similar 4\u2605',
                'locations': 'Cairo',
            },
            {
                'day_number': 3,
                'title': 'Cairo to Luxor \u2013 Nile Cruise Embarkation',
                'title_es': 'El Cairo a Luxor \u2013 Embarque en el Crucero por el Nilo',
                'title_pt': 'Cairo para Luxor \u2013 Embarque no Cruzeiro pelo Nilo',
                'description': j('Early breakfast (boxed) and check-out. Transfer to Cairo Airport for your domestic flight to Luxor (domestic flight is not included) \u2013 the ancient city of Thebes, once the glittering capital of the New Kingdom. Upon arrival, visit the magnificent Karnak Temple, the largest religious complex ever built, covering over 200 acres. Its legendary Hypostyle Hall features 134 towering columns, making it a true open-air museum.')
                    + j('Transfer to your 5\u2605 Nile Cruise and complete check-in. In the late afternoon, explore the majestic Luxor Temple, dedicated to the god Amun, largely built by Pharaoh Amenhotep III and later expanded by Ramses II. The temple is connected to Karnak by the famous Avenue of the Sphinxes. Enjoy dinner on board.')
                    + j('Overnight on cruise (Night 1).'),
                'description_es': j('Desayuno temprano (para llevar) y check-out. Traslado al Aeropuerto de El Cairo para su vuelo dom\u00e9stico a Luxor \u2013 la antigua Tebas, una vez la brillante capital del Imperio Nuevo. A su llegada, visite el magn\u00edfico Templo de Karnak, el complejo religioso m\u00e1s grande jam\u00e1s construido, que cubre m\u00e1s de 200 acres. Su legendaria Sala Hip\u00f3stila presenta 134 columnas imponentes, convirti\u00e9ndolo en un verdadero museo al aire libre.')
                    + j('Traslado a su Crucero 5\u2605 por el Nilo y complete el check-in. A \u00faltima hora de la tarde, explore el majestuoso Templo de Luxor, dedicado al dios Am\u00f3n, construido en gran parte por el fara\u00f3n Amenhotep III y luego expandido por Rams\u00e9s II. El templo est\u00e1 conectado a Karnak por la famosa Avenida de las Esfinges. Cena a bordo.')
                    + j('Noche en el crucero (Noche 1).'),
                'description_pt': j('Caf\u00e9 da manh\u00e3 (caixa) e check-out. Transfer para o Aeroporto do Cairo para seu voo dom\u00e9stico para Luxor \u2013 a antiga Tebas, outrora a capital reluzente do Imp\u00e9rio Novo. Ao chegar, visite o magn\u00edfico Templo de Karnak, o maior complexo religioso j\u00e1 constru\u00eddo, cobrindo mais de 200 acres. Sua lend\u00e1ria Sala Hipostila apresenta 134 colunas imponentes, tornando-o um verdadeiro museu a c\u00e9u aberto.')
                    + j('Transfer para seu Cruzeiro 5\u2605 pelo Nilo e complete o check-in. No final da tarde, explore o majestoso Templo de Luxor, dedicado ao deus Amon, constru\u00eddo em grande parte pelo fara\u00f3 Amenhotep III e posteriormente expandido por Rams\u00e9s II. O templo \u00e9 conectado a Karnak pela famosa Avenida das Esfinges. Jantar a bordo.')
                    + j('Pernoite no cruzeiro (Noite 1).'),
                'meals_included': 'Full Board',
                'meals_included_es': 'Pensi\u00f3n Completa',
                'meals_included_pt': 'Pens\u00e3o Completa',
                'accommodation': 'M/S Paradise Nile Cruise or similar 5\u2605',
                'accommodation_es': 'M/S Paradise Nile Cruise o similar 5\u2605',
                'accommodation_pt': 'M/S Paradise Nile Cruise ou similar 5\u2605',
                'locations': 'Luxor',
            },
            {
                'day_number': 4,
                'title': 'West Bank Luxor \u2013 Sailing to Edfu',
                'title_es': 'Orilla Occidental de Luxor \u2013 Navegaci\u00f3n a Edf\u00fa',
                'title_pt': 'Margem Ocidental de Luxor \u2013 Navega\u00e7\u00e3o para Edfu',
                'description': j('Breakfast on board. Explore the West Bank of Luxor, the ancient necropolis of Thebes. Visit the mysterious Valley of the Kings \u2013 a vast royal burial ground hidden within the Theban hills, where Egypt\u2019s mighty New Kingdom pharaohs were laid to rest in lavishly decorated tombs carved deep into the limestone (entrance to 3 tombs included).')
                    + j('Admire the imposing Colossi of Memnon \u2013 two gigantic stone statues, each over 18 meters tall, that once guarded the entrance of Pharaoh Amenhotep III\u2019s mortuary temple. Then, discover the majestic Temple of Queen Hatshepsut at Deir el-Bahari \u2013 a breathtaking terraced sanctuary carved into the cliffs, dedicated to Egypt\u2019s most famous female pharaoh.')
                    + j('Return to the ship for lunch. Sail towards Edfu, passing through the Esna Lock. Dinner on board.')
                    + j('Overnight on cruise (Night 2).')
                    + j('\u2728 Optional: Early morning hot air balloon ride over Luxor. Ask us for details!'),
                'description_es': j('Desayuno a bordo. Explore la Orilla Occidental de Luxor, la antigua necr\u00f3polis de Tebas. Visite el misterioso Valle de los Reyes \u2013 un vasto cementerio real escondido en las colinas tebanas, donde los poderosos faraones del Imperio Nuevo fueron sepultados en tumbas ricamente decoradas talladas en la piedra caliza (entrada a 3 tumbas incluida).')
                    + j('Admire los imponentes Colosos de Memn\u00f3n \u2013 dos gigantescas estatuas de piedra, cada una de m\u00e1s de 18 metros de altura, que una vez custodiaron la entrada del templo mortuorio del fara\u00f3n Amenhotep III. Luego, descubra el majestuoso Templo de la Reina Hatshepsut en Deir el-Bahari \u2013 un impresionante santuario en terrazas tallado en los acantilados, dedicado a la faraona m\u00e1s famosa de Egipto.')
                    + j('Regreso al barco para almorzar. Navegue hacia Edf\u00fa, pasando por la Esclusa de Esn\u00e1. Cena a bordo.')
                    + j('Noche en el crucero (Noche 2).')
                    + j('\u2728 Opcional: Paseo en globo aerost\u00e1tico al amanecer sobre Luxor. \u00a1Cons\u00faltenos!'),
                'description_pt': j('Caf\u00e9 da manh\u00e3 a bordo. Explore a Margem Ocidental de Luxor, a antiga necr\u00f3pole de Tebas. Visite o misterioso Vale dos Reis \u2013 um vasto cemit\u00e9rio real escondido nas colinas tebanas, onde os poderosos fara\u00f3s do Imp\u00e9rio Novo foram sepultados em tumbas ricamente decoradas esculpidas na rocha (entrada para 3 tumbas inclu\u00edda).')
                    + j('Admire os imponentes Colossos de Memnon \u2013 duas est\u00e1tuas gigantes de pedra, cada uma com mais de 18 metros de altura, que outrora guardavam a entrada do templo mortu\u00e1rio do fara\u00f3 Amenhotep III. Em seguida, descubra o majestoso Templo da Rainha Hatshepsut em Deir el-Bahari \u2013 um deslumbrante santu\u00e1rio em terra\u00e7os esculpido nos penhascos, dedicado \u00e0 mais famosa fara\u00f3 do Egito.')
                    + j('Retorno ao barco para almo\u00e7o. Navegue para Edfu, passando pela Eclusa de Esna. Jantar a bordo.')
                    + j('Pernoite no cruzeiro (Noite 2).')
                    + j('\u2728 Opcional: Passeio de bal\u00e3o de ar quente ao amanhecer sobre Luxor. Consulte-nos!'),
                'meals_included': 'Full Board',
                'meals_included_es': 'Pensi\u00f3n Completa',
                'meals_included_pt': 'Pens\u00e3o Completa',
                'accommodation': 'M/S Paradise Nile Cruise or similar 5\u2605',
                'accommodation_es': 'M/S Paradise Nile Cruise o similar 5\u2605',
                'accommodation_pt': 'M/S Paradise Nile Cruise ou similar 5\u2605',
                'locations': 'Luxor \u2013 Edfu',
            },
            {
                'day_number': 5,
                'title': 'Edfu & Kom Ombo Temples \u2013 Sailing to Aswan',
                'title_es': 'Templos de Edf\u00fa y Kom Ombo \u2013 Navegaci\u00f3n a Asu\u00e1n',
                'title_pt': 'Templos de Edfu e Kom Ombo \u2013 Navega\u00e7\u00e3o para Aswan',
                'description': j('Breakfast on board. Visit the Temple of Horus in Edfu \u2013 the best-preserved temple in all of Egypt, buried under desert sand for centuries until its rediscovery. Dedicated to the falcon-headed god Horus, this Ptolemaic masterpiece offers an almost intact glimpse of ancient religious life.')
                    + j('Return to the ship and sail to Kom Ombo. Lunch on board. In the afternoon, explore the unique double Temple of Kom Ombo, dedicated equally to Sobek (the fearsome crocodile god) and Haroeris (Horus the Elder). Perfectly symmetrical, the temple also contains fascinating reliefs depicting ancient surgical instruments.')
                    + j('Continue sailing to Aswan. Dinner on board.')
                    + j('Overnight on cruise (Night 3).'),
                'description_es': j('Desayuno a bordo. Visite el Templo de Horus en Edf\u00fa \u2013 el templo mejor conservado de todo Egipto, enterrado bajo la arena del desierto durante siglos hasta su redescubrimiento. Dedicado al dios halc\u00f3n Horus, esta obra maestra ptolemaica ofrece una visi\u00f3n casi intacta de la vida religiosa antigua.')
                    + j('Regreso al barco y navegue hacia Kom Ombo. Almuerzo a bordo. Por la tarde, explore el \u00fanico Templo de Kom Ombo, dedicado igualmente a Sobek (el temible dios cocodrilo) y Haroeris (Horus el Viejo). Perfectamente sim\u00e9trico, el templo tambi\u00e9n contiene fascinantes relieves que representan antiguos instrumentos quir\u00fargicos.')
                    + j('Contin\u00fae navegando hacia Asu\u00e1n. Cena a bordo.')
                    + j('Noche en el crucero (Noche 3).'),
                'description_pt': j('Caf\u00e9 da manh\u00e3 a bordo. Visite o Templo de H\u00f3rus em Edfu \u2013 o templo mais bem preservado de todo o Egito, enterrado sob a areia do deserto por s\u00e9culos at\u00e9 seu redescobrimento. Dedicado ao deus falc\u00e3o H\u00f3rus, esta obra-prima ptolemaica oferece um vislumbre quase intacto da vida religiosa antiga.')
                    + j('Retorno ao barco e navegue para Kom Ombo. Almo\u00e7o a bordo. \u00c0 tarde, explore o \u00fanico Templo de Kom Ombo, dedicado igualmente a Sobek (o tem\u00edvel deus crocodilo) e Haroeris (H\u00f3rus, o Velho). Perfeitamente sim\u00e9trico, o templo tamb\u00e9m cont\u00e9m fascinantes relevos que retratam antigos instrumentos cir\u00fargicos.')
                    + j('Continue navegando para Aswan. Jantar a bordo.')
                    + j('Pernoite no cruzeiro (Noite 3).'),
                'meals_included': 'Full Board',
                'meals_included_es': 'Pensi\u00f3n Completa',
                'meals_included_pt': 'Pens\u00e3o Completa',
                'accommodation': 'M/S Paradise Nile Cruise or similar 5\u2605',
                'accommodation_es': 'M/S Paradise Nile Cruise o similar 5\u2605',
                'accommodation_pt': 'M/S Paradise Nile Cruise ou similar 5\u2605',
                'locations': 'Edfu \u2013 Kom Ombo \u2013 Aswan',
            },
            {
                'day_number': 6,
                'title': 'Aswan \u2013 High Dam & Philae Temple',
                'title_es': 'Asu\u00e1n \u2013 Presa Alta y Templo de Filae',
                'title_pt': 'Aswan \u2013 Barragem Alta e Templo de Filas',
                'description': j('Breakfast on board. Visit the monumental High Dam of Aswan \u2013 a modern engineering marvel completed in 1971, controlling the Nile\u2019s annual floods, generating hydroelectric power, and creating Lake Nasser, one of the world\u2019s largest artificial reservoirs.')
                    + j('Then, take a short boat ride to the beautiful Temple of Philae, dedicated to the goddess Isis. Rescued from the rising waters of Lake Nasser and meticulously relocated to the island of Agilkia, this romantic temple complex was the last bastion of ancient Egyptian religion, blending Egyptian, Greek, and Roman architectural styles.')
                    + j('Return to the ship for lunch. In the afternoon, enjoy a relaxing Felucca sail \u2013 a graceful wooden sailboat unchanged for millennia \u2013 gliding through the emerald waters of the Nile around Elephantine Island and the Botanical Garden. Dinner on board.')
                    + j('Overnight on cruise (Night 4).')
                    + j('\u2728 Optional: Excursion to a traditional Nubian village. Ask us for details!'),
                'description_es': j('Desayuno a bordo. Visite la monumental Presa Alta de Asu\u00e1n \u2013 una maravilla de la ingenier\u00eda moderna completada en 1971, que controla las inundaciones anuales del Nilo, genera energ\u00eda hidroel\u00e9ctrica y crea el Lago Nasser, uno de los embalses artificiales m\u00e1s grandes del mundo.')
                    + j('Luego, tome un corto paseo en barco hasta el hermoso Templo de Filae, dedicado a la diosa Isis. Rescatado de las aguas crecientes del Lago Nasser y meticulosamente reubicado en la isla de Agilkia, este rom\u00e1ntico complejo de templos fue el \u00faltimo basti\u00f3n de la religi\u00f3n del antiguo Egipto, combinando estilos arquitect\u00f3nicos egipcios, griegos y romanos.')
                    + j('Regreso al barco para almorzar. Por la tarde, disfrute de un relajante paseo en Faluca \u2013 un elegante velero de madera inalterado durante milenios \u2013 desliz\u00e1ndose por las aguas esmeralda del Nilo alrededor de la Isla de Elefantina y el Jard\u00edn Bot\u00e1nico. Cena a bordo.')
                    + j('Noche en el crucero (Noche 4).')
                    + j('\u2728 Opcional: Excursi\u00f3n a una aldea nubia tradicional. \u00a1Cons\u00faltenos!'),
                'description_pt': j('Caf\u00e9 da manh\u00e3 a bordo. Visite a monumental Barragem Alta de Aswan \u2013 uma maravilha da engenharia moderna conclu\u00edda em 1971, que controla as cheias anuais do Nilo, gera energia hidrel\u00e9trica e cria o Lago Nasser, um dos maiores reservat\u00f3rios artificiais do mundo.')
                    + j('Em seguida, fa\u00e7a um curto passeio de barco at\u00e9 o belo Templo de Filas, dedicado \u00e0 deusa \u00cdsis. Resgatado das \u00e1guas crescentes do Lago Nasser e meticulosamente realocado para a Ilha de Agilkia, este rom\u00e2ntico complexo de templos foi o \u00faltimo basti\u00e3o da religi\u00e3o do antigo Egito, combinando estilos arquitet\u00f4nicos eg\u00edpcios, gregos e romanos.')
                    + j('Retorno ao barco para almo\u00e7o. \u00c0 tarde, desfrute de um relaxante passeio de Feluca \u2013 um elegante veleiro de madeira inalterado por mil\u00eanios \u2013 deslizando pelas \u00e1guas esmeralda do Nilo ao redor da Ilha de Elefantina e do Jardim Bot\u00e2nico. Jantar a bordo.')
                    + j('Pernoite no cruzeiro (Noite 4).')
                    + j('\u2728 Opcional: Excurs\u00e3o a uma aldeia n\u00fabia tradicional. Consulte-nos!'),
                'meals_included': 'Full Board',
                'meals_included_es': 'Pensi\u00f3n Completa',
                'meals_included_pt': 'Pens\u00e3o Completa',
                'accommodation': 'M/S Paradise Nile Cruise or similar 5\u2605',
                'accommodation_es': 'M/S Paradise Nile Cruise o similar 5\u2605',
                'accommodation_pt': 'M/S Paradise Nile Cruise ou similar 5\u2605',
                'locations': 'Aswan',
            },
            {
                'day_number': 7,
                'title': 'Aswan to Cairo',
                'title_es': 'Asu\u00e1n a El Cairo',
                'title_pt': 'Aswan para Cairo',
                'description': j('Breakfast on board and check-out. Transfer to Aswan Airport for your domestic flight back to Cairo (included). Upon arrival, you will be met and transferred to your hotel.')
                    + j('Free afternoon at leisure to explore Cairo independently, relax, or shop for souvenirs.')
                    + j('Overnight in Cairo.')
                    + j('\u2728 Optional: Overland excursion to Abu Simbel (approximately 260 km each way). Visit the two magnificent UNESCO-listed temples of Ramses II and Nefertari. Includes transfers, entrance fees, and local guide. Please contact us for details and pricing!'),
                'description_es': j('Desayuno a bordo y check-out. Traslado al Aeropuerto de Asu\u00e1n para su vuelo dom\u00e9stico de regreso a El Cairo (incluido). A su llegada, ser\u00e1 recibido y trasladado a su hotel.')
                    + j('Tarde libre para explorar El Cairo de forma independiente, relajarse o comprar recuerdos.')
                    + j('Noche en El Cairo.')
                    + j('\u2728 Opcional: Excursi\u00f3n terrestre a Abu Simbel (aproximadamente 260 km cada tramo). Visite los dos magn\u00edficos templos de Rams\u00e9s II y Nefertari, declarados Patrimonio de la UNESCO. Incluye traslados, entradas y gu\u00eda local. \u00a1Cons\u00faltenos para precios y disponibilidad!'),
                'description_pt': j('Caf\u00e9 da manh\u00e3 a bordo e check-out. Transfer para o Aeroporto de Aswan para seu voo dom\u00e9stico de volta ao Cairo (inclu\u00eddo). Ao chegar, voc\u00ea ser\u00e1 recebido e transferido para seu hotel.')
                    + j('Tarde livre para explorar Cairo de forma independente, relaxar ou comprar lembran\u00e7as.')
                    + j('Pernoite no Cairo.')
                    + j('\u2728 Opcional: Excurs\u00e3o terrestre para Abu Simbel (aproximadamente 260 km cada trecho). Visite os dois magn\u00edficos templos de Rams\u00e9s II e Nefertari, Patrim\u00f4nio da UNESCO. Inclui transfers, ingressos e guia local. Consulte-nos para pre\u00e7os e disponibilidade!'),
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Caf\u00e9 da manh\u00e3',
                'accommodation': 'Azal Pyramids Hotel or similar 4\u2605',
                'accommodation_es': 'Azal Pyramids Hotel o similar 4\u2605',
                'accommodation_pt': 'Azal Pyramids Hotel ou similar 4\u2605',
                'locations': 'Aswan \u2013 Cairo',
            },
            {
                'day_number': 8,
                'title': 'Cairo \u2013 Departure',
                'title_es': 'El Cairo \u2013 Salida',
                'title_pt': 'Cairo \u2013 Partida',
                'description': j('Breakfast at the hotel (included if flight schedule permits). Check out from your Cairo hotel. At the scheduled time, transfer to Cairo International Airport for your departure flight.')
                    + j('End of our services. \u2708\ufe0f'),
                'description_es': j('Desayuno en el hotel (incluido si el horario del vuelo lo permite). Check-out de su hotel en El Cairo. A la hora programada, traslado al Aeropuerto Internacional de El Cairo para su vuelo de salida.')
                    + j('Fin de nuestros servicios. \u2708\ufe0f'),
                'description_pt': j('Caf\u00e9 da manh\u00e3 no hotel (inclu\u00eddo se o hor\u00e1rio do voo permitir). Check-out do hotel no Cairo. No hor\u00e1rio programado, transfer para o Aeroporto Internacional do Cairo para seu voo de partida.')
                    + j('Fim dos nossos servi\u00e7os. \u2708\ufe0f'),
                'meals_included': 'Breakfast',
                'meals_included_es': 'Desayuno',
                'meals_included_pt': 'Caf\u00e9 da manh\u00e3',
                'accommodation': '\u2013',
                'accommodation_es': '\u2013',
                'accommodation_pt': '\u2013',
                'locations': 'Cairo',
            },
        ]

        for it in itinerary_data:
            TourItinerary.objects.create(tour=tour, **it)

        # ===== INCLUSIONS & EXCLUSIONS =====
        tour.inclusions.all().delete()

        inclusions = [
            # INCLUSIONS
            ('All services mentioned in the program as included', 'Todos los servicios mencionados en el programa como inclu\u00eddos', 'Todos os servi\u00e7os mencionados no programa como inclu\u00eddos', True),
            ('Cairo hotel: 3 nights accommodation with breakfast (Azal Pyramids Hotel or similar 4\u2605)', 'Hotel en El Cairo: 3 noches de alojamiento con desayuno (Azal Pyramids Hotel o similar 4\u2605)', 'Hotel no Cairo: 3 noites de acomoda\u00e7\u00e3o com caf\u00e9 da manh\u00e3 (Azal Pyramids Hotel ou similar 4\u2605)', True),
            ('Nile Cruise: 4 nights on full board (12 meals included \u2013 beverages not included) on M/S Paradise or similar 5\u2605', 'Crucero por el Nilo: 4 noches en pensi\u00f3n completa (12 comidas incluidas \u2013 bebidas no incluidas) en M/S Paradise o similar 5\u2605', 'Cruzeiro pelo Nilo: 4 noites em pens\u00e3o completa (12 refei\u00e7\u00f5es inclu\u00eddas \u2013 bebidas n\u00e3o inclu\u00eddas) no M/S Paradise ou similar 5\u2605', True),
            ('Guided tours by an official Egyptian Egyptologist guide speaking English according to the itinerary', 'Visitas guiadas por un egipt\u00f3logo oficial de habla inglesa seg\u00fan el itinerario', 'Visitas guiadas por um egipt\u00f3logo oficial de l\u00edngua inglesa conforme o itiner\u00e1rio', True),
            ('Cairo sightseeing: Giza Pyramids, Great Sphinx & Grand Egyptian Museum (GEM)', 'Visitas en El Cairo: Pir\u00e1mides de Guiza, Gran Esfinge y Gran Museo Egipcio (GEM)', 'Passeios no Cairo: Pir\u00e2mides de Giz\u00e9, Grande Esfinge e Grande Museu Eg\u00edpcio (GEM)', True),
            ('Luxor tours: Valley of the Kings (3 tombs), Colossi of Memnon, Temple of Queen Hatshepsut', 'Visitas en Luxor: Valle de los Reyes (3 tumbas), Colosos de Memn\u00f3n, Templo de la Reina Hatshepsut', 'Passeios em Luxor: Vale dos Reis (3 tumbas), Colossos de Memnon, Templo da Rainha Hatshepsut', True),
            ('Aswan tours: Philae Temple, High Dam, Felucca ride, Kom Ombo Temple, Edfu Temple', 'Visitas en Asu\u00e1n: Templo de Filae, Presa Alta, Paseo en Faluca, Templo de Kom Ombo, Templo de Edf\u00fa', 'Passeios em Aswan: Templo de Filas, Barragem Alta, Passeio de Feluca, Templo de Kom Ombo, Templo de Edfu', True),
            ('Entrance fees to all historical sites and museums, as per itinerary', 'Entradas a todos los sitios hist\u00f3ricos y museos, seg\u00fan el itinerario', 'Entradas para todos os s\u00edtios hist\u00f3ricos e museus, conforme o itiner\u00e1rio', True),
            ('Transportation in a modern air-conditioned car/van according to itinerary and group size', 'Transporte en veh\u00edculo moderno con aire acondicionado seg\u00fan itinerario y tama\u00f1o del grupo', 'Transporte em ve\u00edculo moderno com ar condicionado conforme itiner\u00e1rio e tamanho do grupo', True),
            ('Reception and assistance upon arrival in Cairo and departure assistance at Aswan and Luxor airports', 'Recepci\u00f3n y asistencia en la llegada a El Cairo y asistencia de salida en los aeropuertos de Asu\u00e1n y Luxor', 'Recep\u00e7\u00e3o e assist\u00eancia na chegada ao Cairo e assist\u00eancia de sa\u00edda nos aeroportos de Aswan e Luxor', True),
            ('Accommodation taxes in Cairo hotel and Nile cruise + city tax in Egypt', 'Impuestos de alojamiento en el hotel de El Cairo y crucero + impuesto de ciudad en Egipto', 'Impostos de acomoda\u00e7\u00e3o no hotel do Cairo e cruzeiro + imposto municipal no Egito', True),
            # EXCLUSIONS
            ('International flights (home \u2192 Cairo / Cairo \u2192 home)', 'Vuelos internacionales (origen \u2192 El Cairo / El Cairo \u2192 origen)', 'Voos internacionais (origem \u2192 Cairo / Cairo \u2192 origem)', False),
            ('Domestic flights: Cairo \u2192 Luxor / Aswan \u2192 Cairo (not included)', 'Vuelos dom\u00e9sticos: El Cairo \u2192 Luxor / Asu\u00e1n \u2192 El Cairo (no incluidos)', 'Voos dom\u00e9sticos: Cairo \u2192 Luxor / Aswan \u2192 Cairo (n\u00e3o inclu\u00eddos)', False),
            ('Egypt entry visa (available on arrival \u2013 approx. $30 USD \u2013 contact us for more information)', 'Visa de entrada a Egipto (disponible a la llegada \u2013 aproximadamente 30 USD \u2013 cons\u00faltenos para m\u00e1s informaci\u00f3n)', 'Visto de entrada no Egito (dispon\u00edvel na chegada \u2013 aproximadamente US$ 30 \u2013 consulte-nos para mais informa\u00e7\u00f5es)', False),
            ('Optional tours: Abu Simbel, hot air balloon over Luxor, Nubian village excursion', 'Excursiones opcionales: Abu Simbel, globo aerost\u00e1tico sobre Luxor, visita a aldea nubia', 'Passeios opcionais: Abu Simbel, bal\u00e3o de ar quente sobre Luxor, visita \u00e0 aldeia n\u00fabia', False),
            ('Meals not mentioned in the itinerary (lunch on Day 2 \u2013 at your own expense)', 'Comidas no mencionadas en el itinerario (almuerzo del D\u00eda 2 \u2013 por cuenta propia)', 'Refei\u00e7\u00f5es n\u00e3o mencionadas no itiner\u00e1rio (almo\u00e7o do Dia 2 \u2013 por sua conta)', False),
            ('Personal expenses: beverages, laundry, telephone calls, souvenirs, mini-bar', 'Gastos personales: bebidas, lavander\u00eda, llamadas telef\u00f3nicas, souvenirs, mini-bar', 'Despesas pessoais: bebidas, lavanderia, chamadas telef\u00f4nicas, souvenirs, mini-bar', False),
            ('Tips and gratuities for: guides, drivers, cruise crew, hotel staff, restaurant staff, airport porters', 'Propinas para: gu\u00edas, conductores, personal del crucero, personal del hotel, restaurantes, porteros', 'Gorjetas para: guias, motoristas, tripula\u00e7\u00e3o do cruzeiro, funcion\u00e1rios do hotel, restaurantes, carregadores', False),
            ('Excess baggage fees (domestic flights: 1 piece of 23kg per person)', 'Cargos por exceso de equipaje (vuelos dom\u00e9sticos: 1 pieza de 23 kg por persona)', 'Taxas por excesso de bagagem (voos dom\u00e9sticos: 1 pe\u00e7a de 23 kg por pessoa)', False),
            ('Travel insurance (highly recommended)', 'Seguro de viaje (altamente recomendado)', 'Seguro de viagem (altamente recomendado)', False),
        ]

        for i, (en, es, pt, is_inc) in enumerate(inclusions):
            TourInclusion.objects.create(
                tour=tour, item=en, item_es=es, item_pt=pt,
                is_included=is_inc, sort_order=i
            )

        # ===== PRICING =====
        TourPricing.objects.filter(tour=tour).delete()
        TourPricing.objects.create(
            tour=tour,
            season_name='Summer',
            season_name_es='Verano',
            season_name_pt='Ver\u00e3o',
            price_per_person=1077.00,
            single_supplement=630.00,
        )

        self.stdout.write(self.style.SUCCESS(
            f'Tour "Nile Splendor \u2013 Summer Offer" {"created" if created else "updated"} successfully!'
        ))
        self.stdout.write(self.style.SUCCESS(f'Tour ID: {tour.id}, Slug: {tour.slug}'))
