#!/usr/bin/env python
"""
Script to fill empty translation fields for blog posts and tours.
"""
import os
import sys
import django
import time

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.blog.models import Post, Category, Tag
from apps.tours.models import Tour, TourCategory, TourType, TourItinerary, TourHighlight, TourInclusion

# Translation dictionaries for common terms
ES_TRANSLATIONS = {
    # Blog Posts
    'Dahab City and Resort': 'Ciudad y Resort de Dahab',
    'What to Buy and What to Shop in Egypt': 'Qué Comprar en Egipto',
    'Brief History of Cairo': 'Breve Historia de El Cairo',
    'National Park of Gabal Elba': 'Parque Nacional de Gabal Elba',
    'Travel to Egypt During Ramadan': 'Viajar a Egipto Durante el Ramadán',
    'Sharm El Sheikh': 'Sharm El Sheikh',
    'Siwa Oasis': 'Oasis de Siwa',
    'Kharga Oasis': 'Oasis de Kharga',
    'Khan El Khalili Bazaar': 'Bazar Khan El Khalili',
    'Climate of Egypt': 'Clima de Egipto',

    # Tours
    'Egypt with Abu Simbel and Hurghada': 'Egipto con Abu Simbel y Hurghada',
    'Splendid Pharaonic Egypt': 'Espléndido Egipto Faraónico',
    'Queen Isis Route': 'Ruta de la Reina Isis',
    'Pleasing Sharm El Sheikh with Cairo': 'Placentero Sharm El Sheikh con El Cairo',
    'The Journey of Moses': 'El Viaje de Moisés',
    'Exceptional Egypt': 'Egipto Excepcional',
    'The Best of Egypt and Morocco': 'Lo Mejor de Egipto y Marruecos',
    'Promotional Package to Egypt': 'Paquete Promocional a Egipto',

    # Categories
    'Destinations': 'Destinos',
    'Travel Tips': 'Consejos de Viaje',
    'Egyptian History': 'Historia Egipcia',
    'Adventure': 'Aventura',
    'Culture & History': 'Cultura e Historia',
    'Classic Egypt Tours': 'Tours Clásicos de Egipto',
    'Cultural & Historical': 'Cultural e Histórico',
    'Beach & Diving': 'Playa y Buceo',
    'Religious & Spiritual': 'Religioso y Espiritual',
    'Luxury Tours': 'Tours de Lujo',
    'Multi-Country Tours': 'Tours Multi-País',

    # Tour Types
    'Multi-Day Package': 'Paquete de Varios Días',
    'Multi-Country Tour': 'Tour Multi-País',

    # Common terms
    'Day': 'Día',
    'Arrival': 'Llegada',
    'Departure': 'Salida',
    'Cairo': 'El Cairo',
    'Pyramids': 'Pirámides',
    'Temple': 'Templo',
    'Museum': 'Museo',
    'Cruise': 'Crucero',
    'Nile': 'Nilo',
    'Beach': 'Playa',
    'Desert': 'Desierto',
    'Valley': 'Valle',
    'Kings': 'Reyes',

    # Destinations
    'Morocco': 'Marruecos',

    # Inclusions
    'Accommodation in 4-5 star hotels': 'Alojamiento en hoteles de 4-5 estrellas',
    'Daily breakfast': 'Desayuno diario',
    'Airport transfers': 'Traslados al aeropuerto',
    'Professional Egyptologist guide': 'Guía egiptólogo profesional',
    'All entrance fees': 'Todas las entradas',
    'Air-conditioned transportation': 'Transporte con aire acondicionado',
    'International flights': 'Vuelos internacionales',
    'Travel insurance': 'Seguro de viaje',
    'Personal expenses': 'Gastos personales',
    'Tipping': 'Propinas',
}

PT_TRANSLATIONS = {
    # Blog Posts
    'Dahab City and Resort': 'Cidade e Resort de Dahab',
    'What to Buy and What to Shop in Egypt': 'O Que Comprar no Egito',
    'Brief History of Cairo': 'Breve História do Cairo',
    'National Park of Gabal Elba': 'Parque Nacional de Gabal Elba',
    'Travel to Egypt During Ramadan': 'Viajar para o Egito Durante o Ramadã',
    'Sharm El Sheikh': 'Sharm El Sheikh',
    'Siwa Oasis': 'Oásis de Siwa',
    'Kharga Oasis': 'Oásis de Kharga',
    'Khan El Khalili Bazaar': 'Bazar Khan El Khalili',
    'Climate of Egypt': 'Clima do Egito',

    # Tours
    'Egypt with Abu Simbel and Hurghada': 'Egito com Abu Simbel e Hurghada',
    'Splendid Pharaonic Egypt': 'Esplêndido Egito Faraônico',
    'Queen Isis Route': 'Rota da Rainha Ísis',
    'Pleasing Sharm El Sheikh with Cairo': 'Agradável Sharm El Sheikh com Cairo',
    'The Journey of Moses': 'A Jornada de Moisés',
    'Exceptional Egypt': 'Egito Excepcional',
    'The Best of Egypt and Morocco': 'O Melhor do Egito e Marrocos',
    'Promotional Package to Egypt': 'Pacote Promocional para o Egito',

    # Categories
    'Destinations': 'Destinos',
    'Travel Tips': 'Dicas de Viagem',
    'Egyptian History': 'História Egípcia',
    'Adventure': 'Aventura',
    'Culture & History': 'Cultura e História',
    'Classic Egypt Tours': 'Tours Clássicos do Egito',
    'Cultural & Historical': 'Cultural e Histórico',
    'Beach & Diving': 'Praia e Mergulho',
    'Religious & Spiritual': 'Religioso e Espiritual',
    'Luxury Tours': 'Tours de Luxo',
    'Multi-Country Tours': 'Tours Multi-País',

    # Tour Types
    'Multi-Day Package': 'Pacote de Vários Dias',
    'Multi-Country Tour': 'Tour Multi-País',

    # Common terms
    'Day': 'Dia',
    'Arrival': 'Chegada',
    'Departure': 'Partida',
    'Cairo': 'Cairo',
    'Pyramids': 'Pirâmides',
    'Temple': 'Templo',
    'Museum': 'Museu',
    'Cruise': 'Cruzeiro',
    'Nile': 'Nilo',
    'Beach': 'Praia',
    'Desert': 'Deserto',
    'Valley': 'Vale',
    'Kings': 'Reis',

    # Destinations
    'Morocco': 'Marrocos',

    # Inclusions
    'Accommodation in 4-5 star hotels': 'Acomodação em hotéis 4-5 estrelas',
    'Daily breakfast': 'Café da manhã diário',
    'Airport transfers': 'Transfers do aeroporto',
    'Professional Egyptologist guide': 'Guia egiptólogo profissional',
    'All entrance fees': 'Todas as taxas de entrada',
    'Air-conditioned transportation': 'Transporte com ar condicionado',
    'International flights': 'Voos internacionais',
    'Travel insurance': 'Seguro de viagem',
    'Personal expenses': 'Despesas pessoais',
    'Tipping': 'Gorjetas',
}

