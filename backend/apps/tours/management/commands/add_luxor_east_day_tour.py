"""
Management command to add "East Luxor Tour – Karnak & Luxor Temples" 1-day tour.
"""
from django.core.management.base import BaseCommand
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add East Luxor Tour (Karnak & Luxor Temples) 6-hour day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating East Luxor Tour...')

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
            slug='east-luxor-karnak-luxor-temples-tour',
            defaults={
                'name': 'East Luxor Tour – Karnak & Luxor Temples',
                'name_es': 'Tour Luxor Este – Templos de Karnak y Luxor',
                'name_pt': 'Passeio em Luxor Leste – Templo de Karnak e Templo de Luxor',

                'short_description': (
                    'A 6-hour journey through ancient Thebes: explore the magnificent '
                    'Karnak Temple — the largest religious complex in the world — and the '
                    'stunning Luxor Temple on the banks of the Nile. With an expert '
                    'Egyptologist guide, entrance tickets, and air-conditioned transfers included!'
                ),
                'short_description_es': (
                    'Un recorrido de 6 horas por la antigua Tebas: explore el magnífico '
                    'Templo de Karnak — el mayor complejo religioso del mundo — y el '
                    'impresionante Templo de Luxor a orillas del Nilo. ¡Con guía egiptólogo '
                    'experto, entradas y traslados con aire acondicionado incluidos!'
                ),
                'short_description_pt': (
                    'Um passeio de 6 horas pela antiga Tebas: explore o magnífico '
                    'Templo de Karnak — o maior complexo religioso do mundo — e o '
                    'deslumbrante Templo de Luxor às margens do Nilo. Com guia egiptólogo '
                    'especialista, ingressos e traslados com ar-condicionado inclusos!'
                ),

                'description': '''<p>In the morning, meet your guide at the lobby of your hotel in Luxor, the ancient Thebes of Glories, on the banks of the Nile. Then depart to visit the fabulous <strong>Karnak Temple</strong> — an impressive complex of monumental buildings that still bears witness to the magnificent commercial, religious, and artistic prosperity of the ancient Egyptian capital, Thebes.</p>

<p>Upon entering the site, you will be greeted by the famous <strong>Avenue of the Rams</strong>, where ram-headed sphinxes guard the entrance. You will walk through its majestic courtyards, such as the <strong>Great Court of Ramesses II</strong>, explore the immense <strong>Hypostyle Hall</strong> with its 134 colossal richly decorated columns, and contemplate imposing obelisks while discovering fascinating stories of pharaohs such as Amenhotep III, Thutmose I, Hatshepsut, Thutmose III, and Ramesses II, as well as the mysteries of Egyptian deities like Amun-Ra, Mut, and Khonsu.</p>

<p>Then continue to visit the magnificent <strong>Luxor Temple</strong>, which lends its name to the city and is dedicated to Amun. Built primarily by King Amenhotep III (c. 1397–1360 BC) and magnificently expanded by the famous King Ramesses II, the temple captivates with its colossal granite statues, the imposing <strong>Avenue of Sphinxes</strong> that once connected the two sacred temples (Karnak and Luxor), and the harmonious architecture reflecting the splendor of the New Kingdom.</p>

<p>You will walk through the <strong>peristyle court of Amenhotep III</strong>, admire the <strong>sanctuary of Alexander the Great</strong>, and see up close the reliefs depicting the <strong>Opet Festival</strong>, the most important Theban celebration.</p>

<p>At the end of the tour, return to your hotel in Luxor, with your mind full of unforgettable images of one of humanity's most fascinating civilizations.</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
<li>Guaranteed departure from 2 participants</li>
</ul>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water — walking through the temples in Luxor requires good hydration, especially in summer.</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>Book as far in advance as possible to guarantee guide availability and online tickets.</li>
<li>The agency needs at least 24 hours before the tour date to process the booking.</li>
<li>Bookings within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>Por la mañana, encuentro con su guía en el vestíbulo de su hotel en Luxor, la antigua Tebas de las Glorias, a orillas del Nilo. A continuación, salida para visitar el fabuloso <strong>Templo de Karnak</strong> — un impresionante complejo de edificios monumentales que aún atestigua la grandiosa prosperidad comercial, religiosa y artística de la capital del Antiguo Egipto, Tebas.</p>

<p>Al adentrarse en el recinto, le recibirá la famosa <strong>Avenida de los Carneros</strong>, donde esfinges con cabeza de carnero custodian la entrada. Recorrerá sus majestuosos patios, como el <strong>Gran Patio de Ramsés II</strong>, explorará la inmensa <strong>Sala Hipóstila</strong> con sus 134 columnas colosales ricamente decoradas, y contemplará obeliscos imponentes mientras descubre historias fascinantes de faraones como Amenhotep III, Tutmosis I, Hatshepsut, Tutmosis III y Ramsés II, además de los misterios de las divinidades egipcias como Amón-Ra, Mut y Jonsu.</p>

<p>Luego continuación para visitar el magnífico <strong>Templo de Luxor</strong>, que presta su nombre a la ciudad y está dedicado a Amón. Construido primordialmente por el rey Amenhotep III (hacia 1397–1360 a.C.) y magníficamente ampliado por el famoso rey Ramsés II, el templo cautiva con sus colosales estatuas de granito, la imponente <strong>Avenida de las Esfinges</strong> que antaño unía los dos templos sagrados (Karnak y Luxor), y la armoniosa arquitectura que refleja el esplendor del Imperio Nuevo.</p>

<p>Caminará por el <strong>patio peristilo de Amenhotep III</strong>, admirará el <strong>santuario de Alejandro Magno</strong>, y verá de cerca los relieves que narran las festividades del <strong>Opet</strong>, la más importante celebración tebana.</p>

<p>Al final del paseo, regreso a su hotel en Luxor, con la mente repleta de imágenes inolvidables de una de las civilizaciones más fascinantes de la humanidad.</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
<li>Salida garantizada a partir de 2 participantes</li>
</ul>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua — caminar por los templos de Luxor requiere buena hidratación, especialmente en verano.</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías.</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Reserve con la mayor antelación posible para garantizar disponibilidad del guía y boletos online.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>Pela manhã, encontro com seu guia no saguão do seu hotel em Luxor, a antiga Tebas das Glórias, às margens do Nilo. Em seguida, saída para visitar o fabuloso <strong>Templo de Karnak</strong> — um impressionante complexo de edifícios monumentais que ainda testemunha a grandiosa prosperidade comercial, religiosa e artística da capital do Antigo Egito, Tebas.</p>

<p>Ao adentrar o local, você será recebido pela famosa <strong>Avenida dos Carneiros</strong>, onde esfinges com cabeça de carneiro guardam a entrada. Você percorrerá seus pátios majestosos, como o <strong>Grande Pátio de Ramsés II</strong>, explorará a imensa <strong>Sala Hipóstila</strong> com suas 134 colunas colossais ricamente decoradas, e contemplará obeliscos imponentes, enquanto descobre histórias fascinantes de faraós como Amenhotep III, Tutmés I, Hatshepsut, Tutmés III e Ramsés II, além dos mistérios das divindades egípcias como Amon-Rá, Mut e Khonsu.</p>

<p>Depois continuação para visitar o magnífico <strong>Templo de Luxor</strong>, que empresta seu nome à cidade e é dedicado a Amon. Construído primordialmente pelo rei Amenhotep III (por volta de 1397–1360 a.C.) e magnificamente ampliado pelo famoso rei Ramsés II, o templo encanta com suas colossais estátuas de granito, a imponente <strong>Avenida de Esfinges</strong> que outrora ligava os dois templos sagrados (Karnak e Luxor), e a harmoniosa arquitetura que reflete o esplendor do Novo Império.</p>

<p>Você caminhará pelo <strong>pátio peristilo de Amenhotep III</strong>, admirará o <strong>santuário de Alexandre, o Grande</strong>, e verá de perto os relevos que narram as festividades do <strong>Opet</strong>, a mais importante celebração tebana.</p>

<p>Ao final do passeio, retorno ao seu hotel em Luxor, com a mente repleta de imagens inesquecíveis de uma das civilizações mais fascinantes da humanidade.</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
<li>Saída garantida a partir de 2 participantes</li>
</ul>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente — a caminhada nos templos em Luxor exige boa hidratação, especialmente no verão.</li>
<li><strong>Fotografia:</strong> Permitida na maioria das áreas, mas sem flash em algumas galerias.</li>
</ul>

<h3>Política de Reserva e Confirmação:</h3>
<ul>
<li>Recomenda-se reservar com o máximo de antecedência possível para garantir disponibilidade do guia e ingressos online.</li>
<li>A agência necessita de no mínimo 24 horas antes da data do tour para processar a reserva.</li>
<li>Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</li>
</ul>''',

                # Classification
                'category': category,
                'tour_type': tour_type,

                # Duration
                'days': 1,
                'nights': 0,

                # Pricing (placeholder - update in admin)
                'price': 75,
                'child_price': None,
                'currency': 'USD',

                # Group info
                'min_group_size': 2,
                'max_group_size': 12,

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
                'departure_city': 'Luxor',
                'languages': 'English, Spanish, Portuguese',

                # SEO
                'meta_title': 'East Luxor Tour: Karnak & Luxor Temples | 6h',
                'meta_title_es': 'Tour Luxor Este: Templos Karnak y Luxor | 6h',
                'meta_title_pt': 'Passeio Luxor Leste: Karnak e Luxor | 6h',
                'meta_description': '6-hour guided tour of East Luxor: Karnak Temple with its 134 columns and Luxor Temple on the Nile. Egyptologist guide and transfers included.',
                'meta_description_es': 'Tour guiado de 6 horas por Luxor Este: Templo de Karnak con sus 134 columnas y Templo de Luxor junto al Nilo. Guía egiptólogo y traslados incluidos.',
                'meta_description_pt': 'Passeio guiado de 6 horas em Luxor Leste: Templo de Karnak com 134 colunas e Templo de Luxor às margens do Nilo. Guia egiptólogo e traslados inclusos.',

                # Published
                'is_published': True,
            }
        )

        # Link to Luxor destination
        try:
            luxor = Destination.objects.get(slug='luxor')
            tour.destinations.add(luxor)
        except Destination.DoesNotExist:
            self.stdout.write(self.style.WARNING('Luxor destination not found, skipping destination link.'))

        # ============================================================
        # HIGHLIGHTS
        # ============================================================
        tour.highlights.all().delete()
        highlights = [
            {
                'title': 'Karnak Temple – Largest Religious Complex in the World',
                'title_es': 'Templo de Karnak – El Mayor Complejo Religioso del Mundo',
                'title_pt': 'Templo de Karnak – O Maior Complexo Religioso do Mundo',
                'description': 'Walk through the Great Hypostyle Hall with 134 colossal columns, admire the obelisks of Hatshepsut and Thutmose I, and contemplate the sacred lake.',
                'description_es': 'Recorra la Gran Sala Hipóstila con 134 columnas colosales, admire los obeliscos de Hatshepsut y Tutmosis I, y contemple el lago sagrado.',
                'description_pt': 'Percorra a Grande Sala Hipóstila com 134 colunas colossais, admire os obeliscos de Hatshepsut e Tutmés I, e contemple o lago sagrado.',
                'icon': 'temple',
                'sort_order': 1,
            },
            {
                'title': 'Luxor Temple – The Theban Jewel on the Nile',
                'title_es': 'Templo de Luxor – La Joya Tebana junto al Nilo',
                'title_pt': 'Templo de Luxor – A Joia Tebana às Margens do Nilo',
                'description': 'Admire the Avenue of Sphinxes, the colossal granite statues of Ramesses II, the peristyle court of Amenhotep III, the sanctuary of Alexander the Great, and the Opet Festival reliefs.',
                'description_es': 'Admire la Avenida de las Esfinges, las estatuas colosales de granito de Ramsés II, el patio peristilo de Amenhotep III, el santuario de Alejandro Magno y los relieves de la fiesta del Opet.',
                'description_pt': 'Admire a Avenida das Esfinges, as estátuas colossais de granito de Ramsés II, o pátio peristilo de Amenhotep III, o santuário de Alexandre, o Grande, e os relevos da festa do Opet.',
                'icon': 'monument',
                'sort_order': 2,
            },
            {
                'title': 'Expert Egyptologist Guide & Private Transfers',
                'title_es': 'Guía Egiptólogo Experto y Traslados Privados',
                'title_pt': 'Guia Egiptólogo Especialista e Traslados Privados',
                'description': 'Accompanied by a specialist Egyptologist guide with private air-conditioned transfers from and to your Luxor hotel. Guaranteed small group from 2 participants.',
                'description_es': 'Acompañado por un guía egiptólogo especialista con traslados privados con aire acondicionado desde y hacia su hotel en Luxor. Grupo reducido garantizado a partir de 2 participantes.',
                'description_pt': 'Acompanhado por um guia egiptólogo especialista com traslados privados com ar-condicionado de e para seu hotel em Luxor. Grupo reduzido garantido a partir de 2 participantes.',
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
            title='Karnak Temple & Luxor Temple',
            title_es='Templo de Karnak y Templo de Luxor',
            title_pt='Templo de Karnak e Templo de Luxor',
            description='''<p><strong>Morning</strong> – Hotel pick-up in Luxor</p>
<ul>
<li><strong>Karnak Temple</strong> (approx. 3 hours)
<ul>
<li>Avenue of the Rams (ram-headed sphinxes)</li>
<li>Great Court of Ramesses II</li>
<li>Hypostyle Hall – 134 colossal decorated columns</li>
<li>Obelisks of Hatshepsut and Thutmose I</li>
<li>Sacred Lake</li>
</ul></li>
</ul>
<ul>
<li><strong>Luxor Temple</strong> (approx. 2 hours)
<ul>
<li>Avenue of Sphinxes</li>
<li>Colossal granite statues of Ramesses II</li>
<li>Peristyle court of Amenhotep III</li>
<li>Sanctuary of Alexander the Great</li>
<li>Opet Festival reliefs</li>
</ul></li>
</ul>
<p><strong>End</strong> – Return to your hotel in Luxor</p>''',

            description_es='''<p><strong>Mañana</strong> – Recogida en el hotel en Luxor</p>
<ul>
<li><strong>Templo de Karnak</strong> (aprox. 3 horas)
<ul>
<li>Avenida de los Carneros (esfinges con cabeza de carnero)</li>
<li>Gran Patio de Ramsés II</li>
<li>Sala Hipóstila – 134 columnas colosales decoradas</li>
<li>Obeliscos de Hatshepsut y Tutmosis I</li>
<li>Lago Sagrado</li>
</ul></li>
</ul>
<ul>
<li><strong>Templo de Luxor</strong> (aprox. 2 horas)
<ul>
<li>Avenida de las Esfinges</li>
<li>Estatuas colosales de granito de Ramsés II</li>
<li>Patio peristilo de Amenhotep III</li>
<li>Santuario de Alejandro Magno</li>
<li>Relieves de la fiesta del Opet</li>
</ul></li>
</ul>
<p><strong>Final</strong> – Regreso a su hotel en Luxor</p>''',

            description_pt='''<p><strong>Manhã</strong> – Retirada no hotel em Luxor</p>
<ul>
<li><strong>Templo de Karnak</strong> (aprox. 3 horas)
<ul>
<li>Avenida dos Carneiros (esfinges com cabeça de carneiro)</li>
<li>Grande Pátio de Ramsés II</li>
<li>Sala Hipóstila – 134 colunas colossais decoradas</li>
<li>Obeliscos de Hatshepsut e Tutmés I</li>
<li>Lago Sagrado</li>
</ul></li>
</ul>
<ul>
<li><strong>Templo de Luxor</strong> (aprox. 2 horas)
<ul>
<li>Avenida das Esfinges</li>
<li>Estátuas colossais de granito de Ramsés II</li>
<li>Pátio peristilo de Amenhotep III</li>
<li>Santuário de Alexandre, o Grande</li>
<li>Relevos da festa do Opet</li>
</ul></li>
</ul>
<p><strong>Final</strong> – Retorno ao seu hotel em Luxor</p>''',

            locations='Luxor',
            locations_es='Luxor',
            locations_pt='Luxor',
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

        included = [
            {
                'item': 'Modern air-conditioned car transfers',
                'item_es': 'Traslados en coche moderno con aire acondicionado',
                'item_pt': 'Passeio em carro moderno com ar-condicionado',
            },
            {
                'item': 'Hotel pick-up and drop-off in Luxor (private transfers)',
                'item_es': 'Recogida y regreso al hotel en Luxor (traslados privados)',
                'item_pt': 'Pick-up e Drop-off no hotel em Luxor (traslados privados)',
            },
            {
                'item': 'Specialist Egyptologist guide',
                'item_es': 'Guía egiptólogo especialista',
                'item_pt': 'Guia especialista em egiptologia',
            },
            {
                'item': 'Entrance tickets to Karnak Temple and Luxor Temple',
                'item_es': 'Entradas al Templo de Karnak y Templo de Luxor',
                'item_pt': 'Ingressos para o Templo de Karnak e Templo de Luxor',
            },
            {
                'item': 'Guaranteed small group tour (from 2 participants)',
                'item_es': 'Tour en grupo reducido garantizado (a partir de 2 participantes)',
                'item_pt': 'Tour em grupo reduzido garantido (a partir de 2 participantes)',
            },
            {
                'item': '1 bottle of water per participant',
                'item_es': '1 botella de agua por participante',
                'item_pt': '1 garrafa de água por participante',
            },
            {
                'item': 'All local taxes and service fees included',
                'item_es': 'Todas las tasas e impuestos locales incluidos',
                'item_pt': 'Taxas e impostos locais inclusos no serviço',
            },
        ]
        for i, inc in enumerate(included):
            TourInclusion.objects.create(tour=tour, is_included=True, sort_order=i + 1, **inc)

        excluded = [
            {
                'item': 'Meals (lunch, breakfast, or snacks)',
                'item_es': 'Comidas (almuerzo, desayuno o aperitivos)',
                'item_pt': 'Refeições (almoço, café da manhã ou lanches)',
            },
            {
                'item': 'Additional drinks beyond the 1st bottle of water',
                'item_es': 'Bebidas adicionales además de la 1ª botella de agua',
                'item_pt': 'Bebidas adicionais além da 1ª garrafa de água',
            },
            {
                'item': 'Tips for guide and driver (optional but recommended)',
                'item_es': 'Propinas para guía y conductor (opcional pero recomendado)',
                'item_pt': 'Gorjetas para guia e motorista (opcional, mas recomendado)',
            },
            {
                'item': 'Personal expenses (shopping, souvenirs, etc.)',
                'item_es': 'Gastos personales (compras, recuerdos, etc.)',
                'item_pt': 'Despesas pessoais (compras, lembranças, etc.)',
            },
            {
                'item': 'Extras not mentioned in the itinerary (such as entry to additional tombs or temples)',
                'item_es': 'Extras no mencionados en el itinerario (como entrada a tumbas o templos adicionales)',
                'item_pt': 'Extras não mencionados no roteiro (como entrada em tumbas ou templos adicionais)',
            },
        ]
        for i, exc in enumerate(excluded):
            TourInclusion.objects.create(tour=tour, is_included=False, sort_order=i + 1, **exc)

        # ============================================================
        # FAQs
        # ============================================================
        tour.faqs.all().delete()
        faqs = [
            {
                'question': 'What is the minimum group size for this tour?',
                'question_es': '¿Cuál es el tamaño mínimo del grupo para este tour?',
                'question_pt': 'Qual é o tamanho mínimo do grupo para este passeio?',
                'answer': '<p>This tour is guaranteed with a minimum of 2 participants. It operates as a small group experience for a more intimate and personalized visit.</p>',
                'answer_es': '<p>Este tour está garantizado con un mínimo de 2 participantes. Opera como una experiencia en grupo reducido para una visita más íntima y personalizada.</p>',
                'answer_pt': '<p>Este passeio é garantido com um mínimo de 2 participantes. Opera como uma experiência em grupo reduzido para uma visita mais íntima e personalizada.</p>',
                'sort_order': 1,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': '¿Qué debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen. Comfortable walking shoes are essential as you will be walking through extensive temple complexes.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar. El calzado cómodo es esencial ya que caminará por extensos complejos de templos.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapéu, óculos de sol e protetor solar. Calçado confortável é essencial pois você caminhará por extensos complexos de templos.</p>',
                'sort_order': 2,
            },
            {
                'question': 'Is photography allowed inside the temples?',
                'question_es': '¿Se permite la fotografía dentro de los templos?',
                'question_pt': 'A fotografia é permitida dentro dos templos?',
                'answer': '<p>Photography is permitted in most areas of both Karnak and Luxor Temples. However, flash photography is not allowed in some galleries. Please follow security guidelines at each location.</p>',
                'answer_es': '<p>La fotografía está permitida en la mayoría de las áreas de los templos de Karnak y Luxor. Sin embargo, no se permite el flash en algunas galerías. Siga las indicaciones de seguridad en cada ubicación.</p>',
                'answer_pt': '<p>A fotografia é permitida na maioria das áreas dos templos de Karnak e Luxor. No entanto, não é permitido o uso de flash em algumas galerias. Siga as orientações de segurança em cada local.</p>',
                'sort_order': 3,
            },
            {
                'question': 'How far in advance should I book?',
                'question_es': '¿Con cuánta antelación debo reservar?',
                'question_pt': 'Com quanta antecedência devo reservar?',
                'answer': '<p>We recommend booking as far in advance as possible to guarantee guide availability and online tickets. The agency needs at least 24 hours before the tour date. Bookings within less than 24 hours are subject to last-minute availability.</p>',
                'answer_es': '<p>Recomendamos reservar con la mayor antelación posible para garantizar la disponibilidad del guía y boletos online. La agencia necesita al menos 24 horas antes de la fecha del tour. Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</p>',
                'answer_pt': '<p>Recomendamos reservar com o máximo de antecedência possível para garantir a disponibilidade do guia e ingressos online. A agência necessita de no mínimo 24 horas antes da data do tour. Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</p>',
                'sort_order': 4,
            },
        ]
        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: 6 hours (1 day)'
            f'\n  - Departure: Luxor'
            f'\n  - Price: ${tour.price} (placeholder - update in admin)'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
