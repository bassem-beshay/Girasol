"""
Multilingual Data Seeder for Girasol Tours
Adds comprehensive data in English, Spanish, and Portuguese
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.utils import timezone
from datetime import timedelta, date
from decimal import Decimal

# Import models
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.tours.models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight,
    TourItinerary, TourInclusion, TourDeparture, TourFAQ, EarlyBookingOffer
)
from apps.blog.models import Category as BlogCategory, Tag, Post
from apps.contact.models import FAQ, Office, Statistic
from apps.reviews.models import Review, Testimonial


def seed_destinations():
    """Create destinations with multilingual content."""
    print("[*] Creating Destinations...")

    destinations_data = [
        {
            'name': 'Cairo',
            'name_es': 'El Cairo',
            'name_pt': 'Cairo',
            'tagline': 'Where Ancient Wonders Meet Modern Life',
            'tagline_es': 'Donde las Maravillas Antiguas se Encuentran con la Vida Moderna',
            'tagline_pt': 'Onde as Maravilhas Antigas Encontram a Vida Moderna',
            'description': '''Cairo, the sprawling capital of Egypt, is a city that perfectly blends ancient history with vibrant modern life. Home to the iconic Pyramids of Giza and the Sphinx, Cairo offers visitors an unparalleled journey through time.

The city's famous Egyptian Museum houses the world's largest collection of Pharaonic antiquities, including the treasures of Tutankhamun. Wander through the bustling Khan el-Khalili bazaar, where you can find everything from handcrafted jewelry to aromatic spices.

Cairo's Islamic Cairo district features stunning medieval architecture, including the Al-Azhar Mosque and the Citadel of Saladin. The city also offers excellent dining, from traditional Egyptian cuisine to international restaurants along the Nile.''',
            'description_es': '''El Cairo, la extensa capital de Egipto, es una ciudad que combina perfectamente la historia antigua con la vibrante vida moderna. Hogar de las icónicas Pirámides de Giza y la Esfinge, El Cairo ofrece a los visitantes un viaje incomparable a través del tiempo.

El famoso Museo Egipcio de la ciudad alberga la mayor colección del mundo de antigüedades faraónicas, incluyendo los tesoros de Tutankamón. Pasee por el bullicioso bazar de Khan el-Khalili, donde puede encontrar desde joyas artesanales hasta especias aromáticas.

El distrito del Cairo Islámico presenta una impresionante arquitectura medieval, incluyendo la Mezquita de Al-Azhar y la Ciudadela de Saladino. La ciudad también ofrece excelente gastronomía, desde cocina tradicional egipcia hasta restaurantes internacionales a lo largo del Nilo.''',
            'description_pt': '''O Cairo, a extensa capital do Egito, é uma cidade que combina perfeitamente a história antiga com a vibrante vida moderna. Lar das icônicas Pirâmides de Gizé e da Esfinge, o Cairo oferece aos visitantes uma jornada incomparável através do tempo.

O famoso Museu Egípcio da cidade abriga a maior coleção do mundo de antiguidades faraônicas, incluindo os tesouros de Tutancâmon. Passeie pelo movimentado bazar Khan el-Khalili, onde você pode encontrar desde joias artesanais até especiarias aromáticas.

O distrito do Cairo Islâmico apresenta uma impressionante arquitetura medieval, incluindo a Mesquita de Al-Azhar e a Cidadela de Saladino. A cidade também oferece excelente gastronomia, desde cozinha tradicional egípcia até restaurantes internacionais ao longo do Nilo.''',
            'country': 'Egypt',
            'region': 'Lower Egypt',
            'latitude': Decimal('30.0444'),
            'longitude': Decimal('31.2357'),
            'best_time_to_visit': 'October to April when temperatures are mild',
            'is_featured': True,
        },
        {
            'name': 'Luxor',
            'name_es': 'Lúxor',
            'name_pt': 'Luxor',
            'tagline': "The World's Greatest Open-Air Museum",
            'tagline_es': 'El Mayor Museo al Aire Libre del Mundo',
            'tagline_pt': 'O Maior Museu ao Ar Livre do Mundo',
            'description': '''Luxor, often called the world's greatest open-air museum, stands on the site of ancient Thebes, the pharaohs' capital during the height of their power.

The city is divided by the Nile into the East Bank, where the living resided, and the West Bank, where the dead were buried. The East Bank features the magnificent Karnak Temple, the largest religious building ever constructed, and the elegant Luxor Temple.

On the West Bank, explore the Valley of the Kings, where pharaohs were buried for nearly 500 years, including the tomb of Tutankhamun. Visit the stunning Temple of Hatshepsut and the Colossi of Memnon. Hot air balloon rides at sunrise offer breathtaking views of these ancient wonders.''',
            'description_es': '''Lúxor, a menudo llamado el mayor museo al aire libre del mundo, se encuentra en el sitio de la antigua Tebas, la capital de los faraones durante el apogeo de su poder.

La ciudad está dividida por el Nilo en la Orilla Este, donde residían los vivos, y la Orilla Oeste, donde se enterraba a los muertos. La Orilla Este presenta el magnífico Templo de Karnak, el edificio religioso más grande jamás construido, y el elegante Templo de Lúxor.

En la Orilla Oeste, explore el Valle de los Reyes, donde los faraones fueron enterrados durante casi 500 años, incluyendo la tumba de Tutankamón. Visite el impresionante Templo de Hatshepsut y los Colosos de Memnón. Los paseos en globo aerostático al amanecer ofrecen vistas impresionantes de estas maravillas antiguas.''',
            'description_pt': '''Luxor, frequentemente chamada de o maior museu ao ar livre do mundo, está no local da antiga Tebas, a capital dos faraós durante o auge de seu poder.

A cidade é dividida pelo Nilo na Margem Leste, onde os vivos residiam, e na Margem Oeste, onde os mortos eram enterrados. A Margem Leste apresenta o magnífico Templo de Karnak, o maior edifício religioso já construído, e o elegante Templo de Luxor.

Na Margem Oeste, explore o Vale dos Reis, onde os faraós foram enterrados por quase 500 anos, incluindo a tumba de Tutancâmon. Visite o deslumbrante Templo de Hatshepsut e os Colossos de Memnon. Passeios de balão ao nascer do sol oferecem vistas deslumbrantes dessas maravilhas antigas.''',
            'country': 'Egypt',
            'region': 'Upper Egypt',
            'latitude': Decimal('25.6872'),
            'longitude': Decimal('32.6396'),
            'best_time_to_visit': 'October to April for comfortable weather',
            'is_featured': True,
        },
        {
            'name': 'Aswan',
            'name_es': 'Asuán',
            'name_pt': 'Assuã',
            'tagline': 'Gateway to Ancient Nubia',
            'tagline_es': 'Puerta de Entrada a la Antigua Nubia',
            'tagline_pt': 'Portal para a Antiga Núbia',
            'description': '''Aswan, Egypt's sunniest southern city, offers a more relaxed pace than Cairo and Luxor. This beautiful city sits on the banks of the Nile, surrounded by golden sand dunes and dotted with lush islands.

The city is famous for the Aswan High Dam, a modern engineering marvel that created Lake Nasser. Visit the beautiful Philae Temple, dedicated to the goddess Isis, which was relocated to save it from the rising waters.

Take a felucca ride around Elephantine Island, visit the Nubian villages with their colorful houses, or explore the ancient quarries where the unfinished obelisk still lies. Day trips to the magnificent Abu Simbel temples are a must.''',
            'description_es': '''Asuán, la ciudad más soleada del sur de Egipto, ofrece un ritmo más relajado que El Cairo y Lúxor. Esta hermosa ciudad se encuentra a orillas del Nilo, rodeada de dunas de arena dorada y salpicada de exuberantes islas.

La ciudad es famosa por la Presa Alta de Asuán, una maravilla de ingeniería moderna que creó el Lago Nasser. Visite el hermoso Templo de Filae, dedicado a la diosa Isis, que fue reubicado para salvarlo de las aguas crecientes.

Dé un paseo en feluca alrededor de la Isla Elefantina, visite los pueblos nubios con sus casas coloridas, o explore las antiguas canteras donde aún yace el obelisco inacabado. Las excursiones de un día a los magníficos templos de Abu Simbel son imprescindibles.''',
            'description_pt': '''Assuã, a cidade mais ensolarada do sul do Egito, oferece um ritmo mais relaxado que o Cairo e Luxor. Esta bela cidade fica às margens do Nilo, cercada por dunas de areia dourada e pontilhada de ilhas exuberantes.

A cidade é famosa pela Barragem Alta de Assuã, uma maravilha da engenharia moderna que criou o Lago Nasser. Visite o belo Templo de Philae, dedicado à deusa Ísis, que foi relocado para salvá-lo das águas crescentes.

Faça um passeio de felucca ao redor da Ilha Elefantina, visite as aldeias núbias com suas casas coloridas, ou explore as antigas pedreiras onde o obelisco inacabado ainda repousa. Excursões de um dia aos magníficos templos de Abu Simbel são imperdíveis.''',
            'country': 'Egypt',
            'region': 'Upper Egypt',
            'latitude': Decimal('24.0889'),
            'longitude': Decimal('32.8998'),
            'best_time_to_visit': 'November to March for cooler temperatures',
            'is_featured': True,
        },
        {
            'name': 'Hurghada',
            'name_es': 'Hurghada',
            'name_pt': 'Hurghada',
            'tagline': 'Red Sea Paradise',
            'tagline_es': 'Paraíso del Mar Rojo',
            'tagline_pt': 'Paraíso do Mar Vermelho',
            'description': '''Hurghada, once a small fishing village, has transformed into Egypt's premier Red Sea resort destination. With its crystal-clear waters, vibrant coral reefs, and year-round sunshine, it's a paradise for beach lovers and water sports enthusiasts.

The Red Sea offers some of the world's best diving and snorkeling, with colorful coral gardens teeming with tropical fish, dolphins, and even the occasional sea turtle. Popular dive sites include Giftun Island and the famous wrecks.

Beyond the beach, Hurghada offers desert adventures including quad biking, camel rides, and Bedouin dinners under the stars. The town has a lively marina with restaurants and cafes, and easy access to day trips to Luxor.''',
            'description_es': '''Hurghada, que una vez fue un pequeño pueblo pesquero, se ha transformado en el principal destino turístico del Mar Rojo de Egipto. Con sus aguas cristalinas, vibrantes arrecifes de coral y sol durante todo el año, es un paraíso para los amantes de la playa y los entusiastas de los deportes acuáticos.

El Mar Rojo ofrece algunos de los mejores buceos y snorkel del mundo, con coloridos jardines de coral repletos de peces tropicales, delfines e incluso alguna tortuga marina ocasional. Los sitios de buceo populares incluyen la Isla Giftun y los famosos naufragios.

Más allá de la playa, Hurghada ofrece aventuras en el desierto que incluyen paseos en quad, paseos en camello y cenas beduinas bajo las estrellas. La ciudad tiene un animado puerto deportivo con restaurantes y cafés, y fácil acceso a excursiones de un día a Lúxor.''',
            'description_pt': '''Hurghada, que já foi uma pequena vila de pescadores, transformou-se no principal destino turístico do Mar Vermelho do Egito. Com suas águas cristalinas, vibrantes recifes de coral e sol o ano todo, é um paraíso para amantes de praia e entusiastas de esportes aquáticos.

O Mar Vermelho oferece alguns dos melhores mergulhos e snorkeling do mundo, com coloridos jardins de coral repletos de peixes tropicais, golfinhos e até tartarugas marinhas ocasionais. Locais populares de mergulho incluem a Ilha Giftun e os famosos naufrágios.

Além da praia, Hurghada oferece aventuras no deserto, incluindo passeios de quadriciclo, passeios de camelo e jantares beduínos sob as estrelas. A cidade tem uma marina animada com restaurantes e cafés, e fácil acesso a excursões de um dia para Luxor.''',
            'country': 'Egypt',
            'region': 'Red Sea',
            'latitude': Decimal('27.2579'),
            'longitude': Decimal('33.8116'),
            'best_time_to_visit': 'March to May and September to November',
            'is_featured': True,
        },
        {
            'name': 'Sharm El Sheikh',
            'name_es': 'Sharm El Sheikh',
            'name_pt': 'Sharm El Sheikh',
            'tagline': 'Jewel of the Sinai',
            'tagline_es': 'Joya del Sinaí',
            'tagline_pt': 'Jóia do Sinai',
            'description': '''Sharm El Sheikh, located at the southern tip of the Sinai Peninsula, is one of the world's premier diving destinations. The waters here are home to over 250 species of coral and countless marine creatures.

Ras Mohammed National Park offers spectacular diving with dramatic drop-offs and pristine reefs. The famous Tiran Island is accessible by boat and offers encounters with reef sharks and massive schools of fish. Naama Bay is the heart of the resort area, with shops, restaurants, and nightlife.

Beyond diving, Sharm is the gateway to Mount Sinai, where Moses is said to have received the Ten Commandments. The sunrise hike to the summit and visit to St. Catherine's Monastery is a spiritual journey not to be missed.''',
            'description_es': '''Sharm El Sheikh, ubicado en el extremo sur de la Península del Sinaí, es uno de los principales destinos de buceo del mundo. Las aguas aquí albergan más de 250 especies de coral e innumerables criaturas marinas.

El Parque Nacional de Ras Mohammed ofrece buceo espectacular con dramáticos acantilados y arrecifes prístinos. La famosa Isla Tiran es accesible en barco y ofrece encuentros con tiburones de arrecife y enormes cardúmenes de peces. Naama Bay es el corazón de la zona turística, con tiendas, restaurantes y vida nocturna.

Más allá del buceo, Sharm es la puerta de entrada al Monte Sinaí, donde se dice que Moisés recibió los Diez Mandamientos. La caminata al amanecer hasta la cumbre y la visita al Monasterio de Santa Catalina es un viaje espiritual que no debe perderse.''',
            'description_pt': '''Sharm El Sheikh, localizada na ponta sul da Península do Sinai, é um dos principais destinos de mergulho do mundo. As águas aqui abrigam mais de 250 espécies de coral e inúmeras criaturas marinhas.

O Parque Nacional de Ras Mohammed oferece mergulho espetacular com dramáticas paredes e recifes intocados. A famosa Ilha Tiran é acessível de barco e oferece encontros com tubarões de recife e enormes cardumes de peixes. Naama Bay é o coração da área de resort, com lojas, restaurantes e vida noturna.

Além do mergulho, Sharm é o portal para o Monte Sinai, onde se diz que Moisés recebeu os Dez Mandamentos. A caminhada ao nascer do sol até o cume e a visita ao Mosteiro de Santa Catarina é uma jornada espiritual imperdível.''',
            'country': 'Egypt',
            'region': 'Sinai',
            'latitude': Decimal('27.9158'),
            'longitude': Decimal('34.3300'),
            'best_time_to_visit': 'Year-round, best diving March to May',
            'is_featured': True,
        },
        {
            'name': 'Alexandria',
            'name_es': 'Alejandría',
            'name_pt': 'Alexandria',
            'tagline': 'Pearl of the Mediterranean',
            'tagline_es': 'Perla del Mediterráneo',
            'tagline_pt': 'Pérola do Mediterrâneo',
            'description': '''Alexandria, founded by Alexander the Great in 331 BC, was once home to one of the Seven Wonders of the Ancient World - the great Lighthouse of Pharos. Today, this Mediterranean city offers a unique blend of ancient history and seaside charm.

The modern Bibliotheca Alexandrina honors the legacy of the ancient Library of Alexandria, once the largest in the world. Visit the Catacombs of Kom El Shoqafa, a remarkable Greco-Roman necropolis, and explore Pompey's Pillar, a towering red granite column.

Stroll along the Corniche, Alexandria's beautiful waterfront promenade, visit the stunning Montaza Palace gardens, and experience the city's famous café culture. The fish restaurants along the harbor serve some of Egypt's freshest seafood.''',
            'description_es': '''Alejandría, fundada por Alejandro Magno en el 331 a.C., fue una vez el hogar de una de las Siete Maravillas del Mundo Antiguo: el gran Faro de Faros. Hoy, esta ciudad mediterránea ofrece una combinación única de historia antigua y encanto costero.

La moderna Biblioteca de Alejandría honra el legado de la antigua Biblioteca de Alejandría, que fue la más grande del mundo. Visite las Catacumbas de Kom El Shoqafa, una notable necrópolis grecorromana, y explore el Pilar de Pompeyo, una imponente columna de granito rojo.

Pasee por la Corniche, el hermoso paseo marítimo de Alejandría, visite los impresionantes jardines del Palacio de Montaza y experimente la famosa cultura de cafés de la ciudad. Los restaurantes de pescado a lo largo del puerto sirven algunos de los mariscos más frescos de Egipto.''',
            'description_pt': '''Alexandria, fundada por Alexandre, o Grande, em 331 a.C., foi uma vez o lar de uma das Sete Maravilhas do Mundo Antigo - o grande Farol de Faros. Hoje, esta cidade mediterrânea oferece uma combinação única de história antiga e charme à beira-mar.

A moderna Bibliotheca Alexandrina honra o legado da antiga Biblioteca de Alexandria, que já foi a maior do mundo. Visite as Catacumbas de Kom El Shoqafa, uma notável necrópole greco-romana, e explore o Pilar de Pompeu, uma imponente coluna de granito vermelho.

Passeie pela Corniche, o belo calçadão à beira-mar de Alexandria, visite os deslumbrantes jardins do Palácio Montaza e experimente a famosa cultura de cafés da cidade. Os restaurantes de peixe ao longo do porto servem alguns dos frutos do mar mais frescos do Egito.''',
            'country': 'Egypt',
            'region': 'Mediterranean Coast',
            'latitude': Decimal('31.2001'),
            'longitude': Decimal('29.9187'),
            'best_time_to_visit': 'April to June and September to November',
            'is_featured': True,
        },
        {
            'name': 'Siwa Oasis',
            'name_es': 'Oasis de Siwa',
            'name_pt': 'Oásis de Siwa',
            'tagline': 'Desert Paradise of Tranquility',
            'tagline_es': 'Paraíso Desértico de Tranquilidad',
            'tagline_pt': 'Paraíso Desértico de Tranquilidade',
            'description': '''Siwa Oasis, located in Egypt's Western Desert near the Libyan border, is one of the most isolated and magical places in the country. This lush oasis, surrounded by date palms and olive groves, has maintained its unique Berber culture for thousands of years.

Alexander the Great famously visited the Oracle of Amun here to confirm his divine status. Today, you can explore the ruins of the Temple of the Oracle and the ancient fortress of Shali. The oasis is known for its natural springs, including Cleopatra's Spring, where legend says the queen herself bathed.

Experience the Great Sand Sea, one of the world's largest dune fields, on a 4x4 safari adventure. Camp under the stars, sandboard down massive dunes, and witness spectacular sunsets over the endless desert landscape.''',
            'description_es': '''El Oasis de Siwa, ubicado en el desierto occidental de Egipto cerca de la frontera libia, es uno de los lugares más aislados y mágicos del país. Este exuberante oasis, rodeado de palmeras datileras y olivares, ha mantenido su cultura bereber única durante miles de años.

Alejandro Magno visitó famosamente el Oráculo de Amón aquí para confirmar su estatus divino. Hoy, puede explorar las ruinas del Templo del Oráculo y la antigua fortaleza de Shali. El oasis es conocido por sus manantiales naturales, incluyendo el Manantial de Cleopatra, donde la leyenda dice que la propia reina se bañó.

Experimente el Gran Mar de Arena, uno de los campos de dunas más grandes del mundo, en una aventura de safari en 4x4. Acampe bajo las estrellas, haga sandboard por dunas masivas y sea testigo de espectaculares puestas de sol sobre el interminable paisaje desértico.''',
            'description_pt': '''O Oásis de Siwa, localizado no deserto ocidental do Egito perto da fronteira líbia, é um dos lugares mais isolados e mágicos do país. Este oásis exuberante, cercado por palmeiras de tâmaras e olivais, manteve sua cultura berbere única por milhares de anos.

Alexandre, o Grande, visitou o famoso Oráculo de Amon aqui para confirmar seu status divino. Hoje, você pode explorar as ruínas do Templo do Oráculo e a antiga fortaleza de Shali. O oásis é conhecido por suas nascentes naturais, incluindo a Nascente de Cleópatra, onde a lenda diz que a própria rainha se banhou.

Experimente o Grande Mar de Areia, um dos maiores campos de dunas do mundo, em uma aventura de safari 4x4. Acampe sob as estrelas, faça sandboard em dunas massivas e testemunhe espetaculares pores do sol sobre a paisagem desértica infinita.''',
            'country': 'Egypt',
            'region': 'Western Desert',
            'latitude': Decimal('29.2032'),
            'longitude': Decimal('25.5195'),
            'best_time_to_visit': 'October to April for comfortable desert temperatures',
            'is_featured': False,
        },
        {
            'name': 'Dahab',
            'name_es': 'Dahab',
            'name_pt': 'Dahab',
            'tagline': 'Bohemian Beach Paradise',
            'tagline_es': 'Paraíso Playero Bohemio',
            'tagline_pt': 'Paraíso de Praia Boêmio',
            'description': '''Dahab, meaning "gold" in Arabic, is a laid-back beach town on the Gulf of Aqaba that has become a favorite among backpackers, divers, and adventure seekers. Unlike the more developed resorts, Dahab retains a relaxed, bohemian atmosphere.

The town is famous for the Blue Hole, one of the world's most iconic dive sites. This 130-meter deep underwater sinkhole attracts advanced divers from around the globe. For beginners, the calm waters and colorful reefs along the coast offer excellent snorkeling and intro diving.

Dahab is also a world-renowned windsurfing and kitesurfing destination. When you're not in the water, relax in one of the many beachfront cafes, explore the colored canyons of the Sinai, or join a desert safari to meet local Bedouin communities.''',
            'description_es': '''Dahab, que significa "oro" en árabe, es una tranquila ciudad playera en el Golfo de Aqaba que se ha convertido en favorita entre mochileros, buceadores y buscadores de aventuras. A diferencia de los resorts más desarrollados, Dahab conserva una atmósfera relajada y bohemia.

La ciudad es famosa por el Blue Hole, uno de los sitios de buceo más icónicos del mundo. Este sumidero submarino de 130 metros de profundidad atrae a buceadores avanzados de todo el mundo. Para principiantes, las aguas tranquilas y los coloridos arrecifes a lo largo de la costa ofrecen excelente snorkel y buceo introductorio.

Dahab también es un destino de windsurf y kitesurf de renombre mundial. Cuando no esté en el agua, relájese en uno de los muchos cafés frente a la playa, explore los cañones de colores del Sinaí, o únase a un safari por el desierto para conocer a las comunidades beduinas locales.''',
            'description_pt': '''Dahab, que significa "ouro" em árabe, é uma tranquila cidade praiana no Golfo de Aqaba que se tornou favorita entre mochileiros, mergulhadores e aventureiros. Ao contrário dos resorts mais desenvolvidos, Dahab mantém uma atmosfera relaxada e boêmia.

A cidade é famosa pelo Blue Hole, um dos locais de mergulho mais icônicos do mundo. Este sumidouro submarino de 130 metros de profundidade atrai mergulhadores avançados de todo o mundo. Para iniciantes, as águas calmas e os recifes coloridos ao longo da costa oferecem excelente snorkeling e mergulho introdutório.

Dahab também é um destino de windsurf e kitesurf de renome mundial. Quando você não estiver na água, relaxe em um dos muitos cafés à beira-mar, explore os cânions coloridos do Sinai ou participe de um safari no deserto para conhecer as comunidades beduínas locais.''',
            'country': 'Egypt',
            'region': 'Sinai',
            'latitude': Decimal('28.5091'),
            'longitude': Decimal('34.5145'),
            'best_time_to_visit': 'Year-round, best for diving April to November',
            'is_featured': False,
        },
    ]

    for data in destinations_data:
        dest, created = Destination.objects.update_or_create(
            name=data['name'],
            defaults=data
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {dest.name}")

    print(f"  Total: {len(destinations_data)} destinations\n")
    return Destination.objects.all()


def seed_tour_categories():
    """Create tour categories with multilingual content."""
    print("[*] Creating Tour Categories...")

    categories_data = [
        {
            'name': 'Cultural & Historical',
            'name_es': 'Cultural e Histórico',
            'name_pt': 'Cultural e Histórico',
            'description': 'Explore ancient temples, tombs, and monuments that tell the story of Egypt\'s 5,000-year history.',
            'description_es': 'Explore templos antiguos, tumbas y monumentos que cuentan la historia de los 5.000 años de Egipto.',
            'description_pt': 'Explore templos antigos, túmulos e monumentos que contam a história dos 5.000 anos do Egito.',
            'icon': 'landmark',
            'is_active': True,
        },
        {
            'name': 'Adventure & Safari',
            'name_es': 'Aventura y Safari',
            'name_pt': 'Aventura e Safari',
            'description': 'Thrilling desert expeditions, 4x4 safaris, camel treks, and outdoor adventures.',
            'description_es': 'Emocionantes expediciones por el desierto, safaris en 4x4, excursiones en camello y aventuras al aire libre.',
            'description_pt': 'Emocionantes expedições no deserto, safaris de 4x4, passeios de camelo e aventuras ao ar livre.',
            'icon': 'compass',
            'is_active': True,
        },
        {
            'name': 'Beach & Diving',
            'name_es': 'Playa y Buceo',
            'name_pt': 'Praia e Mergulho',
            'description': 'Discover the underwater wonders of the Red Sea with world-class diving and pristine beaches.',
            'description_es': 'Descubra las maravillas submarinas del Mar Rojo con buceo de clase mundial y playas prístinas.',
            'description_pt': 'Descubra as maravilhas submarinas do Mar Vermelho com mergulho de classe mundial e praias intocadas.',
            'icon': 'waves',
            'is_active': True,
        },
        {
            'name': 'Nile Cruises',
            'name_es': 'Cruceros por el Nilo',
            'name_pt': 'Cruzeiros no Nilo',
            'description': 'Sail the legendary Nile River in style aboard luxury cruises and traditional feluccas.',
            'description_es': 'Navegue por el legendario río Nilo con estilo a bordo de cruceros de lujo y tradicionales felucas.',
            'description_pt': 'Navegue pelo lendário rio Nilo com estilo a bordo de cruzeiros de luxo e tradicionais feluccas.',
            'icon': 'ship',
            'is_active': True,
        },
        {
            'name': 'Family Friendly',
            'name_es': 'Familiar',
            'name_pt': 'Familiar',
            'description': 'Specially designed tours for families with children, featuring educational and fun activities.',
            'description_es': 'Tours especialmente diseñados para familias con niños, con actividades educativas y divertidas.',
            'description_pt': 'Tours especialmente projetados para famílias com crianças, com atividades educativas e divertidas.',
            'icon': 'users',
            'is_active': True,
        },
        {
            'name': 'Luxury',
            'name_es': 'Lujo',
            'name_pt': 'Luxo',
            'description': 'Premium experiences with 5-star accommodations, private guides, and exclusive access.',
            'description_es': 'Experiencias premium con alojamiento de 5 estrellas, guías privados y acceso exclusivo.',
            'description_pt': 'Experiências premium com acomodações 5 estrelas, guias privados e acesso exclusivo.',
            'icon': 'crown',
            'is_active': True,
        },
        {
            'name': 'Religious & Spiritual',
            'name_es': 'Religioso y Espiritual',
            'name_pt': 'Religioso e Espiritual',
            'description': 'Visit sacred sites from Christian, Islamic, and ancient Egyptian religious traditions.',
            'description_es': 'Visite sitios sagrados de las tradiciones religiosas cristiana, islámica y del antiguo Egipto.',
            'description_pt': 'Visite locais sagrados das tradições religiosas cristã, islâmica e do antigo Egito.',
            'icon': 'church',
            'is_active': True,
        },
        {
            'name': 'Wellness & Relaxation',
            'name_es': 'Bienestar y Relajación',
            'name_pt': 'Bem-estar e Relaxamento',
            'description': 'Rejuvenating spa retreats, yoga experiences, and relaxing getaways.',
            'description_es': 'Retiros de spa rejuvenecedores, experiencias de yoga y escapadas relajantes.',
            'description_pt': 'Retiros de spa rejuvenescedores, experiências de yoga e escapadas relaxantes.',
            'icon': 'spa',
            'is_active': True,
        },
    ]

    for i, data in enumerate(categories_data):
        data['sort_order'] = i
        cat, created = TourCategory.objects.update_or_create(
            name=data['name'],
            defaults=data
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {cat.name}")

    print(f"  Total: {len(categories_data)} categories\n")


def seed_tour_types():
    """Create tour types with multilingual content."""
    print("[*] Creating Tour Types...")

    types_data = [
        {
            'name': 'Multi-Day Package',
            'name_es': 'Paquete de Varios Días',
            'name_pt': 'Pacote de Vários Dias',
            'description': 'Comprehensive tours spanning multiple days with accommodations included.',
            'icon': 'calendar',
            'is_active': True,
        },
        {
            'name': 'Day Trip',
            'name_es': 'Excursión de un Día',
            'name_pt': 'Passeio de um Dia',
            'description': 'Single-day excursions to popular destinations and attractions.',
            'icon': 'sun',
            'is_active': True,
        },
        {
            'name': 'Nile Cruise',
            'name_es': 'Crucero por el Nilo',
            'name_pt': 'Cruzeiro no Nilo',
            'description': 'Cruise along the Nile River with onboard accommodations and guided temple visits.',
            'icon': 'anchor',
            'is_active': True,
        },
        {
            'name': 'Private Tour',
            'name_es': 'Tour Privado',
            'name_pt': 'Tour Privado',
            'description': 'Exclusive private tours with personal guide and customizable itinerary.',
            'icon': 'user-check',
            'is_active': True,
        },
        {
            'name': 'Small Group',
            'name_es': 'Grupo Pequeño',
            'name_pt': 'Grupo Pequeno',
            'description': 'Intimate group experiences with maximum 12 travelers.',
            'icon': 'users',
            'is_active': True,
        },
        {
            'name': 'Shore Excursion',
            'name_es': 'Excursión en Puerto',
            'name_pt': 'Excursão em Porto',
            'description': 'Perfect for cruise ship passengers with timed returns to port.',
            'icon': 'ship',
            'is_active': True,
        },
    ]

    for i, data in enumerate(types_data):
        data['sort_order'] = i
        tour_type, created = TourType.objects.update_or_create(
            name=data['name'],
            defaults=data
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {tour_type.name}")

    print(f"  Total: {len(types_data)} types\n")


def seed_tours():
    """Create tours with full multilingual content."""
    print("[*] Creating Tours...")

    # Get references
    cultural_cat = TourCategory.objects.filter(name__icontains='Cultural').first()
    nile_cat = TourCategory.objects.filter(name__icontains='Nile').first()
    adventure_cat = TourCategory.objects.filter(name__icontains='Adventure').first()
    beach_cat = TourCategory.objects.filter(name__icontains='Beach').first()

    package_type = TourType.objects.filter(name__icontains='Package').first()
    cruise_type = TourType.objects.filter(name__icontains='Cruise').first()
    day_trip_type = TourType.objects.filter(name__icontains='Day').first()

    cairo = Destination.objects.filter(name='Cairo').first()
    luxor = Destination.objects.filter(name='Luxor').first()
    aswan = Destination.objects.filter(name='Aswan').first()
    hurghada = Destination.objects.filter(name='Hurghada').first()

    tours_data = [
        {
            'name': 'Classic Egypt: Cairo, Luxor & Aswan',
            'name_es': 'Egipto Clásico: El Cairo, Lúxor y Asuán',
            'name_pt': 'Egito Clássico: Cairo, Luxor e Assuã',
            'short_description': 'Experience the best of ancient Egypt in 8 unforgettable days',
            'short_description_es': 'Experimente lo mejor del antiguo Egipto en 8 días inolvidables',
            'short_description_pt': 'Experimente o melhor do antigo Egito em 8 dias inesquecíveis',
            'description': '''Embark on the ultimate Egyptian adventure with our Classic Egypt tour. This carefully crafted 8-day journey takes you through the heart of ancient Egyptian civilization, from the iconic Pyramids of Giza to the stunning temples of Upper Egypt.

**Highlights:**
- Marvel at the Great Pyramids and Sphinx in Giza
- Explore the world-famous Egyptian Museum
- Cruise the Nile in comfort aboard a 5-star ship
- Discover the Valley of the Kings in Luxor
- Visit the magnificent temples of Karnak and Luxor
- Experience the beauty of Aswan and Philae Temple
- Optional: Hot air balloon ride over Luxor

This tour offers the perfect balance of guided exploration and leisure time, with expert Egyptologists bringing history to life at every stop.''',
            'description_es': '''Embárquese en la aventura egipcia definitiva con nuestro tour Egipto Clásico. Este viaje de 8 días cuidadosamente elaborado le lleva a través del corazón de la civilización del antiguo Egipto, desde las icónicas Pirámides de Giza hasta los impresionantes templos del Alto Egipto.

**Destacados:**
- Maravíllese con las Grandes Pirámides y la Esfinge en Giza
- Explore el mundialmente famoso Museo Egipcio
- Navegue por el Nilo con comodidad a bordo de un barco de 5 estrellas
- Descubra el Valle de los Reyes en Lúxor
- Visite los magníficos templos de Karnak y Lúxor
- Experimente la belleza de Asuán y el Templo de Filae
- Opcional: Paseo en globo aerostático sobre Lúxor

Este tour ofrece el equilibrio perfecto entre exploración guiada y tiempo libre, con egiptólogos expertos que dan vida a la historia en cada parada.''',
            'description_pt': '''Embarque na aventura egípcia definitiva com nosso tour Egito Clássico. Esta jornada de 8 dias cuidadosamente elaborada leva você através do coração da civilização do antigo Egito, desde as icônicas Pirâmides de Gizé até os deslumbrantes templos do Alto Egito.

**Destaques:**
- Maravilhe-se com as Grandes Pirâmides e a Esfinge em Gizé
- Explore o mundialmente famoso Museu Egípcio
- Navegue pelo Nilo com conforto a bordo de um navio 5 estrelas
- Descubra o Vale dos Reis em Luxor
- Visite os magníficos templos de Karnak e Luxor
- Experimente a beleza de Assuã e o Templo de Philae
- Opcional: Passeio de balão sobre Luxor

Este tour oferece o equilíbrio perfeito entre exploração guiada e tempo livre, com egiptólogos especializados que dão vida à história em cada parada.''',
            'category': cultural_cat,
            'tour_type': package_type,
            'days': 8,
            'nights': 7,
            'price': Decimal('1299.00'),
            'price_single_supplement': Decimal('350.00'),
            'child_price': Decimal('799.00'),
            'is_featured': True,
            'is_best_seller': True,
            'difficulty_level': 'easy',
            'departure_city': 'Cairo',
            'languages': 'English, Spanish, Portuguese, French, German, Italian',
        },
        {
            'name': 'Nile Cruise: Luxor to Aswan',
            'name_es': 'Crucero por el Nilo: Lúxor a Asuán',
            'name_pt': 'Cruzeiro no Nilo: Luxor a Assuã',
            'short_description': 'Sail the timeless Nile on a luxurious 5-star cruise experience',
            'short_description_es': 'Navegue por el eterno Nilo en una lujosa experiencia de crucero 5 estrellas',
            'short_description_pt': 'Navegue pelo eterno Nilo em uma luxuosa experiência de cruzeiro 5 estrelas',
            'description': '''Experience the magic of the Nile on our luxurious 4-night cruise from Luxor to Aswan. Sail aboard a 5-star vessel while visiting the most remarkable temples and tombs of ancient Egypt.

**Your Journey Includes:**
- 4 nights full board on a 5-star Nile cruise ship
- All temple entrance fees
- Expert Egyptologist guide throughout
- Visit to Valley of the Kings
- Karnak and Luxor Temples
- Edfu Temple (Horus)
- Kom Ombo Temple
- Philae Temple in Aswan
- High Dam visit
- All transfers and porterage

Enjoy fine dining, evening entertainment, and stunning views as you trace the path of pharaohs along the world's longest river.''',
            'description_es': '''Experimente la magia del Nilo en nuestro lujoso crucero de 4 noches desde Lúxor hasta Asuán. Navegue a bordo de un barco 5 estrellas mientras visita los templos y tumbas más notables del antiguo Egipto.

**Su Viaje Incluye:**
- 4 noches pensión completa en un crucero 5 estrellas por el Nilo
- Todas las entradas a los templos
- Guía egiptólogo experto durante todo el recorrido
- Visita al Valle de los Reyes
- Templos de Karnak y Lúxor
- Templo de Edfu (Horus)
- Templo de Kom Ombo
- Templo de Filae en Asuán
- Visita a la Presa Alta
- Todos los traslados y porteo

Disfrute de la alta gastronomía, entretenimiento nocturno y vistas impresionantes mientras sigue el camino de los faraones a lo largo del río más largo del mundo.''',
            'description_pt': '''Experimente a magia do Nilo em nosso luxuoso cruzeiro de 4 noites de Luxor a Assuã. Navegue a bordo de um navio 5 estrelas enquanto visita os templos e túmulos mais notáveis do antigo Egito.

**Sua Jornada Inclui:**
- 4 noites de pensão completa em um cruzeiro 5 estrelas pelo Nilo
- Todas as taxas de entrada dos templos
- Guia egiptólogo especializado durante todo o percurso
- Visita ao Vale dos Reis
- Templos de Karnak e Luxor
- Templo de Edfu (Horus)
- Templo de Kom Ombo
- Templo de Philae em Assuã
- Visita à Barragem Alta
- Todos os traslados e carregamento de bagagem

Desfrute de alta gastronomia, entretenimento noturno e vistas deslumbrantes enquanto traça o caminho dos faraós ao longo do rio mais longo do mundo.''',
            'category': nile_cat,
            'tour_type': cruise_type,
            'days': 5,
            'nights': 4,
            'price': Decimal('899.00'),
            'price_single_supplement': Decimal('250.00'),
            'child_price': Decimal('499.00'),
            'is_featured': True,
            'is_best_seller': True,
            'difficulty_level': 'easy',
            'departure_city': 'Luxor',
            'languages': 'English, Spanish, Portuguese, French, German',
        },
        {
            'name': 'Pyramids & Sphinx Day Tour',
            'name_es': 'Tour de un Día: Pirámides y Esfinge',
            'name_pt': 'Tour de um Dia: Pirâmides e Esfinge',
            'short_description': 'Explore the iconic Pyramids of Giza and the mysterious Sphinx',
            'short_description_es': 'Explore las icónicas Pirámides de Giza y la misteriosa Esfinge',
            'short_description_pt': 'Explore as icônicas Pirâmides de Gizé e a misteriosa Esfinge',
            'description': '''Discover the last remaining Wonder of the Ancient World on our comprehensive Pyramids day tour. This expertly guided experience brings you face to face with 4,500 years of history.

**Tour Highlights:**
- Giza Pyramids Complex (Khufu, Khafre, Menkaure)
- The Great Sphinx
- Valley Temple
- Panoramic photo stops
- Egyptian Museum (treasures of Tutankhamun)
- Traditional Egyptian lunch included
- Optional: Camel ride around the pyramids

Our expert Egyptologist will share fascinating insights about how these monuments were built and the mysteries that still surround them today.''',
            'description_es': '''Descubra la última Maravilla del Mundo Antiguo que queda en pie en nuestro completo tour de las Pirámides. Esta experiencia guiada por expertos le pone cara a cara con 4.500 años de historia.

**Destacados del Tour:**
- Complejo de las Pirámides de Giza (Keops, Kefrén, Micerinos)
- La Gran Esfinge
- Templo del Valle
- Paradas para fotos panorámicas
- Museo Egipcio (tesoros de Tutankamón)
- Almuerzo tradicional egipcio incluido
- Opcional: Paseo en camello alrededor de las pirámides

Nuestro egiptólogo experto compartirá información fascinante sobre cómo se construyeron estos monumentos y los misterios que aún los rodean hoy en día.''',
            'description_pt': '''Descubra a última Maravilha do Mundo Antigo restante em nosso tour completo das Pirâmides. Esta experiência guiada por especialistas coloca você face a face com 4.500 anos de história.

**Destaques do Tour:**
- Complexo das Pirâmides de Gizé (Quéops, Quéfren, Miquerinos)
- A Grande Esfinge
- Templo do Vale
- Paradas para fotos panorâmicas
- Museu Egípcio (tesouros de Tutancâmon)
- Almoço tradicional egípcio incluído
- Opcional: Passeio de camelo ao redor das pirâmides

Nosso egiptólogo especializado compartilhará informações fascinantes sobre como esses monumentos foram construídos e os mistérios que ainda os cercam hoje.''',
            'category': cultural_cat,
            'tour_type': day_trip_type,
            'days': 1,
            'nights': 0,
            'price': Decimal('89.00'),
            'child_price': Decimal('49.00'),
            'is_featured': True,
            'difficulty_level': 'easy',
            'departure_city': 'Cairo',
            'languages': 'English, Spanish, Portuguese, French, German, Italian, Russian',
        },
        {
            'name': 'Desert Safari & Bedouin Experience',
            'name_es': 'Safari por el Desierto y Experiencia Beduina',
            'name_pt': 'Safari no Deserto e Experiência Beduína',
            'short_description': 'Adventure into the Sahara with sunset, stargazing and authentic Bedouin hospitality',
            'short_description_es': 'Aventúrese en el Sahara con atardecer, observación de estrellas y auténtica hospitalidad beduina',
            'short_description_pt': 'Aventure-se no Saara com pôr do sol, observação de estrelas e autêntica hospitalidade beduína',
            'description': '''Experience the magic of the Egyptian desert on this unforgettable adventure. Journey into the Sahara for an authentic encounter with Bedouin culture and the stunning desert landscape.

**Adventure Includes:**
- 4x4 desert safari
- Camel ride at sunset
- Sandboarding on the dunes
- Traditional Bedouin dinner under the stars
- Live music and entertainment
- Stargazing experience
- Mint tea and traditional bread making
- Hotel pickup and drop-off

Watch the sunset paint the dunes in shades of gold and orange before enjoying a feast under the brilliant desert stars.''',
            'description_es': '''Experimente la magia del desierto egipcio en esta aventura inolvidable. Viaje al Sahara para un encuentro auténtico con la cultura beduina y el impresionante paisaje desértico.

**La Aventura Incluye:**
- Safari en el desierto en 4x4
- Paseo en camello al atardecer
- Sandboarding en las dunas
- Cena beduina tradicional bajo las estrellas
- Música en vivo y entretenimiento
- Experiencia de observación de estrellas
- Té de menta y preparación de pan tradicional
- Recogida y regreso al hotel

Observe cómo el atardecer pinta las dunas en tonos de oro y naranja antes de disfrutar de un festín bajo las brillantes estrellas del desierto.''',
            'description_pt': '''Experimente a magia do deserto egípcio nesta aventura inesquecível. Viaje ao Saara para um encontro autêntico com a cultura beduína e a deslumbrante paisagem do deserto.

**A Aventura Inclui:**
- Safari no deserto de 4x4
- Passeio de camelo ao pôr do sol
- Sandboard nas dunas
- Jantar beduíno tradicional sob as estrelas
- Música ao vivo e entretenimento
- Experiência de observação de estrelas
- Chá de menta e preparo de pão tradicional
- Busca e retorno ao hotel

Assista ao pôr do sol pintar as dunas em tons de dourado e laranja antes de desfrutar de um banquete sob as brilhantes estrelas do deserto.''',
            'category': adventure_cat,
            'tour_type': day_trip_type,
            'days': 1,
            'nights': 0,
            'price': Decimal('75.00'),
            'child_price': Decimal('45.00'),
            'is_featured': True,
            'difficulty_level': 'moderate',
            'departure_city': 'Hurghada',
            'languages': 'English, Spanish, Portuguese, German, Russian',
        },
        {
            'name': 'Red Sea Diving Adventure',
            'name_es': 'Aventura de Buceo en el Mar Rojo',
            'name_pt': 'Aventura de Mergulho no Mar Vermelho',
            'short_description': 'Discover the underwater paradise of the Red Sea with world-class diving',
            'short_description_es': 'Descubra el paraíso submarino del Mar Rojo con buceo de clase mundial',
            'short_description_pt': 'Descubra o paraíso submarino do Mar Vermelho com mergulho de classe mundial',
            'description': '''Dive into one of the world's best diving destinations. The Red Sea offers crystal-clear waters, vibrant coral reefs, and an incredible diversity of marine life.

**Package Includes:**
- 2 boat dives to premier sites
- All diving equipment
- PADI certified instructor
- Lunch on board
- Snorkeling option available
- Marine life guide
- Hotel transfers

Suitable for all levels from beginners to advanced divers. Discover colorful coral gardens, tropical fish, dolphins, and maybe even a sea turtle!''',
            'description_es': '''Sumérjase en uno de los mejores destinos de buceo del mundo. El Mar Rojo ofrece aguas cristalinas, vibrantes arrecifes de coral y una increíble diversidad de vida marina.

**El Paquete Incluye:**
- 2 inmersiones en barco a sitios de primera
- Todo el equipo de buceo
- Instructor certificado PADI
- Almuerzo a bordo
- Opción de snorkel disponible
- Guía de vida marina
- Traslados al hotel

Apto para todos los niveles, desde principiantes hasta buceadores avanzados. ¡Descubra coloridos jardines de coral, peces tropicales, delfines y tal vez incluso una tortuga marina!''',
            'description_pt': '''Mergulhe em um dos melhores destinos de mergulho do mundo. O Mar Vermelho oferece águas cristalinas, vibrantes recifes de coral e uma incrível diversidade de vida marinha.

**O Pacote Inclui:**
- 2 mergulhos de barco em locais de primeira
- Todo o equipamento de mergulho
- Instrutor certificado PADI
- Almoço a bordo
- Opção de snorkeling disponível
- Guia de vida marinha
- Traslados do hotel

Adequado para todos os níveis, de iniciantes a mergulhadores avançados. Descubra coloridos jardins de coral, peixes tropicais, golfinhos e talvez até uma tartaruga marinha!''',
            'category': beach_cat,
            'tour_type': day_trip_type,
            'days': 1,
            'nights': 0,
            'price': Decimal('95.00'),
            'child_price': Decimal('65.00'),
            'is_featured': True,
            'difficulty_level': 'moderate',
            'departure_city': 'Hurghada',
            'languages': 'English, Spanish, German, Russian',
        },
        {
            'name': 'Egypt & Jordan Combined',
            'name_es': 'Egipto y Jordania Combinados',
            'name_pt': 'Egito e Jordânia Combinados',
            'short_description': 'Two ancient civilizations in one epic 12-day journey',
            'short_description_es': 'Dos civilizaciones antiguas en un épico viaje de 12 días',
            'short_description_pt': 'Duas civilizações antigas em uma épica jornada de 12 dias',
            'description': '''Experience the best of two ancient worlds on this comprehensive tour combining Egypt and Jordan. From the Pyramids to Petra, this journey covers the greatest treasures of the Middle East.

**Egypt Highlights:**
- Pyramids of Giza and Sphinx
- Egyptian Museum
- Nile Cruise (Luxor to Aswan)
- Valley of the Kings
- Karnak Temple

**Jordan Highlights:**
- Petra, the Rose City
- Wadi Rum desert
- Dead Sea experience
- Amman city tour
- Jerash Roman ruins

All flights, accommodations, and transfers between countries included.''',
            'description_es': '''Experimente lo mejor de dos mundos antiguos en este tour completo que combina Egipto y Jordania. Desde las Pirámides hasta Petra, este viaje cubre los mayores tesoros de Oriente Medio.

**Destacados de Egipto:**
- Pirámides de Giza y Esfinge
- Museo Egipcio
- Crucero por el Nilo (Lúxor a Asuán)
- Valle de los Reyes
- Templo de Karnak

**Destacados de Jordania:**
- Petra, la Ciudad Rosa
- Desierto de Wadi Rum
- Experiencia en el Mar Muerto
- Tour por la ciudad de Amán
- Ruinas romanas de Jerash

Todos los vuelos, alojamientos y traslados entre países incluidos.''',
            'description_pt': '''Experimente o melhor de dois mundos antigos neste tour completo combinando Egito e Jordânia. Das Pirâmides a Petra, esta jornada cobre os maiores tesouros do Oriente Médio.

**Destaques do Egito:**
- Pirâmides de Gizé e Esfinge
- Museu Egípcio
- Cruzeiro no Nilo (Luxor a Assuã)
- Vale dos Reis
- Templo de Karnak

**Destaques da Jordânia:**
- Petra, a Cidade Rosa
- Deserto de Wadi Rum
- Experiência no Mar Morto
- Tour pela cidade de Amã
- Ruínas romanas de Jerash

Todos os voos, acomodações e traslados entre países incluídos.''',
            'category': cultural_cat,
            'tour_type': package_type,
            'days': 12,
            'nights': 11,
            'price': Decimal('2499.00'),
            'price_single_supplement': Decimal('550.00'),
            'child_price': Decimal('1499.00'),
            'is_featured': True,
            'is_multi_destination': True,
            'difficulty_level': 'moderate',
            'departure_city': 'Cairo',
            'languages': 'English, Spanish, Portuguese, French',
        },
    ]

    for data in tours_data:
        category = data.pop('category')
        tour_type = data.pop('tour_type')

        tour, created = Tour.objects.update_or_create(
            name=data['name'],
            defaults={**data, 'category': category, 'tour_type': tour_type, 'is_published': True}
        )

        # Add destinations
        if cairo:
            tour.destinations.add(cairo)
        if 'Luxor' in tour.name or 'Nile' in tour.name:
            if luxor:
                tour.destinations.add(luxor)
            if aswan:
                tour.destinations.add(aswan)
        if 'Red Sea' in tour.name or 'Desert' in tour.name:
            if hurghada:
                tour.destinations.add(hurghada)

        print(f"  {'[+] Created' if created else '[~] Updated'}: {tour.name}")

    print(f"  Total: {len(tours_data)} tours\n")


def seed_blog_categories():
    """Create blog categories with multilingual content."""
    print("[*] Creating Blog Categories...")

    categories_data = [
        {
            'name': 'Travel Tips',
            'name_es': 'Consejos de Viaje',
            'name_pt': 'Dicas de Viagem',
            'description': 'Essential tips and advice for traveling in Egypt',
            'description_es': 'Consejos esenciales para viajar por Egipto',
            'description_pt': 'Dicas essenciais para viajar pelo Egito',
            'is_active': True,
        },
        {
            'name': 'Ancient History',
            'name_es': 'Historia Antigua',
            'name_pt': 'História Antiga',
            'description': 'Explore the fascinating history of ancient Egypt',
            'description_es': 'Explore la fascinante historia del antiguo Egipto',
            'description_pt': 'Explore a fascinante história do antigo Egito',
            'is_active': True,
        },
        {
            'name': 'Culture & Traditions',
            'name_es': 'Cultura y Tradiciones',
            'name_pt': 'Cultura e Tradições',
            'description': 'Discover Egyptian culture, traditions, and way of life',
            'description_es': 'Descubra la cultura, tradiciones y forma de vida egipcia',
            'description_pt': 'Descubra a cultura, tradições e modo de vida egípcio',
            'is_active': True,
        },
        {
            'name': 'Food & Cuisine',
            'name_es': 'Gastronomía',
            'name_pt': 'Gastronomia',
            'description': 'Explore the delicious world of Egyptian cuisine',
            'description_es': 'Explore el delicioso mundo de la cocina egipcia',
            'description_pt': 'Explore o delicioso mundo da culinária egípcia',
            'is_active': True,
        },
        {
            'name': 'Adventure',
            'name_es': 'Aventura',
            'name_pt': 'Aventura',
            'description': 'Adventure activities and outdoor experiences in Egypt',
            'description_es': 'Actividades de aventura y experiencias al aire libre en Egipto',
            'description_pt': 'Atividades de aventura e experiências ao ar livre no Egito',
            'is_active': True,
        },
    ]

    for data in categories_data:
        cat, created = BlogCategory.objects.update_or_create(
            name=data['name'],
            defaults=data
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {cat.name}")

    print(f"  Total: {len(categories_data)} blog categories\n")


def seed_blog_posts():
    """Create blog posts with multilingual content."""
    print("[*] Creating Blog Posts...")

    travel_tips_cat = BlogCategory.objects.filter(name='Travel Tips').first()
    history_cat = BlogCategory.objects.filter(name='Ancient History').first()
    culture_cat = BlogCategory.objects.filter(name='Culture & Traditions').first()

    posts_data = [
        {
            'title': '10 Essential Tips for Your First Trip to Egypt',
            'title_es': '10 Consejos Esenciales para Tu Primer Viaje a Egipto',
            'title_pt': '10 Dicas Essenciais para Sua Primeira Viagem ao Egito',
            'excerpt': 'Planning your first trip to Egypt? Here are the essential tips you need to know before you go.',
            'excerpt_es': '¿Planificando tu primer viaje a Egipto? Aquí están los consejos esenciales que necesitas saber antes de ir.',
            'excerpt_pt': 'Planejando sua primeira viagem ao Egito? Aqui estão as dicas essenciais que você precisa saber antes de ir.',
            'content': '''# 10 Essential Tips for Your First Trip to Egypt

Egypt is a bucket-list destination for many travelers, and for good reason. From the ancient pyramids to the bustling bazaars, Egypt offers an unforgettable experience. Here are our top tips for making the most of your trip.

## 1. Best Time to Visit

The best time to visit Egypt is from October to April when temperatures are milder. Summer months (June-August) can be extremely hot, especially in Upper Egypt.

## 2. Visa Requirements

Most nationalities can obtain a visa on arrival at Egyptian airports or apply for an e-visa online before traveling. Check the requirements for your country.

## 3. Currency & Money

The Egyptian Pound (EGP) is the local currency. Credit cards are accepted in hotels and larger establishments, but carry cash for markets and smaller shops.

## 4. Dress Code

Egypt is a conservative country. Dress modestly, especially when visiting mosques and religious sites. Lightweight, loose-fitting clothing is recommended.

## 5. Stay Hydrated

The Egyptian sun is strong. Always carry water, wear sunscreen, and take breaks in the shade.

## 6. Bargaining

Bargaining is expected in markets and bazaars. Start at about 50% of the asking price and negotiate from there.

## 7. Photography

Always ask permission before photographing locals. Some sites charge extra for photography, especially inside tombs.

## 8. Learn Basic Arabic Phrases

While English is widely spoken in tourist areas, learning a few Arabic phrases like "Shukran" (thank you) goes a long way.

## 9. Book Guides in Advance

Licensed Egyptologist guides make a huge difference. Book through reputable agencies for the best experience.

## 10. Respect Local Customs

Be respectful of local customs and traditions. Egyptians are warm and welcoming hosts.

Happy travels!''',
            'content_es': '''# 10 Consejos Esenciales para Tu Primer Viaje a Egipto

Egipto es un destino soñado para muchos viajeros, y con razón. Desde las antiguas pirámides hasta los bulliciosos bazares, Egipto ofrece una experiencia inolvidable. Aquí están nuestros mejores consejos para aprovechar al máximo tu viaje.

## 1. Mejor Época para Visitar

La mejor época para visitar Egipto es de octubre a abril cuando las temperaturas son más suaves. Los meses de verano (junio-agosto) pueden ser extremadamente calurosos, especialmente en el Alto Egipto.

## 2. Requisitos de Visa

La mayoría de nacionalidades pueden obtener visa a la llegada en aeropuertos egipcios o solicitar una e-visa en línea antes de viajar. Verifica los requisitos para tu país.

## 3. Moneda y Dinero

La Libra Egipcia (EGP) es la moneda local. Las tarjetas de crédito son aceptadas en hoteles y grandes establecimientos, pero lleva efectivo para mercados y tiendas pequeñas.

## 4. Código de Vestimenta

Egipto es un país conservador. Vístete con modestia, especialmente al visitar mezquitas y sitios religiosos. Se recomienda ropa ligera y holgada.

## 5. Mantente Hidratado

El sol egipcio es fuerte. Siempre lleva agua, usa protector solar y toma descansos a la sombra.

## 6. Regateo

El regateo es esperado en mercados y bazares. Comienza con aproximadamente el 50% del precio inicial y negocia desde ahí.

## 7. Fotografía

Siempre pide permiso antes de fotografiar a los locales. Algunos sitios cobran extra por fotografías, especialmente dentro de las tumbas.

## 8. Aprende Frases Básicas en Árabe

Aunque el inglés se habla ampliamente en áreas turísticas, aprender algunas frases en árabe como "Shukran" (gracias) ayuda mucho.

## 9. Reserva Guías con Anticipación

Los guías egiptólogos licenciados hacen una gran diferencia. Reserva a través de agencias de buena reputación para la mejor experiencia.

## 10. Respeta las Costumbres Locales

Sé respetuoso con las costumbres y tradiciones locales. Los egipcios son anfitriones cálidos y acogedores.

¡Feliz viaje!''',
            'content_pt': '''# 10 Dicas Essenciais para Sua Primeira Viagem ao Egito

O Egito é um destino dos sonhos para muitos viajantes, e com razão. Das antigas pirâmides aos movimentados bazares, o Egito oferece uma experiência inesquecível. Aqui estão nossas melhores dicas para aproveitar ao máximo sua viagem.

## 1. Melhor Época para Visitar

A melhor época para visitar o Egito é de outubro a abril, quando as temperaturas são mais amenas. Os meses de verão (junho-agosto) podem ser extremamente quentes, especialmente no Alto Egito.

## 2. Requisitos de Visto

A maioria das nacionalidades pode obter visto na chegada nos aeroportos egípcios ou solicitar um e-visa online antes de viajar. Verifique os requisitos para seu país.

## 3. Moeda e Dinheiro

A Libra Egípcia (EGP) é a moeda local. Cartões de crédito são aceitos em hotéis e grandes estabelecimentos, mas leve dinheiro para mercados e lojas menores.

## 4. Código de Vestimenta

O Egito é um país conservador. Vista-se com modéstia, especialmente ao visitar mesquitas e locais religiosos. Roupas leves e folgadas são recomendadas.

## 5. Mantenha-se Hidratado

O sol egípcio é forte. Sempre leve água, use protetor solar e faça pausas na sombra.

## 6. Barganha

A barganha é esperada em mercados e bazares. Comece com cerca de 50% do preço pedido e negocie a partir daí.

## 7. Fotografia

Sempre peça permissão antes de fotografar os locais. Alguns locais cobram extra por fotografia, especialmente dentro das tumbas.

## 8. Aprenda Frases Básicas em Árabe

Embora o inglês seja amplamente falado em áreas turísticas, aprender algumas frases em árabe como "Shukran" (obrigado) ajuda muito.

## 9. Reserve Guias com Antecedência

Guias egiptólogos licenciados fazem uma grande diferença. Reserve através de agências de boa reputação para a melhor experiência.

## 10. Respeite os Costumes Locais

Seja respeitoso com os costumes e tradições locais. Os egípcios são anfitriões calorosos e acolhedores.

Boa viagem!''',
            'category': travel_tips_cat,
            'is_featured': True,
            'reading_time': 8,
        },
        {
            'title': 'The Mysteries of the Pyramids: What We Know Today',
            'title_es': 'Los Misterios de las Pirámides: Lo Que Sabemos Hoy',
            'title_pt': 'Os Mistérios das Pirâmides: O Que Sabemos Hoje',
            'excerpt': 'Explore the latest discoveries and theories about how the ancient Egyptians built the pyramids.',
            'excerpt_es': 'Explore los últimos descubrimientos y teorías sobre cómo los antiguos egipcios construyeron las pirámides.',
            'excerpt_pt': 'Explore as últimas descobertas e teorias sobre como os antigos egípcios construíram as pirâmides.',
            'content': '''# The Mysteries of the Pyramids: What We Know Today

The Great Pyramid of Giza has fascinated humanity for over 4,500 years. Despite centuries of study, new discoveries continue to shed light on how these incredible structures were built.

## Construction Theories

Modern archaeology has largely debunked the myth of slave labor. Evidence suggests the pyramids were built by skilled Egyptian workers who were well-fed and housed in nearby villages.

## The Ramp Theory

Most Egyptologists believe ramps were used to move the massive stone blocks. Recent discoveries suggest an internal ramp system may have been employed.

## Precision Engineering

The precision of the pyramids continues to amaze. The base of the Great Pyramid is level to within 2.1 centimeters across its entire 230-meter length.

## Recent Discoveries

In 2017, scientists using cosmic ray imaging discovered a large void within the Great Pyramid. The purpose of this chamber remains unknown.

The pyramids continue to reveal their secrets, one discovery at a time.''',
            'content_es': '''# Los Misterios de las Pirámides: Lo Que Sabemos Hoy

La Gran Pirámide de Giza ha fascinado a la humanidad durante más de 4.500 años. A pesar de siglos de estudio, nuevos descubrimientos continúan arrojando luz sobre cómo se construyeron estas increíbles estructuras.

## Teorías de Construcción

La arqueología moderna ha desmentido en gran medida el mito del trabajo esclavo. La evidencia sugiere que las pirámides fueron construidas por trabajadores egipcios calificados que estaban bien alimentados y alojados en aldeas cercanas.

## La Teoría de la Rampa

La mayoría de los egiptólogos creen que se usaron rampas para mover los enormes bloques de piedra. Descubrimientos recientes sugieren que se pudo haber empleado un sistema de rampas internas.

## Ingeniería de Precisión

La precisión de las pirámides sigue asombrando. La base de la Gran Pirámide está nivelada con una diferencia de 2,1 centímetros en toda su longitud de 230 metros.

## Descubrimientos Recientes

En 2017, científicos usando imágenes de rayos cósmicos descubrieron un gran vacío dentro de la Gran Pirámide. El propósito de esta cámara sigue siendo desconocido.

Las pirámides continúan revelando sus secretos, un descubrimiento a la vez.''',
            'content_pt': '''# Os Mistérios das Pirâmides: O Que Sabemos Hoje

A Grande Pirâmide de Gizé fascina a humanidade há mais de 4.500 anos. Apesar de séculos de estudo, novas descobertas continuam a lançar luz sobre como essas incríveis estruturas foram construídas.

## Teorias de Construção

A arqueologia moderna desmentiu em grande parte o mito do trabalho escravo. Evidências sugerem que as pirâmides foram construídas por trabalhadores egípcios qualificados que eram bem alimentados e alojados em aldeias próximas.

## A Teoria da Rampa

A maioria dos egiptólogos acredita que rampas foram usadas para mover os enormes blocos de pedra. Descobertas recentes sugerem que um sistema de rampas internas pode ter sido empregado.

## Engenharia de Precisão

A precisão das pirâmides continua a surpreender. A base da Grande Pirâmide está nivelada com uma diferença de 2,1 centímetros em toda a sua extensão de 230 metros.

## Descobertas Recentes

Em 2017, cientistas usando imagens de raios cósmicos descobriram um grande vazio dentro da Grande Pirâmide. O propósito desta câmara permanece desconhecido.

As pirâmides continuam a revelar seus segredos, uma descoberta de cada vez.''',
            'category': history_cat,
            'is_featured': True,
            'reading_time': 6,
        },
        {
            'title': 'Egyptian Cuisine: A Food Lover\'s Guide',
            'title_es': 'Cocina Egipcia: Guía para Amantes de la Comida',
            'title_pt': 'Culinária Egípcia: Guia para Amantes da Comida',
            'excerpt': 'Discover the delicious flavors of traditional Egyptian cuisine and the must-try dishes.',
            'excerpt_es': 'Descubre los deliciosos sabores de la cocina tradicional egipcia y los platos imprescindibles.',
            'excerpt_pt': 'Descubra os deliciosos sabores da culinária tradicional egípcia e os pratos imperdíveis.',
            'content': '''# Egyptian Cuisine: A Food Lover's Guide

Egyptian cuisine is a delicious blend of Mediterranean, Middle Eastern, and African influences. Here are the dishes you absolutely must try.

## Koshari

Egypt's national dish is a hearty mix of rice, lentils, pasta, and chickpeas, topped with crispy onions and spicy tomato sauce.

## Ful Medames

This traditional breakfast dish of slow-cooked fava beans is a staple of Egyptian cuisine, often served with olive oil, lemon, and fresh bread.

## Ta'meya (Egyptian Falafel)

Unlike the chickpea-based falafel found elsewhere, Egyptian ta'meya is made from fava beans and is bright green inside.

## Molokhia

This leafy green soup has been eaten in Egypt for thousands of years. It's typically served with rice and chicken or rabbit.

## Mahshi

Vegetables like grape leaves, peppers, and zucchini stuffed with seasoned rice are a beloved comfort food.

## Sweet Treats

Don't miss Om Ali (Egyptian bread pudding) and Basbousa (semolina cake soaked in syrup).

Bon appétit - or as the Egyptians say, "Bil hana wish shifa!"''',
            'content_es': '''# Cocina Egipcia: Guía para Amantes de la Comida

La cocina egipcia es una deliciosa mezcla de influencias mediterráneas, del Medio Oriente y africanas. Aquí están los platos que absolutamente debes probar.

## Koshari

El plato nacional de Egipto es una abundante mezcla de arroz, lentejas, pasta y garbanzos, coronado con cebollas crujientes y salsa de tomate picante.

## Ful Medames

Este plato tradicional de desayuno de habas cocidas lentamente es un básico de la cocina egipcia, a menudo servido con aceite de oliva, limón y pan fresco.

## Ta'meya (Falafel Egipcio)

A diferencia del falafel de garbanzos que se encuentra en otros lugares, el ta'meya egipcio se hace con habas y es de color verde brillante por dentro.

## Molokhia

Esta sopa de hojas verdes se ha consumido en Egipto durante miles de años. Típicamente se sirve con arroz y pollo o conejo.

## Mahshi

Verduras como hojas de parra, pimientos y calabacines rellenos de arroz sazonado son una querida comida reconfortante.

## Dulces

No te pierdas Om Ali (pudín de pan egipcio) y Basbousa (pastel de sémola empapado en almíbar).

¡Buen provecho - o como dicen los egipcios, "Bil hana wish shifa!"''',
            'content_pt': '''# Culinária Egípcia: Guia para Amantes da Comida

A culinária egípcia é uma deliciosa mistura de influências mediterrâneas, do Oriente Médio e africanas. Aqui estão os pratos que você absolutamente deve experimentar.

## Koshari

O prato nacional do Egito é uma mistura farta de arroz, lentilhas, macarrão e grão-de-bico, coberto com cebolas crocantes e molho de tomate picante.

## Ful Medames

Este prato tradicional de café da manhã de favas cozidas lentamente é um básico da culinária egípcia, frequentemente servido com azeite, limão e pão fresco.

## Ta'meya (Falafel Egípcio)

Diferente do falafel de grão-de-bico encontrado em outros lugares, o ta'meya egípcio é feito de favas e é verde brilhante por dentro.

## Molokhia

Esta sopa de folhas verdes é consumida no Egito há milhares de anos. Tipicamente é servida com arroz e frango ou coelho.

## Mahshi

Vegetais como folhas de uva, pimentões e abobrinhas recheados com arroz temperado são uma querida comida reconfortante.

## Doces

Não perca Om Ali (pudim de pão egípcio) e Basbousa (bolo de semolina embebido em calda).

Bom apetite - ou como dizem os egípcios, "Bil hana wish shifa!"''',
            'category': culture_cat,
            'is_featured': True,
            'reading_time': 5,
        },
    ]

    for data in posts_data:
        category = data.pop('category')
        post, created = Post.objects.update_or_create(
            title=data['title'],
            defaults={**data, 'category': category, 'is_published': True, 'published_at': timezone.now()}
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {post.title}")

    print(f"  Total: {len(posts_data)} posts\n")


def seed_faqs():
    """Create FAQs with multilingual content."""
    print("[*] Creating FAQs...")

    faqs_data = [
        {
            'question': 'What is the best time to visit Egypt?',
            'question_es': '¿Cuál es la mejor época para visitar Egipto?',
            'question_pt': 'Qual é a melhor época para visitar o Egito?',
            'answer': 'The best time to visit Egypt is from October to April when temperatures are milder. Summer months (May-September) can be very hot, especially in Upper Egypt (Luxor and Aswan), with temperatures often exceeding 40°C (104°F).',
            'answer_es': 'La mejor época para visitar Egipto es de octubre a abril cuando las temperaturas son más suaves. Los meses de verano (mayo-septiembre) pueden ser muy calurosos, especialmente en el Alto Egipto (Lúxor y Asuán), con temperaturas que a menudo superan los 40°C.',
            'answer_pt': 'A melhor época para visitar o Egito é de outubro a abril, quando as temperaturas são mais amenas. Os meses de verão (maio-setembro) podem ser muito quentes, especialmente no Alto Egito (Luxor e Assuã), com temperaturas frequentemente superiores a 40°C.',
            'category': 'travel',
            'sort_order': 1,
        },
        {
            'question': 'Do I need a visa to visit Egypt?',
            'question_es': '¿Necesito visa para visitar Egipto?',
            'question_pt': 'Preciso de visto para visitar o Egito?',
            'answer': 'Most nationalities can obtain a tourist visa on arrival at Egyptian airports for approximately $25 USD. You can also apply for an e-visa online before your trip. The visa is valid for 30 days. Check the requirements specific to your nationality.',
            'answer_es': 'La mayoría de nacionalidades pueden obtener una visa de turista a la llegada en aeropuertos egipcios por aproximadamente $25 USD. También puede solicitar una e-visa en línea antes de su viaje. La visa es válida por 30 días. Verifique los requisitos específicos para su nacionalidad.',
            'answer_pt': 'A maioria das nacionalidades pode obter um visto de turista na chegada nos aeroportos egípcios por aproximadamente $25 USD. Você também pode solicitar um e-visa online antes da sua viagem. O visto é válido por 30 dias. Verifique os requisitos específicos para sua nacionalidade.',
            'category': 'travel',
            'sort_order': 2,
        },
        {
            'question': 'Is Egypt safe for tourists?',
            'question_es': '¿Es Egipto seguro para los turistas?',
            'question_pt': 'O Egito é seguro para turistas?',
            'answer': 'Yes, Egypt is generally safe for tourists. Tourist areas are well-protected by security forces. However, as with any travel destination, it\'s advisable to stay aware of your surroundings, follow local advice, and take standard precautions with your belongings.',
            'answer_es': 'Sí, Egipto es generalmente seguro para los turistas. Las áreas turísticas están bien protegidas por las fuerzas de seguridad. Sin embargo, como en cualquier destino de viaje, es aconsejable estar atento a su entorno, seguir los consejos locales y tomar precauciones estándar con sus pertenencias.',
            'answer_pt': 'Sim, o Egito é geralmente seguro para turistas. As áreas turísticas são bem protegidas pelas forças de segurança. No entanto, como em qualquer destino de viagem, é aconselhável estar atento ao seu entorno, seguir os conselhos locais e tomar precauções padrão com seus pertences.',
            'category': 'travel',
            'sort_order': 3,
        },
        {
            'question': 'What should I wear when visiting Egypt?',
            'question_es': '¿Qué debo usar cuando visite Egipto?',
            'question_pt': 'O que devo vestir ao visitar o Egito?',
            'answer': 'Egypt is a conservative country. We recommend modest clothing that covers shoulders and knees, especially when visiting religious sites. Lightweight, breathable fabrics are ideal. Don\'t forget comfortable walking shoes, a hat, and sunglasses for sun protection.',
            'answer_es': 'Egipto es un país conservador. Recomendamos ropa modesta que cubra hombros y rodillas, especialmente al visitar sitios religiosos. Telas ligeras y transpirables son ideales. No olvide zapatos cómodos para caminar, sombrero y gafas de sol para protección solar.',
            'answer_pt': 'O Egito é um país conservador. Recomendamos roupas modestas que cubram ombros e joelhos, especialmente ao visitar locais religiosos. Tecidos leves e respiráveis são ideais. Não esqueça sapatos confortáveis para caminhar, chapéu e óculos de sol para proteção solar.',
            'category': 'travel',
            'sort_order': 4,
        },
        {
            'question': 'How do I book a tour with Girasol?',
            'question_es': '¿Cómo reservo un tour con Girasol?',
            'question_pt': 'Como reservo um tour com a Girasol?',
            'answer': 'You can book directly through our website by selecting your preferred tour and following the booking process. Alternatively, contact us via email, phone, or WhatsApp for personalized assistance. We accept credit cards and bank transfers.',
            'answer_es': 'Puede reservar directamente a través de nuestro sitio web seleccionando su tour preferido y siguiendo el proceso de reserva. Alternativamente, contáctenos por correo electrónico, teléfono o WhatsApp para asistencia personalizada. Aceptamos tarjetas de crédito y transferencias bancarias.',
            'answer_pt': 'Você pode reservar diretamente através do nosso site, selecionando seu tour preferido e seguindo o processo de reserva. Alternativamente, entre em contato conosco por e-mail, telefone ou WhatsApp para assistência personalizada. Aceitamos cartões de crédito e transferências bancárias.',
            'category': 'booking',
            'sort_order': 1,
        },
        {
            'question': 'What is your cancellation policy?',
            'question_es': '¿Cuál es su política de cancelación?',
            'question_pt': 'Qual é a política de cancelamento?',
            'answer': 'Free cancellation is available up to 30 days before the tour start date for a full refund. Cancellations between 15-30 days receive a 50% refund. Cancellations less than 15 days before departure are non-refundable. We recommend travel insurance.',
            'answer_es': 'La cancelación gratuita está disponible hasta 30 días antes de la fecha de inicio del tour para un reembolso completo. Las cancelaciones entre 15-30 días reciben un reembolso del 50%. Las cancelaciones con menos de 15 días antes de la salida no son reembolsables. Recomendamos seguro de viaje.',
            'answer_pt': 'O cancelamento gratuito está disponível até 30 dias antes da data de início do tour para reembolso total. Cancelamentos entre 15-30 dias recebem reembolso de 50%. Cancelamentos com menos de 15 dias antes da partida não são reembolsáveis. Recomendamos seguro de viagem.',
            'category': 'booking',
            'sort_order': 2,
        },
        {
            'question': 'What is included in the tour price?',
            'question_es': '¿Qué está incluido en el precio del tour?',
            'question_pt': 'O que está incluído no preço do tour?',
            'answer': 'Our tour prices typically include accommodations, transportation, entrance fees, guided tours with licensed Egyptologists, and some meals as specified. Personal expenses, tips, travel insurance, and international flights are not included unless stated.',
            'answer_es': 'Nuestros precios de tour típicamente incluyen alojamiento, transporte, tarifas de entrada, tours guiados con egiptólogos licenciados y algunas comidas según se especifique. Gastos personales, propinas, seguro de viaje y vuelos internacionales no están incluidos a menos que se indique.',
            'answer_pt': 'Nossos preços de tour tipicamente incluem acomodações, transporte, taxas de entrada, tours guiados com egiptólogos licenciados e algumas refeições conforme especificado. Despesas pessoais, gorjetas, seguro de viagem e voos internacionais não estão incluídos, a menos que indicado.',
            'category': 'tours',
            'sort_order': 1,
        },
        {
            'question': 'Are your guides licensed Egyptologists?',
            'question_es': '¿Son sus guías egiptólogos licenciados?',
            'question_pt': 'Seus guias são egiptólogos licenciados?',
            'answer': 'Yes, all our guides are licensed Egyptologists who have completed formal education in Egyptology and are certified by the Egyptian Ministry of Tourism. They speak multiple languages and are passionate about sharing Egypt\'s history.',
            'answer_es': 'Sí, todos nuestros guías son egiptólogos licenciados que han completado educación formal en Egiptología y están certificados por el Ministerio de Turismo de Egipto. Hablan múltiples idiomas y son apasionados por compartir la historia de Egipto.',
            'answer_pt': 'Sim, todos os nossos guias são egiptólogos licenciados que completaram educação formal em Egiptologia e são certificados pelo Ministério do Turismo do Egito. Eles falam vários idiomas e são apaixonados por compartilhar a história do Egito.',
            'category': 'tours',
            'sort_order': 2,
        },
        {
            'question': 'What type of accommodations do you use?',
            'question_es': '¿Qué tipo de alojamiento utilizan?',
            'question_pt': 'Que tipo de acomodações vocês usam?',
            'answer': 'We use carefully selected 4 and 5-star hotels that meet our quality standards. Our Nile cruises are on 5-star vessels. We can also arrange luxury or budget alternatives based on your preferences.',
            'answer_es': 'Utilizamos hoteles de 4 y 5 estrellas cuidadosamente seleccionados que cumplen con nuestros estándares de calidad. Nuestros cruceros por el Nilo son en embarcaciones de 5 estrellas. También podemos organizar alternativas de lujo o económicas según sus preferencias.',
            'answer_pt': 'Utilizamos hotéis de 4 e 5 estrelas cuidadosamente selecionados que atendem aos nossos padrões de qualidade. Nossos cruzeiros no Nilo são em embarcações 5 estrelas. Também podemos organizar alternativas de luxo ou econômicas de acordo com suas preferências.',
            'category': 'accommodation',
            'sort_order': 1,
        },
        {
            'question': 'Can I customize my tour itinerary?',
            'question_es': '¿Puedo personalizar mi itinerario de tour?',
            'question_pt': 'Posso personalizar meu itinerário de tour?',
            'answer': 'Absolutely! We specialize in creating customized itineraries tailored to your interests, schedule, and budget. Contact us to discuss your preferences and we\'ll design the perfect Egyptian adventure for you.',
            'answer_es': '¡Absolutamente! Nos especializamos en crear itinerarios personalizados adaptados a sus intereses, horario y presupuesto. Contáctenos para discutir sus preferencias y diseñaremos la aventura egipcia perfecta para usted.',
            'answer_pt': 'Absolutamente! Somos especializados em criar itinerários personalizados adaptados aos seus interesses, agenda e orçamento. Entre em contato conosco para discutir suas preferências e projetaremos a aventura egípcia perfeita para você.',
            'category': 'tours',
            'sort_order': 3,
        },
    ]

    for data in faqs_data:
        faq, created = FAQ.objects.update_or_create(
            question=data['question'],
            defaults={**data, 'is_active': True}
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {faq.question[:50]}...")

    print(f"  Total: {len(faqs_data)} FAQs\n")


def seed_statistics():
    """Create statistics with multilingual content."""
    print("[*] Creating Statistics...")

    stats_data = [
        {
            'value': '25+',
            'label': 'Years of Experience',
            'label_es': 'Años de Experiencia',
            'label_pt': 'Anos de Experiência',
            'icon': 'clock',
            'description': 'Providing exceptional tours since 1999',
            'sort_order': 1,
        },
        {
            'value': '50,000+',
            'label': 'Happy Travelers',
            'label_es': 'Viajeros Felices',
            'label_pt': 'Viajantes Felizes',
            'icon': 'users',
            'description': 'Satisfied customers from around the world',
            'sort_order': 2,
        },
        {
            'value': '98%',
            'label': 'Satisfaction Rate',
            'label_es': 'Tasa de Satisfacción',
            'label_pt': 'Taxa de Satisfação',
            'icon': 'heart',
            'description': 'Based on customer reviews',
            'sort_order': 3,
        },
        {
            'value': '150+',
            'label': 'Tour Packages',
            'label_es': 'Paquetes de Tours',
            'label_pt': 'Pacotes de Tours',
            'icon': 'globe',
            'description': 'Diverse experiences across Egypt',
            'sort_order': 4,
        },
        {
            'value': '4.9',
            'label': 'Average Rating',
            'label_es': 'Calificación Promedio',
            'label_pt': 'Avaliação Média',
            'icon': 'star',
            'description': 'Out of 5 stars on TripAdvisor',
            'sort_order': 5,
        },
        {
            'value': '6',
            'label': 'Local Offices',
            'label_es': 'Oficinas Locales',
            'label_pt': 'Escritórios Locais',
            'icon': 'map-pin',
            'description': 'Across Egypt for your convenience',
            'sort_order': 6,
        },
    ]

    for data in stats_data:
        stat, created = Statistic.objects.update_or_create(
            value=data['value'],
            label=data['label'],
            defaults={**data, 'is_active': True}
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {stat.value} {stat.label}")

    print(f"  Total: {len(stats_data)} statistics\n")


def seed_offices():
    """Create office locations."""
    print("[*] Creating Offices...")

    offices_data = [
        {
            'name': 'Girasol Tours Headquarters',
            'city': 'Cairo',
            'address': '15 Tahrir Square, Downtown Cairo, Egypt',
            'phone': '+20 2 1234 5678',
            'email': 'info@girasoltours.com',
            'whatsapp': '+20 100 123 4567',
            'working_hours': 'Sunday - Thursday: 9:00 AM - 6:00 PM',
            'is_headquarters': True,
            'latitude': Decimal('30.0444'),
            'longitude': Decimal('31.2357'),
            'sort_order': 1,
        },
        {
            'name': 'Girasol Tours Luxor',
            'city': 'Luxor',
            'address': 'Corniche El-Nile, Luxor, Egypt',
            'phone': '+20 95 123 4567',
            'email': 'luxor@girasoltours.com',
            'whatsapp': '+20 100 234 5678',
            'working_hours': 'Daily: 8:00 AM - 8:00 PM',
            'is_headquarters': False,
            'latitude': Decimal('25.6872'),
            'longitude': Decimal('32.6396'),
            'sort_order': 2,
        },
        {
            'name': 'Girasol Tours Aswan',
            'city': 'Aswan',
            'address': 'Corniche El-Nile, Aswan, Egypt',
            'phone': '+20 97 123 4567',
            'email': 'aswan@girasoltours.com',
            'whatsapp': '+20 100 345 6789',
            'working_hours': 'Daily: 8:00 AM - 8:00 PM',
            'is_headquarters': False,
            'latitude': Decimal('24.0889'),
            'longitude': Decimal('32.8998'),
            'sort_order': 3,
        },
        {
            'name': 'Girasol Tours Hurghada',
            'city': 'Hurghada',
            'address': 'Sheraton Road, Hurghada, Egypt',
            'phone': '+20 65 123 4567',
            'email': 'hurghada@girasoltours.com',
            'whatsapp': '+20 100 456 7890',
            'working_hours': 'Daily: 9:00 AM - 9:00 PM',
            'is_headquarters': False,
            'latitude': Decimal('27.2579'),
            'longitude': Decimal('33.8116'),
            'sort_order': 4,
        },
    ]

    for data in offices_data:
        office, created = Office.objects.update_or_create(
            name=data['name'],
            defaults={**data, 'is_active': True}
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {office.name}")

    print(f"  Total: {len(offices_data)} offices\n")


def seed_testimonials():
    """Create testimonials."""
    print("[*] Creating Testimonials...")

    testimonials_data = [
        {
            'name': 'Maria García',
            'country': 'Spain',
            'quote': 'An incredible experience! Our guide Ahmed was knowledgeable and passionate. The Nile cruise exceeded all expectations. Highly recommend Girasol Tours!',
            'rating': 5,
            'is_active': True,
            'sort_order': 1,
        },
        {
            'name': 'John Smith',
            'country': 'United States',
            'quote': 'From the moment we arrived, everything was perfectly organized. The pyramids at sunrise was a moment I\'ll never forget. Thank you Girasol!',
            'rating': 5,
            'is_active': True,
            'sort_order': 2,
        },
        {
            'name': 'Sophie Martin',
            'country': 'France',
            'quote': 'Third time visiting Egypt with Girasol and they never disappoint. Professional service, excellent guides, and attention to every detail.',
            'rating': 5,
            'is_active': True,
            'sort_order': 3,
        },
        {
            'name': 'Carlos Silva',
            'country': 'Brazil',
            'quote': 'A viagem dos sonhos! O tour combinado Egito e Jordânia foi perfeito. Organização impecável e guias excepcionais.',
            'rating': 5,
            'is_active': True,
            'sort_order': 4,
        },
        {
            'name': 'Hans Mueller',
            'country': 'Germany',
            'quote': 'Excellent value for money. The hotels were fantastic, the cruise was luxurious, and our Egyptologist guide made history come alive.',
            'rating': 5,
            'is_active': True,
            'sort_order': 5,
        },
        {
            'name': 'Yuki Tanaka',
            'country': 'Japan',
            'quote': 'Perfectly organized trip with wonderful attention to detail. The hot air balloon ride over Luxor was breathtaking!',
            'rating': 5,
            'is_active': True,
            'sort_order': 6,
        },
    ]

    for data in testimonials_data:
        testimonial, created = Testimonial.objects.update_or_create(
            name=data['name'],
            country=data['country'],
            defaults=data
        )
        print(f"  {'[+] Created' if created else '[~] Updated'}: {testimonial.name} - {testimonial.country}")

    print(f"  Total: {len(testimonials_data)} testimonials\n")


def seed_early_booking_offers():
    """Create early booking offers."""
    print("[*] Creating Early Booking Offers...")

    tours = Tour.objects.all()[:4]

    if tours.exists():
        offer_data = {
            'title': 'Early Bird Summer 2025',
            'title_ar': 'عرض الحجز المبكر صيف 2025',
            'subtitle': 'Book now and save up to 20% on summer tours',
            'subtitle_ar': 'احجز الآن ووفر حتى 20% على رحلات الصيف',
            'description': 'Take advantage of our early booking discount for summer 2025 tours. Book at least 90 days in advance and enjoy significant savings.',
            'description_ar': 'استفد من خصم الحجز المبكر لرحلات صيف 2025. احجز قبل 90 يوم على الأقل واستمتع بتوفير كبير.',
            'discount_percentage': 20,
            'offer_start_date': timezone.now(),
            'offer_end_date': timezone.now() + timedelta(days=90),
            'travel_start_date': date.today() + timedelta(days=120),
            'travel_end_date': date.today() + timedelta(days=240),
            'min_days_advance': 90,
            'benefits': [
                'Save 20% on tour price',
                'Free airport transfers',
                'Complimentary room upgrade (subject to availability)',
                'Flexible rebooking options',
            ],
            'terms_conditions': 'Offer valid for new bookings only. Cannot be combined with other promotions. Subject to availability.',
            'cancellation_policy': 'Free cancellation up to 60 days before departure. 50% refund for cancellations 30-60 days before. Non-refundable within 30 days.',
            'badge_text': 'Early Bird',
            'background_color': '#2563eb',
            'is_active': True,
            'is_featured': True,
        }

        offer, created = EarlyBookingOffer.objects.update_or_create(
            title=offer_data['title'],
            defaults=offer_data
        )

        # Add tours to the offer
        offer.tours.set(tours)

        print(f"  {'[+] Created' if created else '[~] Updated'}: {offer.title}")
        print(f"  Total: 1 early booking offer\n")
    else:
        print("  [!] No tours found to add to early booking offer\n")


def main():
    """Run all seeders."""
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    print("\n" + "="*60)
    print("GIRASOL TOURS - MULTILINGUAL DATA SEEDER")
    print("="*60 + "\n")

    seed_destinations()
    seed_tour_categories()
    seed_tour_types()
    seed_tours()
    seed_blog_categories()
    seed_blog_posts()
    seed_faqs()
    seed_statistics()
    seed_offices()
    seed_testimonials()
    seed_early_booking_offers()

    print("="*60)
    print("ALL DATA SEEDED SUCCESSFULLY!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