# Detailed translations for excerpts and descriptions
EXCERPT_TRANSLATIONS_ES = {
    'Dahab City and Resort': 'Dahab es la mejor ciudad costera del sur del Sinaí. Puedes esperar excelentes servicios de sus resorts y hoteles con impresionantes vistas al Mar Rojo.',
    'What to Buy and What to Shop in Egypt': 'Una guía completa para comprar en Egipto, desde recuerdos tradicionales hasta artesanías únicas y artículos preciosos que deberías llevar a casa.',
    'Brief History of Cairo': 'Explora los fascinantes orígenes de El Cairo desde la era del antiguo Egipto, pasando por el período griego hasta la conquista romana y más allá.',
    'National Park of Gabal Elba': 'Ubicado a 250 km al sur de Marsa Alam en el desierto oriental de Egipto cerca de la frontera con Sudán, Gabal Elba es un punto único de biodiversidad.',
    'Travel to Egypt During Ramadan': 'Viajar a Egipto durante el Ramadán es una experiencia única que ofrece información sobre la cultura y tradiciones egipcias.',
    'Sharm El Sheikh': 'Sharm El Sheikh es un destino de buceo y snorkel de primer nivel con aguas cristalinas que muestran corales y colorida vida marina.',
    'Siwa Oasis': 'El Oasis de Siwa es uno de los destinos más aislados y encantadores de Egipto, ubicado en el desierto occidental cerca de la frontera con Libia.',
    'Kharga Oasis': 'El Oasis de Kharga es uno de los sitios más encantadores del mundo con una rica historia y varios templos construidos a lo largo de los siglos.',
    'Khan El Khalili Bazaar': 'Khan El Khalili es un mercado histórico en el distrito El-Hussin de El Cairo cerca de la Mezquita Al-Azhar, fundado en 970 d.C.',
    'Climate of Egypt': 'El clima de Egipto difiere según las regiones del Mediterráneo, los desiertos y el Alto Egipto. En general, es moderado tanto en invierno como en verano.',
}

EXCERPT_TRANSLATIONS_PT = {
    'Dahab City and Resort': 'Dahab é a melhor cidade costeira do Sul do Sinai. Você pode esperar excelentes serviços de seus resorts e hotéis com vistas deslumbrantes do Mar Vermelho.',
    'What to Buy and What to Shop in Egypt': 'Um guia completo para compras no Egito, desde souvenirs tradicionais até artesanatos únicos e itens preciosos que você deve levar para casa.',
    'Brief History of Cairo': 'Explore as origens fascinantes do Cairo desde a era do antigo Egito, passando pelo período grego até a conquista romana e além.',
    'National Park of Gabal Elba': 'Localizado a 250 km ao sul de Marsa Alam no deserto oriental do Egito perto da fronteira com o Sudão, Gabal Elba é um hotspot de biodiversidade único.',
    'Travel to Egypt During Ramadan': 'Viajar para o Egito durante o Ramadã é uma experiência única que oferece insights sobre a cultura e tradições egípcias.',
    'Sharm El Sheikh': 'Sharm El Sheikh é um destino de mergulho e snorkeling de primeira classe com águas cristalinas exibindo corais e vida marinha colorida.',
    'Siwa Oasis': 'O Oásis de Siwa é um dos destinos mais isolados e encantadores do Egito, localizado no deserto ocidental perto da fronteira com a Líbia.',
    'Kharga Oasis': 'O Oásis de Kharga é um dos locais mais encantadores do mundo com uma história rica e vários templos construídos ao longo dos séculos.',
    'Khan El Khalili Bazaar': 'Khan El Khalili é um mercado histórico no distrito de El-Hussin do Cairo perto da Mesquita Al-Azhar, fundado em 970 d.C.',
    'Climate of Egypt': 'O clima do Egito difere com base nas regiões do Mediterrâneo, desertos e Alto Egito. No geral, é moderado tanto no inverno quanto no verão.',
}

# Tour short descriptions
TOUR_SHORT_DESC_ES = {
    'Egypt with Abu Simbel and Hurghada': '13 días explorando los tesoros de Egipto con Abu Simbel y relajación en el Mar Rojo en Hurghada.',
    'Splendid Pharaonic Egypt': '10 días descubriendo El Cairo, Alejandría y un crucero por el Nilo de 4 noches desde Luxor a Asuán.',
    'Queen Isis Route': '12 días siguiendo a la diosa Isis por los sitios más sagrados de Egipto incluyendo Abydos y Dendera.',
    'Pleasing Sharm El Sheikh with Cairo': '7 días combinando relajación en el Mar Rojo en Sharm El Sheikh con las maravillas antiguas de El Cairo.',
    'The Journey of Moses': '10 días siguiendo el viaje bíblico a través de Egipto y Jordania incluyendo el Monte Sinaí y Petra.',
    'Exceptional Egypt': '13 días experimentando las atracciones del antiguo Egipto, playas del Mar Rojo y tesoros del Mediterráneo.',
    'The Best of Egypt and Morocco': '14 días explorando el patrimonio cultural de dos increíbles destinos del norte de África.',
    'Promotional Package to Egypt': '8 días experimentando El Cairo, Giza y un crucero por el Nilo de 4 noches a un valor excepcional.',
}

TOUR_SHORT_DESC_PT = {
    'Egypt with Abu Simbel and Hurghada': '13 dias explorando os tesouros do Egito com Abu Simbel e relaxamento no Mar Vermelho em Hurghada.',
    'Splendid Pharaonic Egypt': '10 dias descobrindo Cairo, Alexandria e um cruzeiro de 4 noites pelo Nilo de Luxor a Aswan.',
    'Queen Isis Route': '12 dias seguindo a deusa Ísis pelos locais mais sagrados do Egito incluindo Abydos e Dendera.',
    'Pleasing Sharm El Sheikh with Cairo': '7 dias combinando relaxamento no Mar Vermelho em Sharm El Sheikh com as maravilhas antigas do Cairo.',
    'The Journey of Moses': '10 dias seguindo a jornada bíblica através do Egito e Jordânia incluindo o Monte Sinai e Petra.',
    'Exceptional Egypt': '13 dias experimentando atrações do antigo Egito, praias do Mar Vermelho e tesouros do Mediterrâneo.',
    'The Best of Egypt and Morocco': '14 dias explorando o patrimônio cultural de dois destinos incríveis do norte da África.',
    'Promotional Package to Egypt': '8 dias experimentando Cairo, Giza e um cruzeiro de 4 noites pelo Nilo com valor excepcional.',
}

