"""
Management command to add "Giza Pyramids and Egyptian Civilization Museum" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Giza Pyramids and Egyptian Civilization Museum 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Giza Pyramids and Egyptian Civilization Museum day tour...')

        # Get or create category and type
        category, _ = TourCategory.objects.get_or_create(
            slug='day-tours',
            defaults={
                'name': 'Day Tours',
                'name_es': 'Excursiones de un Día',
                'name_pt': 'Passeios de um Dia',
            }
        )

        tour_type, _ = TourType.objects.get_or_create(
            slug='day-tour',
            defaults={
                'name': 'Day Tour',
                'name_es': 'Excursión de un Día',
                'name_pt': 'Passeio de um Dia',
            }
        )

        # Create the tour
        tour, created = Tour.objects.update_or_create(
            slug='giza-pyramids-egyptian-civilization-museum-tour',
            defaults={
                'name': 'Giza Pyramids and Egyptian Civilization Museum Tour',
                'name_es': 'Tour Pirámides de Guiza y Museo de la Civilización Egipcia',
                'name_pt': 'Passeio às Pirâmides de Gizé e Museu da Civilização Egípcia',

                'short_description': (
                    'An unforgettable day to touch the essence of ancient history: '
                    'discover the majestic Giza Pyramids alongside the treasures of the '
                    'National Museum of Egyptian Civilization. Immerse yourself for 8 hours '
                    'in the pharaonic world, with an expert guide, entrance tickets to the '
                    'main monuments, and transfers included!'
                ),
                'short_description_es': (
                    'Un día inolvidable para tocar la esencia de la historia antigua: '
                    'descubre las majestuosas Pirámides de Guiza junto a las riquezas del '
                    'Museo Nacional de la Civilización Egipcia. ¡Sumérgete durante 8 horas '
                    'en el mundo faraónico, con un guía egiptólogo especializado, entradas '
                    'a los principales monumentos y traslados incluidos!'
                ),
                'short_description_pt': (
                    'Um dia memorável para sentir a essência da história antiga: '
                    'descubra as imponentes Pirâmides de Gizé juntamente com as riquezas '
                    'do Museu Nacional da Civilização Egípcia. São 8 horas imerso no '
                    'universo faraônico, acompanhado por um guia egiptólogo especializado, '
                    'com ingressos para os principais monumentos e traslados inclusos!'
                ),

                'description': '''<p>The Giza Pyramids and Egyptian Civilization Museum Tour is a comprehensive 8-hour experience including the Giza Pyramids in Greater Cairo and the National Museum of Egyptian Civilization.</p>

<p>Our Egyptian Egyptologist guide will meet you at your Cairo hotel. Departure to the Giza Complex to visit Egypt's three great pyramids at Giza: <strong>Khufu, Khafre, and Menkaure</strong> (Note: by decree of the Egyptian Ministry of Tourism, entering the interior galleries of the Great Pyramid requires an extra ticket and is not included).</p>

<p>We will go up to the <strong>panoramic spot</strong> to see all the pyramids and take fascinating photos. Continue to visit the <strong>Valley Temple</strong>, an element of King Khafre's pyramid complex, where a set of statues representing the king was discovered.</p>

<p>Then we proceed to visit the great <strong>Sphinx</strong>, represented with a lion's body and a human head, symbolizing perfection – the combination of strength and intelligence.</p>

<p>Visit to an authentic <strong>Papyrus Factory/Gallery</strong>, an ancient craft preserved for thousands of years in Egypt.</p>

<p><strong>Stop for Lunch</strong> (lunch is not included in this tour).</p>

<p>Visit to the <strong>National Museum of Egyptian Civilization</strong> located in Ein El Sira, a modern museum with unique pieces that narrate Egypt's history from ancient times to the modern era, including the <strong>Royal Mummies Hall</strong> within the museum, which contains several mummies of great kings and queens of Ancient Egypt.</p>

<p>Return to your hotel. (End of Tour).</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
</ul>

<h3>Pricing per Person (USD):</h3>
<ul>
<li><strong>1 Person (Solo):</strong> $147</li>
<li><strong>2 People:</strong> $94 per person</li>
<li><strong>3-4 People:</strong> $90 per person</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water – walking on the plateau and visiting the museum require good hydration.</li>
<li><strong>Lunch:</strong> Not included. You may ask your guide for a lunch stop or purchase something at the Museum cafeterias.</li>
<li><strong>Extra tickets:</strong> To enter the interior of the Great Pyramid of Cheops, you must purchase an additional ticket on site (subject to availability).</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible.</li>
<li>The agency needs at least 24 hours prior to the tour date to process the booking.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>El Tour de las Pirámides de Guiza y el Museo de la Civilización Egipcia es una experiencia completa de 8 horas que incluye las Pirámides de Guiza en la región del Gran Cairo y el Museo Nacional de la Civilización Egipcia.</p>

<p>Nuestro guía egiptólogo egipcio se encontrará con usted en su hotel de El Cairo. Salida con destino al Complejo de Guiza para visitar las tres grandes pirámides de Egipto en Guiza: <strong>Keops, Kefrén y Micerinos</strong> (Nota: por determinación del Ministerio de Turismo Egipcio, la entrada al interior de las galerías de la Gran Pirámide requiere una entrada extra y no está incluida).</p>

<p>Subiremos al <strong>mirador panorámico</strong> para ver todas las pirámides y tomar fotos fascinantes. Continuación para visitar el <strong>Templo del Valle</strong>, un elemento del complejo piramidal del rey Kefrén, donde se descubrió un conjunto de estatuas que representan al rey.</p>

<p>Luego seguimos para visitar la gran <strong>Esfinge</strong>, representada con cuerpo de león y cabeza humana, simbolizando la perfección, es decir, la combinación entre fuerza e inteligencia.</p>

<p>Visita a una <strong>Fábrica/Galería de papiros</strong> originales, artesanía milenaria que aún se conserva en Egipto.</p>

<p><strong>Parada para el Almuerzo</strong> (el almuerzo no está incluido en este tour).</p>

<p>Visita al <strong>Museo Nacional de la Civilización Egipcia</strong> ubicado en Ein El Sira, un museo moderno con piezas únicas que relata la historia de Egipto desde la época antigua hasta los tiempos modernos, además de visitar la <strong>Sala de las Momias Reales</strong> dentro del museo, que contiene varias momias de grandes reyes y reinas del Antiguo Egipto.</p>

<p>Regreso a su hotel en El Cairo. (Fin del Tour).</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
</ul>

<h3>Precios por persona (USD):</h3>
<ul>
<li><strong>1 Persona (Solo):</strong> $147</li>
<li><strong>2 Personas:</strong> $94 por persona</li>
<li><strong>3-4 Personas:</strong> $90 por persona</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a través de un enlace seguro y personalizado. Rápido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua – caminar por la meseta y visitar el museo requiere una buena hidratación.</li>
<li><strong>Almuerzo:</strong> No está incluido. Puede pedir una parada para almorzar a su guía o comprar algo en las cafeterías del Museo.</li>
<li><strong>Boletos adicionales:</strong> Para entrar al interior de la Gran Pirámide de Keops, es necesario adquirir un boleto adicional en el lugar (sujeto a disponibilidad).</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías.</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelación posible.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>Este passeio é uma experiência integral de 8 horas abrangendo as Pirâmides de Gizé, na região do Cairo, e o Museu Nacional da Civilização Egípcia.</p>

<p>Nosso guia egiptólogo irá encontrá-lo em seu hotel. Partida com destino ao Complexo de Gizé para conhecer as três grandes pirâmides: <strong>Quéops, Quéfren e Miquerinos</strong> (Nota: por determinação ministerial, o ingresso para as galerias internas da Grande Pirâmide é extra e não incluso).</p>

<p>Subiremos ao <strong>ponto panorâmico</strong> para admirar todas as pirâmides e registrar fotos incríveis. Visita ao <strong>Templo do Vale</strong>, integrante do complexo do rei Quéfren, local onde estátuas do faraó foram encontradas.</p>

<p>Em seguida, conheceremos a grandiosa <strong>Esfinge</strong>, com corpo de leão e cabeça humana, representando a perfeição entre força e intelecto.</p>

<p>Visita a uma <strong>Oficina/Galeria de papiros</strong> originais, arte milenar preservada no Egito.</p>

<p><strong>Parada para Almoço</strong> (não incluso).</p>

<p>Visita ao <strong>Museu Nacional da Civilização Egípcia</strong>, situado em Ein El Sira, um museu moderno com peças únicas que narram a trajetória do Egito desde a antiguidade até a era moderna, incluindo a <strong>Sala das Múmias Reais</strong>, que abriga diversas múmias de importantes reis e rainhas do Egito Antigo.</p>

<p>Retorno ao seu hotel no Cairo. (Término do Passeio).</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
</ul>

<h3>Valores por pessoa (USD):</h3>
<ul>
<li><strong>1 Pessoa (Individual):</strong> $147</li>
<li><strong>2 Pessoas:</strong> $94 por pessoa</li>
<li><strong>3-4 Pessoas:</strong> $90 por pessoa</li>
</ul>

<h3>Condições de Pagamento:</h3>
<p>Efetue o pagamento com seu cartão Visa ou Mastercard através de um link seguro e personalizado. Processo rápido, confiável e descomplicado.</p>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente – a caminhada no planalto e a visita ao museu exigem boa hidratação.</li>
<li><strong>Almoço:</strong> Não está incluído. Pode pedir uma parada para almoçar ao guia ou adquirir algo nas cafetarias do Museu.</li>
<li><strong>Ingressos extras:</strong> Para entrar no interior da Grande Pirâmide de Quéops, é necessário adquirir um bilhete adicional no local (sujeito à disponibilidade).</li>
<li><strong>Fotografia:</strong> Permitida na maioria das áreas, mas sem flash em algumas galerias.</li>
</ul>

<h3>Política de Reserva e Confirmação:</h3>
<ul>
<li>Recomenda-se reservar com o máximo de antecedência possível.</li>
<li>A agência necessita de no mínimo 24 horas antes da data do tour para processar a reserva.</li>
<li>Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</li>
</ul>''',

                # Classification
                'category': category,
                'tour_type': tour_type,

                # Duration
                'days': 1,
                'nights': 0,

                # Pricing (base price for 3-4 people)
                'price': 90,
                'child_price': None,
                'currency': 'USD',

                # Group info
                'min_group_size': 1,
                'max_group_size': 4,

                # Features
                'is_featured': True,
                'is_best_seller': False,
                'is_new': True,
                'is_multi_destination': False,
                'has_discount': False,

                # Rating
                'average_rating': 4.8,
                'review_count': 0,

                # Difficulty
                'difficulty_level': 'easy',

                # Additional
                'departure_city': 'Cairo',
                'languages': 'English, Spanish, Portuguese',

                # SEO
                'meta_title': 'Giza Pyramids & Egyptian Civilization Museum Tour | 1-Day Cairo',
                'meta_title_es': 'Tour Pirámides de Guiza y Museo de la Civilización Egipcia | 1 Día Cairo',
                'meta_title_pt': 'Passeio Pirâmides de Gizé e Museu da Civilização Egípcia | 1 Dia Cairo',
                'meta_description': 'Full-day 8-hour guided tour of the Giza Pyramids, Sphinx, Valley Temple, and the National Museum of Egyptian Civilization with Royal Mummies Hall. Transfers included.',
                'meta_description_es': 'Tour guiado de día completo de 8 horas por las Pirámides de Guiza, la Esfinge, el Templo del Valle y el Museo Nacional de la Civilización Egipcia con Sala de Momias Reales. Traslados incluidos.',
                'meta_description_pt': 'Passeio guiado de dia inteiro de 8 horas pelas Pirâmides de Gizé, Esfinge, Templo do Vale e Museu Nacional da Civilização Egípcia com Sala das Múmias Reais. Traslados inclusos.',

                # Published
                'is_published': True,
            }
        )

        # Link to Cairo destination
        try:
            cairo = Destination.objects.get(slug='cairo')
            tour.destinations.add(cairo)
        except Destination.DoesNotExist:
            self.stdout.write(self.style.WARNING('Cairo destination not found, skipping destination link.'))

        # ============================================================
        # HIGHLIGHTS
        # ============================================================
        tour.highlights.all().delete()
        highlights = [
            {
                'title': 'Giza Pyramid Complex',
                'title_es': 'Complejo de las Pirámides de Guiza',
                'title_pt': 'Complexo das Pirâmides de Gizé',
                'description': 'Visit the three Great Pyramids of Khufu, Khafre, and Menkaure, the Panoramic Viewpoint, the Valley Temple, and the legendary Sphinx.',
                'description_es': 'Visita las tres Grandes Pirámides de Keops, Kefrén y Micerinos, el Mirador Panorámico, el Templo del Valle y la legendaria Esfinge.',
                'description_pt': 'Visite as três Grandes Pirâmides de Quéops, Quéfren e Miquerinos, o Mirante Panorâmico, o Templo do Vale e a lendária Esfinge.',
                'icon': 'pyramid',
                'sort_order': 1,
            },
            {
                'title': 'National Museum of Egyptian Civilization',
                'title_es': 'Museo Nacional de la Civilización Egipcia',
                'title_pt': 'Museu Nacional da Civilização Egípcia',
                'description': 'Explore the chronological collection from Ancient to Modern Egypt, including the Royal Mummies Hall with Pharaohs and Queens.',
                'description_es': 'Explora la colección cronológica del Antiguo Egipto al moderno, incluyendo la Sala de las Momias Reales con Faraones y Reinas.',
                'description_pt': 'Explore o acervo cronológico do Egito Antigo ao contemporâneo, incluindo a Sala das Múmias Reais com Faraós e Rainhas.',
                'icon': 'museum',
                'sort_order': 2,
            },
            {
                'title': 'Expert Egyptologist Guide & Transfers',
                'title_es': 'Guía Egiptólogo Experto y Traslados',
                'title_pt': 'Guia Egiptólogo Especializado e Traslados',
                'description': 'Accompanied by a professional Egyptologist guide with air-conditioned vehicle transfers from and to your Cairo hotel.',
                'description_es': 'Acompañado por un guía egiptólogo profesional con traslados en vehículo con aire acondicionado desde y hacia su hotel de El Cairo.',
                'description_pt': 'Acompanhado por um guia egiptólogo profissional com traslados em veículo com ar-condicionado de e para seu hotel no Cairo.',
                'icon': 'guide',
                'sort_order': 3,
            },
        ]
        for h in highlights:
            TourHighlight.objects.create(tour=tour, **h)

        # ============================================================
        # ITINERARY (1 day)
        # ============================================================
        tour.itinerary.all().delete()
        TourItinerary.objects.create(
            tour=tour,
            day_number=1,
            title='Giza Pyramids & Egyptian Civilization Museum',
            title_es='Pirámides de Guiza y Museo de la Civilización Egipcia',
            title_pt='Pirâmides de Gizé e Museu da Civilização Egípcia',
            description='''<p><strong>08:00</strong> – Hotel pick-up in Cairo</p>
<p><strong>08:30</strong> – Arrival at Giza Complex (4 hours of exploration)</p>
<ul>
<li>The Three Great Pyramids (Khufu, Khafre, Menkaure)</li>
<li>Panoramic Viewpoint for epic photos</li>
<li>Valley Temple</li>
<li>The Sphinx – symbol of strength and intelligence</li>
<li>Papyrus Institute – authentic ancient art</li>
</ul>
<p><strong>12:30</strong> – Free time for lunch (nearby local restaurants)</p>
<p><strong>14:00</strong> – National Museum of Egyptian Civilization (3-hour visit)</p>
<ul>
<li>Chronological collection from Ancient to Modern Egypt</li>
<li>Royal Mummies Hall (Pharaohs and Queens)</li>
</ul>
<p><strong>17:00</strong> – Return to hotel</p>''',

            description_es='''<p><strong>08:00</strong> – Recogida en el hotel de El Cairo</p>
<p><strong>08:30</strong> – Llegada al Complejo de Guiza (4 horas de exploración)</p>
<ul>
<li>Las Tres Grandes Pirámides (Keops, Kefrén, Micerinos)</li>
<li>Mirador Panorámico para fotos épicas</li>
<li>Templo del Valle</li>
<li>La Esfinge – misterio de fuerza e inteligencia</li>
<li>Fábrica de Papiros – arte milenaria auténtica</li>
</ul>
<p><strong>12:30</strong> – Tiempo libre para almuerzo (restaurantes locales cercanos)</p>
<p><strong>14:00</strong> – Museo de la Civilización Egipcia (visita de 3 horas)</p>
<ul>
<li>Colección cronológica del Antiguo Egipto al moderno</li>
<li>Sala de las Momias Reales (Faraones y Reinas)</li>
</ul>
<p><strong>17:00</strong> – Regreso al hotel</p>''',

            description_pt='''<p><strong>08:00</strong> – Retirada no hotel no Cairo</p>
<p><strong>08:30</strong> – Chegada ao Complexo de Gizé (4 horas de exploração)</p>
<ul>
<li>As Três Grandes Pirâmides (Quéops, Quéfren e Miquerinos)</li>
<li>Vista Panorâmica para fotos espetaculares</li>
<li>Templo do Vale</li>
<li>A Esfinge – símbolo da força e da sabedoria</li>
<li>Fábrica de Papiros – arte tradicional genuína</li>
</ul>
<p><strong>12:30</strong> – Almoço livre (restaurantes locais nas proximidades)</p>
<p><strong>14:00</strong> – Museu da Civilização Egípcia (visita de 3 horas)</p>
<ul>
<li>Acervo cronológico do Egito Antigo ao contemporâneo</li>
<li>Sala das Múmias Reais (Faraós e Rainhas)</li>
</ul>
<p><strong>17:00</strong> – Retorno ao hotel</p>''',

            locations='Giza, Cairo',
            locations_es='Guiza, El Cairo',
            locations_pt='Gizé, Cairo',
            meals_included='',
            meals_included_es='',
            meals_included_pt='',
            accommodation='',
            sort_order=1,
        )

        # ============================================================
        # INCLUSIONS
        # ============================================================
        tour.inclusions.all().delete()

        # Included items
        included = [
            {
                'item': 'Modern, air-conditioned car/van transfers',
                'item_es': 'Traslados en automóvil/van moderno con aire acondicionado',
                'item_pt': 'Traslados em carro/van moderno e com ar-condicionado',
            },
            {
                'item': 'General area entrance tickets for the Pyramids and Sphinx',
                'item_es': 'Entradas generales al área de las Pirámides y la Esfinge',
                'item_pt': 'Ingresso de acesso geral à área das Pirâmides e da Esfinge',
            },
            {
                'item': 'Entrance ticket to the Egyptian Civilization Museum and the Royal Mummies Hall',
                'item_es': 'Entrada al Museo de la Civilización Egipcia y a la Sala de las Momias Reales',
                'item_pt': 'Ingresso para o Museu da Civilização Egípcia e a Sala das Múmias Reais',
            },
            {
                'item': 'Expert Egyptologist guide',
                'item_es': 'Guía oficial egiptólogo',
                'item_pt': 'Guia oficial egiptólogo',
            },
            {
                'item': 'Service and operational assistance',
                'item_es': 'Servicio y asistencia técnica',
                'item_pt': 'Serviço e suporte técnico',
            },
            {
                'item': '1 bottle of mineral water per person during the tour',
                'item_es': '1 botella de agua mineral por persona durante los recorridos',
                'item_pt': '1 garrafa de água mineral por pessoa durante os passeios',
            },
            {
                'item': 'All tour fees and service charges',
                'item_es': 'Todas las tasas de tours y cargos por servicio',
                'item_pt': 'Todas as taxas de visitação e de serviços',
            },
        ]

        for i, inc in enumerate(included):
            TourInclusion.objects.create(
                tour=tour, is_included=True, sort_order=i + 1, **inc
            )

        # Excluded items
        excluded = [
            {
                'item': 'Accommodation in Cairo',
                'item_es': 'Alojamiento en El Cairo',
                'item_pt': 'Hospedagem na cidade do Cairo',
            },
            {
                'item': 'Meals',
                'item_es': 'Comidas',
                'item_pt': 'Refeições',
            },
            {
                'item': 'Entrance ticket to the interior of the Great Pyramid of Giza or any other pyramid',
                'item_es': 'Entrada al interior de la Gran Pirámide de Guiza o de cualquier otra pirámide',
                'item_pt': 'Ingresso para acesso ao interior da Grande Pirâmide de Gizé ou de qualquer outra pirâmide',
            },
            {
                'item': 'Tips, traditionally given to the guide and driver',
                'item_es': 'Propinas, tradicionalmente entregadas al guía y al conductor',
                'item_pt': 'Gorjetas, de praxe, para o guia e o motorista',
            },
            {
                'item': 'Extras and anything not described as included in the itinerary',
                'item_es': 'Extras y todo lo que no esté descrito como incluido en el itinerario',
                'item_pt': 'Itens extras e quaisquer outros serviços não descritos como inclusos no roteiro',
            },
        ]

        for i, exc in enumerate(excluded):
            TourInclusion.objects.create(
                tour=tour, is_included=False, sort_order=i + 1, **exc
            )

        # ============================================================
        # FAQs
        # ============================================================
        tour.faqs.all().delete()
        faqs = [
            {
                'question': 'Can I enter the interior of the Great Pyramid of Khufu?',
                'question_es': '¿Puedo entrar al interior de la Gran Pirámide de Keops?',
                'question_pt': 'Posso entrar no interior da Grande Pirâmide de Quéops?',
                'answer': '<p>Entrance to the interior of the Great Pyramid is not included in the tour. You must purchase an additional ticket on site, subject to availability from the Ministry of Tourism. The number of tickets is limited daily.</p>',
                'answer_es': '<p>La entrada al interior de la Gran Pirámide no está incluida en el tour. Es necesario adquirir un boleto adicional en el lugar, sujeto a disponibilidad del Ministerio de Turismo. El número de boletos es limitado diariamente.</p>',
                'answer_pt': '<p>O acesso ao interior da Grande Pirâmide não está incluso no passeio. É necessário adquirir um bilhete adicional no local, sujeito à disponibilidade do Ministério do Turismo. O número de ingressos é limitado diariamente.</p>',
                'sort_order': 1,
            },
            {
                'question': 'Is lunch included in this tour?',
                'question_es': '¿El almuerzo está incluido en este tour?',
                'question_pt': 'O almoço está incluído neste passeio?',
                'answer': '<p>No, lunch is not included. There is a free time stop where you can eat at nearby local restaurants, or you can purchase something at the Museum cafeterias during visiting hours.</p>',
                'answer_es': '<p>No, el almuerzo no está incluido. Hay una parada de tiempo libre donde puede comer en restaurantes locales cercanos, o puede comprar algo en las cafeterías del Museo durante el horario de visita.</p>',
                'answer_pt': '<p>Não, o almoço não está incluído. Há uma parada de tempo livre onde pode comer em restaurantes locais próximos, ou pode adquirir algo nas cafetarias do Museu durante o horário de visita.</p>',
                'sort_order': 2,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': '¿Qué debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen for the morning at the pyramids. Comfortable walking shoes are essential.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar para la mañana en las pirámides. El calzado cómodo para caminar es esencial.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapéu, óculos de sol e protetor solar para a manhã nas pirâmides. Calçado confortável para caminhar é essencial.</p>',
                'sort_order': 3,
            },
            {
                'question': 'How far in advance should I book?',
                'question_es': '¿Con cuánta antelación debo reservar?',
                'question_pt': 'Com quanta antecedência devo reservar?',
                'answer': '<p>We recommend booking as far in advance as possible to guarantee availability of the Egyptologist guide and online tickets. The agency needs at least 24 hours prior to the tour date. Bookings within less than 24 hours are subject to last-minute availability.</p>',
                'answer_es': '<p>Recomendamos reservar con la mayor antelación posible para garantizar la disponibilidad del guía egiptólogo y de los boletos online. La agencia necesita al menos 24 horas antes de la fecha del tour. Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</p>',
                'answer_pt': '<p>Recomendamos reservar com o máximo de antecedência possível para garantir a disponibilidade do guia egiptólogo e dos ingressos online. A agência necessita de no mínimo 24 horas antes da data do tour. Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</p>',
                'sort_order': 4,
            },
            {
                'question': 'Is photography allowed?',
                'question_es': '¿Se permite la fotografía?',
                'question_pt': 'A fotografia é permitida?',
                'answer': '<p>Photography is permitted in most areas. However, flash photography is not allowed in some museum galleries. Please follow security guidelines at each location.</p>',
                'answer_es': '<p>La fotografía está permitida en la mayoría de las áreas. Sin embargo, no se permite el uso de flash en algunas galerías del museo. Por favor, siga las indicaciones de seguridad en cada ubicación.</p>',
                'answer_pt': '<p>A fotografia é permitida na maioria das áreas. No entanto, não é permitido o uso de flash em algumas galerias do museu. Por favor, siga as orientações de segurança em cada local.</p>',
                'sort_order': 5,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day'
            f'\n  - Price: ${tour.price} (3-4 pax) | Solo: $147 | 2 pax: $94'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
