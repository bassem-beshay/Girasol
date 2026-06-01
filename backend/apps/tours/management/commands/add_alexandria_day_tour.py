"""
Management command to add "Full-Day Tour to Alexandria from Cairo" 1-day tour.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.tours.models import (
    Tour, TourCategory, TourType, TourItinerary,
    TourInclusion, TourHighlight, TourFAQ
)
from apps.destinations.models import Destination


class Command(BaseCommand):
    help = 'Add Full-Day Tour to Alexandria from Cairo 1-day tour'

    def handle(self, *args, **options):
        self.stdout.write('Creating Full-Day Tour to Alexandria from Cairo day tour...')

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
            slug='full-day-tour-alexandria-from-cairo',
            defaults={
                'name': 'Full-Day Tour to Alexandria from Cairo',
                'name_es': 'Excursión de un Día a Alejandría desde El Cairo',
                'name_pt': 'Alexandria por um Dia - Saindo do Cairo',

                'short_description': (
                    'A 12-hour full-day tour from Cairo to Alexandria, Egypt\'s ancient cultural '
                    'capital. Explore the Catacombs of Kom El Shokafa, the Roman Theater, the '
                    'Alexandria National Museum, and the New Library of Alexandria. Includes '
                    'lunch, expert guide, entrance tickets, and round-trip transfers!'
                ),
                'short_description_es': (
                    'Excursión completa de 12 horas desde El Cairo a Alejandría, la antigua '
                    'capital cultural de Egipto. Explora las Catacumbas de Kom El Shokafa, el '
                    'Teatro Romano, el Museo Nacional de Alejandría y la Nueva Biblioteca de '
                    'Alejandría. ¡Incluye almuerzo, guía experto, entradas y traslados!'
                ),
                'short_description_pt': (
                    'Passeio completo de 12 horas do Cairo a Alexandria, a antiga capital '
                    'cultural do Egito. Explore as Catacumbas de Kom El Shokafa, o Teatro '
                    'Romano, o Museu Nacional de Alexandria e a Nova Biblioteca de Alexandria. '
                    'Inclui almoço, guia especializado, ingressos e traslados!'
                ),

                'description': '''<p>The Full-Day Tour to Alexandria from Cairo is a comprehensive 12-hour experience to explore Alexandria, the second most important city in Egypt and its ancient cultural center, famous especially for the legendary Ancient Library of Alexandria and the iconic Lighthouse of Alexandria.</p>

<p>Early morning land transfer to Alexandria (221 km) to explore the city and return to Cairo on the same day.</p>

<p>Upon arriving in the city, founded by <strong>Alexander the Great</strong> in April 331 BC, we head to the old district of Kom El Shokafa to visit the <strong>Catacombs of Kom El Shokafa</strong>, dating back to the Roman rule over Egypt. The catacombs are the largest Roman-era burial site known in Egypt and one of the last great works dedicated to the religion of Ancient Egypt. The cemetery dates from the 1st century AD and was used until the 4th century AD. The catacombs show the characteristic fusion of Pharaonic and Greek styles, with chambers and halls carved into the bedrock at a depth of 35 meters.</p>

<p>Next, we visit the <strong>Roman Theater (Kom El Dekka Amphitheater)</strong>, built in the 4th century AD, when Alexandria was a thriving center of cultural and intellectual exchange. This theater has 13 rows of white and gray marble seats brought from Europe and could accommodate 600 to 800 spectators, with a diameter of about 33 meters.</p>

<p>We proceed to the <strong>Alexandria National Museum</strong>, which recounts the history of Alexandria through the ages, displaying a unique collection of Egyptian and Alexandrian art.</p>

<p><strong>Lunch at a local restaurant</strong> (beverages not included).</p>

<p>We continue to visit the <strong>New Library of Alexandria</strong>, a major work of modern architecture covering about 38,000 square meters, inspired by the ancient Library of Alexandria. Officially inaugurated on October 17, 2002, on the same site as the original library, it houses several educational institutions and museums. The Library of Alexandria is considered the world's first digital library.</p>

<p>We move on to <strong>Qaitbay Citadel</strong> (external visit for photos), built on the former site of the legendary Lighthouse of Alexandria, and then to <strong>Stanley Bridge</strong>, inaugurated in 2001, a modern landmark of Alexandria stretching 400 meters over the Mediterranean Sea.</p>

<p>Return to Cairo (221 km). Land transfer back to your hotel in Cairo. End of tour.</p>

<h3>This tour is:</h3>
<ul>
<li>Ideal for Couples</li>
<li>Perfect for Independent Travelers</li>
<li>Great for Families</li>
<li>Excellent for History Enthusiasts</li>
</ul>

<h3>Payment:</h3>
<p>Pay with your Visa or Mastercard through a secure, personalized link. Fast, reliable, and hassle-free.</p>

<h3>Important Recommendations:</h3>
<ul>
<li><strong>Clothing:</strong> Wear light clothing, especially from April to November, plus a hat, sunglasses, and sunscreen. Comfortable walking shoes.</li>
<li><strong>Hydration:</strong> Bring enough water – walking in the Catacombs and visiting the Museum require good hydration.</li>
<li><strong>Lunch:</strong> Included at a local restaurant (beverages not included).</li>
<li><strong>Photography:</strong> Permitted in most areas, but without flash in some galleries. Follow security guidelines.</li>
</ul>

<h3>Booking & Confirmation Policy:</h3>
<ul>
<li>It is highly recommended to book as far in advance as possible.</li>
<li>The agency needs at least 24 hours prior to the tour date to process the booking.</li>
<li>Bookings made within less than 24 hours are subject to last-minute availability.</li>
</ul>''',

                'description_es': '''<p>La Excursión de un Día a Alejandría desde El Cairo es una experiencia completa de 12 horas para explorar Alejandría, la segunda ciudad más importante de Egipto y su antiguo centro cultural, famosa sobre todo por la legendaria Biblioteca de Alejandría y el icónico Faro de Alejandría.</p>

<p>Por la mañana temprano, traslado terrestre con destino a Alejandría (221 km) para recorrer la ciudad y regresar a El Cairo el mismo día.</p>

<p>Al llegar a la ciudad, fundada por <strong>Alejandro Magno</strong> en abril del 331 a.C., nos dirigimos al antiguo barrio de Kom El Shokafa para visitar las <strong>Catacumbas de Kom El Shokafa</strong>, que datan de la época de la dominación romana sobre Egipto. Las catacumbas constituyen el cementerio más grande de la era romana conocido en Egipto y una de las últimas grandes obras dedicadas a la religión del Antiguo Egipto. El cementerio data del siglo I d.C. y se usó hasta el siglo IV d.C. Las catacumbas muestran la característica fusión de los estilos faraónico y griego, con cámaras y salas excavadas en la roca a 35 metros de profundidad.</p>

<p>A continuación, visitamos el <strong>Teatro Romano (Anfiteatro de Kom El Dekka)</strong>, construido en el siglo IV d.C., cuando Alejandría era un próspero centro de intercambio cultural e intelectual. Este teatro tiene 13 filas de gradas de mármol blanco y gris traído de Europa y podía albergar de 600 a 800 espectadores, con unos 33 metros de diámetro.</p>

<p>Continuamos hacia el <strong>Museo Nacional de Alejandría</strong>, que narra la historia de Alejandría a través de las eras, exhibiendo una colección única de arte egipcio y alejandrino.</p>

<p><strong>Almuerzo en un restaurante local</strong> (bebidas no incluidas).</p>

<p>Seguimos para visitar la <strong>Nueva Biblioteca de Alejandría</strong>, una gran obra de arquitectura moderna que ocupa unos 38 mil metros cuadrados, inspirada en la antigua Biblioteca de Alejandría. Inaugurada oficialmente el 17 de octubre de 2002, en el mismo lugar de la biblioteca original, alberga varias instituciones educativas y museos. La Biblioteca de Alejandría es considerada la primera biblioteca digital del mundo.</p>

<p>Nos dirigimos a la <strong>Fortaleza de Qaitbay</strong> (visita externa para fotografías), construida sobre el lugar donde una vez estuvo el legendario Faro de Alejandría, y al <strong>Puente Stanley</strong>, inaugurado en 2001, un hito moderno de Alejandría con 400 metros de extensión sobre el mar Mediterráneo.</p>

<p>Regreso a El Cairo (221 km). Traslado terrestre de vuelta a su hotel en El Cairo. Fin del tour.</p>

<h3>Este itinerario es:</h3>
<ul>
<li>Ideal para Parejas</li>
<li>Perfecto para Viajeros Independientes</li>
<li>Excelente para Familias</li>
<li>Perfecto para Entusiastas de la Historia</li>
</ul>

<h3>Modo de pago:</h3>
<p>Pague con su tarjeta Visa o Mastercard a través de un enlace seguro y personalizado. Rápido, confiable y sin complicaciones.</p>

<h3>Recomendaciones Importantes:</h3>
<ul>
<li><strong>Vestimenta:</strong> Use ropa ligera, especialmente de abril a noviembre, sombrero, gafas de sol y protector solar. Calzado cómodo para caminar.</li>
<li><strong>Hidratación:</strong> Lleve suficiente agua – caminar por las catacumbas y visitar el museo requiere una buena hidratación.</li>
<li><strong>Almuerzo:</strong> Incluido en restaurante local (bebidas no incluidas).</li>
<li><strong>Fotografía:</strong> Permitida en la mayoría de las áreas, pero sin flash en algunas galerías. Siga las indicaciones de seguridad.</li>
</ul>

<h3>Política de Reserva y Confirmación:</h3>
<ul>
<li>Se recomienda reservar con la mayor antelación posible.</li>
<li>La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva.</li>
<li>Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</li>
</ul>''',

                'description_pt': '''<p>O Passeio de um Dia a Alexandria saindo do Cairo é uma experiência completa de 12 horas para explorar Alexandria, a segunda cidade mais relevante do Egito e seu antigo centro cultural, famosa sobretudo pela lendária Biblioteca de Alexandria e pelo icônico Farol de Alexandria.</p>

<p>No início da manhã, traslado terrestre com destino a Alexandria (221 km), para conhecer a cidade e retornar ao Cairo no mesmo dia.</p>

<p>Ao chegar à cidade, fundada por <strong>Alexandre, o Grande</strong>, em abril de 331 a.C., seguimos para o bairro antigo de Kom El Shokafa para visitar as <strong>Catacumbas de Kom El Shokafa</strong>, que datam da época do domínio romano sobre o Egito. As catacumbas constituem o maior cemitério da era romana conhecido no Egito e uma das últimas grandes obras dedicadas à religião do Antigo Egito. O cemitério remonta ao século I d.C. e foi utilizado até o século IV d.C. As catacumbas exibem a característica fusão dos estilos faraônico e grego, com câmaras e salas escavadas na rocha a uma profundidade de 35 metros.</p>

<p>Em seguida, visitamos o <strong>Teatro Romano (Anfiteatro de Kom El Dekka)</strong>, construído no século IV d.C., quando Alexandria era um próspero centro de intercâmbio cultural e intelectual. Este teatro possui 13 fileiras de bancos de mármore branco e cinza trazido da Europa e podia acomodar de 600 a 800 espectadores, com cerca de 33 metros de diâmetro.</p>

<p>Prosseguimos para o <strong>Museu Nacional de Alexandria</strong>, que narra a história da cidade ao longo das eras, exibindo uma coleção singular da arte egípcia e alexandrina.</p>

<p><strong>Almoço em restaurante local</strong> (bebidas não incluídas).</p>

<p>Continuamos para visitar a <strong>Nova Biblioteca de Alexandria</strong>, uma grande obra da arquitetura moderna que ocupa cerca de 38 mil metros quadrados, inspirada na antiga Biblioteca de Alexandria. Inaugurada oficialmente em 17 de outubro de 2002, no mesmo local da biblioteca original, abriga diversas instituições educacionais e museus. A Biblioteca de Alexandria é considerada a primeira biblioteca digital do mundo.</p>

<p>Seguimos para a <strong>Fortaleza de Quaitbai</strong> (visita externa para fotos), erguida sobre o local onde outrora esteve o lendário Farol de Alexandria, e para a <strong>Ponte Stanley</strong>, inaugurada em 2001, um marco moderno de Alexandria com 400 metros de extensão sobre o Mar Mediterrâneo.</p>

<p>Retorno ao Cairo (221 km). Traslado terrestre de volta ao seu hotel no Cairo. Fim do tour.</p>

<h3>Este roteiro é:</h3>
<ul>
<li>Perfeito para Casais</li>
<li>Ideal para Viajantes Independentes</li>
<li>Recomendado para Famílias</li>
<li>Excelente para Entusiastas de História</li>
</ul>

<h3>Condições de Pagamento:</h3>
<p>Efetue o pagamento com seu cartão Visa ou Mastercard através de um link seguro e personalizado. Processo rápido, confiável e descomplicado.</p>

<h3>Recomendações Importantes:</h3>
<ul>
<li><strong>Vestuário:</strong> Use roupas leves principalmente de abril a novembro, chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar.</li>
<li><strong>Hidratação:</strong> Leve água suficiente – a caminhada nas catacumbas e a visita ao museu exigem boa hidratação.</li>
<li><strong>Almoço:</strong> Incluído em restaurante local (bebidas não inclusas).</li>
<li><strong>Fotografia:</strong> Permitida na maioria das áreas, mas sem flash em algumas galerias. Siga as orientações de segurança.</li>
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

                # Pricing (placeholder – no pricing table in source docs)
                'price': 95,
                'child_price': None,
                'currency': 'USD',

                # Group info
                'min_group_size': 1,
                'max_group_size': 10,

                # Features
                'is_featured': True,
                'is_best_seller': False,
                'is_new': True,
                'is_multi_destination': True,
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
                'meta_title': 'Full-Day Tour to Alexandria from Cairo | 12 Hours',
                'meta_title_es': 'Excursión de un Día a Alejandría desde El Cairo',
                'meta_title_pt': 'Passeio de um Dia a Alexandria saindo do Cairo',
                'meta_description': 'Full-day 12-hour tour from Cairo to Alexandria: Catacombs, Roman Theater, National Museum, Library of Alexandria. Lunch & transfers included.',
                'meta_description_es': 'Excursión de 12 horas desde El Cairo a Alejandría: Catacumbas, Teatro Romano, Museo Nacional, Biblioteca de Alejandría. Almuerzo y traslados incluidos.',
                'meta_description_pt': 'Passeio de 12 horas do Cairo a Alexandria: Catacumbas, Teatro Romano, Museu Nacional, Biblioteca de Alexandria. Almoço e traslados inclusos.',

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

        # Link to Alexandria destination
        try:
            alexandria = Destination.objects.get(slug='alexandria')
            tour.destinations.add(alexandria)
        except Destination.DoesNotExist:
            self.stdout.write(self.style.WARNING('Alexandria destination not found, skipping destination link.'))

        # ============================================================
        # HIGHLIGHTS
        # ============================================================
        tour.highlights.all().delete()
        highlights = [
            {
                'title': 'Catacombs of Kom El Shokafa',
                'title_es': 'Catacumbas de Kom El Shokafa',
                'title_pt': 'Catacumbas de Kom El Shokafa',
                'description': 'The largest Roman-era cemetery in Egypt, 35 meters deep, featuring a unique fusion of Pharaonic and Greco-Roman styles.',
                'description_es': 'El cementerio más grande de la era romana en Egipto, con 35 metros de profundidad y una fusión única de estilos faraónico y grecorromano.',
                'description_pt': 'O maior cemitério da era romana no Egito, com 35 metros de profundidade e fusão única dos estilos faraônico e greco-romano.',
                'icon': 'monument',
                'sort_order': 1,
            },
            {
                'title': 'Roman Theater & Alexandria National Museum',
                'title_es': 'Teatro Romano y Museo Nacional de Alejandría',
                'title_pt': 'Teatro Romano e Museu Nacional de Alexandria',
                'description': 'Visit the 4th-century Kom El Dekka Amphitheater with 13 rows of marble seats, and the National Museum showcasing Egyptian and Alexandrian art.',
                'description_es': 'Visita el Anfiteatro de Kom El Dekka del siglo IV con 13 filas de mármol, y el Museo Nacional con arte egipcio y alejandrino.',
                'description_pt': 'Visite o Anfiteatro de Kom El Dekka do século IV com 13 fileiras de mármore, e o Museu Nacional com arte egípcia e alexandrina.',
                'icon': 'museum',
                'sort_order': 2,
            },
            {
                'title': 'New Library of Alexandria',
                'title_es': 'Nueva Biblioteca de Alejandría',
                'title_pt': 'Nova Biblioteca de Alexandria',
                'description': 'Inaugurated in 2002 on the original site, considered the world\'s first digital library and a landmark of modern architecture covering 38,000 sqm.',
                'description_es': 'Inaugurada en 2002 en el lugar original, considerada la primera biblioteca digital del mundo y un hito de la arquitectura moderna con 38.000 m².',
                'description_pt': 'Inaugurada em 2002 no local da original, considerada a primeira biblioteca digital do mundo e um marco da arquitetura moderna com 38.000 m².',
                'icon': 'library',
                'sort_order': 3,
            },
            {
                'title': 'Qaitbay Citadel & Stanley Bridge',
                'title_es': 'Fortaleza de Qaitbay y Puente Stanley',
                'title_pt': 'Fortaleza de Quaitbai e Ponte Stanley',
                'description': 'External visit to the Citadel built on the site of the legendary Lighthouse of Alexandria, plus Stanley Bridge stretching 400m over the Mediterranean.',
                'description_es': 'Visita externa a la Fortaleza construida donde estuvo el legendario Faro de Alejandría, y el Puente Stanley con 400m sobre el Mediterráneo.',
                'description_pt': 'Visita externa à Fortaleza erguida onde esteve o lendário Farol de Alexandria, e a Ponte Stanley com 400m sobre o Mediterrâneo.',
                'icon': 'castle',
                'sort_order': 4,
            },
            {
                'title': 'Lunch Included & Full Transfers',
                'title_es': 'Almuerzo Incluido y Traslados Completos',
                'title_pt': 'Almoço Incluído e Traslados Completos',
                'description': 'Lunch at a local restaurant included. Round-trip air-conditioned transfers from Cairo (221 km each way) with expert guide.',
                'description_es': 'Almuerzo en restaurante local incluido. Traslados con aire acondicionado ida y vuelta desde El Cairo (221 km por trayecto) con guía experto.',
                'description_pt': 'Almoço em restaurante local incluído. Traslados com ar-condicionado ida e volta do Cairo (221 km por trecho) com guia especializado.',
                'icon': 'transfer',
                'sort_order': 5,
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
            title='Full-Day Alexandria Tour from Cairo',
            title_es='Excursión de un Día Completo a Alejandría desde El Cairo',
            title_pt='Passeio de um Dia Completo a Alexandria saindo do Cairo',
            description='''<p><strong>06:00</strong> – Early morning hotel pick-up in Cairo</p>
<p><strong>06:00–09:00</strong> – Land transfer to Alexandria (221 km)</p>
<p><strong>09:00</strong> – Arrival in Alexandria, city founded by Alexander the Great in 331 BC</p>
<ul>
<li><strong>Catacombs of Kom El Shokafa</strong> – Largest Roman-era burial site in Egypt, 35 meters deep, with Pharaonic-Greco-Roman fusion</li>
<li><strong>Roman Theater (Kom El Dekka Amphitheater)</strong> – 4th century AD, 13 marble rows, capacity for 600-800 spectators</li>
<li><strong>Alexandria National Museum</strong> – History of Alexandria through the ages, Egyptian and Alexandrian art</li>
</ul>
<p><strong>13:00</strong> – Lunch at a local restaurant (beverages not included)</p>
<ul>
<li><strong>New Library of Alexandria</strong> – 38,000 sqm modern architectural marvel, world's first digital library</li>
<li><strong>Qaitbay Citadel</strong> – External visit for photos, site of the legendary Lighthouse of Alexandria</li>
<li><strong>Stanley Bridge</strong> – 400m modern landmark over the Mediterranean Sea</li>
</ul>
<p><strong>15:00–18:00</strong> – Return land transfer to Cairo (221 km)</p>
<p><strong>18:00</strong> – Arrival at your hotel in Cairo. End of tour.</p>''',

            description_es='''<p><strong>06:00</strong> – Recogida temprana en el hotel de El Cairo</p>
<p><strong>06:00–09:00</strong> – Traslado terrestre a Alejandría (221 km)</p>
<p><strong>09:00</strong> – Llegada a Alejandría, ciudad fundada por Alejandro Magno en 331 a.C.</p>
<ul>
<li><strong>Catacumbas de Kom El Shokafa</strong> – El mayor cementerio romano en Egipto, 35 metros de profundidad, fusión faraónico-grecorromana</li>
<li><strong>Teatro Romano (Anfiteatro de Kom El Dekka)</strong> – Siglo IV d.C., 13 filas de mármol, capacidad para 600-800 espectadores</li>
<li><strong>Museo Nacional de Alejandría</strong> – Historia de Alejandría a través de las eras, arte egipcio y alejandrino</li>
</ul>
<p><strong>13:00</strong> – Almuerzo en restaurante local (bebidas no incluidas)</p>
<ul>
<li><strong>Nueva Biblioteca de Alejandría</strong> – 38.000 m² de arquitectura moderna, primera biblioteca digital del mundo</li>
<li><strong>Fortaleza de Qaitbay</strong> – Visita externa para fotos, sitio del legendario Faro de Alejandría</li>
<li><strong>Puente Stanley</strong> – Hito moderno de 400m sobre el mar Mediterráneo</li>
</ul>
<p><strong>15:00–18:00</strong> – Traslado terrestre de regreso a El Cairo (221 km)</p>
<p><strong>18:00</strong> – Llegada a su hotel en El Cairo. Fin del tour.</p>''',

            description_pt='''<p><strong>06:00</strong> – Retirada no hotel no Cairo pela manhã cedo</p>
<p><strong>06:00–09:00</strong> – Traslado terrestre para Alexandria (221 km)</p>
<p><strong>09:00</strong> – Chegada a Alexandria, cidade fundada por Alexandre, o Grande, em 331 a.C.</p>
<ul>
<li><strong>Catacumbas de Kom El Shokafa</strong> – Maior cemitério romano no Egito, 35 metros de profundidade, fusão faraônico-greco-romana</li>
<li><strong>Teatro Romano (Anfiteatro de Kom El Dekka)</strong> – Século IV d.C., 13 fileiras de mármore, capacidade para 600-800 espectadores</li>
<li><strong>Museu Nacional de Alexandria</strong> – História de Alexandria ao longo das eras, arte egípcia e alexandrina</li>
</ul>
<p><strong>13:00</strong> – Almoço em restaurante local (bebidas não incluídas)</p>
<ul>
<li><strong>Nova Biblioteca de Alexandria</strong> – 38.000 m² de arquitetura moderna, primeira biblioteca digital do mundo</li>
<li><strong>Fortaleza de Quaitbai</strong> – Visita externa para fotos, local do lendário Farol de Alexandria</li>
<li><strong>Ponte Stanley</strong> – Marco moderno de 400m sobre o Mar Mediterrâneo</li>
</ul>
<p><strong>15:00–18:00</strong> – Traslado terrestre de retorno ao Cairo (221 km)</p>
<p><strong>18:00</strong> – Chegada ao seu hotel no Cairo. Fim do tour.</p>''',

            locations='Cairo, Alexandria',
            locations_es='El Cairo, Alejandría',
            locations_pt='Cairo, Alexandria',
            meals_included='Lunch',
            meals_included_es='Almuerzo',
            meals_included_pt='Almoço',
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
                'item': 'Round-trip land transfer from your hotel in Cairo (Pick up & Drop off)',
                'item_es': 'Traslado terrestre de ida y vuelta desde su hotel en El Cairo (Pick up & Drop off)',
                'item_pt': 'Traslado terrestre de ida e volta do seu hotel no Cairo (Pick up & Drop off)',
            },
            {
                'item': 'English-speaking Egyptologist guide (subject to availability)',
                'item_es': 'Guía egiptólogo hablante de español (según disponibilidad)',
                'item_pt': 'Guia egiptólogo em português ou espanhol (conforme disponibilidade)',
            },
            {
                'item': 'Entry tickets to all sites: Catacombs of Kom El Shokafa, Roman Theater, Alexandria National Museum, New Library of Alexandria, external visits to Qaitbay Citadel and Stanley Bridge',
                'item_es': 'Entradas a todos los sitios: Catacumbas de Kom El Shokafa, Teatro Romano, Museo Nacional de Alejandría, Nueva Biblioteca de Alejandría, visitas externas a la Fortaleza de Qaitbay y al Puente Stanley',
                'item_pt': 'Entradas para todos os locais: Catacumbas de Kom El Shokafa, Teatro Romano, Museu Nacional de Alexandria, Nova Biblioteca de Alexandria, visita externa à Fortaleza de Quaitbai e à Ponte Stanley',
            },
            {
                'item': 'Lunch at a local restaurant (beverages not included)',
                'item_es': 'Almuerzo en restaurante local (bebidas no incluidas)',
                'item_pt': 'Almoço em restaurante local (bebidas não inclusas)',
            },
            {
                'item': '2 bottles of mineral water per person during the tour',
                'item_es': '2 botellas de agua mineral por persona durante el recorrido',
                'item_pt': '2 garrafas de água mineral por pessoa durante o passeio',
            },
            {
                'item': 'Tour taxes and service fees',
                'item_es': 'Impuestos de tours y tarifas de servicio',
                'item_pt': 'Taxas de tours e taxas de serviços',
            },
            {
                'item': 'Air-conditioned vehicle transport',
                'item_es': 'Transporte en vehículo privado con aire acondicionado',
                'item_pt': 'Transporte em veículo privado com ar-condicionado',
            },
            {
                'item': 'All fuel, tolls, and parking costs',
                'item_es': 'Todos los costos de combustible, peajes y estacionamiento',
                'item_pt': 'Todos os custos de combustível, pedágios e estacionamento',
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
                'item': 'Beverages during lunch',
                'item_es': 'Bebidas durante el almuerzo',
                'item_pt': 'Bebidas durante o almoço',
            },
            {
                'item': 'Tips (gratuities for driver, guide, restaurant)',
                'item_es': 'Propinas (para conductor, guía, restaurante)',
                'item_pt': 'Gorjetas (caixinhas para motorista, guia, restaurante)',
            },
            {
                'item': 'Personal shopping and souvenirs',
                'item_es': 'Compras personales y souvenirs',
                'item_pt': 'Compras pessoais e souvenirs',
            },
            {
                'item': 'Personal expenses (phone, laundry, etc.)',
                'item_es': 'Gastos personales (teléfono, lavandería, etc.)',
                'item_pt': 'Despesas de caráter pessoal (telefone, lavanderia, etc.)',
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
                'question': 'How long is the transfer from Cairo to Alexandria?',
                'question_es': '¿Cuánto dura el traslado de El Cairo a Alejandría?',
                'question_pt': 'Quanto tempo dura o traslado do Cairo a Alexandria?',
                'answer': '<p>The land transfer from Cairo to Alexandria is approximately 221 km each way, taking about 2.5 to 3 hours depending on traffic conditions. The total tour duration is 12 hours including transfers.</p>',
                'answer_es': '<p>El traslado terrestre de El Cairo a Alejandría es de aproximadamente 221 km por trayecto, con una duración de 2,5 a 3 horas según las condiciones del tráfico. La duración total del tour es de 12 horas incluyendo traslados.</p>',
                'answer_pt': '<p>O traslado terrestre do Cairo a Alexandria é de aproximadamente 221 km por trecho, levando cerca de 2,5 a 3 horas dependendo das condições de trânsito. A duração total do passeio é de 12 horas incluindo traslados.</p>',
                'sort_order': 1,
            },
            {
                'question': 'Is lunch included in this tour?',
                'question_es': '¿El almuerzo está incluido en este tour?',
                'question_pt': 'O almoço está incluído neste passeio?',
                'answer': '<p>Yes, lunch at a local restaurant is included in this tour. However, beverages during lunch are not included and must be purchased separately.</p>',
                'answer_es': '<p>Sí, el almuerzo en un restaurante local está incluido en este tour. Sin embargo, las bebidas durante el almuerzo no están incluidas y deben adquirirse por separado.</p>',
                'answer_pt': '<p>Sim, o almoço em restaurante local está incluído neste passeio. No entanto, as bebidas durante o almoço não estão inclusas e devem ser adquiridas separadamente.</p>',
                'sort_order': 2,
            },
            {
                'question': 'Can I enter the Qaitbay Citadel?',
                'question_es': '¿Puedo entrar en la Fortaleza de Qaitbay?',
                'question_pt': 'Posso entrar na Fortaleza de Quaitbai?',
                'answer': '<p>The tour includes an external visit to Qaitbay Citadel for photos only. To enter the Citadel, you would need to purchase an additional ticket on site. Please consult your guide for availability.</p>',
                'answer_es': '<p>El tour incluye una visita externa a la Fortaleza de Qaitbay solo para fotografías. Para entrar en la Fortaleza, es necesario adquirir un boleto adicional en el lugar. Consulte a su guía sobre disponibilidad.</p>',
                'answer_pt': '<p>O passeio inclui uma visita externa à Fortaleza de Quaitbai apenas para fotos. Para entrar na Fortaleza, é necessário adquirir um ingresso adicional no local. Consulte seu guia sobre disponibilidade.</p>',
                'sort_order': 3,
            },
            {
                'question': 'What should I wear for this tour?',
                'question_es': '¿Qué debo vestir para este tour?',
                'question_pt': 'O que devo vestir para este passeio?',
                'answer': '<p>Wear light clothing, especially from April to November. Bring a hat, sunglasses, and sunscreen. Comfortable walking shoes are essential as you will be visiting multiple archaeological sites and museums.</p>',
                'answer_es': '<p>Use ropa ligera, especialmente de abril a noviembre. Traiga sombrero, gafas de sol y protector solar. El calzado cómodo para caminar es esencial ya que visitará varios sitios arqueológicos y museos.</p>',
                'answer_pt': '<p>Use roupas leves, principalmente de abril a novembro. Traga chapéu, óculos de sol e protetor solar. Calçado confortável para caminhar é essencial pois visitará diversos sítios arqueológicos e museus.</p>',
                'sort_order': 4,
            },
            {
                'question': 'How far in advance should I book?',
                'question_es': '¿Con cuánta antelación debo reservar?',
                'question_pt': 'Com quanta antecedência devo reservar?',
                'answer': '<p>We recommend booking as far in advance as possible to guarantee availability of the Egyptologist guide and online tickets. The agency needs at least 24 hours prior to the tour date to process the booking, assign the guide, purchase tickets, and confirm all services. Bookings within less than 24 hours are subject to last-minute availability.</p>',
                'answer_es': '<p>Recomendamos reservar con la mayor antelación posible para garantizar la disponibilidad del guía egiptólogo y de los boletos en línea. La agencia necesita al menos 24 horas antes de la fecha del tour para procesar la reserva, asignar el guía, adquirir los boletos y confirmar todos los servicios. Reservas con menos de 24 horas sujetas a disponibilidad de última hora.</p>',
                'answer_pt': '<p>Recomendamos reservar com o máximo de antecedência possível para garantir a disponibilidade do guia egiptólogo e dos ingressos online. A agência necessita de no mínimo 24 horas antes da data do tour para processar a reserva, alocar o guia, adquirir os ingressos e confirmar todos os serviços. Reservas com menos de 24 horas sujeitas à disponibilidade de última hora.</p>',
                'sort_order': 5,
            },
            {
                'question': 'Is photography allowed at the sites?',
                'question_es': '¿Se permite la fotografía en los sitios?',
                'question_pt': 'A fotografia é permitida nos locais?',
                'answer': '<p>Photography is permitted in most areas. However, flash photography is not allowed in some museum galleries and inside the Catacombs. Please follow the security guidelines at each location.</p>',
                'answer_es': '<p>La fotografía está permitida en la mayoría de las áreas. Sin embargo, no se permite el uso de flash en algunas galerías del museo y dentro de las Catacumbas. Siga las indicaciones de seguridad en cada ubicación.</p>',
                'answer_pt': '<p>A fotografia é permitida na maioria das áreas. No entanto, não é permitido o uso de flash em algumas galerias do museu e dentro das Catacumbas. Siga as orientações de segurança em cada local.</p>',
                'sort_order': 6,
            },
        ]

        for faq in faqs:
            TourFAQ.objects.create(tour=tour, **faq)

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'\n{action} tour: "{tour.name}" (slug: {tour.slug})'
            f'\n  - Type: Day Tour | Duration: {tour.days} day (12 hours)'
            f'\n  - Price: ${tour.price} (placeholder)'
            f'\n  - Highlights: {tour.highlights.count()}'
            f'\n  - Itinerary: {tour.itinerary.count()} day'
            f'\n  - Inclusions: {tour.inclusions.filter(is_included=True).count()} included, '
            f'{tour.inclusions.filter(is_included=False).count()} excluded'
            f'\n  - FAQs: {tour.faqs.count()}'
        ))