# Itinerary translations
ITINERARY_ES = {
    'Arrival in Cairo': 'Llegada a El Cairo',
    'Arrival Cairo': 'Llegada a El Cairo',
    'Pyramids & Egyptian Museum': 'Pirámides y Museo Egipcio',
    'Pyramids & Saqqara': 'Pirámides y Saqqara',
    'Pyramids & Museum': 'Pirámides y Museo',
    'Fly to Aswan': 'Vuelo a Asuán',
    'Fly to Luxor': 'Vuelo a Luxor',
    'Fly to Luxor - Nile Cruise': 'Vuelo a Luxor - Crucero por el Nilo',
    'Fly to Cairo, then Casablanca': 'Vuelo a El Cairo, luego Casablanca',
    'Abu Simbel Excursion': 'Excursión a Abu Simbel',
    'Nile Cruise - Kom Ombo & Edfu': 'Crucero por el Nilo - Kom Ombo y Edfu',
    'Nile Cruise - Luxor': 'Crucero por el Nilo - Luxor',
    'Nile Cruise': 'Crucero por el Nilo',
    'West Bank Luxor': 'Orilla Occidental de Luxor',
    'Luxor West Bank': 'Orilla Occidental de Luxor',
    'Transfer to Hurghada': 'Traslado a Hurghada',
    'Return to Cairo': 'Regreso a El Cairo',
    'Fly to Cairo': 'Vuelo a El Cairo',
    'Departure': 'Salida',
    'Hurghada - Free Day': 'Hurghada - Día Libre',
    'Hurghada': 'Hurghada',
    'Alexandria Day Trip': 'Excursión a Alejandría',
    'Alexandria': 'Alejandría',
    'Cairo Sightseeing': 'Visita a El Cairo',
    'Egyptian Museum & Old Cairo': 'Museo Egipcio y El Cairo Antiguo',
    'Egyptian Museum & Cairo': 'Museo Egipcio y El Cairo',
    'Abydos & Dendera': 'Abydos y Dendera',
    'Edfu Temple': 'Templo de Edfu',
    'Edfu': 'Edfu',
    'Kom Ombo - Aswan': 'Kom Ombo - Asuán',
    'Kom Ombo & Aswan': 'Kom Ombo y Asuán',
    'Aswan Sightseeing': 'Visita a Asuán',
    'Aswan': 'Asuán',
    'Fly to Sharm El Sheikh': 'Vuelo a Sharm El Sheikh',
    'Sharm El Sheikh': 'Sharm El Sheikh',
    'Coptic Cairo': 'El Cairo Copto',
    'Mount Sinai Sunrise': 'Amanecer en el Monte Sinaí',
    'Cross to Jordan': 'Cruce a Jordania',
    'Petra Full Day': 'Día Completo en Petra',
    'Wadi Rum': 'Wadi Rum',
    'Mount Nebo & Amman': 'Monte Nebo y Amán',
    'Transfer to Hurghada': 'Traslado a Hurghada',
    'Casablanca - Rabat': 'Casablanca - Rabat',
    'Fes': 'Fez',
    'Sahara Desert': 'Desierto del Sahara',
    'Dades Valley': 'Valle del Dades',
    'Marrakech': 'Marrakech',
    'Edfu & Kom Ombo': 'Edfu y Kom Ombo',
}

ITINERARY_PT = {
    'Arrival in Cairo': 'Chegada ao Cairo',
    'Arrival Cairo': 'Chegada ao Cairo',
    'Pyramids & Egyptian Museum': 'Pirâmides e Museu Egípcio',
    'Pyramids & Saqqara': 'Pirâmides e Saqqara',
    'Pyramids & Museum': 'Pirâmides e Museu',
    'Fly to Aswan': 'Voo para Aswan',
    'Fly to Luxor': 'Voo para Luxor',
    'Fly to Luxor - Nile Cruise': 'Voo para Luxor - Cruzeiro pelo Nilo',
    'Fly to Cairo, then Casablanca': 'Voo para Cairo, depois Casablanca',
    'Abu Simbel Excursion': 'Excursão a Abu Simbel',
    'Nile Cruise - Kom Ombo & Edfu': 'Cruzeiro pelo Nilo - Kom Ombo e Edfu',
    'Nile Cruise - Luxor': 'Cruzeiro pelo Nilo - Luxor',
    'Nile Cruise': 'Cruzeiro pelo Nilo',
    'West Bank Luxor': 'Margem Ocidental de Luxor',
    'Luxor West Bank': 'Margem Ocidental de Luxor',
    'Transfer to Hurghada': 'Transfer para Hurghada',
    'Return to Cairo': 'Retorno ao Cairo',
    'Fly to Cairo': 'Voo para Cairo',
    'Departure': 'Partida',
    'Hurghada - Free Day': 'Hurghada - Dia Livre',
    'Hurghada': 'Hurghada',
    'Alexandria Day Trip': 'Excursão a Alexandria',
    'Alexandria': 'Alexandria',
    'Cairo Sightseeing': 'Passeio pelo Cairo',
    'Egyptian Museum & Old Cairo': 'Museu Egípcio e Cairo Antigo',
    'Egyptian Museum & Cairo': 'Museu Egípcio e Cairo',
    'Abydos & Dendera': 'Abydos e Dendera',
    'Edfu Temple': 'Templo de Edfu',
    'Edfu': 'Edfu',
    'Kom Ombo - Aswan': 'Kom Ombo - Aswan',
    'Kom Ombo & Aswan': 'Kom Ombo e Aswan',
    'Aswan Sightseeing': 'Passeio por Aswan',
    'Aswan': 'Aswan',
    'Fly to Sharm El Sheikh': 'Voo para Sharm El Sheikh',
    'Sharm El Sheikh': 'Sharm El Sheikh',
    'Coptic Cairo': 'Cairo Copta',
    'Mount Sinai Sunrise': 'Nascer do Sol no Monte Sinai',
    'Cross to Jordan': 'Travessia para Jordânia',
    'Petra Full Day': 'Dia Completo em Petra',
    'Wadi Rum': 'Wadi Rum',
    'Mount Nebo & Amman': 'Monte Nebo e Amã',
    'Transfer to Hurghada': 'Transfer para Hurghada',
    'Casablanca - Rabat': 'Casablanca - Rabat',
    'Fes': 'Fez',
    'Sahara Desert': 'Deserto do Saara',
    'Dades Valley': 'Vale do Dades',
    'Marrakech': 'Marrakech',
    'Edfu & Kom Ombo': 'Edfu e Kom Ombo',
}

