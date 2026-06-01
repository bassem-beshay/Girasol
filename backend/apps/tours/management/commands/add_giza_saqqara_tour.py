"""
Management command to add "Giza Pyramids and Saqqara" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Giza Pyramids and Saqqara 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Giza Pyramids and Saqqara day tour...')

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
            slug='giza-pyramids-and-saqqara-tour',
            defaults={
                'name': 'Giza Pyramids and Saqqara Tour',
                'name_es': 'Tour Pirámides de Giza y Saqqara',
                'name_pt': 'Passeio às Pirâmides de Gizé e Sacará',

                'short_description': (
                    'An unforgettable 8-hour private tour combining the majestic Giza Pyramids '
                    'with the ancient Saqqara necropolis. Explore the Great Pyramids, the Sphinx, '
                    'the Step Pyramid of Djoser, the Mastabas of the Nobles, and the Imhotep Museum, '
                    'all with an expert Egyptologist guide and transfers included!'
                ),
                'short_description_es': (
                    'Un tour privado de 8 horas que combina las majestuosas Pirámides de Giza '
                    'con la antigua necrópolis de Saqqara. Explore las Grandes Pirámides, la Esfinge, '
                    'la Pirámide Escalonada de Zoser, las Mastabas de los Nobles y el Museo de Imhotep, '
                    '¡todo con un guía egiptólogo experto y traslados incluidos!'
                ),
                'short_description_pt': (
                    'Um passeio privado de 8 horas combinando as majestosas Pirâmides de Gizé '
                    'com a antiga necrópole de Sacará. Explore as Grandes Pirâmides, a Esfinge, '
                    'a Pirâmide Escalonada de Djser, as Mastabas dos Nobres e o Museu de Imhotep, '
                    'tudo com um guia egiptólogo especializado e traslados inclusos!'
                ),

                'description': '''<p>The Giza Pyramids and Saqqara Tour is a comprehensive 8-hour experience combining the iconic Giza Pyramid Complex with the ancient Saqqara necropolis, located 30 km south of Giza.</p>

<p>Our Egyptian Egyptologist guide will meet you at your Cairo hotel. First, we will visit the Great Pyramids of Egypt in Giza: <strong>Khufu, Khafra, and Men-Kau-Ra</strong>, i.e., Cheops, Chephren, and Mycerinus (as determined by the Egyptian Ministry of Tourism, entry into the interior galleries of the Great Pyramid requires an extra ticket and is not included). The Pyramids of Giza are the only remaining of the Ancient Seven Wonders of the World since the 4th dynasty of the Old Kingdom.</p>

<p>We will proceed to the <strong>panoramic plateau</strong> to take wonderful photos from unique angles and perspectives, including all the pyramids. View of the <strong>Valley Temple</strong> belonging to King Khafra, the owner of the second pyramid of Giza and the fourth king of the IV Dynasty, where 11 statues of King Khafra were discovered.</p>

<p>Visit to the <strong>Great Sphinx</strong>, the enormous colossus, carved from a single monolithic limestone block, with a human head and a lion's body, symbolizing the solar god, Hor-em-Akhet (Horus on the Horizon).</p>

<p><strong>Lunch stop</strong> (lunch is not included in this tour).</p>

<p>Proceed to <strong>Saqqara</strong> (30 km from the Giza area). Visit the famous <strong>Complex of King Zoser</strong>, especially the <strong>Step Pyramid</strong>, considered the first pyramid built in limestone, 60 m high with 6 large steps. Visit the <strong>Mastabas of the Nobles</strong>, including the Mastaba of Princess Idut and the Mastaba of Prince Ty, known for their beautiful decorations and scenes. Finally, visit the beautiful <strong>Imhotep Museum</strong>, dedicated to the wise architect of the Saqqara Complex, housing a variety of antiquities discovered in the region.</p>

<p>Return to your hotel in Cairo. (End of Tour).</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
</ul>

<h3>Pricing per Person (USD):</h3>
<ul>
<li><strong>1 Person (Solo):</strong> $197</li>
<li><strong>2 People:</strong> $127 per person</li>
<li><strong>3-4 People:</strong> $120 per person</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water – walking on the plateau and visiting the sites require good hydration.</li>
<li><strong>Lunch:</strong> Not included. You may ask your guide for a lunch stop during the tour.</li>
<li><strong>Extra tickets:</strong> To enter the interior of the Great Pyramid of Cheops, the Step Pyramid of Saqqara, or any specific Mastaba, you must purchase an additional ticket on site (subject to availability).</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible.</li>
<li>The agency needs at least 24 hours prior to the tour date to process the booking.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>El Tour Pirámides de Giza y Saqqara es una experiencia completa de 8 horas que combina el icónico Complejo de las Pirámides de Giza con la antigua necrópolis de Saqqara, ubicada a 30 km al sur de Giza.</p>

<p>Nuestro guía egiptólogo egipcio se encontrará con usted en su hotel de El Cairo. Primero visitaremos las Grandes Pirámides de Egipto en Giza: <strong>Khufu, Khafra y Men-Kau-Ra</strong>, es decir: Keops, Kefrén y Micerinos (por determinación del Ministerio de Turismo Egipcio, la entrada al interior de las galerías de la Gran Pirámide requiere un boleto adicional y no está incluida). Las Pirámides de Giza son las únicas remanentes de las Antiguas Siete Maravillas del mundo desde la IV dinastía del Reino Antiguo.</p>

<p>A continuación, se dirigirá a la zona de la <strong>meseta panorámica</strong> para tomar fotos maravillosas desde ángulos y perspectivas únicas, que incluyen todas las pirámides. Vista al <strong>Templo del Valle</strong> que pertenece al rey Kefrén, el dueño de la segunda pirámide de Giza y el cuarto rey de la Dinastía IV, donde fueron descubiertas 11 estatuas del rey Kefrén.</p>

<p>Visita a la <strong>Gran Esfinge</strong>, el enorme coloso, esculpido en un monolito de piedra caliza, con cabeza humana y cuerpo de león, que simboliza al dios solar, Hor-em-Akhet (Horus en el Horizonte).</p>

<p><strong>Parada para el Almuerzo</strong> (el almuerzo no está incluido en este tour).</p>

<p>Prosiguiendo hacia <strong>Saqqara</strong> (30 km del área de Giza). Visita al famoso <strong>Complejo del rey Zoser</strong>, especialmente la <strong>Pirámide Escalonada</strong>, considerada la primera pirámide construida en piedra caliza, tiene 60 m de altura y consiste en 6 grandes escalones. Visita a las <strong>Mastabas de los Nobles</strong>, incluyendo la Mastaba de la Princesa Idut y la Mastaba del Príncipe Ty, conocidas por sus bellas decoraciones y escenas. Finalmente, visitará el bello <strong>Museo de Imhotep</strong>, el sabio arquitecto del Complejo de Saqqara, que alberga variedad de antigüedades descubiertas en la región.</p>

<p>Regreso a su hotel en El Cairo. (Fin del Tour).</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
</ul>

<h3>Precios por persona (USD):</h3>
<ul>
<li><strong>1 Persona (Solo):</strong> $197</li>
<li><strong>2 Personas:</strong> $127 por persona</li>
<li><strong>3-4 Personas:</strong> $120 por persona</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a través de un enlace seguro y personalizado. Rápido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua – caminar por la meseta y visitar los sitios requiere una buena hidratación.</li>
<li><strong>Almuerzo:</strong> No está incluido. Puede pedir una parada para almorzar a su guía durante el paseo.</li>
<li><strong>Boletos adicionales:</strong> Para entrar al interior de la Gran Pirámide de Keops, la Pirámide Escalonada, etc., es necesario adquirir un boleto adicional en el lugar (sujeto a disponibilidad del Ministerio de Turismo).</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías.</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelación posible.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>O Passeio às Pirâmides de Gizé e Sacará é uma experiência completa de 8 horas combinando o icônico Complexo das Pirâmides de Gizé com a antiga necrópole de Sacará, localizada a 30 km ao sul de Gizé.</p>

<p>Nosso guia egiptólogo egípcio irá encontrá-lo em seu hotel no Cairo. Primeiramente, visitaremos as Grandes Pirâmides do Egito em Gizé: <strong>Khufu, Khafra e Men-Kau-Rá</strong>, ou seja: Quéops, Quéfren e Miquerinos (por determinação do Ministério do Turismo Egípcio, a entrada no interior das galerias da Grande Pirâmide requer um ingresso extra e não está inclusa). As Pirâmides de Gizé são as únicas remanescentes das Antigas Sete Maravilhas do mundo desde a IV dinastia do Reino Antigo.</p>

<p>Na sequência, seguirá para a região do <strong>planalto panorâmico</strong> para tirar fotos maravilhosas de ângulos e perspectivas únicas, que incluem todas as pirâmides. Vista ao <strong>Templo do Vale</strong> que pertence ao rei Quéfren, o dono da segunda pirâmide de Gizé e o quarto rei da Dinastia IV, onde foram descobertas 11 estátuas do rei Quéfren.</p>

<p>Visita à <strong>Grande Esfinge</strong>, o enorme colosso, esculpido em um monólito de pedra calcária, com cabeça humana e corpo de leão, que simboliza o deus solar, Hor-em-Akhet (Hórus no Horizonte).</p>

<p><strong>Parada para Almoço</strong> (almoço não incluso).</p>

<p>Prosseguimento para <strong>Sacará</strong> (30 km da área de Gizé). Visita ao famoso <strong>Complexo do rei Djser</strong>, especialmente a <strong>Pirâmide Escalonada</strong>, considerada a primeira pirâmide construída em pedra calcária, tem 60 m de altura e consiste em 6 grandes degraus. Visita às <strong>Mastabas dos Nobres</strong>, incluindo a Mastaba da Princesa Idut e a Mastaba do Príncipe Ti, conhecidas por suas belas decorações e cenas. Finalmente, visitará o belo <strong>Museu de Imhotep</strong>, o sábio arquiteto do Complexo de Sacará, que abriga variedades de antiguidades descobertas na região.</p>

<p>Retorno ao seu hotel no Cairo. (Fim do Tour).</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
</ul>

<h3>Valores por pessoa (USD):</h3>
<ul>
<li><strong>1 Pessoa (Individual):</strong> $197</li>
<li><strong>2 Pessoas:</strong> $127 por pessoa</li>
<li><strong>3-4 Pessoas:</strong> $120 por pessoa</li>
</ul>

<h3>Condições de Pagamento:</h3>
<p>Efetue o pagamento com seu cartão Visa ou Mastercard através de um link seguro e personalizado. Processo rápido, confiável e descomplicado.</p>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente – a caminhada no planalto e a visita aos sítios exigem boa hidratação.</li>
<li><strong>Almoço:</strong> Não está incluído. Pode pedir uma parada para almoçar ao guia durante o passeio.</li>
<li><strong>Ingressos extras:</strong> Para entrar no interior da Grande Pirâmide de Quéops, a Pirâmide Escalonada, etc., é necessário adquirir um bilhete adicional no local (sujeito à disponibilidade do Ministério do Turismo).</li>
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
                'price': 120,
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

                # SEO (meta_title max 70, meta_description max 160)
                'meta_title': 'Giza Pyramids & Saqqara Tour | 1 Day Private Tour',
                'meta_title_es': 'Tour Pirámides de Giza y Saqqara | 1 Día Privado',
                'meta_title_pt': 'Pirâmides de Gizé e Sacará | Passeio 1 Dia',
                'meta_description': '8-hour guided tour: Giza Pyramids, Sphinx, Saqqara Step Pyramid, Mastabas of the Nobles & Imhotep Museum. Transfers included.',
                'meta_description_es': 'Tour guiado de 8 horas: Pirámides de Giza, Esfinge, Pirámide Escalonada de Saqqara, Mastabas de los Nobles y Museo Imhotep. Traslados incluidos.',
                'meta_description_pt': 'Passeio guiado de 8 horas: Pirâmides de Gizé, Esfinge, Pirâmide Escalonada de Sacará, Mastabas dos Nobres e Museu Imhotep. Traslados inclusos.',

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
                'title_es': 'Complejo de las Pirámides de Giza',
                'title_pt': 'Complexo das Pirâmides de Gizé',
                'description': 'Visit the three Great Pyramids of Khufu, Khafra, and Menkaure, the Panoramic Plateau, the Valley Temple, and the legendary Great Sphinx.',
                'description_es': 'Visite las tres Grandes Pirámides de Keops, Kefrén y Micerinos, la Meseta Panorámica, el Templo del Valle y la legendaria Gran Esfinge.',
                'description_pt': 'Visite as três Grandes Pirâmides de Quéops, Quéfren e Miquerinos, o Planalto Panorâmico, o Templo do Vale e a lendária Grande Esfinge.',
                'icon': 'pyramid',
                'sort_order': 1,
            },
            {
                'title': 'Saqqara Necropolis & Step Pyramid',
                'title_es': 'Necrópolis de Saqqara y Pirámide Escalonada',
                'title_pt': 'Necrópole de Sacará e Pirâmide Escalonada',
                'description': 'Explore the Step Pyramid of Djoser, the first pyramid ever built in limestone, along with the beautifully decorated Mastabas of Princess Idut and Prince Ty.',
                'description_es': 'Explore la Pirámide Escalonada de Zoser, la primera pirámide construida en piedra caliza, junto con las bellamente decoradas Mastabas de la Princesa Idut y el Príncipe Ty.',
                'description_pt': 'Explore a Pirâmide Escalonada de Djser, a primeira pirâmide construída em pedra calcária, junto com as belamente decoradas Mastabas da Princesa Idut e do Príncipe Ti.',
                'icon': 'monument',
                'sort_order': 2,
            },
            {
                'title': 'Imhotep Museum',
                'title_es': 'Museo de Imhotep',
                'title_pt': 'Museu de Imhotep',
                'description': 'Visit the Imhotep Museum in Saqqara, dedicated to the wise architect of the complex, housing a variety of antiquities discovered in the region.',
                'description_es': 'Visite el Museo de Imhotep en Saqqara, dedicado al sabio arquitecto del complejo, que alberga variedad de antigüedades descubiertas en la región.',
                'description_pt': 'Visite o Museu de Imhotep em Sacará, dedicado ao sábio arquiteto do complexo, que abriga variedades de antiguidades descobertas na região.',
                'icon': 'museum',
                'sort_order': 3,
            },
            {
                'title': 'Expert Egyptologist Guide & Transfers',
                'title_es': 'Guía Egiptólogo Experto y Traslados',
                'title_pt': 'Guia Egiptólogo Especializado e Traslados',
                'description': 'Accompanied by a professional Egyptologist guide with air-conditioned vehicle transfers from and to your Cairo hotel.',
                'description_es': 'Acompañado por un guía egiptólogo profesional con traslados en vehículo con aire acondicionado desde y hacia su hotel de El Cairo.',
                'description_pt': 'Acompanhado por um guia egiptólogo profissional com traslados em veículo com ar-condicionado de e para seu hotel no Cairo.',
                'icon': 'guide',
                'sort_order': 4,
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
            title='Giza Pyramids & Saqqara Necropolis',
            title_es='Pirámides de Giza y Necrópolis de Saqqara',
            title_pt='Pirâmides de Gizé e Necrópole de Sacará',
            description='''<p><strong>08:00</strong> – Hotel pick-up in Cairo</p>
<p><strong>08:30</strong> – Arrival at Giza Complex</p>
<ul>
<li>The Three Great Pyramids (Khufu, Khafra, Men-Kau-Ra)</li>
<li>Panoramic Plateau for photos from unique angles</li>
<li>Valley Temple of King Khafra</li>
<li>The Great Sphinx – symbol of the solar god Hor-em-Akhet</li>
</ul>
<p><strong>12:30</strong> – Free time for lunch (not included)</p>
<p><strong>13:30</strong> – Transfer to Saqqara (30 km from Giza)</p>
<ul>
<li>Complex of King Zoser with the Step Pyramid (60 m, 6 steps)</li>
<li>Mastabas of the Nobles (Princess Idut and Prince Ty)</li>
<li>Imhotep Museum – antiquities from the Saqqara region</li>
</ul>
<p><strong>17:00</strong> – Return to hotel in Cairo</p>''',

            description_es='''<p><strong>08:00</strong> – Recogida en el hotel de El Cairo</p>
<p><strong>08:30</strong> – Llegada al Complejo de Giza</p>
<ul>
<li>Las Tres Grandes Pirámides (Keops, Kefrén, Micerinos)</li>
<li>Meseta Panorámica para fotos desde ángulos únicos</li>
<li>Templo del Valle del rey Kefrén</li>
<li>La Gran Esfinge – símbolo del dios solar Hor-em-Akhet</li>
</ul>
<p><strong>12:30</strong> – Tiempo libre para almuerzo (no incluido)</p>
<p><strong>13:30</strong> – Traslado a Saqqara (30 km de Giza)</p>
<ul>
<li>Complejo del rey Zoser con la Pirámide Escalonada (60 m, 6 escalones)</li>
<li>Mastabas de los Nobles (Princesa Idut y Príncipe Ty)</li>
<li>Museo de Imhotep – antigüedades de la región de Saqqara</li>
</ul>
<p><strong>17:00</strong> – Regreso al hotel en El Cairo</p>''',

            description_pt='''<p><strong>08:00</strong> – Retirada no hotel no Cairo</p>
<p><strong>08:30</strong> – Chegada ao Complexo de Gizé</p>
<ul>
<li>As Três Grandes Pirâmides (Quéops, Quéfren, Miquerinos)</li>
<li>Planalto Panorâmico para fotos de ângulos únicos</li>
<li>Templo do Vale do rei Quéfren</li>
<li>A Grande Esfinge – símbolo do deus solar Hor-em-Akhet</li>
</ul>
<p><strong>12:30</strong> – Tempo livre para almoço (não incluso)</p>
<p><strong>13:30</strong> – Traslado para Sacará (30 km de Gizé)</p>
<ul>
<li>Complexo do rei Djser com a Pirâmide Escalonada (60 m, 6 degraus)</li>
<li>Mastabas dos Nobres (Princesa Idut e Príncipe Ti)</li>
<li>Museu de Imhotep – antiguidades da região de Sacará</li>
</ul>
<p><strong>17:00</strong> – Retorno ao hotel no Cairo</p>''',

            locations='Giza, Saqqara, Cairo',
            locations_es='Giza, Saqqara, El Cairo',
            locations_pt='Gizé, Sacará, Cairo',
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
                'item_es': 'Traslado en coche/van moderna con aire acondicionado',
                'item_pt': 'Translado em carro/van moderna com ar-condicionado',
            },
            {
                'item': 'Entrance tickets to tourist sites and Museums described as included in the itinerary',
                'item_es': 'Entradas a los lugares turísticos y Museos descritos como incluidos en el itinerario',
                'item_pt': 'Ingressos dos lugares turísticos e Museus descritos como inclusos no roteiro',
            },
            {
                'item': 'Expert Egyptologist guide',
                'item_es': 'Guía egiptólogo egipcio',
                'item_pt': 'Guia egiptólogo egípcio',
            },
            {
                'item': 'Service and technical assistance from the support team',
                'item_es': 'Servicio y ayuda técnica del equipo de apoyo',
                'item_pt': 'Serviço e auxílio técnico da equipe de apoio',
            },
            {
                'item': '1 bottle of mineral water per person during the tour',
                'item_es': '1 botella de agua mineral por persona durante el día',
                'item_pt': '1 garrafa de água mineral por pessoa durante o dia',
            },
            {
                'item': 'All tour fees and service charges',
                'item_es': 'Tasas de tours y tasas de servicios',
                'item_pt': 'Taxas de tours e taxas de serviços',
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
                'item_pt': 'Hospedagem no Cairo',
            },
            {
                'item': 'Meals',
                'item_es': 'Comidas',
                'item_pt': 'Refeições',
            },
            {
                'item': 'Entrance ticket to the interior of the Great Pyramid of Giza or any other pyramid and any specific tomb in Saqqara not mentioned in the itinerary',
                'item_es': 'Boleto de entrada al interior de la Gran Pirámide de Giza o cualquier otra pirámide y cualquier tumba específica en Saqqara no mencionada en el itinerario',
                'item_pt': 'Ingresso do interior da Grande Pirâmide de Gizé ou qualquer outra pirâmide e qualquer tumba específica em Sacará não mencionada no roteiro',
            },
            {
                'item': 'Tips, traditionally given to the guide and driver',
                'item_es': 'Propinas, tradicionalmente dadas al guía y al conductor',
                'item_pt': 'Gorjetas, tradicionalmente oferecidas ao guia e motorista',
            },
            {
                'item': 'Extras and anything not described as included in the itinerary',
                'item_es': 'Extras y todo lo que no esté descrito como incluido en el itinerario',
                'item_pt': 'Extras e tudo o que não está descrito como incluso no roteiro',
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
                'question': 'Can I enter the interior of the Great Pyramid or the Step Pyramid?',
                'question_es': '¿Puedo entrar al interior de la Gran Pirámide o la Pirámide Escalonada?',
                'question_pt': 'Posso entrar no interior da Grande Pirâmide ou da Pirâmide Escalonada?',
                'answer': '<p>Entrance to the interior of the Great Pyramid and the Step Pyramid of Saqqara is not included in the tour. You must purchase an additional ticket on site, subject to availability from the Ministry of Tourism. The number of tickets is limited daily.</p>',
                'answer_es': '<p>La entrada al interior de la Gran Pirámide y la Pirámide Escalonada de Saqqara no está incluida en el tour. Es necesario adquirir un boleto adicional en el lugar, sujeto a disponibilidad del Ministerio de Turismo. El número de boletos es limitado diariamente.</p>',
                'answer_pt': '<p>O acesso ao interior da Grande Pirâmide e da Pirâmide Escalonada de Sacará não está incluso no passeio. É necessário adquirir um bilhete adicional no local, sujeito à disponibilidade do Ministério do Turismo. O número de ingressos é limitado diariamente.</p>',
                'sort_order': 1,
            },
            {
                'question': 'Is lunch included in this tour?',
                'question_es': '¿El almuerzo está incluido en este tour?',
                'question_pt': 'O almoço está incluído neste passeio?',
                'answer': '<p>No, lunch is not included. There is a free time stop where you can eat at nearby local restaurants. You may ask your guide for a lunch stop during the tour.</p>',
                'answer_es': '<p>No, el almuerzo no está incluido. Hay una parada de tiempo libre donde puede comer en restaurantes locales cercanos. Puede pedir una parada para almorzar a su guía durante el paseo.</p>',
                'answer_pt': '<p>Não, o almoço não está incluído. Há uma parada de tempo livre onde pode comer em restaurantes locais próximos. Pode pedir uma parada para almoçar ao guia durante o passeio.</p>',
                'sort_order': 2,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': '¿Qué debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen for the morning at the pyramids and the afternoon at Saqqara. Comfortable walking shoes are essential.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar para la mañana en las pirámides y la tarde en Saqqara. El calzado cómodo para caminar es esencial.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapéu, óculos de sol e protetor solar para a manhã nas pirâmides e a tarde em Sacará. Calçado confortável para caminhar é essencial.</p>',
                'sort_order': 3,
            },
            {
                'question': 'How far in advance should I book?',
                'question_es': '¿Con cuánta antelación debo reservar?',
                'question_pt': 'Com quanta antecedência devo reservar?',
                'answer': '<p>We recommend booking as far in advance as possible to guarantee availability of the Egyptologist guide and online tickets. The agency needs at least 24 hours prior to the tour date. Bookings within less than 24 hours are subject to last-minute availability.</p>',
                'answer_es': '<p>Recomendamos reservar con la mayor antelación posible para garantizar la disponibilidad del guía egiptólogo y de los boletos en línea. La agencia necesita al menos 24 horas antes de la fecha del tour. Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</p>',
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
            {
                'question': 'How far is Saqqara from Giza?',
                'question_es': '¿Qué tan lejos está Saqqara de Giza?',
                'question_pt': 'Qual a distância de Sacará a Gizé?',
                'answer': '<p>Saqqara is approximately 30 km south of the Giza Pyramid Complex. The transfer between the two sites takes about 30-40 minutes by air-conditioned vehicle, which is included in the tour.</p>',
                'answer_es': '<p>Saqqara está a aproximadamente 30 km al sur del Complejo de las Pirámides de Giza. El traslado entre los dos sitios toma alrededor de 30-40 minutos en vehículo con aire acondicionado, incluido en el tour.</p>',
                'answer_pt': '<p>Sacará fica a aproximadamente 30 km ao sul do Complexo das Pirâmides de Gizé. O traslado entre os dois locais leva cerca de 30-40 minutos em veículo com ar-condicionado, incluído no passeio.</p>',
                'sort_order': 6,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day'
            f'\n  - Price: ${tour.price} (3-4 pax) | Solo: $197 | 2 pax: $127'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
