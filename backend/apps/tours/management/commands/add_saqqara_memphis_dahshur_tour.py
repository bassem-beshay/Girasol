"""
Management command to add "Saqqara Tour with Memphis and Dahshur" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Saqqara Tour with Memphis and Dahshur 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Saqqara Tour with Memphis and Dahshur day tour...')

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
            slug='saqqara-memphis-dahshur-tour',
            defaults={
                'name': 'Saqqara Tour with Memphis and Dahshur',
                'name_es': 'Tour Saqqara con Menfis y Dahshur',
                'name_pt': 'Passeio Sacará com Mênfis e Dahshur',

                'short_description': (
                    'An extraordinary 8-9 hour journey through the origins of pyramid '
                    'architecture: explore the Memphis Open-Air Museum with the Colossus '
                    'of Ramses II, the Step Pyramid of Saqqara and its decorated Mastabas, '
                    'the Imhotep Museum, and the revolutionary Bent and Red Pyramids of '
                    'Dahshur. Private tour with expert Egyptologist guide and transfers included!'
                ),
                'short_description_es': (
                    'Un extraordinario viaje de 8-9 horas por los orígenes de la arquitectura '
                    'piramidal: explore el Museo Abierto de Menfis con el Coloso de Ramsés II, '
                    'la Pirámide Escalonada de Saqqara y sus Mastabas decoradas, el Museo de '
                    'Imhotep, y las revolucionarias Pirámides Acodada y Roja de Dahshur. '
                    '¡Tour privado con guía egiptólogo experto y traslados incluidos!'
                ),
                'short_description_pt': (
                    'Uma jornada extraordinária de 8-9 horas pelas origens da arquitetura '
                    'piramidal: explore o Museu Aberto de Mênfis com o Colosso de Ramsés II, '
                    'a Pirâmide Escalonada de Sacará e suas Mastabas decoradas, o Museu de '
                    'Imhotep, e as revolucionárias Pirâmides Curvada e Vermelha de Dahshur. '
                    'Tour privado com guia egiptólogo especializado e traslados inclusos!'
                ),

                'description': '''<p>The Saqqara Tour with Memphis and Dahshur is an 8-9 hour tour with visits to the Memphis Open-Air Museum and the Recumbent Colossus of King Ramses II, visiting Saqqara including the Step Pyramid and two of the Mastabas (tombs decorated with scenes from daily life in ancient Egypt belonging to nobles: Mastaba of Princess Idut and Mastaba of Prince Ty). Visit to the beautiful Imhotep Museum.</p>

<p>Our Egyptian Egyptologist guide, who speaks English, will meet you at your hotel. Departure to the <strong>Memphis Open-Air Museum</strong>, an open-air museum displaying antiquities discovered on the site of the ancient capital Memphis, currently located in the local village of Mit Rahina, 35 km south of Cairo. You will admire antiquities from different periods of ancient Egyptian history, especially the impressive <strong>Recumbent Colossus of King Ramses II</strong>, weighing 60 tons and over 10 meters long. Despite the passage of time, the details of the statue are still visible, a testament to the skill of ancient Egyptian craftsmen. There, we will also see other colossal statues representing King Ramses II and pieces from the Temple of Ptah in Memphis, such as the <strong>Statue of the Memphis Triad</strong> (Ptah, Sekhmet, and Nefertum). Furthermore, in this open-air museum, you will find the <strong>Alabaster Sphinx</strong>, an incredible work carved from a single piece of alabaster.</p>

<p>We continue to visit <strong>Saqqara</strong>, located 7 km from the Memphis Open-Air Museum. It is one of Egypt's most fascinating archaeological sites, serving as the main cemetery for the ancient capital Memphis. We begin with the magnificent <strong>Complex of King Zoser</strong>, the first group of buildings entirely constructed in stone in human history. At the center of this complex stands the <strong>Step Pyramid</strong>, also known as the Pyramid of Saqqara, built by the genius architect Imhotep for King Zoser as a step pyramid, 60 m high, consisting of 6 steps, each built upon the other. We will visit the <strong>Heb-Sed Court</strong>, a representation of the same court that once stood in Memphis, where the Trinitarian Festival Heb-Sed was celebrated, expressing the "renewal of the strength and abundance of the King of Egypt." Proceed to visit the <strong>Pyramid of King Unas</strong>, the last king of the 6th Dynasty. We will enter the interior of the pyramid, famous for the hieroglyphic texts known as the <strong>Pyramid Texts</strong>. Afterwards, we will visit two of the <strong>Mastabas</strong> (tombs decorated with scenes from daily life in ancient Egypt belonging to nobles): the Mastaba of Princess Idut and the Mastaba of Prince Ty. Continue to visit the beautiful <strong>Imhotep Museum</strong>, which exhibits wonderful antiquities discovered in Saqqara. We will visit a <strong>Handmade Carpet School/Workshop</strong> in the village of Saqqara, an ancient, traditional craft in the region.</p>

<p><strong>Stop for Lunch</strong> (lunch is not included in this tour).</p>

<p>We will continue to the <strong>Dahshur Archaeological Site</strong>, a place of fundamental importance and serene atmosphere, where Pharaonic architecture took its decisive step towards perfection. This visit is an immersion behind the scenes of the Great Era of the Pyramids. It was in Dahshur that the visionary Pharaoh Snefru, father of Khufu, sponsored the audacious experiments that would culminate in the classical pyramid form.</p>

<p>Our first stop will be to admire the fascinating <strong>Bent Pyramid</strong>. Its unique profile, which changes inclination smoothly, is a rare testament to real-time engineering adjustment. The ancient builders, perceiving a risk of instability, simply recalculated the angle to ensure the structure's solidity, accidentally creating one of Egypt's most distinct and well-preserved pyramids.</p>

<p>Next, we will come face to face with the magnificent <strong>Red Pyramid</strong>. Named for the color of its limestone blocks, this is the crowning achievement of Snefru's effort: the world's first truly successful smooth-sided pyramid. Its perfect and imposing lines established the architectural standard that would be consecrated at Giza.</p>

<p>The adventure reaches its peak when we enter the interior of the Red Pyramid. We will descend through an ancestral corridor to its burial chambers, a profound and authentic experience that few sites offer, allowing a unique connection with this landmark of human history.</p>

<p>After exploring this crucial chapter of Egyptian civilization, we will return to the hotel in Cairo. (End of Tour).</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
</ul>

<h3>Pricing per Person (USD):</h3>
<ul>
<li><strong>1 Person (Solo):</strong> $187</li>
<li><strong>2 People:</strong> $122 per person</li>
<li><strong>3-4 People:</strong> $110 per person</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water – walking on the plateau and visiting the museum require good hydration.</li>
<li><strong>Lunch:</strong> Not included. You may ask your guide for a lunch stop during the tour or purchase something on route.</li>
<li><strong>Extra tickets:</strong> To enter the interior of the Step Pyramid of Saqqara, or any specific Mastaba (such as Mastaba of Mereruka) you must purchase an additional ticket on site (subject to availability).</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible.</li>
<li>The agency needs at least 24 hours prior to the tour date to process the booking.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>El Tour Saqqara con Menfis y Dahshur es un tour de 8 a 9 horas con visitas al Museo Abierto de Menfis y al Coloso Yacente del Rey Ramsés II, con visita a Saqqara incluyendo la Pirámide Escalonada y dos de las Mastabas (tumbas decoradas con escenas de la vida cotidiana del antiguo Egipto que pertenecen a los nobles: Mastaba de la Princesa Idut y la Mastaba del Príncipe Ty). Visita al bello Museo de Imhotep.</p>

<p>Nuestro guía egiptólogo egipcio que habla español, se encontrará con usted en su hotel. Salida con destino al <strong>Museo Abierto de Menfis</strong>, un museo al aire libre que exhibe las antigüedades descubiertas en el mismo lugar de la antigua capital Menfis, donde actualmente se encuentra la villa local Mit Rahina, a 35 km al sur de El Cairo. Usted admirará antigüedades que pertenecen a diferentes épocas de la historia del antiguo Egipto, especialmente el impresionante <strong>Coloso Yacente del Rey Ramsés II</strong> con 60 toneladas de peso y más de 10 metros de longitud que, a pesar del paso del tiempo, los detalles de la estatua aún son visibles, una prueba de la habilidad de los antiguos artesanos egipcios. Veremos allí también otros colosos y estatuas que representan al rey Ramsés II y piezas que formaban parte del templo de Ptah en Menfis, como la <strong>Estatua de la Tríada de Menfis</strong> (Ptah, Sekhmet y Nefertum). Además, en este museo abierto se encuentra la <strong>Esfinge de Alabastro</strong>, una obra increíble, esculpida en una sola pieza de alabastro.</p>

<p>Continuamos para visitar <strong>Saqqara</strong>, que está a 7 km de distancia del Museo Abierto de Menfis, uno de los sitios arqueológicos más fascinantes de Egipto que fue el cementerio principal de la antigua capital Menfis. Comenzamos con el magnífico <strong>Complejo del rey Zoser</strong>, el primer grupo de edificios construido enteramente en piedra en la historia de la humanidad y en el centro de este complejo se encuentra la <strong>Pirámide Escalonada</strong>, conocida también como la Pirámide de Saqqara, construida por el genio arquitecto Imhotep para el rey Zoser como una pirámide de escalones, con 60 m de altura, y consistía en 6 escalones, cada uno construido sobre el otro. Visitaremos el <strong>Patio del Heb Sed</strong>, representación del mismo patio que un día estaba en la capital Menfis, en el que se celebraba el Festival Trinitario Heb-Sed en expresión de la "renovación de las fuerzas y de la abundancia del rey de Egipto". Prosiguiendo para visitar la <strong>Pirámide del rey Unas</strong>, último rey de la dinastía VI. Visitaremos el interior de la pirámide famosa por los textos de jeroglíficos conocidos como los <strong>Textos de las Pirámides</strong>. Después vamos a visitar dos de las <strong>Mastabas</strong> (tumbas decoradas con escenas de la vida cotidiana del antiguo Egipto que pertenecen a los nobles): la Mastaba de la Princesa Idut y la Mastaba del Príncipe Ty. Continuación para visitar el bello <strong>Museo de Imhotep</strong> donde se exhiben maravillosas antigüedades descubiertas en Saqqara. Visitaremos una <strong>Escuela / Taller de Alfombras Hechas a Mano</strong> en la villa de Saqqara, una artesanía milenaria, tradicional en la región.</p>

<p><strong>Parada para el Almuerzo</strong> (el almuerzo no está incluido en este tour).</p>

<p>Seguimos con destino al <strong>yacimiento arqueológico de Dahshur</strong>, un lugar de importancia fundamental y atmósfera serena, donde la arquitectura faraónica dio su paso decisivo hacia la perfección. Esta visita es una inmersión en los bastidores de la Gran Era de las Pirámides. Fue en Dahshur donde el visionario Faraón Snefru, padre de Keops, patrocinó los audaces experimentos que culminarían en la forma piramidal clásica.</p>

<p>Nuestra primera parada será para admirar la fascinante <strong>Pirámide Acodada</strong>. Su perfil único, que cambia de inclinación suavemente, es un testimonio raro de un ajuste de ingeniería en tiempo real. Los antiguos constructores, percibiendo un riesgo de inestabilidad, simplemente recalcularon el ángulo para garantizar la solidez de la estructura, creando accidentalmente una de las pirámides más distintivas y bien conservadas de Egipto.</p>

<p>A continuación, nos encontraremos frente a frente con la magnífica <strong>Pirámide Roja</strong>. Bautizada por el color de sus bloques de caliza, esta es la coronación del esfuerzo de Snefru: la primera pirámide de caras lisas y verdaderamente exitosa del mundo. Sus líneas perfectas e imponentes establecieron el estándar arquitectónico que sería consagrado en Giza.</p>

<p>La aventura alcanza su clímax cuando accedemos al interior de la Pirámide Roja. Descenderemos por un corredor ancestral hasta sus cámaras funerarias, una experiencia profunda y auténtica que pocos lugares ofrecen, permitiendo una conexión única con este hito de la historia humana.</p>

<p>Tras explorar este capítulo crucial de la civilización egipcia, regresaremos al hotel en El Cairo. (Fin del Tour).</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
</ul>

<h3>Precios por persona (USD):</h3>
<ul>
<li><strong>1 Persona (Solo):</strong> $187</li>
<li><strong>2 Personas:</strong> $122 por persona</li>
<li><strong>3-4 Personas:</strong> $110 por persona</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a través de un enlace seguro y personalizado. Rápido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua – caminar por la meseta y visitar el museo requiere una buena hidratación.</li>
<li><strong>Almuerzo:</strong> No está incluido. Puede pedir una parada para almorzar a su guía durante el paseo.</li>
<li><strong>Boletos adicionales:</strong> Para entrar al interior de la Pirámide Escalonada, o para visitar una mastaba específica en Saqqara (ejemplo: Mastaba de Mereruka) es necesario adquirir un boleto adicional en el lugar.</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías.</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelación posible.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>O Passeio Sacará com Mênfis e Dahshur é um passeio de 8 a 9 horas com visitas ao Museu Aberto de Mênfis e ao Colosso Deitado do Rei Ramsés II, com visita a Sacará incluindo a Pirâmide Escalonada e duas das Mastabas (tumbas decoradas com cenas da vida cotidiana do antigo Egito que pertencem aos nobres: Mastaba da Princesa Idut e a Mastaba do Príncipe Ti). Visita ao belo Museu de Imhotep.</p>

<p>O nosso guia egiptólogo egípcio que fala português, irá encontrar-se consigo no seu hotel. Saída com destino ao <strong>Museu Aberto de Mênfis</strong>, um museu a céu aberto que exibe as antiguidades descobertas no mesmo local da antiga capital Mênfis, onde atualmente se encontra a vila local Mit Rahina, situada a 35 km ao sul do Cairo. Você irá contemplar antiguidades que pertencem a diferentes períodos da história egípcia antiga, especialmente o impressionante <strong>Colosso Deitado do Rei Ramsés II</strong> com 60 toneladas de peso e mais de 10 metros de comprimento que, apesar da passagem do tempo, os detalhes da estátua ainda são visíveis, uma prova da perícia dos antigos artesãos egípcios. Veremos ali também outros colossos e estátuas que representam igualmente o rei Ramsés II e peças que faziam parte do templo de Ptá em Mênfis, como a <strong>Estátua da Tríade de Mênfis</strong> (Ptá, Sekhmet e Nefertum). Ademais, encontra-se neste museu aberto a <strong>Esfinge de Alabastro</strong>, uma obra incrível, esculpida em um único bloco de alabastro.</p>

<p>Seguimos para visitar <strong>Sacará</strong>, que está a 7 km de distância do Museu Aberto de Mênfis, um dos sítios arqueológicos mais fascinantes do Egito que foi o cemitério principal da antiga capital Mênfis. Começamos com o magnífico <strong>Complexo do rei Djser</strong>, o primeiro conjunto de edifícios construído inteiramente em pedra na história da humanidade e, no centro deste complexo, encontra-se a <strong>Pirâmide Escalonada</strong>, conhecida também como a Pirâmide de Sacará, erguida pelo genial arquiteto Imhotep para o rei Djser como uma pirâmide de degraus, com 60 m de altura, e consistia em 6 degraus, cada um construído sobre o outro. Visitaremos o <strong>Pátio do Heb Sed</strong>, representação do mesmo pátio que outrora estava na capital Mênfis, no qual se celebrava o Festival Trinitário Heb-Sed em expressão da "renovação das forças e da abundância do rei do Egito". Prosseguimento para visitar a <strong>Pirâmide do rei Unas</strong>, último rei da VI dinastia. Adentraremos o interior da pirâmide, famosa pelos textos hieroglíficos conhecidos como <strong>Textos das Pirâmides</strong>. Depois, iremos visitar duas das <strong>Mastabas</strong> (tumbas adornadas com cenas da vida cotidiana do antigo Egito que pertencem aos nobres): a Mastaba da Princesa Idut e a Mastaba do Príncipe Ti. Continuação para visitar o belo <strong>Museu de Imhotep</strong>, onde se exibem maravilhosas antiguidades descobertas em Sacará. Iremos visitar uma <strong>Escola / Oficina de Tapetes Feitos à Mão</strong> na vila de Sacará, um artesanato milenar, tradicional na região.</p>

<p><strong>Parada para Almoço</strong> (almoço não incluso).</p>

<p>Continuação com destino ao <strong>sítio arqueológico de Dahshur</strong>, um local de importância fundamental e atmosfera serena, onde a arquitetura faraônica deu seu passo decisivo em direção à perfeição. Esta visita é uma imersão nos bastidores da Grande Era das Pirâmides. Foi em Dahshur que o visionário Faraó Snefru, pai de Quéops, patrocinou os experimentos audaciosos que culminariam na forma piramidal clássica.</p>

<p>Nossa primeira parada será para admirar a fascinante <strong>Pirâmide Curvada</strong>. Seu perfil único, que muda de inclinação suavemente, é um testemunho raro de um ajuste de engenharia em tempo real. Os antigos construtores, percebendo um risco de instabilidade, simplesmente recalcularam o ângulo para garantir a solidez da estrutura, criando acidentalmente uma das pirâmides mais distintas e bem preservadas do Egito.</p>

<p>Em seguida, nos encontraremos frente a frente com a magnífica <strong>Pirâmide Vermelha</strong>. Batizada pela cor de seus blocos de calcário, esta é a coroação do esforço de Snefru: a primeira pirâmide de faces lisas e verdadeiramente bem-sucedida do mundo. Suas linhas perfeitas e imponentes estabeleceram o padrão arquitetônico que seria consagrado em Gizé.</p>

<p>A aventura atinge seu ápice quando adentramos o interior da Pirâmide Vermelha. Desceremos por um corredor ancestral até suas câmaras funerárias, uma experiência profunda e autêntica que poucos locais oferecem, permitindo uma conexão ímpar com este marco da história humana.</p>

<p>Após explorar este capítulo crucial da civilização egípcia, retornaremos ao hotel no Cairo. (Fim do Tour).</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
</ul>

<h3>Valores por pessoa (USD):</h3>
<ul>
<li><strong>1 Pessoa (Individual):</strong> $187</li>
<li><strong>2 Pessoas:</strong> $122 por pessoa</li>
<li><strong>3-4 Pessoas:</strong> $110 por pessoa</li>
</ul>

<h3>Condições de Pagamento:</h3>
<p>Efetue o pagamento com seu cartão Visa ou Mastercard através de um link seguro e personalizado. Processo rápido, confiável e descomplicado.</p>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente – a caminhada no planalto e a visita ao museu exigem boa hidratação.</li>
<li><strong>Almoço:</strong> Não está incluído. Pode pedir uma parada para almoçar ao guia durante o passeio.</li>
<li><strong>Ingressos extras:</strong> Para entrar no interior da Pirâmide Escalonada ou uma das mastabas específicas em Sacará (por exemplo Mastaba de Mereruka), é necessário adquirir um bilhete adicional no local (sujeito à disponibilidade).</li>
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
                'price': 110,
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
                'meta_title': 'Saqqara, Memphis & Dahshur Day Tour | Cairo',
                'meta_title_es': 'Tour Saqqara, Menfis y Dahshur | 1 Día Cairo',
                'meta_title_pt': 'Passeio Sacará, Mênfis e Dahshur | 1 Dia Cairo',
                'meta_description': '8-9 hour guided tour: Memphis Museum, Step Pyramid of Saqqara, Mastabas, Imhotep Museum & Dahshur Bent and Red Pyramids. Transfers included.',
                'meta_description_es': 'Tour guiado de 8-9 horas: Museo de Menfis, Pirámide Escalonada de Saqqara, Mastabas, Museo Imhotep y Pirámides de Dahshur. Traslados incluidos.',
                'meta_description_pt': 'Passeio guiado de 8-9 horas: Museu de Mênfis, Pirâmide Escalonada de Sacará, Mastabas, Museu Imhotep e Pirâmides de Dahshur. Traslados inclusos.',

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
                'description': 'Admire the Recumbent Colossus of Ramses II (60 tons), the Alabaster Sphinx, and the Memphis Triad statues at the ancient capital site.',
                'description_es': 'Admire el Coloso Yacente de Ramsés II (60 toneladas), la Esfinge de Alabastro y las estatuas de la Tríada de Menfis en el sitio de la antigua capital.',
                'description_pt': 'Admire o Colosso Deitado de Ramsés II (60 toneladas), a Esfinge de Alabastro e as estátuas da Tríade de Mênfis no local da antiga capital.',
                'icon': 'museum',
                'sort_order': 1,
            },
            {
                'title': 'Saqqara Step Pyramid & Mastabas',
                'title_es': 'Pirámide Escalonada y Mastabas de Saqqara',
                'title_pt': 'Pirâmide Escalonada e Mastabas de Sacará',
                'description': 'Visit the Step Pyramid of Zoser, the Heb-Sed Court, Pyramid Texts inside Unas Pyramid, Mastabas of Princess Idut and Prince Ty, and the Imhotep Museum.',
                'description_es': 'Visite la Pirámide Escalonada de Zoser, el Patio del Heb Sed, los Textos de las Pirámides dentro de la Pirámide de Unas, las Mastabas de la Princesa Idut y del Príncipe Ty, y el Museo de Imhotep.',
                'description_pt': 'Visite a Pirâmide Escalonada de Djser, o Pátio do Heb Sed, os Textos das Pirâmides na Pirâmide de Unas, as Mastabas da Princesa Idut e do Príncipe Ti, e o Museu de Imhotep.',
                'icon': 'pyramid',
                'sort_order': 2,
            },
            {
                'title': 'Dahshur: Bent & Red Pyramids',
                'title_es': 'Dahshur: Pirámides Acodada y Roja',
                'title_pt': 'Dahshur: Pirâmides Curvada e Vermelha',
                'description': 'Explore the revolutionary Bent Pyramid and enter the Red Pyramid, the world\'s first successful smooth-sided pyramid built by Pharaoh Snefru.',
                'description_es': 'Explore la revolucionaria Pirámide Acodada y entre en la Pirámide Roja, la primera pirámide de caras lisas exitosa del mundo, construida por el Faraón Snefru.',
                'description_pt': 'Explore a revolucionária Pirâmide Curvada e entre na Pirâmide Vermelha, a primeira pirâmide de faces lisas bem-sucedida do mundo, construída pelo Faraó Snefru.',
                'icon': 'pyramid',
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
            title='Saqqara, Memphis & Dahshur Full Day',
            title_es='Saqqara, Menfis y Dahshur Día Completo',
            title_pt='Sacará, Mênfis e Dahshur Dia Completo',
            description='''<p><strong>08:00</strong> – Hotel pick-up in Cairo</p>
<p><strong>08:45</strong> – Memphis Open-Air Museum (1.5 hours)</p>
<ul>
<li>Recumbent Colossus of King Ramses II (60 tons)</li>
<li>Alabaster Sphinx</li>
<li>Memphis Triad statues (Ptah, Sekhmet, Nefertum)</li>
</ul>
<p><strong>10:30</strong> – Saqqara Archaeological Site (3 hours)</p>
<ul>
<li>Complex of King Zoser – first stone buildings in history</li>
<li>Step Pyramid of Saqqara (60 m, 6 steps)</li>
<li>Heb-Sed Court</li>
<li>Pyramid of King Unas – interior with Pyramid Texts</li>
<li>Mastaba of Princess Idut</li>
<li>Mastaba of Prince Ty</li>
<li>Imhotep Museum</li>
<li>Handmade Carpet School/Workshop</li>
</ul>
<p><strong>13:30</strong> – Free time for lunch (not included)</p>
<p><strong>14:30</strong> – Dahshur Archaeological Site (2 hours)</p>
<ul>
<li>Bent Pyramid – unique changing-angle profile</li>
<li>Red Pyramid – world's first smooth-sided pyramid</li>
<li>Enter the interior of the Red Pyramid – burial chambers</li>
</ul>
<p><strong>17:00</strong> – Return to hotel in Cairo</p>''',

            description_es='''<p><strong>08:00</strong> – Recogida en el hotel de El Cairo</p>
<p><strong>08:45</strong> – Museo Abierto de Menfis (1.5 horas)</p>
<ul>
<li>Coloso Yacente del Rey Ramsés II (60 toneladas)</li>
<li>Esfinge de Alabastro</li>
<li>Estatuas de la Tríada de Menfis (Ptah, Sekhmet, Nefertum)</li>
</ul>
<p><strong>10:30</strong> – Sitio Arqueológico de Saqqara (3 horas)</p>
<ul>
<li>Complejo del Rey Zoser – primeros edificios de piedra de la historia</li>
<li>Pirámide Escalonada de Saqqara (60 m, 6 escalones)</li>
<li>Patio del Heb Sed</li>
<li>Pirámide del Rey Unas – interior con Textos de las Pirámides</li>
<li>Mastaba de la Princesa Idut</li>
<li>Mastaba del Príncipe Ty</li>
<li>Museo de Imhotep</li>
<li>Escuela / Taller de Alfombras Hechas a Mano</li>
</ul>
<p><strong>13:30</strong> – Tiempo libre para almuerzo (no incluido)</p>
<p><strong>14:30</strong> – Yacimiento Arqueológico de Dahshur (2 horas)</p>
<ul>
<li>Pirámide Acodada – perfil único de ángulo cambiante</li>
<li>Pirámide Roja – primera pirámide de caras lisas del mundo</li>
<li>Acceso al interior de la Pirámide Roja – cámaras funerarias</li>
</ul>
<p><strong>17:00</strong> – Regreso al hotel en El Cairo</p>''',

            description_pt='''<p><strong>08:00</strong> – Retirada no hotel no Cairo</p>
<p><strong>08:45</strong> – Museu Aberto de Mênfis (1,5 horas)</p>
<ul>
<li>Colosso Deitado do Rei Ramsés II (60 toneladas)</li>
<li>Esfinge de Alabastro</li>
<li>Estátuas da Tríade de Mênfis (Ptá, Sekhmet, Nefertum)</li>
</ul>
<p><strong>10:30</strong> – Sítio Arqueológico de Sacará (3 horas)</p>
<ul>
<li>Complexo do Rei Djser – primeiros edifícios de pedra da história</li>
<li>Pirâmide Escalonada de Sacará (60 m, 6 degraus)</li>
<li>Pátio do Heb Sed</li>
<li>Pirâmide do Rei Unas – interior com Textos das Pirâmides</li>
<li>Mastaba da Princesa Idut</li>
<li>Mastaba do Príncipe Ti</li>
<li>Museu de Imhotep</li>
<li>Escola / Oficina de Tapetes Feitos à Mão</li>
</ul>
<p><strong>13:30</strong> – Tempo livre para almoço (não incluso)</p>
<p><strong>14:30</strong> – Sítio Arqueológico de Dahshur (2 horas)</p>
<ul>
<li>Pirâmide Curvada – perfil único com mudança de ângulo</li>
<li>Pirâmide Vermelha – primeira pirâmide de faces lisas do mundo</li>
<li>Acesso ao interior da Pirâmide Vermelha – câmaras funerárias</li>
</ul>
<p><strong>17:00</strong> – Retorno ao hotel no Cairo</p>''',

            locations='Memphis, Saqqara, Dahshur',
            locations_es='Menfis, Saqqara, Dahshur',
            locations_pt='Mênfis, Sacará, Dahshur',
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
                'item': 'Entrance tickets to historical sites and museums in Memphis, Saqqara, and Dahshur according to the itinerary',
                'item_es': 'Entradas a los lugares históricos y museos en Menfis, Saqqara y Dahshur según el itinerario',
                'item_pt': 'Ingressos dos lugares históricos e museus em Mênfis, Sacará e Dahshur conforme o roteiro',
            },
            {
                'item': 'English-speaking Egyptologist guide',
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
                'item_es': '1 botella de agua mineral por persona durante el paseo',
                'item_pt': '1 garrafa de água mineral por pessoa durante o passeio',
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
                'item': 'Lunch or meals and any non-included services',
                'item_es': 'Almuerzo o comidas y cualquier servicio extra',
                'item_pt': 'Almoço ou refeições',
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
                'question': 'Can I enter the interior of the Step Pyramid of Saqqara?',
                'question_es': '¿Puedo entrar al interior de la Pirámide Escalonada de Saqqara?',
                'question_pt': 'Posso entrar no interior da Pirâmide Escalonada de Sacará?',
                'answer': '<p>Entrance to the interior of the Step Pyramid is not included in the tour. You must purchase an additional ticket on site, subject to availability from the Ministry of Tourism. The number of tickets is limited daily.</p>',
                'answer_es': '<p>La entrada al interior de la Pirámide Escalonada no está incluida en el tour. Es necesario adquirir un boleto adicional en el lugar, sujeto a disponibilidad del Ministerio de Turismo. El número de boletos es limitado diariamente.</p>',
                'answer_pt': '<p>O acesso ao interior da Pirâmide Escalonada não está incluso no passeio. É necessário adquirir um bilhete adicional no local, sujeito à disponibilidade do Ministério do Turismo. O número de ingressos é limitado diariamente.</p>',
                'sort_order': 1,
            },
            {
                'question': 'Is lunch included in this tour?',
                'question_es': '¿El almuerzo está incluido en este tour?',
                'question_pt': 'O almoço está incluído neste passeio?',
                'answer': '<p>No, lunch is not included. There is a free time stop where you can eat at nearby local restaurants, or you may ask your guide for a lunch stop during the tour.</p>',
                'answer_es': '<p>No, el almuerzo no está incluido. Hay una parada de tiempo libre donde puede comer en restaurantes locales cercanos, o puede pedir una parada para almorzar a su guía durante el paseo.</p>',
                'answer_pt': '<p>Não, o almoço não está incluído. Há uma parada de tempo livre onde pode comer em restaurantes locais próximos, ou pode pedir uma parada para almoçar ao guia durante o passeio.</p>',
                'sort_order': 2,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': '¿Qué debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen for the morning at the archaeological sites. Comfortable walking shoes are essential as you will be walking on uneven terrain.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar para la mañana en los sitios arqueológicos. El calzado cómodo para caminar es esencial ya que caminará por terreno irregular.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapéu, óculos de sol e protetor solar para a manhã nos sítios arqueológicos. Calçado confortável para caminhar é essencial pois haverá terreno irregular.</p>',
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
                'question': 'Can I enter the Red Pyramid at Dahshur?',
                'question_es': '¿Puedo entrar en la Pirámide Roja de Dahshur?',
                'question_pt': 'Posso entrar na Pirâmide Vermelha de Dahshur?',
                'answer': '<p>Yes! Entering the interior of the Red Pyramid is included in this tour. You will descend through an ancestral corridor to its burial chambers, a profound and authentic experience that few sites offer.</p>',
                'answer_es': '<p>¡Sí! El acceso al interior de la Pirámide Roja está incluido en este tour. Descenderá por un corredor ancestral hasta sus cámaras funerarias, una experiencia profunda y auténtica que pocos lugares ofrecen.</p>',
                'answer_pt': '<p>Sim! O acesso ao interior da Pirâmide Vermelha está incluso neste passeio. Você descerá por um corredor ancestral até suas câmaras funerárias, uma experiência profunda e autêntica que poucos locais oferecem.</p>',
                'sort_order': 5,
            },
            {
                'question': 'Is photography allowed?',
                'question_es': '¿Se permite la fotografía?',
                'question_pt': 'A fotografia é permitida?',
                'answer': '<p>Photography is permitted in most areas. However, flash photography is not allowed in some museum galleries and inside the pyramids. Please follow security guidelines at each location.</p>',
                'answer_es': '<p>La fotografía está permitida en la mayoría de las áreas. Sin embargo, no se permite el uso de flash en algunas galerías del museo ni dentro de las pirámides. Por favor, siga las indicaciones de seguridad en cada ubicación.</p>',
                'answer_pt': '<p>A fotografia é permitida na maioria das áreas. No entanto, não é permitido o uso de flash em algumas galerias do museu nem dentro das pirâmides. Por favor, siga as orientações de segurança em cada local.</p>',
                'sort_order': 6,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day'
            f'\n  - Price: ${tour.price} (3-4 pax) | Solo: $187 | 2 pax: $122'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