# Itinerary description translations
ITINERARY_DESC_ES = {
    'Welcome to Egypt! Meet and assist at Cairo International Airport. Transfer to your hotel.': '¡Bienvenido a Egipto! Recepción y asistencia en el Aeropuerto Internacional de El Cairo. Traslado a su hotel.',
    'Welcome to Egypt! Airport meet and greet, transfer to hotel.': '¡Bienvenido a Egipto! Recepción en el aeropuerto, traslado al hotel.',
    'Welcome to Egypt! Transfer to your luxury hotel.': '¡Bienvenido a Egipto! Traslado a su hotel de lujo.',
    'Welcome to Egypt! Transfer to your Cairo hotel.': '¡Bienvenido a Egipto! Traslado a su hotel en El Cairo.',
    'Welcome to Egypt! Transfer to hotel.': '¡Bienvenido a Egipto! Traslado al hotel.',
    'Welcome to Egypt! VIP airport meet and greet.': '¡Bienvenido a Egipto! Recepción VIP en el aeropuerto.',
    'Airport transfer to hotel. Welcome meeting.': 'Traslado del aeropuerto al hotel. Reunión de bienvenida.',
    'Visit the Pyramids of Giza, Sphinx, and the Egyptian Museum with its treasures of Tutankhamun.': 'Visite las Pirámides de Giza, la Esfinge y el Museo Egipcio con los tesoros de Tutankamón.',
    'Full day visiting the Pyramids of Giza, Sphinx, and the Egyptian Museum.': 'Día completo visitando las Pirámides de Giza, la Esfinge y el Museo Egipcio.',
    'Visit Pyramids, Sphinx, and Egyptian Museum.': 'Visite las Pirámides, la Esfinge y el Museo Egipcio.',
    'Full day: Pyramids, Sphinx, Egyptian Museum.': 'Día completo: Pirámides, Esfinge, Museo Egipcio.',
    'Visit Giza Pyramids, Sphinx, and the Step Pyramid at Saqqara.': 'Visite las Pirámides de Giza, la Esfinge y la Pirámide Escalonada en Saqqara.',
    'Visit Giza Pyramids, Sphinx, and the ancient burial grounds of Saqqara.': 'Visite las Pirámides de Giza, la Esfinge y las antiguas necrópolis de Saqqara.',
    'Morning flight to Aswan. Visit the High Dam, Unfinished Obelisk, and Philae Temple. Board Nile Cruise.': 'Vuelo matutino a Asuán. Visite la Presa Alta, el Obelisco Inacabado y el Templo de Filae. Embarque en el Crucero por el Nilo.',
    'Flight to Aswan. Board Nile Cruise.': 'Vuelo a Asuán. Embarque en el Crucero por el Nilo.',
    'Early morning excursion to Abu Simbel to see the magnificent temples of Ramses II.': 'Excursión temprano por la mañana a Abu Simbel para ver los magníficos templos de Ramsés II.',
    'Sail to Kom Ombo Temple, then continue to Edfu to visit the Temple of Horus.': 'Navegue al Templo de Kom Ombo, luego continúe a Edfu para visitar el Templo de Horus.',
    'Visit both temples as you sail south.': 'Visite ambos templos mientras navega hacia el sur.',
    'Arrive in Luxor. Visit Karnak Temple and Luxor Temple.': 'Llegada a Luxor. Visite el Templo de Karnak y el Templo de Luxor.',
    'Morning flight to Luxor. Visit Karnak and Luxor Temples. Board your Nile Cruise.': 'Vuelo matutino a Luxor. Visite los Templos de Karnak y Luxor. Embarque en su Crucero por el Nilo.',
    'Flight to Luxor. Board cruise. Karnak Temple.': 'Vuelo a Luxor. Embarque en el crucero. Templo de Karnak.',
    'Flight to Luxor. Board your luxury Nile cruise. Visit Luxor Temple.': 'Vuelo a Luxor. Embarque en su crucero de lujo por el Nilo. Visite el Templo de Luxor.',
    'Explore the Valley of the Kings, Hatshepsut Temple, and the Colossi of Memnon.': 'Explore el Valle de los Reyes, el Templo de Hatshepsut y los Colosos de Memnón.',
    'Visit Valley of the Kings, Hatshepsut Temple, and Colossi of Memnon. Sail towards Edfu.': 'Visite el Valle de los Reyes, el Templo de Hatshepsut y los Colosos de Memnón. Navegue hacia Edfu.',
    'Valley of the Kings, Hatshepsut Temple, Colossi of Memnon.': 'Valle de los Reyes, Templo de Hatshepsut, Colosos de Memnón.',
    'Valley of the Kings, Karnak Temple.': 'Valle de los Reyes, Templo de Karnak.',
    'Valley of the Kings, Hatshepsut Temple.': 'Valle de los Reyes, Templo de Hatshepsut.',
    'Private transfer to Hurghada. Afternoon free for beach relaxation.': 'Traslado privado a Hurghada. Tarde libre para relajarse en la playa.',
    'Scenic drive to Hurghada. Check in to beach resort.': 'Viaje panorámico a Hurghada. Registro en el resort de playa.',
    'Full day at leisure. Optional activities: snorkeling, diving, or desert safari.': 'Día completo libre. Actividades opcionales: snorkel, buceo o safari en el desierto.',
    'Another day to enjoy Hurghada\'s beaches and water activities.': 'Otro día para disfrutar de las playas y actividades acuáticas de Hurghada.',
    'Continue enjoying your Red Sea paradise.': 'Continúe disfrutando de su paraíso en el Mar Rojo.',
    'Free day for beach and water activities.': 'Día libre para playa y actividades acuáticas.',
    'Another day of Red Sea relaxation.': 'Otro día de relajación en el Mar Rojo.',
    'Transfer back to Cairo. Free time for last-minute shopping at Khan El Khalili.': 'Regreso a El Cairo. Tiempo libre para compras de último momento en Khan El Khalili.',
    'Fly back to Cairo. Free afternoon.': 'Vuelo de regreso a El Cairo. Tarde libre.',
    'Fly back to Cairo. Free afternoon for shopping.': 'Vuelo de regreso a El Cairo. Tarde libre para compras.',
    'Transfer to Cairo International Airport for your departure flight.': 'Traslado al Aeropuerto Internacional de El Cairo para su vuelo de salida.',
    'Transfer to airport for your departure flight.': 'Traslado al aeropuerto para su vuelo de salida.',
    'Transfer to Sharm El Sheikh Airport for your departure flight.': 'Traslado al Aeropuerto de Sharm El Sheikh para su vuelo de salida.',
    'Transfer to Amman Airport for departure.': 'Traslado al Aeropuerto de Amán para la salida.',
    'Transfer to Marrakech airport.': 'Traslado al aeropuerto de Marrakech.',
    'Transfer to Hurghada or Cairo airport.': 'Traslado al aeropuerto de Hurghada o El Cairo.',
    'Transfer to airport.': 'Traslado al aeropuerto.',
    'Day trip to Alexandria visiting Catacombs, Pompey\'s Pillar, and the new Bibliotheca Alexandrina.': 'Excursión a Alejandría visitando las Catacumbas, el Pilar de Pompeyo y la nueva Biblioteca de Alejandría.',
    'Full day in the Mediterranean city of Alexander the Great.': 'Día completo en la ciudad mediterránea de Alejandro Magno.',
    'Visit the magnificent Temple of Horus at Edfu. Continue sailing to Kom Ombo.': 'Visite el magnífico Templo de Horus en Edfu. Continúe navegando hacia Kom Ombo.',
    'Visit Temple of Horus at Edfu. Continue sailing south.': 'Visite el Templo de Horus en Edfu. Continúe navegando hacia el sur.',
    'Visit Kom Ombo Temple dedicated to Sobek and Horus. Sail to Aswan.': 'Visite el Templo de Kom Ombo dedicado a Sobek y Horus. Navegue hacia Asuán.',
    'Morning visit to Kom Ombo. Arrive in Aswan, visit Philae Temple.': 'Visita matutina a Kom Ombo. Llegada a Asuán, visite el Templo de Filae.',
    'Kom Ombo Temple. Arrive Aswan. Felucca ride at sunset.': 'Templo de Kom Ombo. Llegada a Asuán. Paseo en faluca al atardecer.',
    'Visit Aswan High Dam, Unfinished Obelisk, and the beautiful Philae Temple.': 'Visite la Presa Alta de Asuán, el Obelisco Inacabado y el hermoso Templo de Filae.',
    'High Dam, Unfinished Obelisk. Optional felucca ride around Elephantine Island.': 'Presa Alta, Obelisco Inacabado. Paseo opcional en faluca alrededor de la Isla Elefantina.',
    'High Dam, Philae Temple, Unfinished Obelisk.': 'Presa Alta, Templo de Filae, Obelisco Inacabado.',
    'Disembark cruise. Flight to Cairo. Afternoon free for shopping.': 'Desembarque del crucero. Vuelo a El Cairo. Tarde libre para compras.',
    'Morning at the Egyptian Museum. Afternoon visit Coptic Cairo and Islamic Cairo.': 'Mañana en el Museo Egipcio. Tarde visitando El Cairo Copto y El Cairo Islámico.',
    'Egyptian Museum, Old Cairo, Khan El Khalili bazaar.': 'Museo Egipcio, El Cairo Antiguo, bazar Khan El Khalili.',
    'Day trip to Alexandria. Visit the Library, Catacombs, and Mediterranean waterfront.': 'Excursión a Alejandría. Visite la Biblioteca, las Catacumbas y el paseo marítimo del Mediterráneo.',
    'Full day excursion to Abydos Temple and Dendera\'s Temple of Hathor.': 'Excursión de día completo al Templo de Abydos y al Templo de Hathor en Dendera.',
    'Morning flight to Sharm El Sheikh. Check in to your beach resort. Afternoon at leisure.': 'Vuelo matutino a Sharm El Sheikh. Registro en su resort de playa. Tarde libre.',
    'Free day to enjoy the beach, pool, or optional excursions.': 'Día libre para disfrutar de la playa, la piscina o excursiones opcionales.',
    'Another day of relaxation. Optional snorkeling at Ras Mohammed or diving trip.': 'Otro día de relajación. Snorkel opcional en Ras Mohammed o excursión de buceo.',
    'Last full day in paradise. Optional desert safari or glass-bottom boat trip.': 'Último día completo en el paraíso. Safari en el desierto opcional o paseo en bote con fondo de cristal.',
    'Free day at Red Sea resort. Relax or optional snorkeling.': 'Día libre en el resort del Mar Rojo. Relájese o snorkel opcional.',
    'Visit Coptic Churches, Hanging Church, and Ben Ezra Synagogue. Transfer to Sinai.': 'Visite las Iglesias Coptas, la Iglesia Colgante y la Sinagoga Ben Ezra. Traslado al Sinaí.',
    'Pre-dawn climb to Mount Sinai for sunrise. Visit St. Catherine\'s Monastery.': 'Ascenso antes del amanecer al Monte Sinaí para ver el amanecer. Visite el Monasterio de Santa Catalina.',
    'Ferry to Aqaba, Jordan. Transfer to Petra.': 'Ferry a Aqaba, Jordania. Traslado a Petra.',
    'Explore the ancient rose-red city of Petra, one of the New Seven Wonders.': 'Explore la antigua ciudad rosa de Petra, una de las Nuevas Siete Maravillas.',
    'Morning in Wadi Rum desert. Jeep safari through the stunning landscape.': 'Mañana en el desierto de Wadi Rum. Safari en jeep por el impresionante paisaje.',
    'Visit Mount Nebo where Moses saw the Promised Land. Continue to Amman.': 'Visite el Monte Nebo donde Moisés vio la Tierra Prometida. Continúe hacia Amán.',
    'Sail from Aswan towards Luxor with temple visits.': 'Navegue desde Asuán hacia Luxor con visitas a templos.',
    'International flight to Morocco.': 'Vuelo internacional a Marruecos.',
    'Hassan II Mosque. Drive to Rabat.': 'Mezquita Hassan II. Viaje a Rabat.',
    'Drive to Fes. Explore the ancient medina.': 'Viaje a Fez. Explore la antigua medina.',
    'Full day in Fes - tanneries, madrasas, souks.': 'Día completo en Fez - curtidurías, madrazas, zocos.',
    'Journey to Merzouga. Camel trek into the Sahara.': 'Viaje a Merzouga. Trek en camello por el Sahara.',
    'Drive through the dramatic Dades Gorges.': 'Conduzca a través de las dramáticas Gargantas del Dades.',
    'Arrive in Marrakech. Evening in Djemaa el-Fna square.': 'Llegada a Marrakech. Noche en la plaza Djemaa el-Fna.',
    'Full day exploring Marrakech - palaces, gardens, souks.': 'Día completo explorando Marrakech - palacios, jardines, zocos.',
}

