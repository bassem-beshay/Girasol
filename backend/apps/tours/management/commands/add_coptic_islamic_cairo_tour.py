"""
Management command to add "Coptic & Islamic Cairo Tour with Khan El Khalili" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Coptic & Islamic Cairo Tour with Khan El Khalili 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Coptic & Islamic Cairo Tour with Khan El Khalili day tour...')

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
            slug='coptic-islamic-cairo-khan-el-khalili-tour',
            defaults={
                'name': 'Cairo Coptic & Islamic Cairo Tour with Khan El Khalili',
                'name_es': 'Tour Cairo Copto e Islámico con Bazar Khan El Khalili',
                'name_pt': 'Passeio pelo Cairo Copta e Islâmico com Bazar Khan El Khalili',

                'short_description': (
                    'A full-day journey through Cairo\'s spiritual and cultural heart: '
                    'explore the historic Coptic Quarter with its ancient churches, '
                    'the majestic Saladin Citadel and Alabaster Mosque, and finish '
                    'with a vibrant shopping experience at the legendary Khan El Khalili '
                    'Bazaar. Expert guide, entrance tickets, and transfers included!'
                ),
                'short_description_es': (
                    'Una jornada completa por el corazón espiritual y cultural de El Cairo: '
                    'explora el histórico Barrio Copto con sus iglesias milenarias, '
                    'la majestuosa Ciudadela de Saladino y la Mezquita de Alabastro, '
                    'y finaliza con una vibrante experiencia de compras en el legendario '
                    'Bazar Khan El Khalili. ¡Guía experto, entradas y traslados incluidos!'
                ),
                'short_description_pt': (
                    'Uma jornada completa pelo coração espiritual e cultural do Cairo: '
                    'explore o histórico Bairro Copta com suas igrejas milenares, '
                    'a majestosa Cidadela de Saladino e a Mesquita de Alabastro, '
                    'e finalize com uma vibrante experiência de compras no lendário '
                    'Bazar Khan El Khalili. Guia especializado, ingressos e traslados inclusos!'
                ),

                'description': '''<p>The Cairo Coptic & Islamic Cairo Tour with Khan El Khalili is a comprehensive day tour that takes you through the sacred and historic heart of Cairo, from the ancient Christian Coptic Quarter to the medieval Islamic district and the vibrant Khan El Khalili Bazaar.</p>

<p>Your English-speaking local guide will meet you at your Cairo hotel. We begin with the <strong>Christian Coptic Quarter</strong>, located in the southern part of Cairo in Misr Al Qadima (Old Cairo), where Egypt's historic churches are found.</p>

<p>Visit the <strong>Hanging Church</strong> (Church of the Virgin), built in the 3rd century upon the ruins of two towers of an ancient fortress known as Babylon Fortress. Consecrated to the Virgin Mary and St. Damiana, this basilica-shaped church has 3 sanctuaries and 3 naves and contains a fantastic collection of ancient icons dating from the 5th century.</p>

<p>Continue to the <strong>Church of St. Sergius</strong> (Abu Serga), built over the Grotto of the Holy Family, dating from the 6th century and consecrated to the Martyr Sergius.</p>

<p>Proceed through the alleys of the Coptic Quarter to visit the <strong>Church of St. Barbara</strong>, built in the 5th century and consecrated to the Martyr Barbara and her friend the Martyr St. Juliana. A basilica-shaped church with 3 sanctuaries on the eastern side, containing a chapel housing relics of St. Barbara and other local saints.</p>

<p>Continue to the <strong>Saladin Citadel</strong>, in the ancient district of Al-Qala'a, built on the Muqattam Mountain by Sultan Saladin in the 12th century to defend Cairo against Crusader attacks. From 1207, the castle served as the administrative seat of the Egyptian government until the 19th century. Visit the <strong>Mosque of Mohamed Ali</strong>, known as the Alabaster Mosque, in Ottoman style.</p>

<p>Afterwards, enjoy 1.5 to 2 hours at the <strong>Khan El Khalili Bazaar Market</strong>, one of the oldest and most famous markets in the Middle East. Return to your hotel.</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
</ul>

<h3>Pricing per Person (USD):</h3>
<ul>
<li><strong>1 Person (Solo):</strong> $164</li>
<li><strong>2 People:</strong> $97 per person</li>
<li><strong>3-4 People:</strong> $90 per person</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water – walking through the historical streets of Old Cairo, the Saladin Citadel, and Khan El Khalili requires good hydration.</li>
<li><strong>Lunch:</strong> Not included. You may ask your guide for a lunch stop during the tour.</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries (follow security guidelines).</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible.</li>
<li>The agency needs at least 24 hours prior to the tour date to process the booking.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>El Tour Cairo Copto e Islámico con Bazar Khan El Khalili es un recorrido completo de un día que lo lleva por el corazón sagrado e histórico de El Cairo, desde el antiguo Barrio Copto cristiano hasta el distrito islámico medieval y el vibrante Bazar Khan El Khalili.</p>

<p>Su guía local de habla inglesa se encontrará con usted en su hotel en El Cairo. Comenzaremos con el <strong>Barrio Copto Cristiano</strong>, ubicado en la parte sur de El Cairo en Misr Al Qadima (El Cairo Antiguo), donde se encuentran las iglesias históricas de Egipto.</p>

<p>Visita a la <strong>Iglesia Colgante</strong> (Iglesia de la Virgen), construida en el siglo III sobre las ruinas de dos torres de una antigua fortaleza conocida como Fortaleza de Babilonia. Consagrada a la Virgen María y Santa Damiana, esta iglesia en forma de basílica tiene 3 santuarios y 3 naves y contiene un fantástico conjunto de iconos antiguos desde el siglo V.</p>

<p>Continuación para visitar la <strong>Iglesia de San Sergio</strong> (Abu Serga), construida sobre la Gruta de la Sagrada Familia, datada del siglo VI y consagrada al Mártir Sergio.</p>

<p>Continuación por las callejuelas del Barrio Copto para visitar la <strong>Iglesia de Santa Bárbara</strong>, construida en el siglo V y consagrada a la Mártir Bárbara y su amiga la mártir Santa Juliana. Una iglesia en forma de basílica con 3 santuarios en el lado oriental, que contiene una capilla que alberga reliquias de Santa Bárbara y otros santos locales.</p>

<p>Continuación a la <strong>Ciudadela de Saladino</strong>, en el barrio antiguo de Al-Qala'a, construida sobre la montaña de Al-Muqattam por el Sultán Saladino en el siglo XII para defender El Cairo contra los ataques de los cruzados. El castillo fue convertido a partir de 1207 en la sede administrativa del gobierno de Egipto hasta el siglo XIX. Visitaremos la <strong>Mezquita de Mohamed Ali</strong>, conocida como la Mezquita de Alabastro, de estilo otomano.</p>

<p>Luego, disfrute de 1,5 a 2 horas en el <strong>Mercado Bazar Khan El Khalili</strong>, uno de los mercados más antiguos y famosos del Medio Oriente. Regreso a su hotel.</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
</ul>

<h3>Precios por persona (USD):</h3>
<ul>
<li><strong>1 Persona (Solo):</strong> $164</li>
<li><strong>2 Personas:</strong> $97 por persona</li>
<li><strong>3-4 Personas:</strong> $90 por persona</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a través de un enlace seguro y personalizado. Rápido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua – caminar por las calles históricas del Cairo Antiguo, la Ciudadela de Saladino y el Khan El Khalili requiere una buena hidratación.</li>
<li><strong>Almuerzo:</strong> No está incluido. Puede pedir una parada para almorzar a su guía durante el paseo.</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías (siga las indicaciones de seguridad).</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelación posible.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>O Passeio pelo Cairo Copta e Islâmico com Bazar Khan El Khalili é um roteiro completo de um dia que o leva pelo coração sagrado e histórico do Cairo, desde o antigo Bairro Copta cristão até o distrito islâmico medieval e o vibrante Bazar Khan El Khalili.</p>

<p>Seu guia local se encontrará com você no seu hotel no Cairo. Começaremos pelo <strong>Bairro Copta Cristão</strong>, localizado na parte sul do Cairo, em Misr Al Qadima (Cairo Antigo), onde se encontram as igrejas históricas do Egito.</p>

<p>Visita à <strong>Igreja Suspensa</strong> (Igreja da Virgem), construída no século III sobre as ruínas de duas torres de uma antiga fortaleza conhecida como Fortaleza da Babilónia. Consagrada à Virgem Maria e a Santa Damiana, esta igreja em forma de basílica tem 3 santuários e 3 naves e contém um fantástico conjunto de ícones antigos desde o século V.</p>

<p>Continuação para visitar a <strong>Igreja de São Sérgio</strong> (Abu Serga), construída sobre a Gruta da Sagrada Família, datada do século VI e consagrada ao Mártir Sérgio.</p>

<p>Continuação pelas vielas do Bairro Copta para visitar a <strong>Igreja de Santa Bárbara</strong>, construída no século V e consagrada à Mártir Bárbara e à sua amiga, a mártir Santa Juliana. Uma igreja em forma de basílica com 3 santuários no lado oriental, contendo uma capela que abriga relíquias de Santa Bárbara e outros santos locais.</p>

<p>Continuação para a <strong>Cidadela de Saladino</strong>, no bairro antigo de Al-Qala'a, construída na montanha de Al-Muqattam pelo Sultão Saladino no século XII para defender o Cairo contra ataques dos cruzados. O castelo foi convertido a partir de 1207 na sede administrativa do governo do Egito até ao século XIX. Visitaremos a <strong>Mesquita de Mohamed Ali</strong>, conhecida como a Mesquita de Alabastro, de estilo otomano.</p>

<p>Em seguida, desfrute de 1,5 a 2 horas no <strong>Mercado Bazar Khan El Khalili</strong>, um dos mercados mais antigos e famosos do Médio Oriente. Regresso ao seu hotel.</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
</ul>

<h3>Valores por pessoa (USD):</h3>
<ul>
<li><strong>1 Pessoa (Individual):</strong> $164</li>
<li><strong>2 Pessoas:</strong> $97 por pessoa</li>
<li><strong>3-4 Pessoas:</strong> $90 por pessoa</li>
</ul>

<h3>Condições de Pagamento:</h3>
<p>Efetue o pagamento com seu cartão Visa ou Mastercard através de um link seguro e personalizado. Processo rápido, confiável e descomplicado.</p>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente – a caminhada pelas ruas históricas do Cairo Antigo, a Cidadela de Saladino e o Khan El Khalili exigem boa hidratação.</li>
<li><strong>Almoço:</strong> Não está incluído. Pode pedir uma parada para almoçar ao guia durante o passeio.</li>
<li><strong>Fotografia:</strong> Permitida na maioria das áreas, mas sem flash em algumas galerias (siga as orientações de segurança).</li>
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

                # SEO (meta_title max 70, meta_description max 160)
                'meta_title': 'Coptic & Islamic Cairo Tour with Khan El Khalili | 1 Day',
                'meta_title_es': 'Tour Cairo Copto e Islámico con Khan El Khalili | 1 Día',
                'meta_title_pt': 'Cairo Copta e Islâmico com Khan El Khalili | 1 Dia',
                'meta_description': 'Full-day guided tour: Coptic Quarter churches, Saladin Citadel, Alabaster Mosque & Khan El Khalili Bazaar. Transfers included.',
                'meta_description_es': 'Tour guiado de día completo: iglesias del Barrio Copto, Ciudadela de Saladino, Mezquita de Alabastro y Bazar Khan El Khalili. Traslados incluidos.',
                'meta_description_pt': 'Passeio guiado de dia inteiro: igrejas do Bairro Copta, Cidadela de Saladino, Mesquita de Alabastro e Bazar Khan El Khalili. Traslados inclusos.',

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
                'title': 'Coptic Quarter & Historic Churches',
                'title_es': 'Barrio Copto e Iglesias Históricas',
                'title_pt': 'Bairro Copta e Igrejas Históricas',
                'description': 'Visit the Hanging Church, Church of St. Sergius (over the Holy Family Grotto), and Church of St. Barbara with its relics chapel in Old Cairo.',
                'description_es': 'Visita la Iglesia Colgante, la Iglesia de San Sergio (sobre la Gruta de la Sagrada Familia) y la Iglesia de Santa Bárbara con su capilla de reliquias en El Cairo Antiguo.',
                'description_pt': 'Visite a Igreja Suspensa, a Igreja de São Sérgio (sobre a Gruta da Sagrada Família) e a Igreja de Santa Bárbara com sua capela de relíquias no Cairo Antigo.',
                'icon': 'church',
                'sort_order': 1,
            },
            {
                'title': 'Saladin Citadel & Alabaster Mosque',
                'title_es': 'Ciudadela de Saladino y Mezquita de Alabastro',
                'title_pt': 'Cidadela de Saladino e Mesquita de Alabastro',
                'description': 'Explore the 12th-century Citadel built by Sultan Saladin on Muqattam Mountain, and the Ottoman-style Mosque of Mohamed Ali (Alabaster Mosque).',
                'description_es': 'Explora la Ciudadela del siglo XII construida por el Sultán Saladino en la montaña de Muqattam, y la Mezquita de Mohamed Ali (Mezquita de Alabastro) de estilo otomano.',
                'description_pt': 'Explore a Cidadela do século XII construída pelo Sultão Saladino na montanha de Muqattam, e a Mesquita de Mohamed Ali (Mesquita de Alabastro) de estilo otomano.',
                'icon': 'mosque',
                'sort_order': 2,
            },
            {
                'title': 'Khan El Khalili Bazaar & Transfers',
                'title_es': 'Bazar Khan El Khalili y Traslados',
                'title_pt': 'Bazar Khan El Khalili e Traslados',
                'description': 'Enjoy 1.5 to 2 hours browsing one of the oldest and most famous markets in the Middle East, with air-conditioned transfers from and to your Cairo hotel.',
                'description_es': 'Disfrute de 1,5 a 2 horas recorriendo uno de los mercados más antiguos y famosos del Medio Oriente, con traslados con aire acondicionado desde y hacia su hotel en El Cairo.',
                'description_pt': 'Desfrute de 1,5 a 2 horas percorrendo um dos mercados mais antigos e famosos do Médio Oriente, com traslados com ar-condicionado de e para seu hotel no Cairo.',
                'icon': 'market',
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
            title='Coptic Cairo, Saladin Citadel & Khan El Khalili',
            title_es='Cairo Copto, Ciudadela de Saladino y Khan El Khalili',
            title_pt='Cairo Copta, Cidadela de Saladino e Khan El Khalili',
            description='''<p><strong>Morning</strong> – Hotel pick-up in Cairo</p>
<p><strong>Coptic Quarter</strong> – Old Cairo (Misr Al Qadima)</p>
<ul>
<li>Hanging Church (Church of the Virgin) – 3rd century basilica with ancient icons</li>
<li>Church of St. Sergius (Abu Serga) – built over the Holy Family Grotto</li>
<li>Church of St. Barbara – 5th century basilica with relics chapel</li>
</ul>
<p><strong>Saladin Citadel</strong> – Al-Qala'a district</p>
<ul>
<li>Citadel of Saladin – 12th century fortress on Muqattam Mountain</li>
<li>Mosque of Mohamed Ali (Alabaster Mosque) – Ottoman-style mosque</li>
</ul>
<p><strong>Khan El Khalili Bazaar</strong> – 1.5 to 2 hours of free time for shopping and exploration</p>
<p><strong>End of Tour</strong> – Return to your hotel in Cairo</p>''',

            description_es='''<p><strong>Mañana</strong> – Recogida en el hotel de El Cairo</p>
<p><strong>Barrio Copto</strong> – El Cairo Antiguo (Misr Al Qadima)</p>
<ul>
<li>Iglesia Colgante (Iglesia de la Virgen) – basílica del siglo III con iconos antiguos</li>
<li>Iglesia de San Sergio (Abu Serga) – construida sobre la Gruta de la Sagrada Familia</li>
<li>Iglesia de Santa Bárbara – basílica del siglo V con capilla de reliquias</li>
</ul>
<p><strong>Ciudadela de Saladino</strong> – barrio de Al-Qala'a</p>
<ul>
<li>Ciudadela de Saladino – fortaleza del siglo XII en la montaña de Muqattam</li>
<li>Mezquita de Mohamed Ali (Mezquita de Alabastro) – mezquita de estilo otomano</li>
</ul>
<p><strong>Bazar Khan El Khalili</strong> – 1,5 a 2 horas de tiempo libre para compras y exploración</p>
<p><strong>Fin del Tour</strong> – Regreso a su hotel en El Cairo</p>''',

            description_pt='''<p><strong>Manhã</strong> – Retirada no hotel no Cairo</p>
<p><strong>Bairro Copta</strong> – Cairo Antigo (Misr Al Qadima)</p>
<ul>
<li>Igreja Suspensa (Igreja da Virgem) – basílica do século III com ícones antigos</li>
<li>Igreja de São Sérgio (Abu Serga) – construída sobre a Gruta da Sagrada Família</li>
<li>Igreja de Santa Bárbara – basílica do século V com capela de relíquias</li>
</ul>
<p><strong>Cidadela de Saladino</strong> – bairro de Al-Qala'a</p>
<ul>
<li>Cidadela de Saladino – fortaleza do século XII na montanha de Muqattam</li>
<li>Mesquita de Mohamed Ali (Mesquita de Alabastro) – mesquita de estilo otomano</li>
</ul>
<p><strong>Bazar Khan El Khalili</strong> – 1,5 a 2 horas de tempo livre para compras e exploração</p>
<p><strong>Fim do Passeio</strong> – Regresso ao seu hotel no Cairo</p>''',

            locations='Old Cairo, Saladin Citadel, Khan El Khalili',
            locations_es='El Cairo Antiguo, Ciudadela de Saladino, Khan El Khalili',
            locations_pt='Cairo Antigo, Cidadela de Saladino, Khan El Khalili',
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
                'item_pt': 'Transfer em carro/van moderno com ar-condicionado',
            },
            {
                'item': 'General entrance tickets to all sites described in the itinerary',
                'item_es': 'Entradas generales a todos los lugares descritos en el itinerario',
                'item_pt': 'Entradas gerais em todos os locais descritos no itinerário',
            },
            {
                'item': 'Expert Egyptologist guide',
                'item_es': 'Guía oficial egiptólogo',
                'item_pt': 'Guia oficial egiptólogo',
            },
            {
                'item': 'Service and operational assistance',
                'item_es': 'Servicio y asistencia técnica',
                'item_pt': 'Serviço e assistência técnica',
            },
            {
                'item': '1 bottle of mineral water per person during the tour',
                'item_es': '1 botella de agua mineral por persona durante los tours',
                'item_pt': '1 garrafa de água mineral por pessoa durante os passeios',
            },
            {
                'item': 'All tour fees and service charges',
                'item_es': 'Todas las tasas de tours y cargos por servicio',
                'item_pt': 'Todas as taxas de passeios e de serviço',
            },
        ]

        for i, inc in enumerate(included):
            TourInclusion.objects.create(
                tour=tour, is_included=True, sort_order=i + 1, **inc
            )

        # Excluded items
        excluded = [
            {
                'item': 'Lunch or any meals',
                'item_es': 'Almuerzo o comidas',
                'item_pt': 'Almoço ou qualquer refeição',
            },
            {
                'item': 'Tips, traditionally given to the guide and driver',
                'item_es': 'Propinas, tradicionalmente dadas al guía y al conductor',
                'item_pt': 'Gorjetas (para guia e motorista – facultativo, mas sugerido)',
            },
            {
                'item': 'Personal expenses and shopping',
                'item_es': 'Gastos personales y compras',
                'item_pt': 'Despesas pessoais e compras',
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
                'question': 'Is lunch included in this tour?',
                'question_es': '¿El almuerzo está incluido en este tour?',
                'question_pt': 'O almoço está incluído neste passeio?',
                'answer': '<p>No, lunch is not included. You may ask your guide for a lunch stop during the tour, or purchase food at local restaurants along the way or at the Khan El Khalili Bazaar.</p>',
                'answer_es': '<p>No, el almuerzo no está incluido. Puede pedir una parada para almorzar a su guía durante el paseo o comprar algo en restaurantes locales por el camino o en el Bazar Khan El Khalili.</p>',
                'answer_pt': '<p>Não, o almoço não está incluído. Pode pedir uma parada para almoçar ao guia durante o passeio ou adquirir algo em restaurantes locais pelo caminho ou no Bazar Khan El Khalili.</p>',
                'sort_order': 1,
            },
            {
                'question': 'What should I wear for visiting the churches and mosque?',
                'question_es': '¿Qué debo vestir para visitar las iglesias y la mezquita?',
                'question_pt': 'O que devo vestir para visitar as igrejas e a mesquita?',
                'answer': '<p>Wear light, modest clothing that covers shoulders and knees, especially for visiting the Alabaster Mosque. Women may need a headscarf for the mosque. Comfortable walking shoes are essential as the tour involves considerable walking through historic streets.</p>',
                'answer_es': '<p>Use ropa ligera y modesta que cubra hombros y rodillas, especialmente para visitar la Mezquita de Alabastro. Las mujeres pueden necesitar un pañuelo para la cabeza en la mezquita. El calzado cómodo para caminar es esencial ya que el tour implica caminar considerablemente por calles históricas.</p>',
                'answer_pt': '<p>Use roupas leves e modestas que cubram ombros e joelhos, especialmente para visitar a Mesquita de Alabastro. As mulheres podem precisar de um lenço para a cabeça na mesquita. Calçado confortável para caminhar é essencial pois o passeio envolve caminhada considerável por ruas históricas.</p>',
                'sort_order': 2,
            },
            {
                'question': 'How much time do we spend at Khan El Khalili?',
                'question_es': '¿Cuánto tiempo pasamos en Khan El Khalili?',
                'question_pt': 'Quanto tempo passamos no Khan El Khalili?',
                'answer': '<p>You will have approximately 1.5 to 2 hours of free time at Khan El Khalili Bazaar for shopping, exploring, and enjoying the atmosphere. Your guide can recommend the best stalls and help with bargaining.</p>',
                'answer_es': '<p>Tendrá aproximadamente 1,5 a 2 horas de tiempo libre en el Bazar Khan El Khalili para compras, exploración y disfrutar del ambiente. Su guía puede recomendar los mejores puestos y ayudar con el regateo.</p>',
                'answer_pt': '<p>Terá aproximadamente 1,5 a 2 horas de tempo livre no Bazar Khan El Khalili para compras, exploração e apreciar o ambiente. Seu guia pode recomendar as melhores bancas e ajudar na negociação.</p>',
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
                'answer': '<p>Photography is permitted in most areas. However, flash photography is not allowed in some church and mosque interiors. Please follow security guidelines at each location.</p>',
                'answer_es': '<p>La fotografía está permitida en la mayoría de las áreas. Sin embargo, no se permite el uso de flash en el interior de algunas iglesias y la mezquita. Por favor, siga las indicaciones de seguridad en cada ubicación.</p>',
                'answer_pt': '<p>A fotografia é permitida na maioria das áreas. No entanto, não é permitido o uso de flash no interior de algumas igrejas e da mesquita. Por favor, siga as orientações de segurança em cada local.</p>',
                'sort_order': 5,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day'
            f'\n  - Price: ${tour.price} (3-4 pax) | Solo: $164 | 2 pax: $97'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
