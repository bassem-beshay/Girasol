"""
Management command to add "Memphis and Sakkara Tour in Cairo" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Memphis and Sakkara Tour in Cairo 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Memphis and Sakkara Tour in Cairo day tour...')

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
            slug='memphis-and-sakkara-tour-cairo',
            defaults={
                'name': 'Memphis and Sakkara Tour in Cairo',
                'name_es': 'Tour Menfis y Saqqara en El Cairo',
                'name_pt': 'Passeio Mênfis e Sacará no Cairo',

                'short_description': (
                    'A fascinating 6-7 hour private tour through the ancient capital Memphis '
                    'and the legendary necropolis of Sakkara. Discover the Recumbent Colossus of '
                    'Ramses II, the Alabaster Sphinx, the Step Pyramid, the Pyramid of Unas, '
                    'decorated Mastabas, and the Imhotep Museum – with an expert Egyptologist guide, '
                    'entrance tickets, and transfers included!'
                ),
                'short_description_es': (
                    'Un fascinante tour privado de 6-7 horas por la antigua capital Menfis '
                    'y la legendaria necrópolis de Saqqara. Descubra el Coloso Yacente de '
                    'Ramsés II, la Esfinge de Alabastro, la Pirámide Escalonada, la Pirámide de Unas, '
                    'Mastabas decoradas y el Museo de Imhotep – con guía egiptólogo experto, '
                    'entradas y traslados incluidos!'
                ),
                'short_description_pt': (
                    'Um fascinante passeio privado de 6-7 horas pela antiga capital Mênfis '
                    'e a lendária necrópole de Sacará. Descubra o Colosso Deitado de '
                    'Ramsés II, a Esfinge de Alabastro, a Pirâmide Escalonada, a Pirâmide de Unas, '
                    'Mastabas decoradas e o Museu de Imhotep – com guia egiptólogo especializado, '
                    'ingressos e traslados inclusos!'
                ),

                'description': '''<p>The Memphis and Sakkara Tour is a comprehensive 6-7 hour experience covering the ancient capital Memphis and the legendary Sakkara necropolis, located 35 km south of Cairo.</p>

<p>Our Egyptian Egyptologist guide will meet you at your Cairo hotel. Departure to the <strong>Memphis Open-Air Museum</strong>, an open-air museum displaying antiquities discovered on the site of the ancient capital Memphis, currently located in the local village of Mit Rahina. You will admire antiquities from different periods of ancient Egyptian history, especially the impressive <strong>Recumbent Colossus of King Ramses II</strong>, weighing 60 tons and over 10 meters long. Despite the passage of time, the details of the statue are still visible, a testament to the skill of ancient Egyptian craftsmen. There, we will also see other colossal statues representing King Ramses II and pieces from the <strong>Temple of Ptah</strong> in Memphis, such as the Statue of the Memphis Triad (Ptah, Sekhmet, and Nefertum). Furthermore, in this open-air museum, you will find the <strong>Alabaster Sphinx</strong>, an incredible work carved from a single piece of alabaster.</p>

<p>We continue to visit <strong>Sakkara</strong>, located 7 km from the Memphis Open-Air Museum. It is one of Egypt's most fascinating archaeological sites, serving as the main cemetery for the ancient capital Memphis. We begin with the magnificent <strong>Complex of King Zoser</strong>, the first group of buildings entirely constructed in stone in human history. At the center of this complex stands the <strong>Step Pyramid</strong>, also known as the Pyramid of Saqqara, built by the genius architect Imhotep for King Zoser, 60 m high, consisting of 6 steps.</p>

<p>We will visit the <strong>Heb-Sed Court</strong>, a representation of the same court that once stood in Memphis, where the Trinitarian Festival Heb-Sed was celebrated, expressing the "renewal of the strength and abundance of the King of Egypt." Proceed to visit the <strong>Pyramid of King Unas</strong>, the last king of the 6th Dynasty. We will enter the interior of the pyramid, famous for the hieroglyphic texts known as the <strong>Pyramid Texts</strong>.</p>

<p>Afterwards, we will visit two of the <strong>Mastabas</strong> (tombs decorated with scenes from daily life in ancient Egypt) belonging to nobles: the <strong>Mastaba of Princess Idut</strong> and the <strong>Mastaba of Prince Ty</strong>. Continue to visit the beautiful <strong>Imhotep Museum</strong>, which exhibits wonderful antiquities discovered in Saqqara.</p>

<p>Return transfer to your hotel. (End of Tour).</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
</ul>

<h3>Pricing per Person (USD):</h3>
<ul>
<li><strong>1 Person (Solo):</strong> $164</li>
<li><strong>2 People:</strong> $107 per person</li>
<li><strong>3-4 People:</strong> $97 per person</li>
</ul>

<h3>Children Policy:</h3>
<ul>
<li><strong>Under 2 years (on lap):</strong> Free (sharing the tour with one or two adults).</li>
<li><strong>From 2 to under 7 years:</strong> 50% discount on the adult price.</li>
<li><strong>From 7 to under 12 years:</strong> 25% discount on the adult price.</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water – walking on the plateau and visiting the museum require good hydration.</li>
<li><strong>Lunch:</strong> Not included. You may ask your guide for a lunch stop during the tour or purchase something on route.</li>
<li><strong>Extra tickets:</strong> To enter the interior of the Step Pyramid of Sakkara, or any specific Mastaba (such as Mastaba of Meriruka), you must purchase an additional ticket on site (subject to availability).</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible.</li>
<li>The agency needs at least 48 hours prior to the tour date to process the booking.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>El Tour a Menfis y Saqqara es una experiencia completa de 6 a 7 horas que abarca la antigua capital Menfis y la legendaria necrópolis de Saqqara, ubicadas a 35 km al sur de El Cairo.</p>

<p>Nuestro guía egiptólogo egipcio que habla español le encontrará en su hotel. Salida con destino al <strong>Museo Abierto de Menfis</strong>, un museo al aire libre que exhibe las antigüedades descubiertas en el mismo lugar de la antigua capital Menfis, donde actualmente se encuentra la villa local Mit Rahina. Usted admirará antigüedades que pertenecen a diferentes épocas de la historia del antiguo Egipto, especialmente el impresionante <strong>Coloso Yacente del Rey Ramsés II</strong> con 60 toneladas de peso y más de 10 metros de longitud. A pesar del paso del tiempo, los detalles de la estatua aún son visibles, una prueba de la habilidad de los antiguos artesanos egipcios. Veremos allí también otros colosos y estatuas que representan al rey Ramsés II y piezas que formaban parte del <strong>Templo de Ptah</strong> en Menfis, como la Estatua de la Tríada de Menfis (Ptah, Sekhmet y Nefertum). Además, en este museo abierto se encuentra la <strong>Esfinge de Alabastro</strong>, una obra increíble, esculpida en una sola pieza de alabastro.</p>

<p>Continuamos para visitar <strong>Saqqara</strong>, que está a 7 km de distancia del Museo Abierto de Menfis, uno de los sitios arqueológicos más fascinantes de Egipto que fue el cementerio principal de la antigua capital Menfis. Comenzamos con el magnífico <strong>Complejo del rey Zoser</strong>, el primer grupo de edificios construido enteramente en piedra en la historia de la humanidad. En el centro de este complejo se encuentra la <strong>Pirámide Escalonada</strong>, conocida también como la Pirámide de Saqqara, construida por el genio arquitecto Imhotep para el rey Zoser, con 60 m de altura, y consistía en 6 escalones.</p>

<p>Visitaremos el <strong>Patio del Heb Sed</strong>, representación del mismo patio que un día estaba en la capital Menfis, en el que se celebraba el Festival Trinitario Heb-Sed en expresión de la "renovación de las fuerzas y de la abundancia del rey de Egipto". Prosiguiendo para visitar la <strong>Pirámide del rey Unas</strong>, último rey de la dinastía VI. Visitaremos el interior de la pirámide famosa por los textos de jeroglíficos conocidos como los <strong>Textos de las Pirámides</strong>.</p>

<p>Después vamos a visitar dos de las <strong>Mastabas</strong> (tumbas decoradas con escenas de la vida cotidiana del antiguo Egipto que pertenecen a los nobles): la <strong>Mastaba de la Princesa Idut</strong> y la <strong>Mastaba del Príncipe Ty</strong>. Continuación para visitar el bello <strong>Museo de Imhotep</strong> donde se exhiben maravillosas antigüedades descubiertas en Saqqara.</p>

<p>Traslado de regreso a su hotel. (Fin del Tour).</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
</ul>

<h3>Precios por persona (USD):</h3>
<ul>
<li><strong>1 Persona (Solo):</strong> $164</li>
<li><strong>2 Personas:</strong> $107 por persona</li>
<li><strong>3-4 Personas:</strong> $97 por persona</li>
</ul>

<h3>Política de Niños:</h3>
<ul>
<li><strong>Menos de 2 años (en brazos):</strong> Gratuito (compartiendo la excursión con uno o dos adultos).</li>
<li><strong>De 2 a menores de 7 años:</strong> 50% de descuento sobre el valor del adulto.</li>
<li><strong>De 7 a menores de 12 años:</strong> 25% de descuento sobre el valor del adulto.</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a través de un enlace seguro y personalizado. Rápido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua – caminar por la meseta y visitar el museo requiere una buena hidratación.</li>
<li><strong>Almuerzo:</strong> No está incluido. Puede pedir una parada para almorzar a su guía durante el paseo o comprar algo en el camino.</li>
<li><strong>Boletos adicionales:</strong> Para entrar al interior de la Pirámide Escalonada de Saqqara, o cualquier Mastaba específica (como la Mastaba de Meriruka), es necesario adquirir un boleto adicional en el lugar (sujeto a disponibilidad).</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías.</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelación posible.</li>
<li>La agencia necesita al menos 48 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>O Passeio a Mênfis e Sacará é uma experiência completa de 6 a 7 horas que abrange a antiga capital Mênfis e a lendária necrópole de Sacará, localizadas a 35 km ao sul do Cairo.</p>

<p>O nosso guia egiptólogo egípcio que fala português irá encontrá-lo no seu hotel. Saída com destino ao <strong>Museu Aberto de Mênfis</strong>, um museu a céu aberto que exibe as antiguidades descobertas no mesmo local da antiga capital Mênfis, onde atualmente se encontra a vila local Mit Rahina. Você irá contemplar antiguidades que pertencem a diferentes períodos da história egípcia antiga, especialmente o impressionante <strong>Colosso Deitado do Rei Ramsés II</strong> com 60 toneladas de peso e mais de 10 metros de comprimento. Apesar da passagem do tempo, os detalhes da estátua ainda são visíveis, uma prova da perícia dos antigos artesãos egípcios. Veremos ali também outros colossos e estátuas que representam o rei Ramsés II e peças que faziam parte do <strong>Templo de Ptá</strong> em Mênfis, como a Estátua da Tríade de Mênfis (Ptá, Sekhmet e Nefertum). Ademais, encontra-se neste museu aberto a <strong>Esfinge de Alabastro</strong>, uma obra incrível, esculpida em um único bloco de alabastro.</p>

<p>Seguimos para visitar <strong>Sacará</strong>, que está a 7 km de distância do Museu Aberto de Mênfis, um dos sítios arqueológicos mais fascinantes do Egito que foi o cemitério principal da antiga capital Mênfis. Começamos com o magnífico <strong>Complexo do rei Djser</strong>, o primeiro conjunto de edifícios construído inteiramente em pedra na história da humanidade. No centro deste complexo encontra-se a <strong>Pirâmide Escalonada</strong>, conhecida também como a Pirâmide de Sacará, erguida pelo genial arquiteto Imhotep para o rei Djser, com 60 m de altura, consistindo em 6 degraus.</p>

<p>Visitaremos o <strong>Pátio do Heb Sed</strong>, representação do mesmo pátio que outrora estava na capital Mênfis, no qual se celebrava o Festival Trinitário Heb-Sed em expressão da "renovação das forças e da abundância do rei do Egito". Prosseguimento para visitar a <strong>Pirâmide do rei Unas</strong>, último rei da VI dinastia. Adentraremos o interior da pirâmide, famosa pelos textos hieroglíficos conhecidos como os <strong>Textos das Pirâmides</strong>.</p>

<p>Depois, iremos visitar duas das <strong>Mastabas</strong> (tumbas adornadas com cenas da vida cotidiana do antigo Egito que pertencem aos nobres): a <strong>Mastaba da Princesa Idute</strong> e a <strong>Mastaba do Príncipe Ti</strong>. Continuação para visitar o belo <strong>Museu de Imhotep</strong>, onde se exibem maravilhosas antiguidades descobertas em Sacará.</p>

<p>Translado de retorno ao seu hotel. (Fim do Tour).</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
</ul>

<h3>Valores por pessoa (USD):</h3>
<ul>
<li><strong>1 Pessoa (Individual):</strong> $164</li>
<li><strong>2 Pessoas:</strong> $107 por pessoa</li>
<li><strong>3-4 Pessoas:</strong> $97 por pessoa</li>
</ul>

<h3>Política de Crianças:</h3>
<ul>
<li><strong>Menos de 2 anos (ao colo):</strong> Gratuito (compartilhando a excursão com um ou dois adultos).</li>
<li><strong>De 2 a menores de 7 anos:</strong> 50% de desconto no valor do adulto.</li>
<li><strong>De 7 a menores de 12 anos:</strong> 25% de desconto no valor do adulto.</li>
</ul>

<h3>Condições de Pagamento:</h3>
<p>Efetue o pagamento com seu cartão Visa ou Mastercard através de um link seguro e personalizado. Processo rápido, confiável e descomplicado.</p>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente – a caminhada no planalto e a visita ao museu exigem boa hidratação.</li>
<li><strong>Almoço:</strong> Não está incluído. Pode pedir uma parada para almoçar ao guia durante o passeio ou adquirir algo no caminho.</li>
<li><strong>Ingressos extras:</strong> Para entrar no interior da Pirâmide Escalonada de Sacará, ou visitar uma tumba específica (por exemplo Mastaba de Meriruka), é necessário adquirir um bilhete adicional no local.</li>
<li><strong>Fotografia:</strong> Permitida na maioria das áreas, mas sem flash em algumas galerias.</li>
</ul>

<h3>Política de Reserva e Confirmação:</h3>
<ul>
<li>Recomenda-se reservar com o máximo de antecedência possível.</li>
<li>A agência necessita de no mínimo 48 horas antes da data do tour para processar a reserva.</li>
<li>Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</li>
</ul>''',

                # Classification
                'category': category,
                'tour_type': tour_type,

                # Duration
                'days': 1,
                'nights': 0,

                # Pricing (base price for 3-4 people)
                'price': 97,
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
                'meta_title': 'Memphis & Sakkara Tour in Cairo | 1 Day',
                'meta_title_es': 'Tour Menfis y Saqqara en El Cairo | 1 Día',
                'meta_title_pt': 'Passeio Mênfis e Sacará no Cairo | 1 Dia',
                'meta_description': 'Private 6-7 hour tour: Memphis Open-Air Museum, Ramses II Colossus, Step Pyramid, Pyramid of Unas, Mastabas & Imhotep Museum. Transfers included.',
                'meta_description_es': 'Tour privado de 6-7 horas: Museo de Menfis, Coloso de Ramsés II, Pirámide Escalonada, Pirámide de Unas, Mastabas y Museo de Imhotep. Traslados incluidos.',
                'meta_description_pt': 'Passeio privado de 6-7 horas: Museu de Mênfis, Colosso de Ramsés II, Pirâmide Escalonada, Pirâmide de Unas, Mastabas e Museu de Imhotep. Inclusos.',

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
                'title': 'Memphis Open-Air Museum',
                'title_es': 'Museo Abierto de Menfis',
                'title_pt': 'Museu Aberto de Mênfis',
                'description': 'Explore the ancient capital of Egypt with the impressive Recumbent Colossus of Ramses II (60 tons), the Alabaster Sphinx, and relics from the Temple of Ptah.',
                'description_es': 'Explore la antigua capital de Egipto con el impresionante Coloso Yacente de Ramsés II (60 toneladas), la Esfinge de Alabastro y reliquias del Templo de Ptah.',
                'description_pt': 'Explore a antiga capital do Egito com o impressionante Colosso Deitado de Ramsés II (60 toneladas), a Esfinge de Alabastro e relíquias do Templo de Ptá.',
                'icon': 'monument',
                'sort_order': 1,
            },
            {
                'title': 'Sakkara Necropolis & Step Pyramid',
                'title_es': 'Necrópolis de Saqqara y Pirámide Escalonada',
                'title_pt': 'Necrópole de Sacará e Pirâmide Escalonada',
                'description': 'Visit the Step Pyramid of King Zoser, the Heb-Sed Court, the Pyramid of Unas with its famous Pyramid Texts, and the decorated Mastabas of Princess Idut and Prince Ty.',
                'description_es': 'Visite la Pirámide Escalonada del rey Zoser, el Patio de Heb Sed, la Pirámide de Unas con sus famosos Textos de las Pirámides, y las Mastabas decoradas de la Princesa Idut y el Príncipe Ty.',
                'description_pt': 'Visite a Pirâmide Escalonada do rei Djser, o Pátio de Heb Sed, a Pirâmide de Unas com seus famosos Textos das Pirâmides, e as Mastabas decoradas da Princesa Idute e do Príncipe Ti.',
                'icon': 'pyramid',
                'sort_order': 2,
            },
            {
                'title': 'Expert Egyptologist Guide & Transfers',
                'title_es': 'Guía Egiptólogo Experto y Traslados',
                'title_pt': 'Guia Egiptólogo Especializado e Traslados',
                'description': 'Accompanied by a professional Egyptologist guide with air-conditioned vehicle transfers from and to your Cairo hotel, plus entrance tickets to all sites.',
                'description_es': 'Acompañado por un guía egiptólogo profesional con traslados en vehículo con aire acondicionado desde y hacia su hotel de El Cairo, más entradas a todos los sitios.',
                'description_pt': 'Acompanhado por um guia egiptólogo profissional com traslados em veículo com ar-condicionado de e para seu hotel no Cairo, mais ingressos para todos os locais.',
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
            title='Memphis Open-Air Museum & Sakkara Necropolis',
            title_es='Museo Abierto de Menfis y Necrópolis de Saqqara',
            title_pt='Museu Aberto de Mênfis e Necrópole de Sacará',
            description='''<p><strong>08:00</strong> – Hotel pick-up in Cairo</p>
<p><strong>08:45</strong> – Arrival at Memphis Open-Air Museum in Mit Rahina (1.5 hours)</p>
<ul>
<li>Recumbent Colossus of King Ramses II (60 tons, 10+ meters)</li>
<li>Alabaster Sphinx – carved from a single piece of alabaster</li>
<li>Statue of the Memphis Triad (Ptah, Sekhmet, Nefertum)</li>
<li>Temple of Ptah relics and other colossal statues</li>
</ul>
<p><strong>10:30</strong> – Transfer to Sakkara (7 km, 15 min drive)</p>
<p><strong>10:45</strong> – Sakkara Necropolis (3.5 hours of exploration)</p>
<ul>
<li>Complex of King Zoser – first stone buildings in human history</li>
<li>Step Pyramid of Saqqara – 60 m high, 6 steps, by architect Imhotep</li>
<li>Heb-Sed Court – ceremonial renewal court</li>
<li>Pyramid of King Unas – interior visit with Pyramid Texts</li>
<li>Mastaba of Princess Idut – decorated noble tomb</li>
<li>Mastaba of Prince Ty – scenes of daily life in ancient Egypt</li>
<li>Imhotep Museum – wonderful antiquities from Saqqara</li>
</ul>
<p><strong>14:30</strong> – Return transfer to your hotel in Cairo</p>''',

            description_es='''<p><strong>08:00</strong> – Recogida en el hotel de El Cairo</p>
<p><strong>08:45</strong> – Llegada al Museo Abierto de Menfis en Mit Rahina (1,5 horas)</p>
<ul>
<li>Coloso Yacente del Rey Ramsés II (60 toneladas, más de 10 metros)</li>
<li>Esfinge de Alabastro – esculpida en una sola pieza de alabastro</li>
<li>Estatua de la Tríada de Menfis (Ptah, Sekhmet y Nefertum)</li>
<li>Reliquias del Templo de Ptah y otras estatuas colosales</li>
</ul>
<p><strong>10:30</strong> – Traslado a Saqqara (7 km, 15 min en coche)</p>
<p><strong>10:45</strong> – Necrópolis de Saqqara (3,5 horas de exploración)</p>
<ul>
<li>Complejo del Rey Zoser – primeros edificios de piedra de la humanidad</li>
<li>Pirámide Escalonada de Saqqara – 60 m de altura, 6 escalones, por el arquitecto Imhotep</li>
<li>Patio del Heb Sed – patio de renovación ceremonial</li>
<li>Pirámide del Rey Unas – visita interior con Textos de las Pirámides</li>
<li>Mastaba de la Princesa Idut – tumba noble decorada</li>
<li>Mastaba del Príncipe Ty – escenas de la vida cotidiana del antiguo Egipto</li>
<li>Museo de Imhotep – maravillosas antigüedades de Saqqara</li>
</ul>
<p><strong>14:30</strong> – Traslado de regreso a su hotel en El Cairo</p>''',

            description_pt='''<p><strong>08:00</strong> – Retirada no hotel no Cairo</p>
<p><strong>08:45</strong> – Chegada ao Museu Aberto de Mênfis em Mit Rahina (1,5 horas)</p>
<ul>
<li>Colosso Deitado do Rei Ramsés II (60 toneladas, mais de 10 metros)</li>
<li>Esfinge de Alabastro – esculpida em um único bloco de alabastro</li>
<li>Estátua da Tríade de Mênfis (Ptá, Sekhmet e Nefertum)</li>
<li>Relíquias do Templo de Ptá e outras estátuas colossais</li>
</ul>
<p><strong>10:30</strong> – Translado para Sacará (7 km, 15 min de carro)</p>
<p><strong>10:45</strong> – Necrópole de Sacará (3,5 horas de exploração)</p>
<ul>
<li>Complexo do Rei Djser – primeiros edifícios de pedra da humanidade</li>
<li>Pirâmide Escalonada de Sacará – 60 m de altura, 6 degraus, pelo arquiteto Imhotep</li>
<li>Pátio do Heb Sed – pátio de renovação cerimonial</li>
<li>Pirâmide do Rei Unas – visita interior com Textos das Pirâmides</li>
<li>Mastaba da Princesa Idute – tumba nobre decorada</li>
<li>Mastaba do Príncipe Ti – cenas da vida cotidiana do antigo Egito</li>
<li>Museu de Imhotep – maravilhosas antiguidades de Sacará</li>
</ul>
<p><strong>14:30</strong> – Translado de retorno ao seu hotel no Cairo</p>''',

            locations='Memphis, Sakkara',
            locations_es='Menfis, Saqqara',
            locations_pt='Mênfis, Sacará',
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
                'item_es': 'Traslado en coche/van moderno con aire acondicionado',
                'item_pt': 'Translado em carro/van moderno com ar-condicionado',
            },
            {
                'item': 'Entrance tickets to the places and museums described in the itinerary',
                'item_es': 'Entradas a los lugares y museos descritos en el itinerario como incluidos',
                'item_pt': 'Ingressos dos lugares e museus descritos no roteiro como inclusos',
            },
            {
                'item': 'Expert Egyptologist guide',
                'item_es': 'Guía egiptólogo que habla español',
                'item_pt': 'Guia egiptólogo que fala português',
            },
            {
                'item': 'Service and technical assistance',
                'item_es': 'Servicio y ayuda técnica',
                'item_pt': 'Serviço e auxílio técnico',
            },
            {
                'item': '1 bottle of mineral water per person during the tour',
                'item_es': '1 botella de agua mineral por persona durante los paseos',
                'item_pt': '1 garrafa de água mineral por pessoa durante os passeios',
            },
            {
                'item': 'All tour fees and service charges',
                'item_es': 'Todas las tasas de tours y tasas de servicios',
                'item_pt': 'Todas as taxas de tours e taxas de serviços',
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
                'question': 'Can I enter the interior of the Step Pyramid of Sakkara?',
                'question_es': '¿Puedo entrar al interior de la Pirámide Escalonada de Saqqara?',
                'question_pt': 'Posso entrar no interior da Pirâmide Escalonada de Sacará?',
                'answer': '<p>The entrance to the interior of the Step Pyramid is included in this tour as part of the itinerary. However, if specific Mastabas such as the Mastaba of Meriruka require an additional ticket, it must be purchased on site, subject to availability from the Ministry of Tourism.</p>',
                'answer_es': '<p>La entrada al interior de la Pirámide Escalonada está incluida en este tour como parte del itinerario. Sin embargo, si Mastabas específicas como la Mastaba de Meriruka requieren un boleto adicional, debe adquirirse en el lugar, sujeto a disponibilidad del Ministerio de Turismo.</p>',
                'answer_pt': '<p>A entrada ao interior da Pirâmide Escalonada está incluída neste passeio como parte do roteiro. No entanto, se Mastabas específicas como a Mastaba de Meriruka exigirem um bilhete adicional, este deve ser adquirido no local, sujeito à disponibilidade do Ministério do Turismo.</p>',
                'sort_order': 1,
            },
            {
                'question': 'What if the Mastabas mentioned are closed?',
                'question_es': '¿Qué sucede si las Mastabas mencionadas están cerradas?',
                'question_pt': 'E se as Mastabas mencionadas estiverem fechadas?',
                'answer': '<p>If the Mastabas of Princess Idut or Prince Ty are closed for visits, they will be replaced by other similar Mastabas in the Sakkara region belonging to other nobles. The guide will select the best available alternatives.</p>',
                'answer_es': '<p>Si eventualmente las Mastabas de la Princesa Idut o del Príncipe Ty estuvieran cerradas a la visita, serán sustituidas por otras Mastabas similares en la región de Saqqara pertenecientes a otros nobles. El guía seleccionará las mejores alternativas disponibles.</p>',
                'answer_pt': '<p>Se eventualmente as Mastabas da Princesa Idute ou do Príncipe Ti estiverem fechadas à visitação, as mesmas serão substituídas por outras Mastabas similares na região de Sacará pertencentes a outros nobres. O guia selecionará as melhores alternativas disponíveis.</p>',
                'sort_order': 2,
            },
            {
                'question': 'Is lunch included in this tour?',
                'question_es': '¿El almuerzo está incluido en este tour?',
                'question_pt': 'O almoço está incluído neste passeio?',
                'answer': '<p>No, lunch is not included. You may ask your guide for a lunch stop during the tour or purchase something on route. The tour duration is 6-7 hours, so you may also eat after returning to your hotel.</p>',
                'answer_es': '<p>No, el almuerzo no está incluido. Puede pedir una parada para almorzar a su guía durante el paseo o comprar algo en el camino. La duración del tour es de 6-7 horas, así que también puede comer después de regresar a su hotel.</p>',
                'answer_pt': '<p>Não, o almoço não está incluído. Pode pedir uma parada para almoçar ao guia durante o passeio ou adquirir algo no caminho. A duração do passeio é de 6-7 horas, então também pode comer após retornar ao seu hotel.</p>',
                'sort_order': 3,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': '¿Qué debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen. Comfortable walking shoes are essential as you will be walking on uneven terrain at the archaeological sites.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar. El calzado cómodo para caminar es esencial ya que caminará por terreno irregular en los sitios arqueológicos.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar é essencial pois você caminhará por terreno irregular nos sítios arqueológicos.</p>',
                'sort_order': 4,
            },
            {
                'question': 'How far in advance should I book?',
                'question_es': '¿Con cuánta antelación debo reservar?',
                'question_pt': 'Com quanta antecedência devo reservar?',
                'answer': '<p>We recommend booking as far in advance as possible to guarantee availability of the Egyptologist guide and online tickets. The agency needs at least 48 hours prior to the tour date. Bookings within less than 24 hours are subject to last-minute availability.</p>',
                'answer_es': '<p>Recomendamos reservar con la mayor antelación posible para garantizar la disponibilidad del guía egiptólogo y de los boletos en línea. La agencia necesita al menos 48 horas antes de la fecha del tour. Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</p>',
                'answer_pt': '<p>Recomendamos reservar com o máximo de antecedência possível para garantir a disponibilidade do guia egiptólogo e dos ingressos online. A agência necessita de no mínimo 48 horas antes da data do tour. Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</p>',
                'sort_order': 5,
            },
            {
                'question': 'Is photography allowed?',
                'question_es': '¿Se permite la fotografía?',
                'question_pt': 'A fotografia é permitida?',
                'answer': '<p>Photography is permitted in most areas. However, flash photography is not allowed in some galleries and interiors. Please follow security guidelines at each location.</p>',
                'answer_es': '<p>La fotografía está permitida en la mayoría de las áreas. Sin embargo, no se permite el uso de flash en algunas galerías e interiores. Por favor, siga las indicaciones de seguridad en cada ubicación.</p>',
                'answer_pt': '<p>A fotografia é permitida na maioria das áreas. No entanto, não é permitido o uso de flash em algumas galerias e interiores. Por favor, siga as orientações de segurança em cada local.</p>',
                'sort_order': 6,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day'
            f'\n  - Price: ${tour.price} (3-4 pax) | Solo: $164 | 2 pax: $107'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