ITINERARY_DESC_PT = {
    'Welcome to Egypt! Meet and assist at Cairo International Airport. Transfer to your hotel.': 'Bem-vindo ao Egito! Recepção e assistência no Aeroporto Internacional do Cairo. Transfer para o seu hotel.',
    'Welcome to Egypt! Airport meet and greet, transfer to hotel.': 'Bem-vindo ao Egito! Recepção no aeroporto, transfer para o hotel.',
    'Welcome to Egypt! Transfer to your luxury hotel.': 'Bem-vindo ao Egito! Transfer para o seu hotel de luxo.',
    'Welcome to Egypt! Transfer to your Cairo hotel.': 'Bem-vindo ao Egito! Transfer para o seu hotel no Cairo.',
    'Welcome to Egypt! Transfer to hotel.': 'Bem-vindo ao Egito! Transfer para o hotel.',
    'Welcome to Egypt! VIP airport meet and greet.': 'Bem-vindo ao Egito! Recepção VIP no aeroporto.',
    'Airport transfer to hotel. Welcome meeting.': 'Transfer do aeroporto para o hotel. Reunião de boas-vindas.',
    'Visit the Pyramids of Giza, Sphinx, and the Egyptian Museum with its treasures of Tutankhamun.': 'Visite as Pirâmides de Gizé, a Esfinge e o Museu Egípcio com os tesouros de Tutancâmon.',
    'Full day visiting the Pyramids of Giza, Sphinx, and the Egyptian Museum.': 'Dia inteiro visitando as Pirâmides de Gizé, a Esfinge e o Museu Egípcio.',
    'Visit Pyramids, Sphinx, and Egyptian Museum.': 'Visite as Pirâmides, a Esfinge e o Museu Egípcio.',
    'Full day: Pyramids, Sphinx, Egyptian Museum.': 'Dia inteiro: Pirâmides, Esfinge, Museu Egípcio.',
    'Visit Giza Pyramids, Sphinx, and the Step Pyramid at Saqqara.': 'Visite as Pirâmides de Gizé, a Esfinge e a Pirâmide de Degraus em Saqqara.',
    'Visit Giza Pyramids, Sphinx, and the ancient burial grounds of Saqqara.': 'Visite as Pirâmides de Gizé, a Esfinge e as antigas necrópoles de Saqqara.',
    'Morning flight to Aswan. Visit the High Dam, Unfinished Obelisk, and Philae Temple. Board Nile Cruise.': 'Voo matinal para Aswan. Visite a Barragem Alta, o Obelisco Inacabado e o Templo de Philae. Embarque no Cruzeiro pelo Nilo.',
    'Flight to Aswan. Board Nile Cruise.': 'Voo para Aswan. Embarque no Cruzeiro pelo Nilo.',
    'Early morning excursion to Abu Simbel to see the magnificent temples of Ramses II.': 'Excursão no início da manhã a Abu Simbel para ver os magníficos templos de Ramsés II.',
    'Sail to Kom Ombo Temple, then continue to Edfu to visit the Temple of Horus.': 'Navegue até o Templo de Kom Ombo, depois continue até Edfu para visitar o Templo de Hórus.',
    'Visit both temples as you sail south.': 'Visite ambos os templos enquanto navega para o sul.',
    'Arrive in Luxor. Visit Karnak Temple and Luxor Temple.': 'Chegada em Luxor. Visite o Templo de Karnak e o Templo de Luxor.',
    'Morning flight to Luxor. Visit Karnak and Luxor Temples. Board your Nile Cruise.': 'Voo matinal para Luxor. Visite os Templos de Karnak e Luxor. Embarque no seu Cruzeiro pelo Nilo.',
    'Flight to Luxor. Board cruise. Karnak Temple.': 'Voo para Luxor. Embarque no cruzeiro. Templo de Karnak.',
    'Flight to Luxor. Board your luxury Nile cruise. Visit Luxor Temple.': 'Voo para Luxor. Embarque no seu cruzeiro de luxo pelo Nilo. Visite o Templo de Luxor.',
    'Explore the Valley of the Kings, Hatshepsut Temple, and the Colossi of Memnon.': 'Explore o Vale dos Reis, o Templo de Hatshepsut e os Colossos de Mêmnon.',
    'Visit Valley of the Kings, Hatshepsut Temple, and Colossi of Memnon. Sail towards Edfu.': 'Visite o Vale dos Reis, o Templo de Hatshepsut e os Colossos de Mêmnon. Navegue em direção a Edfu.',
    'Valley of the Kings, Hatshepsut Temple, Colossi of Memnon.': 'Vale dos Reis, Templo de Hatshepsut, Colossos de Mêmnon.',
    'Valley of the Kings, Karnak Temple.': 'Vale dos Reis, Templo de Karnak.',
    'Valley of the Kings, Hatshepsut Temple.': 'Vale dos Reis, Templo de Hatshepsut.',
    'Private transfer to Hurghada. Afternoon free for beach relaxation.': 'Transfer privado para Hurghada. Tarde livre para relaxar na praia.',
    'Scenic drive to Hurghada. Check in to beach resort.': 'Viagem panorâmica para Hurghada. Check-in no resort de praia.',
    'Full day at leisure. Optional activities: snorkeling, diving, or desert safari.': 'Dia inteiro livre. Atividades opcionais: snorkeling, mergulho ou safari no deserto.',
    'Another day to enjoy Hurghada\'s beaches and water activities.': 'Outro dia para aproveitar as praias e atividades aquáticas de Hurghada.',
    'Continue enjoying your Red Sea paradise.': 'Continue aproveitando seu paraíso no Mar Vermelho.',
    'Free day for beach and water activities.': 'Dia livre para praia e atividades aquáticas.',
    'Another day of Red Sea relaxation.': 'Outro dia de relaxamento no Mar Vermelho.',
    'Transfer back to Cairo. Free time for last-minute shopping at Khan El Khalili.': 'Retorno ao Cairo. Tempo livre para compras de última hora no Khan El Khalili.',
    'Fly back to Cairo. Free afternoon.': 'Voo de volta ao Cairo. Tarde livre.',
    'Fly back to Cairo. Free afternoon for shopping.': 'Voo de volta ao Cairo. Tarde livre para compras.',
    'Transfer to Cairo International Airport for your departure flight.': 'Transfer para o Aeroporto Internacional do Cairo para seu voo de partida.',
    'Transfer to airport for your departure flight.': 'Transfer para o aeroporto para seu voo de partida.',
    'Transfer to Sharm El Sheikh Airport for your departure flight.': 'Transfer para o Aeroporto de Sharm El Sheikh para seu voo de partida.',
    'Transfer to Amman Airport for departure.': 'Transfer para o Aeroporto de Amã para partida.',
    'Transfer to Marrakech airport.': 'Transfer para o aeroporto de Marrakech.',
    'Transfer to Hurghada or Cairo airport.': 'Transfer para o aeroporto de Hurghada ou Cairo.',
    'Transfer to airport.': 'Transfer para o aeroporto.',
    'Day trip to Alexandria visiting Catacombs, Pompey\'s Pillar, and the new Bibliotheca Alexandrina.': 'Excursão a Alexandria visitando as Catacumbas, o Pilar de Pompeu e a nova Biblioteca de Alexandria.',
    'Full day in the Mediterranean city of Alexander the Great.': 'Dia inteiro na cidade mediterrânea de Alexandre, o Grande.',
    'Visit the magnificent Temple of Horus at Edfu. Continue sailing to Kom Ombo.': 'Visite o magnífico Templo de Hórus em Edfu. Continue navegando para Kom Ombo.',
    'Visit Temple of Horus at Edfu. Continue sailing south.': 'Visite o Templo de Hórus em Edfu. Continue navegando para o sul.',
    'Visit Kom Ombo Temple dedicated to Sobek and Horus. Sail to Aswan.': 'Visite o Templo de Kom Ombo dedicado a Sobek e Hórus. Navegue para Aswan.',
    'Morning visit to Kom Ombo. Arrive in Aswan, visit Philae Temple.': 'Visita matinal a Kom Ombo. Chegada em Aswan, visite o Templo de Philae.',
    'Kom Ombo Temple. Arrive Aswan. Felucca ride at sunset.': 'Templo de Kom Ombo. Chegada em Aswan. Passeio de feluca ao pôr do sol.',
    'Visit Aswan High Dam, Unfinished Obelisk, and the beautiful Philae Temple.': 'Visite a Barragem Alta de Aswan, o Obelisco Inacabado e o belo Templo de Philae.',
    'High Dam, Unfinished Obelisk. Optional felucca ride around Elephantine Island.': 'Barragem Alta, Obelisco Inacabado. Passeio opcional de feluca ao redor da Ilha Elefantina.',
    'High Dam, Philae Temple, Unfinished Obelisk.': 'Barragem Alta, Templo de Philae, Obelisco Inacabado.',
    'Disembark cruise. Flight to Cairo. Afternoon free for shopping.': 'Desembarque do cruzeiro. Voo para Cairo. Tarde livre para compras.',
    'Morning at the Egyptian Museum. Afternoon visit Coptic Cairo and Islamic Cairo.': 'Manhã no Museu Egípcio. Tarde visitando o Cairo Copta e o Cairo Islâmico.',
    'Egyptian Museum, Old Cairo, Khan El Khalili bazaar.': 'Museu Egípcio, Cairo Antigo, bazar Khan El Khalili.',
    'Day trip to Alexandria. Visit the Library, Catacombs, and Mediterranean waterfront.': 'Excursão a Alexandria. Visite a Biblioteca, as Catacumbas e a orla do Mediterrâneo.',
    'Full day excursion to Abydos Temple and Dendera\'s Temple of Hathor.': 'Excursão de dia inteiro ao Templo de Abydos e ao Templo de Hathor em Dendera.',
    'Morning flight to Sharm El Sheikh. Check in to your beach resort. Afternoon at leisure.': 'Voo matinal para Sharm El Sheikh. Check-in no seu resort de praia. Tarde livre.',
    'Free day to enjoy the beach, pool, or optional excursions.': 'Dia livre para aproveitar a praia, piscina ou excursões opcionais.',
    'Another day of relaxation. Optional snorkeling at Ras Mohammed or diving trip.': 'Outro dia de relaxamento. Snorkeling opcional em Ras Mohammed ou excursão de mergulho.',
    'Last full day in paradise. Optional desert safari or glass-bottom boat trip.': 'Último dia inteiro no paraíso. Safari no deserto opcional ou passeio de barco com fundo de vidro.',
    'Free day at Red Sea resort. Relax or optional snorkeling.': 'Dia livre no resort do Mar Vermelho. Relaxe ou snorkeling opcional.',
    'Visit Coptic Churches, Hanging Church, and Ben Ezra Synagogue. Transfer to Sinai.': 'Visite as Igrejas Coptas, a Igreja Suspensa e a Sinagoga Ben Ezra. Transfer para o Sinai.',
    'Pre-dawn climb to Mount Sinai for sunrise. Visit St. Catherine\'s Monastery.': 'Subida antes do amanhecer ao Monte Sinai para o nascer do sol. Visite o Mosteiro de Santa Catarina.',
    'Ferry to Aqaba, Jordan. Transfer to Petra.': 'Ferry para Aqaba, Jordânia. Transfer para Petra.',
    'Explore the ancient rose-red city of Petra, one of the New Seven Wonders.': 'Explore a antiga cidade rosa de Petra, uma das Novas Sete Maravilhas.',
    'Morning in Wadi Rum desert. Jeep safari through the stunning landscape.': 'Manhã no deserto de Wadi Rum. Safari de jipe pela paisagem deslumbrante.',
    'Visit Mount Nebo where Moses saw the Promised Land. Continue to Amman.': 'Visite o Monte Nebo onde Moisés viu a Terra Prometida. Continue para Amã.',
    'Sail from Aswan towards Luxor with temple visits.': 'Navegue de Aswan em direção a Luxor com visitas a templos.',
    'International flight to Morocco.': 'Voo internacional para o Marrocos.',
    'Hassan II Mosque. Drive to Rabat.': 'Mesquita Hassan II. Viagem para Rabat.',
    'Drive to Fes. Explore the ancient medina.': 'Viagem para Fez. Explore a antiga medina.',
    'Full day in Fes - tanneries, madrasas, souks.': 'Dia inteiro em Fez - curtumes, madraças, souks.',
    'Journey to Merzouga. Camel trek into the Sahara.': 'Viagem para Merzouga. Trek de camelo pelo Saara.',
    'Drive through the dramatic Dades Gorges.': 'Dirija através das dramáticas Gargantas do Dades.',
    'Arrive in Marrakech. Evening in Djemaa el-Fna square.': 'Chegada em Marrakech. Noite na praça Djemaa el-Fna.',
    'Full day exploring Marrakech - palaces, gardens, souks.': 'Dia inteiro explorando Marrakech - palácios, jardins, souks.',
}


