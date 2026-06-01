"""
Management command to add "Giza Pyramids and Grand Egyptian Museum (GEM)" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Giza Pyramids and Grand Egyptian Museum (GEM) 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Giza Pyramids and Grand Egyptian Museum (GEM) day tour...')

        # Get or create category and type
        category, _ = TourCategory.objects.get_or_create(
            slug='day-tours',
            defaults={
                'name': 'Day Tours',
                'name_es': 'Excursiones de un Dia',
                'name_pt': 'Passeios de um Dia',
            }
        )

        tour_type, _ = TourType.objects.get_or_create(
            slug='day-tour',
            defaults={
                'name': 'Day Tour',
                'name_es': 'Excursion de un Dia',
                'name_pt': 'Passeio de um Dia',
            }
        )

        # Create the tour
        tour, created = Tour.objects.update_or_create(
            slug='giza-pyramids-grand-egyptian-museum-day-tour',
            defaults={
                'name': 'Giza Pyramids and Grand Egyptian Museum (GEM) Day Tour',
                'name_es': 'Paseo Piramides de Guiza con el Gran Museo Egipcio',
                'name_pt': 'Passeio Piramides de Gize com o Grande Museu Egipcio',

                'short_description': (
                    'An unforgettable 8-hour tour in Cairo to discover the majestic '
                    'Giza Pyramids, the Sphinx, and the Grand Egyptian Museum (GEM) '
                    '- the largest archaeological museum in the world dedicated to a '
                    'single civilization. Accompanied by an expert Egyptologist guide, '
                    'with entrance tickets and transfers included!'
                ),
                'short_description_es': (
                    'Un tour inolvidable de 8 horas en El Cairo para descubrir las '
                    'majestuosas Piramides de Guiza, la Esfinge y el Gran Museo '
                    'Egipcio (GEM), el museo arqueologico mas grande del mundo '
                    'dedicado a una sola civilizacion. Acompanado por un guia '
                    'egiptologo especializado, con entradas y traslados incluidos!'
                ),
                'short_description_pt': (
                    'Um tour inesquecivel de 8 horas no Cairo para descobrir as '
                    'majestosas Piramides de Gize, a Esfinge e o Grande Museu '
                    'Egipcio (GEM), o maior museu arqueologico do mundo dedicado '
                    'a uma unica civilizacao. Acompanhado por um guia egiptologo '
                    'especializado, com ingressos e traslados inclusos!'
                ),

                'description': '''<p>The Giza Pyramids and Grand Egyptian Museum (GEM) Day Tour is a comprehensive 8-hour experience combining the ancient Giza Pyramid Complex with the world's largest archaeological museum dedicated to a single civilization.</p>

<p>Our official Egyptologist guide will meet you at your Cairo hotel around <strong>08:00</strong>. We head to the Giza Plateau to visit the three Great Pyramids of Egypt: <strong>Khufu, Khafre, and Menkaure</strong> (Note: by decree of the Egyptian Ministry of Tourism, entering the interior galleries of the Great Pyramid requires an extra ticket, offered in limited daily numbers and purchased personally by the visitor, and is not included).</p>

<p>We will go up to the <strong>Panoramic Viewpoint</strong> to see all the pyramids and take epic photos. Continue to visit the <strong>Valley Temple</strong> of King Khafre, an impressive structure built with gigantic blocks of limestone and granite, part of the pharaoh's funerary complex.</p>

<p>Then we proceed to visit the great <strong>Sphinx</strong>, an iconic monument with a lion's body and a human head, representing the combination of strength and intelligence.</p>

<p>Visit to an authentic <strong>Papyrus Institute/Gallery</strong>, with a live demonstration of the ancient art of papyrus making, with the opportunity to acquire authentic pieces (no obligation to purchase).</p>

<p><strong>Free time for Lunch</strong> (lunch is not included in this tour).</p>

<p>Visit to the <strong>Grand Egyptian Museum (GEM)</strong>, located near the Giza Pyramids. This majestic new jewel of culture houses a pharaonic collection of treasures, notably those of <strong>King Tutankhamun</strong> - over 5,000 pieces displayed in their entirety for the first time: the three golden coffins, the ceremonial throne, the golden sandals, the meteorite dagger, and the iconic death mask. The GEM houses over 100,000 artifacts and establishes itself as the largest and most sophisticated museum in the world dedicated to a single civilization.</p>

<p>Return to your hotel in Cairo. (End of Tour).</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
<li>Essential for History Lovers</li>
</ul>

<h3>Pricing per Person (USD):</h3>
<ul>
<li><strong>1 Person (Solo):</strong> $187</li>
<li><strong>2 People:</strong> $110 per person</li>
<li><strong>3-4 People:</strong> $105 per person</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water - walking on the plateau and visiting the museum require good hydration.</li>
<li><strong>Lunch:</strong> Not included. You may ask your guide for a lunch stop or purchase something at the GEM cafeterias.</li>
<li><strong>Extra tickets:</strong> To enter the interior of the Great Pyramid of Cheops, you must purchase an additional ticket on site (subject to availability).</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible to guarantee availability of the Egyptologist guide and online tickets.</li>
<li>The agency needs at least 24 hours prior to the tour date to process the booking, assign the guide, purchase tickets, and confirm all services.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>El Paseo Piramides de Guiza con el Gran Museo Egipcio es una experiencia completa de 8 horas que combina el antiguo Complejo de Piramides de Guiza con el museo arqueologico mas grande del mundo dedicado a una sola civilizacion.</p>

<p>Nuestro guia egiptologo oficial, hablante nativo de espanol, se encontrara con usted en su hotel de El Cairo alrededor de las <strong>08:00</strong>. Nos dirigimos a la meseta de Guiza para visitar las tres grandes piramides de Egipto: <strong>Keops, Kefren y Micerinos</strong> (Nota: el Ministerio de Turismo Egipcio exige un boleto adicional para acceder al interior de las galerias de la Gran Piramide. Este valor no esta incluido en el paquete basico).</p>

<p>Subiremos al <strong>Mirador Panoramico</strong> para ver todas las piramides y tomar fotos fascinantes. Continuacion para visitar el <strong>Templo del Valle</strong> del rey Kefren, una estructura impresionante construida con bloques gigantescos de caliza y granito, parte del complejo funerario del faraon.</p>

<p>Luego seguimos para visitar la gran <strong>Esfinge</strong>, un monumento iconico con cuerpo de leon y cabeza humana, que representa el poder real egipcio.</p>

<p>Visita a una <strong>Fabrica/Galeria de Papiros Originales</strong>, con demostracion en vivo del antiguo arte milenario de la fabricacion de papiro, con la oportunidad de adquirir piezas autenticas (sin obligacion de compra).</p>

<p><strong>Tiempo libre para el Almuerzo</strong> (el almuerzo no esta incluido en este tour).</p>

<p>Visita al <strong>Gran Museo Egipcio (GEM)</strong>, ubicado cerca de las Piramides de Guiza. Esta majestuosa nueva joya de la cultura alberga una coleccion faraonica de tesoros, especialmente los del <strong>Rey Tutankamon</strong>: mas de 5,000 piezas expuestas integramente por primera vez: los tres ataudes dorados, el trono ceremonial, las sandalias de oro, el punal de meteorito y la iconica mascara mortuoria. El GEM alberga mas de 100,000 artefactos y se establece como el museo mas grande y sofisticado del mundo dedicado a una sola civilizacion.</p>

<p>Regreso a su hotel en El Cairo. (Fin del Tour).</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
<li>Imprescindible para Amantes de la Historia</li>
</ul>

<h3>Precios por persona (USD):</h3>
<ul>
<li><strong>1 Persona (Solo):</strong> $187</li>
<li><strong>2 Personas:</strong> $110 por persona</li>
<li><strong>3-4 Personas:</strong> $105 por persona</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a traves de un enlace seguro y personalizado. Rapido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado comodo para caminar.</li>
<li><strong>Hidratacion:</strong> Lleve suficiente agua - caminar por la meseta y visitar el museo requiere una buena hidratacion.</li>
<li><strong>Almuerzo:</strong> No esta incluido. Puede pedir una parada para almorzar a su guia o comprar algo en las cafeterias del GEM.</li>
<li><strong>Boletos adicionales:</strong> Para entrar al interior de la Gran Piramide de Keops, es necesario adquirir un boleto adicional en el lugar (sujeto a disponibilidad).</li>
<li><strong>Fotografia:</strong> Permitida en la mayoria de las areas, pero sin flash en algunas galerias.</li>
</ul>

<h3>Politica de Reserva y Confirmacion:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelacion posible para garantizar la disponibilidad del guia egiptologo hablante de espanol y de los boletos en linea.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva, asignar el guia, adquirir los boletos y confirmar todos los servicios.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de ultima hora.</li>
</ul>''',

                'description_pt': '''<p>O Passeio Piramides de Gize com o Grande Museu Egipcio e uma experiencia integral de 8 horas que combina o antigo Complexo de Piramides de Gize com o maior museu arqueologico do mundo dedicado a uma unica civilizacao.</p>

<p>Nosso guia egiptologo oficial, falante nativo de portugues, ira encontra-lo em seu hotel no Cairo por volta das <strong>08h00</strong>. Seguimos para o planalto de Gize para conhecer as tres grandes piramides do Egito: <strong>Queops, Quefren e Miquerinos</strong> (Nota: o Ministerio do Turismo Egipcio exige ingresso extra para acessar o interior das galerias da Grande Piramide. Este valor nao esta incluso no pacote basico).</p>

<p>Subiremos ao <strong>Miradouro Panoramico</strong> para admirar todas as piramides e registrar fotos incriveis. Visita ao <strong>Templo do Vale</strong> do rei Quefren, estrutura impressionante construida com blocos gigantescos de calcario e granito, parte do complexo funerario do farao.</p>

<p>Em seguida, conheceremos a grandiosa <strong>Esfinge</strong>, monumento iconico com corpo de leao e cabeca humana, representando o poder real egipcio.</p>

<p>Visita a uma <strong>Fabrica/Galeria de Papiros Originais</strong>, com demonstracao ao vivo da antiga arte milenar da fabricacao de papiro, com oportunidade de adquirir pecas autenticas (sem obrigacao de compra).</p>

<p><strong>Tempo livre para Almoco</strong> (nao incluso).</p>

<p>Visita ao <strong>Grande Museu Egipcio (GEM)</strong>, localizado proximo as Piramides de Gize. Esta majestosa nova joia da cultura abriga uma colecao faraonica de tesouros, notadamente os do <strong>Rei Tutancamon</strong>: mais de 5.000 pecas expostas integralmente pela primeira vez: as tres camaras douradas, o trono cerimonial, as sandalias de ouro, o punhal de meteorito e a iconica mascara mortuaria. O GEM abriga mais de 100.000 artefatos e se estabelece como o maior e mais sofisticado museu do mundo dedicado a uma unica civilizacao.</p>

<p>Retorno ao seu hotel no Cairo. (Termino do Passeio).</p>

<h3>Este roteiro e:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Familias</li>
<li>Essencial para Amantes da Historia</li>
</ul>

<h3>Valores por pessoa (USD):</h3>
<ul>
<li><strong>1 Pessoa (Individual):</strong> $187</li>
<li><strong>2 Pessoas:</strong> $110 por pessoa</li>
<li><strong>3-4 Pessoas:</strong> $105 por pessoa</li>
</ul>

<h3>Condicoes de Pagamento:</h3>
<p>Efetue o pagamento com seu cartao Visa ou Mastercard atraves de um link seguro e personalizado. Processo rapido, confiavel e descomplicado.</p>

<h3>Recomendacoes Importantes:</h3>
<ul>
<li><strong>Vestuario:</strong> Use roupas leves principalmente de abril a novembro, chapeu, oculos de sol e protetor solar. Calcado confortavel para caminhar.</li>
<li><strong>Hidratacao:</strong> Leve agua suficiente - a caminhada no planalto e a visita ao museu exigem boa hidratacao.</li>
<li><strong>Almoco:</strong> Nao esta incluido. Pode pedir uma parada para almocar ao guia ou adquirir algo nas cafetarias do GEM.</li>
<li><strong>Ingressos extras:</strong> Para entrar no interior da Grande Piramide de Queops, e necessario adquirir um bilhete adicional no local (sujeito a disponibilidade).</li>
<li><strong>Fotografia:</strong> Permitida na maioria das areas, mas sem flash em algumas galerias.</li>
</ul>

<h3>Politica de Reserva e Confirmacao:</h3>
<ul>
<li>Recomenda-se reservar com o maximo de antecedencia possivel para garantir a disponibilidade do guia egiptologo falante de portugues e dos ingressos online.</li>
<li>A agencia necessita de no minimo 24 horas antes da data do tour para processar a reserva, alocar o guia, adquirir os ingressos e confirmar todos os servicos.</li>
<li>Reservas com menos de 24 horas sujeitas a disponibilidade de ultima hora.</li>
</ul>''',

                # Classification
                'category': category,
                'tour_type': tour_type,

                # Duration
                'days': 1,
                'nights': 0,

                # Pricing (base price for 3-4 people)
                'price': 105,
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
                'average_rating': 4.9,
                'review_count': 0,

                # Difficulty
                'difficulty_level': 'easy',

                # Additional
                'departure_city': 'Cairo',
                'languages': 'English, Spanish, Portuguese',

                # SEO (meta_title max 70, meta_description max 160)
                'meta_title': 'Giza Pyramids & Grand Egyptian Museum (GEM) Tour | 1 Day',
                'meta_title_es': 'Piramides de Guiza y Gran Museo Egipcio (GEM) | 1 Dia',
                'meta_title_pt': 'Piramides de Gize e Grande Museu Egipcio (GEM) | 1 Dia',
                'meta_description': '8-hour guided tour: Giza Pyramids, Sphinx, Valley Temple & Grand Egyptian Museum with Tutankhamun treasures. Transfers included.',
                'meta_description_es': 'Tour guiado de 8 horas: Piramides de Guiza, Esfinge, Templo del Valle y Gran Museo Egipcio con tesoros de Tutankamon. Traslados incluidos.',
                'meta_description_pt': 'Passeio guiado de 8 horas: Piramides de Gize, Esfinge, Templo do Vale e Grande Museu Egipcio com tesouros de Tutancamon. Traslados inclusos.',

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
                'title_es': 'Complejo de las Piramides de Guiza',
                'title_pt': 'Complexo das Piramides de Gize',
                'description': 'Visit the three Great Pyramids of Khufu, Khafre, and Menkaure, the Panoramic Viewpoint, the Valley Temple, and the legendary Sphinx.',
                'description_es': 'Visita las tres Grandes Piramides de Keops, Kefren y Micerinos, el Mirador Panoramico, el Templo del Valle y la legendaria Esfinge.',
                'description_pt': 'Visite as tres Grandes Piramides de Queops, Quefren e Miquerinos, o Miradouro Panoramico, o Templo do Vale e a lendaria Esfinge.',
                'icon': 'pyramid',
                'sort_order': 1,
            },
            {
                'title': 'Grand Egyptian Museum (GEM)',
                'title_es': 'Gran Museo Egipcio (GEM)',
                'title_pt': 'Grande Museu Egipcio (GEM)',
                'description': 'Explore the largest archaeological museum in the world dedicated to a single civilization, featuring over 100,000 artifacts including the complete Tutankhamun treasure collection.',
                'description_es': 'Explore el museo arqueologico mas grande del mundo dedicado a una sola civilizacion, con mas de 100,000 artefactos incluyendo la coleccion completa de tesoros de Tutankamon.',
                'description_pt': 'Explore o maior museu arqueologico do mundo dedicado a uma unica civilizacao, com mais de 100.000 artefatos incluindo a colecao completa de tesouros de Tutancamon.',
                'icon': 'museum',
                'sort_order': 2,
            },
            {
                'title': 'Expert Egyptologist Guide & Transfers',
                'title_es': 'Guia Egiptologo Experto y Traslados',
                'title_pt': 'Guia Egiptologo Especializado e Traslados',
                'description': 'Accompanied by a professional Egyptologist guide with air-conditioned vehicle transfers from and to your Cairo hotel.',
                'description_es': 'Acompanado por un guia egiptologo profesional con traslados en vehiculo con aire acondicionado desde y hacia su hotel de El Cairo.',
                'description_pt': 'Acompanhado por um guia egiptologo profissional com traslados em veiculo com ar-condicionado de e para seu hotel no Cairo.',
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
            title='Giza Pyramids & Grand Egyptian Museum (GEM)',
            title_es='Piramides de Guiza y Gran Museo Egipcio (GEM)',
            title_pt='Piramides de Gize e Grande Museu Egipcio (GEM)',
            description='''<p><strong>08:00</strong> - Hotel pick-up in Cairo</p>
<p><strong>08:30</strong> - Arrival at Giza Complex (3-4 hours of exploration)</p>
<ul>
<li>The Three Great Pyramids (Khufu, Khafre, Menkaure)</li>
<li>Panoramic Viewpoint for epic photos</li>
<li>Valley Temple of King Khafre</li>
<li>The Sphinx - symbol of strength and intelligence</li>
<li>Papyrus Institute - authentic ancient art</li>
</ul>
<p><strong>12:30</strong> - Free time for lunch (not included)</p>
<p><strong>14:00</strong> - Grand Egyptian Museum / GEM (3-hour visit)</p>
<ul>
<li>Over 100,000 artifacts from ancient Egyptian civilization</li>
<li>Complete Tutankhamun treasure collection (5,000+ pieces)</li>
<li>The three golden coffins, ceremonial throne, golden sandals</li>
<li>The meteorite dagger and iconic death mask</li>
</ul>
<p><strong>17:00</strong> - Return to hotel</p>''',

            description_es='''<p><strong>08:00</strong> - Recogida en el hotel de El Cairo</p>
<p><strong>08:30</strong> - Llegada al Complejo de Guiza (3-4 horas de exploracion)</p>
<ul>
<li>Las Tres Grandes Piramides (Keops, Kefren, Micerinos)</li>
<li>Mirador Panoramico para fotos epicas</li>
<li>Templo del Valle del rey Kefren</li>
<li>La Esfinge - misterio de fuerza e inteligencia</li>
<li>Fabrica de Papiros - arte milenaria autentica</li>
</ul>
<p><strong>12:30</strong> - Tiempo libre para almuerzo (no incluido)</p>
<p><strong>14:00</strong> - Gran Museo Egipcio / GEM (visita de 3 horas)</p>
<ul>
<li>Mas de 100,000 artefactos de la civilizacion del antiguo Egipto</li>
<li>Coleccion completa de tesoros de Tutankamon (mas de 5,000 piezas)</li>
<li>Los tres ataudes dorados, trono ceremonial, sandalias de oro</li>
<li>El punal de meteorito y la iconica mascara mortuoria</li>
</ul>
<p><strong>17:00</strong> - Regreso al hotel</p>''',

            description_pt='''<p><strong>08:00</strong> - Retirada no hotel no Cairo</p>
<p><strong>08:30</strong> - Chegada ao Complexo de Gize (3-4 horas de exploracao)</p>
<ul>
<li>As Tres Grandes Piramides (Queops, Quefren e Miquerinos)</li>
<li>Miradouro Panoramico para fotos espetaculares</li>
<li>Templo do Vale do rei Quefren</li>
<li>A Esfinge - simbolo da forca e da sabedoria</li>
<li>Fabrica de Papiros - arte tradicional genuina</li>
</ul>
<p><strong>12:30</strong> - Almoco livre (nao incluso)</p>
<p><strong>14:00</strong> - Grande Museu Egipcio / GEM (visita de 3 horas)</p>
<ul>
<li>Mais de 100.000 artefatos da civilizacao do antigo Egito</li>
<li>Colecao completa de tesouros de Tutancamon (mais de 5.000 pecas)</li>
<li>As tres camaras douradas, trono cerimonial, sandalias de ouro</li>
<li>O punhal de meteorito e a iconica mascara mortuaria</li>
</ul>
<p><strong>17:00</strong> - Retorno ao hotel</p>''',

            locations='Giza, Cairo',
            locations_es='Guiza, El Cairo',
            locations_pt='Gize, Cairo',
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
                'item': 'Modern, air-conditioned car/van transfers (round trip to hotel)',
                'item_es': 'Transporte moderno con aire acondicionado (ida y vuelta al hotel)',
                'item_pt': 'Transporte privado com ar-condicionado (ida e volta ao hotel)',
            },
            {
                'item': 'General area entrance tickets for the Pyramids, Sphinx, and Valley Temple',
                'item_es': 'Entradas al Complejo de Piramides de Guiza (area exterior de las tres piramides + Esfinge + Templo del Valle)',
                'item_pt': 'Ingressos para o Complexo de Piramides de Gize (area externa das tres piramides + Esfinge + Templo do Vale)',
            },
            {
                'item': 'Entrance ticket to the Grand Egyptian Museum (GEM)',
                'item_es': 'Entrada al Gran Museo Egipcio (GEM)',
                'item_pt': 'Ingresso para o Grande Museu Egipcio (GEM)',
            },
            {
                'item': 'Expert Egyptologist guide (accredited by the Ministry of Tourism)',
                'item_es': 'Guia egiptologo oficial hablante de espanol (acreditado por el Ministerio de Turismo)',
                'item_pt': 'Guia egiptologo oficial falante de portugues (credenciado pelo Ministerio do Turismo)',
            },
            {
                'item': 'Visit to papyrus factory/gallery (no additional cost)',
                'item_es': 'Visita a la fabrica/galeria de papiros (sin costo adicional)',
                'item_pt': 'Visita a fabrica/galeria de papiros (sem custo adicional)',
            },
            {
                'item': 'Service and technical assistance',
                'item_es': 'Servicio y asistencia tecnica',
                'item_pt': 'Servico e suporte tecnico',
            },
            {
                'item': '2 bottles of mineral water per person during the tour',
                'item_es': '2 botellas de agua durante el paseo',
                'item_pt': '2 garrafas de agua durante o passeio',
            },
            {
                'item': 'All tour fees and service charges',
                'item_es': 'Todas las tasas de tours y cargos por servicio',
                'item_pt': 'Todas as taxas de visitacao e de servicos',
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
                'item': 'Meals (lunch or any other meal)',
                'item_es': 'Almuerzo o cualquier comida',
                'item_pt': 'Almoco ou qualquer refeicao',
            },
            {
                'item': 'Entrance ticket to the interior of the Great Pyramid of Giza or any other pyramid',
                'item_es': 'Entrada al interior de la Gran Piramide de Keops',
                'item_pt': 'Entrada no interior da Grande Piramide de Queops',
            },
            {
                'item': 'Tips, traditionally given to the guide and driver (optional but suggested)',
                'item_es': 'Propinas (para guia y conductor - opcional pero sugerido)',
                'item_pt': 'Gorjetas (para guia e motorista - facultativo, mas sugerido)',
            },
            {
                'item': 'Personal expenses, shopping, and anything not described as included',
                'item_es': 'Gastos personales, compras y todo lo que no este descrito como incluido en el itinerario',
                'item_pt': 'Despesas pessoais, compras e quaisquer outros servicos nao descritos como inclusos no roteiro',
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
                'question_es': 'Puedo entrar al interior de la Gran Piramide de Keops?',
                'question_pt': 'Posso entrar no interior da Grande Piramide de Queops?',
                'answer': '<p>Entrance to the interior of the Great Pyramid is not included in the tour. You must purchase an additional ticket on site, subject to availability from the Ministry of Tourism. The number of tickets is limited daily.</p>',
                'answer_es': '<p>La entrada al interior de la Gran Piramide no esta incluida en el tour. Es necesario adquirir un boleto adicional en el lugar, sujeto a disponibilidad del Ministerio de Turismo. El numero de boletos es limitado diariamente.</p>',
                'answer_pt': '<p>O acesso ao interior da Grande Piramide nao esta incluso no passeio. E necessario adquirir um bilhete adicional no local, sujeito a disponibilidade do Ministerio do Turismo. O numero de ingressos e limitado diariamente.</p>',
                'sort_order': 1,
            },
            {
                'question': 'Is lunch included in this tour?',
                'question_es': 'El almuerzo esta incluido en este tour?',
                'question_pt': 'O almoco esta incluido neste passeio?',
                'answer': '<p>No, lunch is not included. There is a free time stop where you can eat at nearby local restaurants, or you can purchase something at the GEM cafeterias during visiting hours.</p>',
                'answer_es': '<p>No, el almuerzo no esta incluido. Hay una parada de tiempo libre donde puede comer en restaurantes locales cercanos, o puede comprar algo en las cafeterias del GEM durante el horario de visita.</p>',
                'answer_pt': '<p>Nao, o almoco nao esta incluido. Ha uma parada de tempo livre onde pode comer em restaurantes locais proximos, ou pode adquirir algo nas cafetarias do GEM durante o horario de visita.</p>',
                'sort_order': 2,
            },
            {
                'question': 'What makes the Grand Egyptian Museum (GEM) special?',
                'question_es': 'Que hace especial al Gran Museo Egipcio (GEM)?',
                'question_pt': 'O que torna o Grande Museu Egipcio (GEM) especial?',
                'answer': '<p>The Grand Egyptian Museum is the largest archaeological museum in the world dedicated to a single civilization. It houses over 100,000 artifacts, including for the first time the complete collection of King Tutankhamun\'s treasure - over 5,000 pieces including the three golden coffins, the ceremonial throne, golden sandals, the meteorite dagger, and the iconic death mask.</p>',
                'answer_es': '<p>El Gran Museo Egipcio es el museo arqueologico mas grande del mundo dedicado a una sola civilizacion. Alberga mas de 100,000 artefactos, incluyendo por primera vez la coleccion completa del tesoro del Rey Tutankamon: mas de 5,000 piezas incluyendo los tres ataudes dorados, el trono ceremonial, las sandalias de oro, el punal de meteorito y la iconica mascara mortuoria.</p>',
                'answer_pt': '<p>O Grande Museu Egipcio e o maior museu arqueologico do mundo dedicado a uma unica civilizacao. Abriga mais de 100.000 artefatos, incluindo pela primeira vez a colecao completa do tesouro do Rei Tutancamon: mais de 5.000 pecas incluindo as tres camaras douradas, o trono cerimonial, as sandalias de ouro, o punhal de meteorito e a iconica mascara mortuaria.</p>',
                'sort_order': 3,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': 'Que debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen for the morning at the pyramids. Comfortable walking shoes are essential.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar para la manana en las piramides. El calzado comodo para caminar es esencial.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapeu, oculos de sol e protetor solar para a manha nas piramides. Calcado confortavel para caminhar e essencial.</p>',
                'sort_order': 4,
            },
            {
                'question': 'How far in advance should I book?',
                'question_es': 'Con cuanta antelacion debo reservar?',
                'question_pt': 'Com quanta antecedencia devo reservar?',
                'answer': '<p>We recommend booking as far in advance as possible to guarantee availability of the Egyptologist guide and online tickets. The agency needs at least 24 hours prior to the tour date to process the booking, assign the guide, purchase tickets, and confirm all services. Bookings within less than 24 hours are subject to last-minute availability.</p>',
                'answer_es': '<p>Recomendamos reservar con la mayor antelacion posible para garantizar la disponibilidad del guia egiptologo hablante de espanol y de los boletos en linea. La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva, asignar el guia, adquirir los boletos y confirmar todos los servicios. Reservas con menos de 24 horas sujetas a disponibilidad de ultima hora.</p>',
                'answer_pt': '<p>Recomendamos reservar com o maximo de antecedencia possivel para garantir a disponibilidade do guia egiptologo falante de portugues e dos ingressos online. A agencia necessita de no minimo 24 horas antes da data do tour para processar a reserva, alocar o guia, adquirir os ingressos e confirmar todos os servicos. Reservas com menos de 24 horas sujeitas a disponibilidade de ultima hora.</p>',
                'sort_order': 5,
            },
            {
                'question': 'Is photography allowed?',
                'question_es': 'Se permite la fotografia?',
                'question_pt': 'A fotografia e permitida?',
                'answer': '<p>Photography is permitted in most areas of the GEM and at the pyramids. However, flash photography is not allowed in some museum galleries. Please follow security guidelines at each location.</p>',
                'answer_es': '<p>La fotografia esta permitida en la mayoria de las areas del GEM y en las piramides. Sin embargo, no se permite el uso de flash en algunas galerias del museo. Por favor, siga las indicaciones de seguridad en cada ubicacion.</p>',
                'answer_pt': '<p>A fotografia e permitida na maioria das areas do GEM e nas piramides. No entanto, nao e permitido o uso de flash em algumas galerias do museu. Por favor, siga as orientacoes de seguranca em cada local.</p>',
                'sort_order': 6,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day'
            f'\n  - Price: ${tour.price} (3-4 pax) | Solo: $187 | 2 pax: $110'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
