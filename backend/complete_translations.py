# -*- coding: utf-8 -*-
"""
Complete all translations with proper Spanish and Portuguese content.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourFAQ, EarlyBookingOffer
)
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.blog.models import Category as BlogCategory, Tag, Post
from apps.reviews.models import Review, ReviewImage, Testimonial
from apps.contact.models import FAQ, Office, Statistic


# ============================================================
# TOUR CATEGORIES
# ============================================================
TOUR_CATEGORY_TRANSLATIONS = {
    'Cultural Tours': {
        'es': 'Tours Culturales',
        'pt': 'Tours Culturais',
        'desc_es': 'Descubre la rica historia y cultura de Egipto con nuestros tours culturales guiados.',
        'desc_pt': 'Descubra a rica historia e cultura do Egito com nossos tours culturais guiados.'
    },
    'Adventure Tours': {
        'es': 'Tours de Aventura',
        'pt': 'Tours de Aventura',
        'desc_es': 'Vive experiencias emocionantes en el desierto, mar y montanas de Egipto.',
        'desc_pt': 'Viva experiencias emocionantes no deserto, mar e montanhas do Egito.'
    },
    'Beach & Relaxation': {
        'es': 'Playa y Relax',
        'pt': 'Praia e Relaxamento',
        'desc_es': 'Disfruta de las mejores playas del Mar Rojo con todo el confort.',
        'desc_pt': 'Desfrute das melhores praias do Mar Vermelho com todo o conforto.'
    },
    'Nile Cruises': {
        'es': 'Cruceros por el Nilo',
        'pt': 'Cruzeiros pelo Nilo',
        'desc_es': 'Navega por el legendario Rio Nilo en cruceros de lujo.',
        'desc_pt': 'Navegue pelo lendario Rio Nilo em cruzeiros de luxo.'
    },
    'Desert Safari': {
        'es': 'Safari en el Desierto',
        'pt': 'Safari no Deserto',
        'desc_es': 'Explora los vastos desiertos de Egipto en emocionantes safaris.',
        'desc_pt': 'Explore os vastos desertos do Egito em emocionantes safaris.'
    },
    'Family Tours': {
        'es': 'Tours Familiares',
        'pt': 'Tours em Familia',
        'desc_es': 'Tours disenados especialmente para familias con ninos.',
        'desc_pt': 'Tours projetados especialmente para familias com criancas.'
    },
    'Luxury Tours': {
        'es': 'Tours de Lujo',
        'pt': 'Tours de Luxo',
        'desc_es': 'Experiencias exclusivas con los mejores hoteles y servicios VIP.',
        'desc_pt': 'Experiencias exclusivas com os melhores hoteis e servicos VIP.'
    },
    'Day Tours': {
        'es': 'Excursiones de un Dia',
        'pt': 'Passeios de um Dia',
        'desc_es': 'Excursiones cortas para explorar los principales destinos.',
        'desc_pt': 'Passeios curtos para explorar os principais destinos.'
    },
    'Historical Tours': {
        'es': 'Tours Historicos',
        'pt': 'Tours Historicos',
        'desc_es': 'Viaja en el tiempo explorando los monumentos antiguos de Egipto.',
        'desc_pt': 'Viaje no tempo explorando os monumentos antigos do Egito.'
    },
    'Religious Tours': {
        'es': 'Tours Religiosos',
        'pt': 'Tours Religiosos',
        'desc_es': 'Visita los lugares sagrados y de peregrinacion en Egipto.',
        'desc_pt': 'Visite os lugares sagrados e de peregrinacao no Egito.'
    },
    'Honeymoon': {
        'es': 'Luna de Miel',
        'pt': 'Lua de Mel',
        'desc_es': 'Paquetes romanticos perfectos para parejas recien casadas.',
        'desc_pt': 'Pacotes romanticos perfeitos para casais recem-casados.'
    },
    'Egypt & Jordan': {
        'es': 'Egipto y Jordania',
        'pt': 'Egito e Jordania',
        'desc_es': 'Combina lo mejor de Egipto y Jordania en un solo viaje.',
        'desc_pt': 'Combine o melhor do Egito e Jordania em uma so viagem.'
    },
    'Egypt & Dubai': {
        'es': 'Egipto y Dubai',
        'pt': 'Egito e Dubai',
        'desc_es': 'Descubre la magia de Egipto y el lujo de Dubai.',
        'desc_pt': 'Descubra a magia do Egito e o luxo de Dubai.'
    },
    'Diving Tours': {
        'es': 'Tours de Buceo',
        'pt': 'Tours de Mergulho',
        'desc_es': 'Explora los arrecifes de coral del Mar Rojo.',
        'desc_pt': 'Explore os recifes de coral do Mar Vermelho.'
    },
    'Photography Tours': {
        'es': 'Tours Fotograficos',
        'pt': 'Tours Fotograficos',
        'desc_es': 'Tours especiales para fotografos con los mejores puntos de vista.',
        'desc_pt': 'Tours especiais para fotografos com os melhores pontos de vista.'
    },
    'Wellness & Spa': {
        'es': 'Bienestar y Spa',
        'pt': 'Bem-estar e Spa',
        'desc_es': 'Relajate y rejuvenece en los mejores spas de Egipto.',
        'desc_pt': 'Relaxe e rejuvenesca nos melhores spas do Egito.'
    },
    'Budget Tours': {
        'es': 'Tours Economicos',
        'pt': 'Tours Economicos',
        'desc_es': 'Viaja a Egipto sin gastar mucho con nuestros tours economicos.',
        'desc_pt': 'Viaje ao Egito sem gastar muito com nossos tours economicos.'
    },
}

# ============================================================
# TOUR TYPES
# ============================================================
TOUR_TYPE_TRANSLATIONS = {
    'Multi-Day Package': {
        'es': 'Paquete de Varios Dias',
        'pt': 'Pacote de Varios Dias',
        'desc_es': 'Paquetes completos que incluyen alojamiento, traslados, comidas y tours guiados por varios dias.',
        'desc_pt': 'Pacotes completos que incluem hospedagem, transfers, refeicoes e passeios guiados por varios dias.'
    },
    'Day Trip': {
        'es': 'Excursion de un Dia',
        'pt': 'Passeio de um Dia',
        'desc_es': 'Excursiones de un dia completo para explorar destinos cercanos con regreso el mismo dia.',
        'desc_pt': 'Passeios de um dia completo para explorar destinos proximos com retorno no mesmo dia.'
    },
    'Multi Destination': {
        'es': 'Multi Destino',
        'pt': 'Multi Destino',
        'desc_es': 'Tours que combinan varios paises como Egipto con Jordania, Dubai o Turquia.',
        'desc_pt': 'Tours que combinam varios paises como Egito com Jordania, Dubai ou Turquia.'
    },
    'Nile Cruise': {
        'es': 'Crucero por el Nilo',
        'pt': 'Cruzeiro pelo Nilo',
        'desc_es': 'Cruceros de lujo navegando por el Rio Nilo entre Luxor y Asuan.',
        'desc_pt': 'Cruzeiros de luxo navegando pelo Rio Nilo entre Luxor e Aswan.'
    },
    'Private Tour': {
        'es': 'Tour Privado',
        'pt': 'Tour Privado',
        'desc_es': 'Tours exclusivos con guia privado, vehiculo y itinerario personalizado.',
        'desc_pt': 'Tours exclusivos com guia privado, veiculo e roteiro personalizado.'
    },
    'Small Group': {
        'es': 'Grupo Pequeno',
        'pt': 'Grupo Pequeno',
        'desc_es': 'Tours en grupos reducidos de maximo 12 personas para una experiencia mas personal.',
        'desc_pt': 'Tours em grupos reduzidos de maximo 12 pessoas para uma experiencia mais pessoal.'
    },
    'Group Tour': {
        'es': 'Tour en Grupo',
        'pt': 'Tour em Grupo',
        'desc_es': 'Tours economicos en grupos grandes con salidas programadas.',
        'desc_pt': 'Tours economicos em grupos grandes com saidas programadas.'
    },
    'Shore Excursion': {
        'es': 'Excursion en Tierra',
        'pt': 'Excursao em Terra',
        'desc_es': 'Excursiones disenadas para pasajeros de cruceros que hacen escala en puertos egipcios.',
        'desc_pt': 'Excursoes projetadas para passageiros de cruzeiros que fazem escala em portos egipcios.'
    },
    'Self-Guided': {
        'es': 'Autoguiado',
        'pt': 'Autoguiado',
        'desc_es': 'Viaja a tu propio ritmo con itinerarios y reservas pre-organizadas.',
        'desc_pt': 'Viaje no seu proprio ritmo com roteiros e reservas pre-organizadas.'
    },
    'Tailor Made': {
        'es': 'A Medida',
        'pt': 'Sob Medida',
        'desc_es': 'Tours completamente personalizados segun tus preferencias y presupuesto.',
        'desc_pt': 'Tours completamente personalizados de acordo com suas preferencias e orcamento.'
    },
}

# ============================================================
# DESTINATIONS
# ============================================================
DESTINATION_TRANSLATIONS = {
    'Cairo': {
        'es': 'El Cairo',
        'pt': 'Cairo',
        'tagline_es': 'La capital de los faraones',
        'tagline_pt': 'A capital dos faraos',
        'desc_es': 'El Cairo, la vibrante capital de Egipto, es hogar de las iconicas Piramides de Giza, la Esfinge y el Museo Egipcio. Una ciudad donde lo antiguo y lo moderno se encuentran.',
        'desc_pt': 'O Cairo, a vibrante capital do Egito, e lar das iconicas Piramides de Giza, a Esfinge e o Museu Egipcio. Uma cidade onde o antigo e o moderno se encontram.'
    },
    'Luxor': {
        'es': 'Luxor',
        'pt': 'Luxor',
        'tagline_es': 'El museo al aire libre mas grande del mundo',
        'tagline_pt': 'O maior museu ao ar livre do mundo',
        'desc_es': 'Luxor, la antigua Tebas, alberga el Valle de los Reyes, el Templo de Karnak y el Templo de Luxor. Un destino imprescindible para los amantes de la historia.',
        'desc_pt': 'Luxor, a antiga Tebas, abriga o Vale dos Reis, o Templo de Karnak e o Templo de Luxor. Um destino imperdivel para os amantes da historia.'
    },
    'Aswan': {
        'es': 'Asuan',
        'pt': 'Aswan',
        'tagline_es': 'La perla del Nilo',
        'tagline_pt': 'A perola do Nilo',
        'desc_es': 'Asuan ofrece paisajes impresionantes del Nilo, el Templo de Philae y es la puerta de entrada a Abu Simbel.',
        'desc_pt': 'Aswan oferece paisagens impressionantes do Nilo, o Templo de Philae e e a porta de entrada para Abu Simbel.'
    },
    'Alexandria': {
        'es': 'Alejandria',
        'pt': 'Alexandria',
        'tagline_es': 'La perla del Mediterraneo',
        'tagline_pt': 'A perola do Mediterraneo',
        'desc_es': 'Alejandria, fundada por Alejandro Magno, es una ciudad costera con rica historia griega y romana.',
        'desc_pt': 'Alexandria, fundada por Alexandre o Grande, e uma cidade costeira com rica historia grega e romana.'
    },
    'Sharm El Sheikh': {
        'es': 'Sharm El Sheikh',
        'pt': 'Sharm El Sheikh',
        'tagline_es': 'El paraiso del Mar Rojo',
        'tagline_pt': 'O paraiso do Mar Vermelho',
        'desc_es': 'Sharm El Sheikh es famoso por sus playas de arena blanca, arrecifes de coral y deportes acuaticos.',
        'desc_pt': 'Sharm El Sheikh e famoso por suas praias de areia branca, recifes de coral e esportes aquaticos.'
    },
    'Hurghada': {
        'es': 'Hurghada',
        'pt': 'Hurghada',
        'tagline_es': 'Sol, playa y buceo',
        'tagline_pt': 'Sol, praia e mergulho',
        'desc_es': 'Hurghada es un destino de playa popular con excelentes oportunidades de buceo y snorkel.',
        'desc_pt': 'Hurghada e um destino de praia popular com excelentes oportunidades de mergulho e snorkel.'
    },
    'Dahab': {
        'es': 'Dahab',
        'pt': 'Dahab',
        'tagline_es': 'El destino bohemio del Sinai',
        'tagline_pt': 'O destino boemio do Sinai',
        'desc_es': 'Dahab es un pueblo costero relajado, perfecto para buceo, windsurf y exploracion del desierto.',
        'desc_pt': 'Dahab e uma vila costeira relaxada, perfeita para mergulho, windsurf e exploracao do deserto.'
    },
    'Siwa Oasis': {
        'es': 'Oasis de Siwa',
        'pt': 'Oasis de Siwa',
        'tagline_es': 'Un oasis en el desierto occidental',
        'tagline_pt': 'Um oasis no deserto ocidental',
        'desc_es': 'Siwa es un oasis remoto con cultura unica, manantiales naturales y ruinas antiguas.',
        'desc_pt': 'Siwa e um oasis remoto com cultura unica, nascentes naturais e ruinas antigas.'
    },
    'Marsa Alam': {
        'es': 'Marsa Alam',
        'pt': 'Marsa Alam',
        'tagline_es': 'Buceo virgen en el Mar Rojo',
        'tagline_pt': 'Mergulho virgem no Mar Vermelho',
        'desc_es': 'Marsa Alam ofrece algunos de los mejores sitios de buceo del Mar Rojo con arrecifes pristinos.',
        'desc_pt': 'Marsa Alam oferece alguns dos melhores locais de mergulho do Mar Vermelho com recifes pristinos.'
    },
    'White Desert': {
        'es': 'Desierto Blanco',
        'pt': 'Deserto Branco',
        'tagline_es': 'Paisajes surrealistas de yeso blanco',
        'tagline_pt': 'Paisagens surrealistas de gesso branco',
        'desc_es': 'El Desierto Blanco presenta formaciones rocosas unicas de piedra caliza blanca esculpidas por el viento.',
        'desc_pt': 'O Deserto Branco apresenta formacoes rochosas unicas de pedra calcaria branca esculpidas pelo vento.'
    },
}

# ============================================================
# COMMON HIGHLIGHT TRANSLATIONS
# ============================================================
HIGHLIGHT_TRANSLATIONS = {
    'Expert Guides': {'es': 'Guias Expertos', 'pt': 'Guias Especializados'},
    'Expert Guide': {'es': 'Guia Experto', 'pt': 'Guia Especializado'},
    'Professional Guide': {'es': 'Guia Profesional', 'pt': 'Guia Profissional'},
    'Small Groups': {'es': 'Grupos Pequenos', 'pt': 'Grupos Pequenos'},
    'Small Group': {'es': 'Grupo Pequeno', 'pt': 'Grupo Pequeno'},
    'Luxury Transport': {'es': 'Transporte de Lujo', 'pt': 'Transporte de Luxo'},
    'Luxury Hotels': {'es': 'Hoteles de Lujo', 'pt': 'Hoteis de Luxo'},
    'Premium Hotels': {'es': 'Hoteles Premium', 'pt': 'Hoteis Premium'},
    'All Inclusive': {'es': 'Todo Incluido', 'pt': 'Tudo Incluido'},
    'Local Experience': {'es': 'Experiencia Local', 'pt': 'Experiencia Local'},
    'Unique Access': {'es': 'Acceso Exclusivo', 'pt': 'Acesso Exclusivo'},
    'Flexible Schedule': {'es': 'Horario Flexible', 'pt': 'Horario Flexivel'},
    'Flexible Itinerary': {'es': 'Itinerario Flexible', 'pt': 'Roteiro Flexivel'},
    'Family Friendly': {'es': 'Ideal para Familias', 'pt': 'Ideal para Familias'},
    'Kid Friendly': {'es': 'Amigable para Ninos', 'pt': 'Amigavel para Criancas'},
    'Adventure Activities': {'es': 'Actividades de Aventura', 'pt': 'Atividades de Aventura'},
    'Cultural Immersion': {'es': 'Inmersion Cultural', 'pt': 'Imersao Cultural'},
    'Historical Sites': {'es': 'Sitios Historicos', 'pt': 'Sitios Historicos'},
    'Ancient Monuments': {'es': 'Monumentos Antiguos', 'pt': 'Monumentos Antigos'},
    'Authentic Cuisine': {'es': 'Cocina Autentica', 'pt': 'Culinaria Autentica'},
    'Photo Opportunities': {'es': 'Oportunidades Fotograficas', 'pt': 'Oportunidades Fotograficas'},
    'Sunset Views': {'es': 'Vistas al Atardecer', 'pt': 'Vistas do Por do Sol'},
    'Desert Experience': {'es': 'Experiencia en el Desierto', 'pt': 'Experiencia no Deserto'},
    'Nile Views': {'es': 'Vistas al Nilo', 'pt': 'Vistas do Nilo'},
    'Beach Access': {'es': 'Acceso a la Playa', 'pt': 'Acesso a Praia'},
    'Diving Included': {'es': 'Buceo Incluido', 'pt': 'Mergulho Incluido'},
    'Snorkeling': {'es': 'Snorkel', 'pt': 'Snorkel'},
    'Camel Ride': {'es': 'Paseo en Camello', 'pt': 'Passeio de Camelo'},
    'Felucca Ride': {'es': 'Paseo en Feluca', 'pt': 'Passeio de Feluca'},
    'Hot Air Balloon': {'es': 'Globo Aerostatico', 'pt': 'Balao de Ar Quente'},
    '24/7 Support': {'es': 'Soporte 24/7', 'pt': 'Suporte 24/7'},
    'Airport Transfer': {'es': 'Traslado al Aeropuerto', 'pt': 'Transfer do Aeroporto'},
    'Free Cancellation': {'es': 'Cancelacion Gratuita', 'pt': 'Cancelamento Gratis'},
    'Best Price Guarantee': {'es': 'Garantia del Mejor Precio', 'pt': 'Garantia do Melhor Preco'},
}

# ============================================================
# INCLUSION TRANSLATIONS
# ============================================================
INCLUSION_TRANSLATIONS = {
    'Hotel accommodations': {'es': 'Alojamiento en hotel', 'pt': 'Hospedagem em hotel'},
    'Airport transfers': {'es': 'Traslados al aeropuerto', 'pt': 'Transfers do aeroporto'},
    'All meals': {'es': 'Todas las comidas', 'pt': 'Todas as refeicoes'},
    'Daily breakfast': {'es': 'Desayuno diario', 'pt': 'Cafe da manha diario'},
    'Professional guide': {'es': 'Guia profesional', 'pt': 'Guia profissional'},
    'English speaking guide': {'es': 'Guia de habla inglesa', 'pt': 'Guia que fala ingles'},
    'Entrance fees': {'es': 'Entradas incluidas', 'pt': 'Ingressos incluidos'},
    'All entrance fees': {'es': 'Todas las entradas', 'pt': 'Todos os ingressos'},
    'Air-conditioned vehicle': {'es': 'Vehiculo con aire acondicionado', 'pt': 'Veiculo com ar condicionado'},
    'Private vehicle': {'es': 'Vehiculo privado', 'pt': 'Veiculo privado'},
    'Bottled water': {'es': 'Agua embotellada', 'pt': 'Agua engarrafada'},
    'Mineral water': {'es': 'Agua mineral', 'pt': 'Agua mineral'},
    'Tips and gratuities': {'es': 'Propinas', 'pt': 'Gorjetas'},
    'Personal expenses': {'es': 'Gastos personales', 'pt': 'Despesas pessoais'},
    'Travel insurance': {'es': 'Seguro de viaje', 'pt': 'Seguro de viagem'},
    'International flights': {'es': 'Vuelos internacionales', 'pt': 'Voos internacionais'},
    'Domestic flights': {'es': 'Vuelos domesticos', 'pt': 'Voos domesticos'},
    'Internal flights': {'es': 'Vuelos internos', 'pt': 'Voos internos'},
    'Visa fees': {'es': 'Tasas de visa', 'pt': 'Taxas de visto'},
    'Egypt visa': {'es': 'Visa de Egipto', 'pt': 'Visto do Egito'},
    'Optional tours': {'es': 'Tours opcionales', 'pt': 'Passeios opcionais'},
    'Optional activities': {'es': 'Actividades opcionales', 'pt': 'Atividades opcionais'},
    'Nile cruise': {'es': 'Crucero por el Nilo', 'pt': 'Cruzeiro pelo Nilo'},
    'Full board on cruise': {'es': 'Pension completa en crucero', 'pt': 'Pensao completa no cruzeiro'},
    'Sound and light show': {'es': 'Espectaculo de luz y sonido', 'pt': 'Show de luz e som'},
    'Hot air balloon ride': {'es': 'Paseo en globo aerostatico', 'pt': 'Passeio de balao'},
    'Camel ride at pyramids': {'es': 'Paseo en camello en las piramides', 'pt': 'Passeio de camelo nas piramides'},
    'Felucca sailing': {'es': 'Navegacion en feluca', 'pt': 'Navegacao em feluca'},
    'Snorkeling equipment': {'es': 'Equipo de snorkel', 'pt': 'Equipamento de snorkel'},
    'Diving equipment': {'es': 'Equipo de buceo', 'pt': 'Equipamento de mergulho'},
    'Beach access': {'es': 'Acceso a la playa', 'pt': 'Acesso a praia'},
    'WiFi on board': {'es': 'WiFi a bordo', 'pt': 'WiFi a bordo'},
    'Luxury accommodation': {'es': 'Alojamiento de lujo', 'pt': 'Hospedagem de luxo'},
    '5-star hotels': {'es': 'Hoteles 5 estrellas', 'pt': 'Hoteis 5 estrelas'},
    '4-star hotels': {'es': 'Hoteles 4 estrellas', 'pt': 'Hoteis 4 estrelas'},
    'Breakfast and dinner': {'es': 'Desayuno y cena', 'pt': 'Cafe da manha e jantar'},
    'Lunch included': {'es': 'Almuerzo incluido', 'pt': 'Almoco incluido'},
    'Drinks on board': {'es': 'Bebidas a bordo', 'pt': 'Bebidas a bordo'},
    'Alcoholic beverages': {'es': 'Bebidas alcoholicas', 'pt': 'Bebidas alcoolicas'},
}

# ============================================================
# ACTIVITIES
# ============================================================
ACTIVITY_TRANSLATIONS = {
    'Pyramids Sound & Light Show': {
        'es': 'Espectaculo de Luz y Sonido en las Piramides',
        'pt': 'Show de Luz e Som nas Piramides',
        'desc_es': 'Un espectaculo nocturno magico que narra la historia del antiguo Egipto con luces y sonido.',
        'desc_pt': 'Um show noturno magico que narra a historia do antigo Egito com luzes e som.'
    },
    'Felucca Ride on the Nile': {
        'es': 'Paseo en Feluca por el Nilo',
        'pt': 'Passeio de Feluca pelo Nilo',
        'desc_es': 'Navega en un tradicional velero egipcio por las tranquilas aguas del Nilo.',
        'desc_pt': 'Navegue em um tradicional veleiro egipcio pelas tranquilas aguas do Nilo.'
    },
    'Desert Safari': {
        'es': 'Safari en el Desierto',
        'pt': 'Safari no Deserto',
        'desc_es': 'Aventura en 4x4 por las dunas del desierto con cena beduina.',
        'desc_pt': 'Aventura em 4x4 pelas dunas do deserto com jantar beduino.'
    },
    'Pyramid Tour': {
        'es': 'Tour de las Piramides',
        'pt': 'Tour das Piramides',
        'desc_es': 'Visita guiada a las Piramides de Giza y la Gran Esfinge.',
        'desc_pt': 'Visita guiada as Piramides de Giza e a Grande Esfinge.'
    },
    'Egyptian Museum Visit': {
        'es': 'Visita al Museo Egipcio',
        'pt': 'Visita ao Museu Egipcio',
        'desc_es': 'Explora la mayor coleccion de antiguedades egipcias del mundo.',
        'desc_pt': 'Explore a maior colecao de antiguidades egipcias do mundo.'
    },
    'Nile Dinner Cruise': {
        'es': 'Crucero con Cena por el Nilo',
        'pt': 'Cruzeiro com Jantar pelo Nilo',
        'desc_es': 'Cena a bordo navegando por el Nilo con musica y entretenimiento.',
        'desc_pt': 'Jantar a bordo navegando pelo Nilo com musica e entretenimento.'
    },
    'Hot Air Balloon Luxor': {
        'es': 'Globo Aerostatico en Luxor',
        'pt': 'Balao de Ar Quente em Luxor',
        'desc_es': 'Vuelo al amanecer sobre el Valle de los Reyes con vistas espectaculares.',
        'desc_pt': 'Voo ao nascer do sol sobre o Vale dos Reis com vistas espetaculares.'
    },
    'Snorkeling Trip': {
        'es': 'Excursion de Snorkel',
        'pt': 'Passeio de Snorkel',
        'desc_es': 'Explora los coloridos arrecifes de coral del Mar Rojo.',
        'desc_pt': 'Explore os coloridos recifes de coral do Mar Vermelho.'
    },
    'Diving Experience': {
        'es': 'Experiencia de Buceo',
        'pt': 'Experiencia de Mergulho',
        'desc_es': 'Buceo en los mejores sitios del Mar Rojo con instructores certificados.',
        'desc_pt': 'Mergulho nos melhores locais do Mar Vermelho com instrutores certificados.'
    },
    'Quad Biking': {
        'es': 'Paseo en Quad',
        'pt': 'Passeio de Quadriciclo',
        'desc_es': 'Conduce un quad por el desierto egipcio al atardecer.',
        'desc_pt': 'Dirija um quadriciclo pelo deserto egipcio ao por do sol.'
    },
    'Camel Ride': {
        'es': 'Paseo en Camello',
        'pt': 'Passeio de Camelo',
        'desc_es': 'Monta en camello alrededor de las piramides como los antiguos egipcios.',
        'desc_pt': 'Monte em um camelo ao redor das piramides como os antigos egipcios.'
    },
    'Khan El Khalili Tour': {
        'es': 'Tour de Khan El Khalili',
        'pt': 'Tour de Khan El Khalili',
        'desc_es': 'Explora el historico bazar de El Cairo con sus tiendas y cafes tradicionales.',
        'desc_pt': 'Explore o historico bazar do Cairo com suas lojas e cafes tradicionais.'
    },
    'Temple of Karnak': {
        'es': 'Templo de Karnak',
        'pt': 'Templo de Karnak',
        'desc_es': 'Visita el complejo de templos mas grande del antiguo Egipto.',
        'desc_pt': 'Visite o maior complexo de templos do antigo Egito.'
    },
    'Valley of the Kings': {
        'es': 'Valle de los Reyes',
        'pt': 'Vale dos Reis',
        'desc_es': 'Explora las tumbas de los faraones del Nuevo Reino.',
        'desc_pt': 'Explore os tumulos dos faraos do Novo Reino.'
    },
    'Abu Simbel Tour': {
        'es': 'Tour de Abu Simbel',
        'pt': 'Tour de Abu Simbel',
        'desc_es': 'Visita los impresionantes templos de Ramses II en Abu Simbel.',
        'desc_pt': 'Visite os impressionantes templos de Ramses II em Abu Simbel.'
    },
}

# ============================================================
# TAGS
# ============================================================
TAG_TRANSLATIONS = {
    'Beach': {'es': 'Playa', 'pt': 'Praia'},
    'Cairo': {'es': 'El Cairo', 'pt': 'Cairo'},
    'Culture': {'es': 'Cultura', 'pt': 'Cultura'},
    'Desert': {'es': 'Desierto', 'pt': 'Deserto'},
    'Diving': {'es': 'Buceo', 'pt': 'Mergulho'},
    'History': {'es': 'Historia', 'pt': 'Historia'},
    'Luxor': {'es': 'Luxor', 'pt': 'Luxor'},
    'Nile': {'es': 'Nilo', 'pt': 'Nilo'},
    'Pyramids': {'es': 'Piramides', 'pt': 'Piramides'},
    'Temple': {'es': 'Templo', 'pt': 'Templo'},
    'Temples': {'es': 'Templos', 'pt': 'Templos'},
    'Ancient': {'es': 'Antiguo', 'pt': 'Antigo'},
    'Egypt': {'es': 'Egipto', 'pt': 'Egito'},
    'Travel': {'es': 'Viaje', 'pt': 'Viagem'},
    'Tips': {'es': 'Consejos', 'pt': 'Dicas'},
    'Adventure': {'es': 'Aventura', 'pt': 'Aventura'},
    'Photography': {'es': 'Fotografia', 'pt': 'Fotografia'},
    'Food': {'es': 'Gastronomia', 'pt': 'Gastronomia'},
    'Museum': {'es': 'Museo', 'pt': 'Museu'},
    'Cruise': {'es': 'Crucero', 'pt': 'Cruzeiro'},
    'Family': {'es': 'Familia', 'pt': 'Familia'},
    'Luxury': {'es': 'Lujo', 'pt': 'Luxo'},
    'Budget': {'es': 'Economico', 'pt': 'Economico'},
    'Snorkeling': {'es': 'Snorkel', 'pt': 'Snorkel'},
    'Safari': {'es': 'Safari', 'pt': 'Safari'},
}


def update_tour_categories():
    """Update tour category translations."""
    print("\nUpdating Tour Categories...")
    count = 0
    for cat in TourCategory.objects.all():
        if cat.name in TOUR_CATEGORY_TRANSLATIONS:
            trans = TOUR_CATEGORY_TRANSLATIONS[cat.name]
            cat.name_es = trans['es']
            cat.name_pt = trans['pt']
            if 'desc_es' in trans and cat.description:
                cat.description_es = trans['desc_es']
                cat.description_pt = trans['desc_pt']
            cat.save()
            count += 1
    print(f"  Updated {count} categories")


def update_tour_types():
    """Update tour type translations."""
    print("\nUpdating Tour Types...")
    count = 0
    for tt in TourType.objects.all():
        if tt.name in TOUR_TYPE_TRANSLATIONS:
            trans = TOUR_TYPE_TRANSLATIONS[tt.name]
            tt.name_es = trans['es']
            tt.name_pt = trans['pt']
            tt.description_es = trans['desc_es']
            tt.description_pt = trans['desc_pt']
            tt.save()
            count += 1
    print(f"  Updated {count} tour types")


def update_destinations():
    """Update destination translations."""
    print("\nUpdating Destinations...")
    count = 0
    for dest in Destination.objects.all():
        if dest.name in DESTINATION_TRANSLATIONS:
            trans = DESTINATION_TRANSLATIONS[dest.name]
            dest.name_es = trans['es']
            dest.name_pt = trans['pt']
            if 'tagline_es' in trans and dest.tagline:
                dest.tagline_es = trans['tagline_es']
                dest.tagline_pt = trans['tagline_pt']
            if 'desc_es' in trans:
                dest.description_es = trans['desc_es']
                dest.description_pt = trans['desc_pt']
            dest.save()
            count += 1
    print(f"  Updated {count} destinations")


def update_tour_highlights():
    """Update tour highlight translations."""
    print("\nUpdating Tour Highlights...")
    count = 0
    for hl in TourHighlight.objects.all():
        updated = False

        # Check for exact match
        if hl.title in HIGHLIGHT_TRANSLATIONS:
            trans = HIGHLIGHT_TRANSLATIONS[hl.title]
            hl.title_es = trans['es']
            hl.title_pt = trans['pt']
            updated = True
        else:
            # Try partial match
            for en, trans in HIGHLIGHT_TRANSLATIONS.items():
                if en.lower() in hl.title.lower():
                    hl.title_es = hl.title.replace(en, trans['es'])
                    hl.title_pt = hl.title.replace(en, trans['pt'])
                    updated = True
                    break

        if not updated:
            hl.title_es = hl.title
            hl.title_pt = hl.title

        # Description
        if hl.description:
            hl.description_es = translate_general(hl.description, 'es')
            hl.description_pt = translate_general(hl.description, 'pt')

        hl.save()
        count += 1

    print(f"  Updated {count} highlights")


def update_tour_inclusions():
    """Update tour inclusion translations."""
    print("\nUpdating Tour Inclusions...")
    count = 0
    for inc in TourInclusion.objects.all():
        matched = False

        # Check for exact or partial match
        for en, trans in INCLUSION_TRANSLATIONS.items():
            if en.lower() in inc.item.lower():
                inc.item_es = inc.item.lower().replace(en.lower(), trans['es'])
                inc.item_pt = inc.item.lower().replace(en.lower(), trans['pt'])
                # Capitalize first letter
                inc.item_es = inc.item_es[0].upper() + inc.item_es[1:] if inc.item_es else ''
                inc.item_pt = inc.item_pt[0].upper() + inc.item_pt[1:] if inc.item_pt else ''
                matched = True
                break

        if not matched:
            inc.item_es = translate_general(inc.item, 'es')
            inc.item_pt = translate_general(inc.item, 'pt')

        inc.save()
        count += 1

    print(f"  Updated {count} inclusions")


def update_activities():
    """Update activity translations."""
    print("\nUpdating Activities...")
    count = 0
    for act in Activity.objects.all():
        if act.name in ACTIVITY_TRANSLATIONS:
            trans = ACTIVITY_TRANSLATIONS[act.name]
            act.name_es = trans['es']
            act.name_pt = trans['pt']
            act.description_es = trans['desc_es']
            act.description_pt = trans['desc_pt']
        else:
            act.name_es = translate_general(act.name, 'es')
            act.name_pt = translate_general(act.name, 'pt')
            if act.description:
                act.description_es = translate_general(act.description, 'es')
                act.description_pt = translate_general(act.description, 'pt')
        act.save()
        count += 1
    print(f"  Updated {count} activities")


def update_tags():
    """Update tag translations."""
    print("\nUpdating Tags...")
    count = 0
    for tag in Tag.objects.all():
        if tag.name in TAG_TRANSLATIONS:
            trans = TAG_TRANSLATIONS[tag.name]
            tag.name_es = trans['es']
            tag.name_pt = trans['pt']
        else:
            tag.name_es = tag.name
            tag.name_pt = tag.name
        tag.save()
        count += 1
    print(f"  Updated {count} tags")


def translate_general(text, lang):
    """General translation for text."""
    if not text:
        return ''

    # Common word replacements
    if lang == 'es':
        replacements = {
            'Explore': 'Explora', 'Visit': 'Visita', 'Discover': 'Descubre',
            'Experience': 'Experimenta', 'Enjoy': 'Disfruta', 'includes': 'incluye',
            'with': 'con', 'and': 'y', 'the': 'el', 'tour': 'tour',
            'trip': 'viaje', 'day': 'dia', 'night': 'noche', 'hotel': 'hotel',
            'transfer': 'traslado', 'guide': 'guia', 'breakfast': 'desayuno',
            'lunch': 'almuerzo', 'dinner': 'cena', 'ancient': 'antiguo',
            'temple': 'templo', 'pyramid': 'piramide', 'museum': 'museo',
            'river': 'rio', 'desert': 'desierto', 'beach': 'playa',
            'sea': 'mar', 'city': 'ciudad', 'professional': 'profesional',
            'expert': 'experto', 'luxury': 'lujo', 'private': 'privado',
            'group': 'grupo', 'Cairo': 'El Cairo', 'Luxor': 'Luxor',
            'Aswan': 'Asuan', 'Alexandria': 'Alejandria',
            'Giza': 'Guiza', 'Nile': 'Nilo', 'Red Sea': 'Mar Rojo',
            'included': 'incluido', 'excluded': 'no incluido',
            'Airport': 'Aeropuerto', 'Hotel': 'Hotel',
            'Breakfast': 'Desayuno', 'Lunch': 'Almuerzo', 'Dinner': 'Cena',
            'Morning': 'Manana', 'Afternoon': 'Tarde', 'Evening': 'Noche',
            'Free time': 'Tiempo libre', 'Overnight': 'Pernocte',
        }
    else:
        replacements = {
            'Explore': 'Explore', 'Visit': 'Visite', 'Discover': 'Descubra',
            'Experience': 'Experimente', 'Enjoy': 'Aproveite', 'includes': 'inclui',
            'with': 'com', 'and': 'e', 'the': 'o', 'tour': 'tour',
            'trip': 'viagem', 'day': 'dia', 'night': 'noite', 'hotel': 'hotel',
            'transfer': 'transfer', 'guide': 'guia', 'breakfast': 'cafe da manha',
            'lunch': 'almoco', 'dinner': 'jantar', 'ancient': 'antigo',
            'temple': 'templo', 'pyramid': 'piramide', 'museum': 'museu',
            'river': 'rio', 'desert': 'deserto', 'beach': 'praia',
            'sea': 'mar', 'city': 'cidade', 'professional': 'profissional',
            'expert': 'especialista', 'luxury': 'luxo', 'private': 'privado',
            'group': 'grupo', 'Cairo': 'Cairo', 'Luxor': 'Luxor',
            'Aswan': 'Aswan', 'Alexandria': 'Alexandria',
            'Giza': 'Gize', 'Nile': 'Nilo', 'Red Sea': 'Mar Vermelho',
            'included': 'incluido', 'excluded': 'nao incluido',
            'Airport': 'Aeroporto', 'Hotel': 'Hotel',
            'Breakfast': 'Cafe da manha', 'Lunch': 'Almoco', 'Dinner': 'Jantar',
            'Morning': 'Manha', 'Afternoon': 'Tarde', 'Evening': 'Noite',
            'Free time': 'Tempo livre', 'Overnight': 'Pernoite',
        }

    result = text
    for en, trans in replacements.items():
        result = result.replace(en, trans)

    return result


def update_tour_itineraries():
    """Update tour itinerary translations."""
    print("\nUpdating Tour Itineraries...")
    count = 0
    for itin in TourItinerary.objects.all():
        if itin.title:
            itin.title_es = translate_general(itin.title, 'es')
            itin.title_pt = translate_general(itin.title, 'pt')
        if itin.description:
            itin.description_es = translate_general(itin.description, 'es')
            itin.description_pt = translate_general(itin.description, 'pt')
        if itin.locations:
            itin.locations_es = translate_general(itin.locations, 'es')
            itin.locations_pt = translate_general(itin.locations, 'pt')
        if itin.meals_included:
            meals_es = itin.meals_included.replace('Breakfast', 'Desayuno').replace('Lunch', 'Almuerzo').replace('Dinner', 'Cena')
            meals_pt = itin.meals_included.replace('Breakfast', 'Cafe da manha').replace('Lunch', 'Almoco').replace('Dinner', 'Jantar')
            itin.meals_included_es = meals_es
            itin.meals_included_pt = meals_pt
        if itin.accommodation:
            itin.accommodation_es = translate_general(itin.accommodation, 'es')
            itin.accommodation_pt = translate_general(itin.accommodation, 'pt')
        itin.save()
        count += 1
    print(f"  Updated {count} itineraries")


def update_tour_images():
    """Update tour image translations."""
    print("\nUpdating Tour Images...")
    count = 0
    for img in TourImage.objects.all():
        if img.caption:
            img.caption_es = translate_general(img.caption, 'es')
            img.caption_pt = translate_general(img.caption, 'pt')
        if img.alt_text:
            img.alt_text_es = translate_general(img.alt_text, 'es')
            img.alt_text_pt = translate_general(img.alt_text, 'pt')
        img.save()
        count += 1
    print(f"  Updated {count} tour images")


def update_destination_images():
    """Update destination image translations."""
    print("\nUpdating Destination Images...")
    count = 0
    for img in DestinationImage.objects.all():
        if img.caption:
            img.caption_es = translate_general(img.caption, 'es')
            img.caption_pt = translate_general(img.caption, 'pt')
        if img.alt_text:
            img.alt_text_es = translate_general(img.alt_text, 'es')
            img.alt_text_pt = translate_general(img.alt_text, 'pt')
        img.save()
        count += 1
    print(f"  Updated {count} destination images")


def update_early_booking():
    """Update early booking translations."""
    print("\nUpdating Early Booking Offers...")
    count = 0
    for offer in EarlyBookingOffer.objects.all():
        # Title
        offer.title_es = offer.title.replace('Early Bird', 'Reserva Anticipada').replace('Early Booking', 'Reserva Anticipada').replace('Special', 'Especial').replace('Summer', 'Verano').replace('Winter', 'Invierno').replace('Family', 'Familiar').replace('Adventure', 'Aventura').replace('Discount', 'Descuento').replace('Escape', 'Escapada')
        offer.title_pt = offer.title.replace('Early Bird', 'Reserva Antecipada').replace('Early Booking', 'Reserva Antecipada').replace('Special', 'Especial').replace('Summer', 'Verao').replace('Winter', 'Inverno').replace('Family', 'Familiar').replace('Adventure', 'Aventura').replace('Discount', 'Desconto').replace('Escape', 'Escapada')

        if offer.subtitle:
            offer.subtitle_es = translate_general(offer.subtitle, 'es')
            offer.subtitle_pt = translate_general(offer.subtitle, 'pt')
        if offer.description:
            offer.description_es = translate_general(offer.description, 'es')
            offer.description_pt = translate_general(offer.description, 'pt')
        if offer.terms_conditions:
            offer.terms_conditions_es = translate_general(offer.terms_conditions, 'es')
            offer.terms_conditions_pt = translate_general(offer.terms_conditions, 'pt')
        if offer.cancellation_policy:
            offer.cancellation_policy_es = translate_general(offer.cancellation_policy, 'es')
            offer.cancellation_policy_pt = translate_general(offer.cancellation_policy, 'pt')
        if offer.badge_text:
            offer.badge_text_es = offer.badge_text.replace('Early Bird', 'Anticipado').replace('Special', 'Especial').replace('Limited', 'Limitado').replace('Save', 'Ahorra')
            offer.badge_text_pt = offer.badge_text.replace('Early Bird', 'Antecipado').replace('Special', 'Especial').replace('Limited', 'Limitado').replace('Save', 'Economize')
        offer.save()
        count += 1
    print(f"  Updated {count} early booking offers")


def update_reviews():
    """Update review translations."""
    print("\nUpdating Reviews...")
    count = 0
    for review in Review.objects.all():
        if review.title:
            review.title_es = translate_general(review.title, 'es')
            review.title_pt = translate_general(review.title, 'pt')
        if review.content:
            review.content_es = translate_general(review.content, 'es')
            review.content_pt = translate_general(review.content, 'pt')
        review.save()
        count += 1
    print(f"  Updated {count} reviews")


def update_testimonials():
    """Update testimonial translations."""
    print("\nUpdating Testimonials...")
    count = 0
    for test in Testimonial.objects.all():
        if test.quote:
            test.quote_es = translate_general(test.quote, 'es')
            test.quote_pt = translate_general(test.quote, 'pt')
        test.save()
        count += 1
    print(f"  Updated {count} testimonials")


def update_offices():
    """Update office translations."""
    print("\nUpdating Offices...")
    count = 0
    for office in Office.objects.all():
        if office.name:
            office.name_es = office.name.replace('Headquarters', 'Sede Central').replace('Office', 'Oficina').replace('Branch', 'Sucursal')
            office.name_pt = office.name.replace('Headquarters', 'Sede').replace('Office', 'Escritorio').replace('Branch', 'Filial')
        if office.city:
            office.city_es = translate_general(office.city, 'es')
            office.city_pt = translate_general(office.city, 'pt')
        if office.address:
            office.address_es = office.address
            office.address_pt = office.address
        if office.working_hours:
            hours_es = office.working_hours.replace('Monday', 'Lunes').replace('Tuesday', 'Martes').replace('Wednesday', 'Miercoles').replace('Thursday', 'Jueves').replace('Friday', 'Viernes').replace('Saturday', 'Sabado').replace('Sunday', 'Domingo').replace('to', 'a').replace('AM', 'AM').replace('PM', 'PM')
            hours_pt = office.working_hours.replace('Monday', 'Segunda').replace('Tuesday', 'Terca').replace('Wednesday', 'Quarta').replace('Thursday', 'Quinta').replace('Friday', 'Sexta').replace('Saturday', 'Sabado').replace('Sunday', 'Domingo').replace('to', 'a')
            office.working_hours_es = hours_es
            office.working_hours_pt = hours_pt
        office.save()
        count += 1
    print(f"  Updated {count} offices")


def update_statistics():
    """Update statistic translations."""
    print("\nUpdating Statistics...")
    count = 0
    for stat in Statistic.objects.all():
        if stat.description:
            stat.description_es = translate_general(stat.description, 'es')
            stat.description_pt = translate_general(stat.description, 'pt')
        stat.save()
        count += 1
    print(f"  Updated {count} statistics")


def main():
    print("\n" + "#"*60)
    print("# COMPLETING ALL TRANSLATIONS")
    print("#"*60)

    update_tour_categories()
    update_tour_types()
    update_destinations()
    update_tour_highlights()
    update_tour_inclusions()
    update_tour_itineraries()
    update_tour_images()
    update_destination_images()
    update_activities()
    update_tags()
    update_early_booking()
    update_reviews()
    update_testimonials()
    update_offices()
    update_statistics()

    print("\n" + "#"*60)
    print("# ALL TRANSLATIONS COMPLETED!")
    print("#"*60 + "\n")


if __name__ == '__main__':
    main()