def fill_blog_translations():
    """Fill empty translation fields for blog posts."""
    print("\n=== Filling Blog Post Translations ===\n")

    updated_count = 0

    # Get posts that need translations
    posts = Post.objects.filter(
        title__in=list(ES_TRANSLATIONS.keys())
    )

    for post in posts:
        updated = False

        # Title translations
        if not post.title_es and post.title in ES_TRANSLATIONS:
            post.title_es = ES_TRANSLATIONS[post.title]
            updated = True
        if not post.title_pt and post.title in PT_TRANSLATIONS:
            post.title_pt = PT_TRANSLATIONS[post.title]
            updated = True

        # Excerpt translations
        if not post.excerpt_es and post.title in EXCERPT_TRANSLATIONS_ES:
            post.excerpt_es = EXCERPT_TRANSLATIONS_ES[post.title]
            updated = True
        if not post.excerpt_pt and post.title in EXCERPT_TRANSLATIONS_PT:
            post.excerpt_pt = EXCERPT_TRANSLATIONS_PT[post.title]
            updated = True

        if updated:
            post.save()
            updated_count += 1
            print(f"  Updated: {post.title}")

    print(f"\nTotal blog posts updated: {updated_count}")
    return updated_count


def fill_tour_translations():
    """Fill empty translation fields for tours."""
    print("\n=== Filling Tour Translations ===\n")

    updated_count = 0

    # Get tours that need translations
    tours = Tour.objects.filter(
        name__in=list(ES_TRANSLATIONS.keys())
    )

    for tour in tours:
        updated = False

        # Name translations
        if not tour.name_es and tour.name in ES_TRANSLATIONS:
            tour.name_es = ES_TRANSLATIONS[tour.name]
            updated = True
        if not tour.name_pt and tour.name in PT_TRANSLATIONS:
            tour.name_pt = PT_TRANSLATIONS[tour.name]
            updated = True

        # Short description translations
        if not tour.short_description_es and tour.name in TOUR_SHORT_DESC_ES:
            tour.short_description_es = TOUR_SHORT_DESC_ES[tour.name]
            updated = True
        if not tour.short_description_pt and tour.name in TOUR_SHORT_DESC_PT:
            tour.short_description_pt = TOUR_SHORT_DESC_PT[tour.name]
            updated = True

        if updated:
            tour.save()
            updated_count += 1
            print(f"  Updated tour: {tour.name}")

        # Update itinerary
        for item in tour.itinerary.all():
            item_updated = False

            if not item.title_es and item.title in ITINERARY_ES:
                item.title_es = ITINERARY_ES[item.title]
                item_updated = True
            if not item.title_pt and item.title in ITINERARY_PT:
                item.title_pt = ITINERARY_PT[item.title]
                item_updated = True

            if not item.description_es and item.description in ITINERARY_DESC_ES:
                item.description_es = ITINERARY_DESC_ES[item.description]
                item_updated = True
            if not item.description_pt and item.description in ITINERARY_DESC_PT:
                item.description_pt = ITINERARY_DESC_PT[item.description]
                item_updated = True

            if item_updated:
                item.save()
                print(f"    - Updated itinerary day {item.day_number}")

        # Update inclusions
        for inclusion in tour.inclusions.all():
            inc_updated = False

            if not inclusion.item_es and inclusion.item in ES_TRANSLATIONS:
                inclusion.item_es = ES_TRANSLATIONS[inclusion.item]
                inc_updated = True
            if not inclusion.item_pt and inclusion.item in PT_TRANSLATIONS:
                inclusion.item_pt = PT_TRANSLATIONS[inclusion.item]
                inc_updated = True

            if inc_updated:
                inclusion.save()

        # Update highlights
        for highlight in tour.highlights.all():
            hl_updated = False

            if not highlight.title_es:
                # Simple translation for highlights
                title_es = highlight.title
                for en, es in ES_TRANSLATIONS.items():
                    title_es = title_es.replace(en, es)
                if title_es != highlight.title:
                    highlight.title_es = title_es
                    hl_updated = True

            if not highlight.title_pt:
                title_pt = highlight.title
                for en, pt in PT_TRANSLATIONS.items():
                    title_pt = title_pt.replace(en, pt)
                if title_pt != highlight.title:
                    highlight.title_pt = title_pt
                    hl_updated = True

            if hl_updated:
                highlight.save()

    print(f"\nTotal tours updated: {updated_count}")
    return updated_count


def fill_category_translations():
    """Fill translations for categories."""
    print("\n=== Filling Category Translations ===\n")

    updated_count = 0

    # Blog categories
    for cat in Category.objects.all():
        updated = False
        if not cat.name_es and cat.name in ES_TRANSLATIONS:
            cat.name_es = ES_TRANSLATIONS[cat.name]
            updated = True
        if not cat.name_pt and cat.name in PT_TRANSLATIONS:
            cat.name_pt = PT_TRANSLATIONS[cat.name]
            updated = True
        if updated:
            cat.save()
            updated_count += 1
            print(f"  Updated blog category: {cat.name}")

    # Tour categories
    for cat in TourCategory.objects.all():
        updated = False
        if not cat.name_es and cat.name in ES_TRANSLATIONS:
            cat.name_es = ES_TRANSLATIONS[cat.name]
            updated = True
        if not cat.name_pt and cat.name in PT_TRANSLATIONS:
            cat.name_pt = PT_TRANSLATIONS[cat.name]
            updated = True
        if updated:
            cat.save()
            updated_count += 1
            print(f"  Updated tour category: {cat.name}")

    # Tour types
    for tt in TourType.objects.all():
        updated = False
        if not tt.name_es and tt.name in ES_TRANSLATIONS:
            tt.name_es = ES_TRANSLATIONS[tt.name]
            updated = True
        if not tt.name_pt and tt.name in PT_TRANSLATIONS:
            tt.name_pt = PT_TRANSLATIONS[tt.name]
            updated = True
        if updated:
            tt.save()
            updated_count += 1
            print(f"  Updated tour type: {tt.name}")

    print(f"\nTotal categories updated: {updated_count}")
    return updated_count


if __name__ == '__main__':
    print("=" * 60)
    print("Filling Translation Fields")
    print("=" * 60)

    cats = fill_category_translations()
    posts = fill_blog_translations()
    tours = fill_tour_translations()

    print("\n" + "=" * 60)
    print(f"Summary: Updated {cats} categories, {posts} posts, {tours} tours")
    print("=" * 60)
