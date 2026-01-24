"""
Script to add Spanish translations for the 10 new tours.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import Tour, TourItinerary

TRANSLATIONS = {
    'Magic of the White Desert with Cairo and Alexandria': {
        'name_es': 'Encanto del Desierto Blanco con El Cairo y Alejandria',
        'short_description_es': '9 dias de aventura e historia en Egipto. Descubre El Cairo, Alejandria y la magia surrealista de los oasis y desiertos del Oeste egipcio.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al Aeropuerto Internacional de El Cairo. Recepcion y asistencia por nuestro representante local para los tramites del visado. Traslado al hotel seleccionado. Check-in y resto del dia libre para descansar del viaje.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Guiza - Museo Egipcio', 'description': 'Desayuno en el hotel. Visita a la meseta de Guiza para admirar las Grandes Piramides de Keops, Kefren y Micerinos. Visita al Templo del Valle y a la Gran Esfinge. Almuerzo en restaurante local. Por la tarde, visita al Museo Egipcio de El Cairo en Tahrir. Regreso al hotel.'},
            {'day': 3, 'title': 'El Cairo - Oasis de Bahariya', 'description': 'Desayuno y check-out. Salida hacia el Oasis de Bahariya (aprox. 4 horas). Llegada y almuerzo. Por la tarde, visita al Desierto Negro y a la Montana de Cristal. Cena y pernocte en campamento.'},
            {'day': 4, 'title': 'Desierto Blanco - Oasis de Farafra', 'description': 'Desayuno. Exploracion del Desierto Blanco con sus formaciones rocosas surrealistas. Almuerzo picnic. Visita al Oasis El Heiz. Cena bajo las estrellas y pernocte en campamento de lujo en el Desierto Blanco.'},
            {'day': 5, 'title': 'Desierto Blanco - Oasis de Bahariya - El Cairo', 'description': 'Amanecer en el Desierto Blanco. Desayuno. Retorno al Oasis de Bahariya y continuacion hacia El Cairo. Llegada y check-in en el hotel. Resto del dia libre.'},
            {'day': 6, 'title': 'El Cairo - Alejandria - El Cairo', 'description': 'Desayuno. Excursion de dia completo a Alejandria. Visita al Museo Nacional, Biblioteca de Alejandria, Ciudadela de Qaitbay y Puente Stanley. Almuerzo en restaurante local. Regreso a El Cairo.'},
            {'day': 7, 'title': 'El Cairo - Menfis y Saqqara', 'description': 'Desayuno. Visita a Menfis, la primera capital del Egipto Unificado. Continuacion a Saqqara para ver la Piramide Escalonada del Faraon Djoser. Almuerzo en restaurante local. Regreso al hotel.'},
            {'day': 8, 'title': 'El Cairo - Dia Libre', 'description': 'Desayuno. Dia libre en El Cairo para actividades independientes, compras o descanso. Opcional: Tour por el Cairo Cristiano e Islamico.'},
            {'day': 9, 'title': 'El Cairo - Partida', 'description': 'Desayuno en el hotel. A la hora programada, traslado al aeropuerto internacional de El Cairo para embarcar en su vuelo de regreso. Fin de nuestros servicios.'},
        ]
    },
    'Best of Millennial Egypt with Abu Simbel and Dendera': {
        'name_es': 'Lo Mejor del Egipto Milenario con Abu Simbel y Dendera',
        'short_description_es': '10 dias de inmersion en Egipto con 2 vuelos domesticos incluidos. Combina alojamiento en El Cairo y un crucero por el Nilo para explorar los tesoros de Giza, Luxor, Dendera, Edfu, Kom Ombo, Asuan y el majestuoso Abu Simbel.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al aeropuerto de El Cairo. Recepcion y asistencia en los tramites de entrada. Traslado al hotel. Check-in.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Giza - Museo Egipcio', 'description': 'Desayuno. Visita al Complejo de Giza para ver las Grandes Piramides, el Templo del Valle y la Esfinge. Almuerzo en restaurante local. Por la tarde, visita al Museo Egipcio de El Cairo.'},
            {'day': 3, 'title': 'El Cairo - Cairo Copto e Islamico', 'description': 'Desayuno. Visita al Barrio Copto Cristiano con la Iglesia Colgante y la Iglesia de San Sergio. Almuerzo. Visita a la Ciudadela de Saladino y la Mezquita de Mohamed Ali.'},
            {'day': 4, 'title': 'El Cairo - Dia Libre', 'description': 'Desayuno. Dia libre en El Cairo. Opcional: Visita a Saqqara y Menfis o al Gran Museo Egipcio (GEM).'},
            {'day': 5, 'title': 'El Cairo - Luxor - Dendera - Crucero', 'description': 'Desayuno. Vuelo domestico a Luxor. Visita al Templo de Dendera. Traslado al crucero. Almuerzo a bordo. Visita a los Templos de Karnak y Luxor. Cena a bordo.'},
            {'day': 6, 'title': 'Orilla Oeste de Luxor - Navegacion a Edfu', 'description': 'Desayuno. Visita al Valle de los Reyes, Templo de Hatshepsut y Colosos de Memnon. Almuerzo a bordo. Navegacion pasando por la Esclusa de Esna hacia Edfu.'},
            {'day': 7, 'title': 'Edfu - Kom Ombo - Asuan', 'description': 'Desayuno. Visita al Templo de Horus en Edfu. Navegacion a Kom Ombo. Almuerzo a bordo. Visita al Templo de Kom Ombo. Navegacion a Asuan.'},
            {'day': 8, 'title': 'Asuan - Isla de File - Presa Alta', 'description': 'Desayuno. Visita a la Gran Presa de Asuan y al Templo de Isis en la isla de File. Almuerzo a bordo. Paseo en Faluca por el Nilo.'},
            {'day': 9, 'title': 'Asuan - Abu Simbel - El Cairo', 'description': 'Desayuno. Check-out del crucero. Excursion a Abu Simbel para visitar los templos de Ramses II y Nefertari. Vuelo domestico de regreso a El Cairo. Traslado al hotel.'},
            {'day': 10, 'title': 'El Cairo - Partida', 'description': 'Desayuno. Check-out del hotel y traslado al Aeropuerto Internacional de El Cairo para su vuelo de regreso. Fin de nuestros servicios.'},
        ]
    },
    'Classic Egypt with Nile Cruise': {
        'name_es': 'Viaje Egipto Clasico con Crucero por el Nilo',
        'short_description_es': 'Itinerario terrestre completo de 10 dias y 9 noches, ideal para explorar las maravillas del Antiguo Egipto con total comodidad. Incluye dos vuelos domesticos, alojamiento seleccionado en El Cairo y un encantador crucero por el Rio Nilo.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al aeropuerto internacional de El Cairo. Recepcion y asistencia en los tramites de visado. Traslado al hotel en El Cairo. Check-in.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Guiza y Esfinge - Museo Egipcio', 'description': 'Desayuno en el hotel. Visita a la meseta de Guiza para ver las tres Grandes Piramides, el Templo del Valle y la Gran Esfinge. Visita a un Instituto de Papiro. Almuerzo en restaurante local. Visita al Museo Egipcio en la Plaza Tahrir.'},
            {'day': 3, 'title': 'El Cairo Cristiano e Islamico', 'description': 'Desayuno. Visita a las iglesias del Barrio Copto, incluyendo la Iglesia Colgante y la Iglesia de San Sergio. Almuerzo. Visita a la Ciudadela de Saladino y la Mezquita de Mohamed Ali.'},
            {'day': 4, 'title': 'El Cairo - Dia Libre', 'description': 'Desayuno. Dia libre en El Cairo para explorar por su cuenta. Opcional: Excursion a Menfis y Saqqara con Almuerzo.'},
            {'day': 5, 'title': 'El Cairo - Luxor - Crucero', 'description': 'Desayuno y check-out. Vuelo domestico a Luxor. Check-in en el Crucero 5 estrellas. Almuerzo a bordo. Visita al complejo de templos de Karnak y al Templo de Luxor. Cena a bordo.'},
            {'day': 6, 'title': 'Orilla Oeste de Luxor - Navegacion a Edfu', 'description': 'Desayuno a bordo. Visita al Valle de los Reyes, los Colosos de Memnon y el Templo de la Reina Hatshepsut. Almuerzo a bordo. Navegacion hacia Edfu, pasando por la Esclusa de Esna.'},
            {'day': 7, 'title': 'Edfu - Kom Ombo - Asuan', 'description': 'Desayuno a bordo. Visita al Templo de Horus en Edfu. Navegacion a Kom Ombo. Almuerzo a bordo. Visita al Templo de Kom Ombo. Navegacion a Asuan.'},
            {'day': 8, 'title': 'Asuan - Templo de Filae - Paseo en Faluca', 'description': 'Desayuno a bordo. Visita al Templo de Isis en la Isla de File. Almuerzo a bordo. Paseo en faluca por el Nilo alrededor de las islas de Asuan.'},
            {'day': 9, 'title': 'Asuan - El Cairo', 'description': 'Desayuno y check-out del crucero. Vuelo domestico a El Cairo. Traslado al hotel. Tiempo libre. Opcional: Excursion a Abu Simbel.'},
            {'day': 10, 'title': 'El Cairo - Partida', 'description': 'Desayuno y check-out del hotel. Traslado al aeropuerto internacional de El Cairo para su vuelo de salida. Fin de nuestros servicios.'},
        ]
    },
    'Cultural Cairo and Marsa Alam on the Red Sea': {
        'name_es': 'Cairo Cultural y Marsa Alam en el Mar Rojo',
        'short_description_es': '8 dias que combinan la fascinante historia milenaria de los faraones con la relajacion absoluta en una de las costas mas preservadas del Mar Rojo.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al Aeropuerto Internacional de El Cairo. Asistencia personalizada en los tramites de inmigracion y obtencion del visado turistico. Traslado privado al hotel seleccionado. Check-in y resto del dia libre.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Guiza - Museo Egipcio', 'description': 'Desayuno. Visita a la Meseta de Guiza con las Grandes Piramides y la Esfinge. Almuerzo en restaurante local. Por la tarde, visita al Museo Egipcio de El Cairo. Regreso al hotel para la cena.'},
            {'day': 3, 'title': 'El Cairo - Marsa Alam', 'description': 'Desayuno y check-out. Traslado al aeropuerto para el vuelo domestico a Marsa Alam. Llegada, traslado al resort 4 estrellas y check-in en regimen Soft Todo Incluido. Tiempo libre para disfrutar del Mar Rojo.'},
            {'day': 4, 'title': 'Marsa Alam - Dia Libre', 'description': 'Desayuno en el resort. Dia completo libre para relajarse. Disfrute de las piscinas, la playa de arena dorada y las aguas transparentes, perfectas para hacer snorkel.'},
            {'day': 5, 'title': 'Marsa Alam - Dia Libre', 'description': 'Desayuno en el resort. Segundo dia libre para actividades de ocio. Opcionalmente puede explorar los vibrantes arrecifes de coral en un paseo en barco.'},
            {'day': 6, 'title': 'Marsa Alam - Dia Libre', 'description': 'Desayuno en el resort. Tercer dia libre para disfrutar de este refugio del Mar Rojo. Oportunidad ideal para actividades opcionales como buceo o safari por el desierto.'},
            {'day': 7, 'title': 'Marsa Alam - El Cairo', 'description': 'Desayuno. Tiempo libre hasta el traslado al aeropuerto de Marsa Alam para el vuelo domestico de regreso a El Cairo. Check-in en el hotel. Cena incluida.'},
            {'day': 8, 'title': 'El Cairo - Partida', 'description': 'Desayuno. Check-out. Traslado privado al Aeropuerto Internacional de El Cairo para su vuelo internacional de regreso. Fin de nuestros servicios.'},
        ]
    },
    'Egypt in 8 Days: Cairo, Alexandria and Sharm El Sheikh': {
        'name_es': 'Egipto en 8 Dias: El Cairo, Alejandria y Sharm El Sheikh',
        'short_description_es': 'Viaje esencial que reune los destinos mas iconicos de Egipto en 8 dias. Vive la grandiosidad de El Cairo, viaja por la historia hasta Alejandria, experimenta el Monte Sinai y relajate en Sharm El Sheikh.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al Aeropuerto Internacional de El Cairo. Recepcion personalizada por nuestro representante para asistir en los tramites de entrada. Traslado privado al hotel y check-in.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Guiza - Museo Egipcio', 'description': 'Desayuno. Visita a la Meseta de Guiza para admirar las tres Grandes Piramides y la majestuosa Esfinge. Visita a una galeria de papiros. Almuerzo en restaurante local. Por la tarde, exploracion del Museo Egipcio de El Cairo.'},
            {'day': 3, 'title': 'El Cairo - Monte Sinai (Santa Catalina)', 'description': 'Desayuno y check-out. Viaje por carretera hacia la region del Monte Sinai. Paso por el Tunel Ahmed Hamdi y parada en las Fuentes de Moises. Llegada a la Reserva de Santa Catalina. Check-in y cena incluida.'},
            {'day': 4, 'title': 'Santa Catalina - Sharm El Sheikh', 'description': 'Desayuno y check-out. Traslado al aeropuerto para el vuelo domestico a Sharm El Sheikh. Llegada, recepcion y traslado al resort 4 estrellas Superior. Check-in en regimen Soft Todo Incluido.'},
            {'day': 5, 'title': 'Sharm El Sheikh - Dia Libre', 'description': 'Desayuno. Dia completamente libre para relajarse en el resort, disfrutar de la playa o realizar actividades opcionales como buceo o snorkel.'},
            {'day': 6, 'title': 'Sharm El Sheikh - El Cairo', 'description': 'Desayuno. Check-out y traslado al aeropuerto de Sharm El Sheikh para el vuelo domestico de regreso a El Cairo. Traslado al hotel. Resto del dia libre.'},
            {'day': 7, 'title': 'El Cairo - Alejandria - El Cairo', 'description': 'Desayuno. Excursion de dia completo a Alejandria. Visita al Teatro Romano, Museo Nacional y Biblioteca de Alejandria. Almuerzo en restaurante local. Paseo por la Ciudadela de Qaitbay y el Puente Stanley. Regreso a El Cairo.'},
            {'day': 8, 'title': 'El Cairo - Partida', 'description': 'Desayuno y check-out. Traslado privado al Aeropuerto Internacional de El Cairo para su vuelo internacional de regreso. Fin de nuestros servicios.'},
        ]
    },
    'Incredible Egypt Package: Cairo, Luxor and Hurghada': {
        'name_es': 'Paquete Egipto Increible: El Cairo, Luxor y Hurghada',
        'short_description_es': '9 dias de viaje por Egipto con excursiones en El Cairo (piramides), Luxor (templos faraonicos) y estancia en un resort a orillas del mar en Hurghada. Historia, cultura y relajacion en un solo viaje.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al aeropuerto de El Cairo. Recepcion por nuestro representante para facilitar los tramites de entrada. Traslado al hotel en El Cairo.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Giza - Museo Egipcio', 'description': 'Desayuno. Visita al Complejo de Giza para ver las tres grandes piramides, el Templo del Valle y la Esfinge. Visita a una galeria de papiro. Almuerzo en restaurante local. Visita al Museo Egipcio de El Cairo en la Plaza de Tahrir.'},
            {'day': 3, 'title': 'El Cairo - Luxor', 'description': 'Desayuno. Vuelo domestico a Luxor. Visita al Valle de los Reyes, los Colosos de Memnon y el Templo de Hatshepsut. Check-in en el hotel. Por la tarde, visita a los Templos de Karnak y Luxor. Cena en el hotel.'},
            {'day': 4, 'title': 'Luxor - Hurghada', 'description': 'Desayuno y check-out. Traslado por carretera a Hurghada, capital de la provincia del Mar Rojo. Check-in en el hotel con regimen Todo Incluido. Resto del dia libre.'},
            {'day': 5, 'title': 'Hurghada - Dia Libre', 'description': 'Desayuno. Dia libre para actividades personales en el resort, disfrutar del mar o relajarse en la playa de Hurghada, conocida como paraiso del buceo.'},
            {'day': 6, 'title': 'Hurghada - Dia Libre', 'description': 'Desayuno. Segundo dia libre para disfrutar del resort y las playas del Mar Rojo. Posibilidad de actividades opcionales como buceo o excursiones.'},
            {'day': 7, 'title': 'Hurghada - El Cairo', 'description': 'Desayuno y check-out. Traslado al aeropuerto para el vuelo domestico a El Cairo. Recepcion y traslado al hotel.'},
            {'day': 8, 'title': 'El Cairo - Dia Libre', 'description': 'Desayuno. Dia libre en El Cairo. Opcional: Paseo a Saqqara con visita al complejo del rey Zoser y las iglesias del Barrio Copto.'},
            {'day': 9, 'title': 'El Cairo - Partida', 'description': 'Desayuno y check-out. Traslado al aeropuerto de El Cairo para el vuelo internacional de regreso. Fin de nuestros servicios.'},
        ]
    },
    'Best of Egypt with Dubai and Abu Dhabi': {
        'name_es': 'Lo Mejor de Egipto con Dubai y Abu Dabi',
        'short_description_es': '14 dias por las maravillas historicas de Egipto y la modernidad de los Emiratos. Crucero 5 estrellas por el Nilo, piramides, templos y las ciudades futuristas de Dubai y Abu Dabi.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al Aeropuerto Internacional de El Cairo. Recepcion por nuestro representante para asistencia con los tramites del visado e inmigracion. Traslado al hotel seleccionado. Check-in y resto del dia libre.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Guiza - Museo Egipcio', 'description': 'Desayuno. Visita a la Meseta de Guiza con las Grandes Piramides y la Esfinge. Parada en una galeria de papiro. Almuerzo en restaurante local. Por la tarde, visita al Museo Egipcio de El Cairo.'},
            {'day': 3, 'title': 'El Cairo - Luxor - Embarque en el Crucero', 'description': 'Desayuno y check-out. Vuelo domestico a Luxor. Visita al Templo de Karnak. Traslado al Crucero 5 estrellas. Al atardecer, visita al Templo de Luxor. Cena a bordo.'},
            {'day': 4, 'title': 'Luxor (Margen Occidental) - Navegacion a Edfu', 'description': 'Desayuno a bordo. Visita al Valle de los Reyes, los Colosos de Memnon y el Templo de Hatshepsut. Almuerzo a bordo. Navegacion pasando por la Esclusa de Esna hacia Edfu.'},
            {'day': 5, 'title': 'Edfu - Kom Ombo - Navegacion a Asuan', 'description': 'Desayuno a bordo. Visita al Templo de Horus en Edfu. Navegacion a Kom Ombo. Almuerzo a bordo. Visita al Templo de Kom Ombo. Navegacion hacia Asuan.'},
            {'day': 6, 'title': 'Asuan - Presa Alta - Templo de Filae', 'description': 'Desayuno a bordo. Visita a la Gran Presa de Asuan y al Templo de Filae en la isla. Almuerzo a bordo. Paseo en Feluca por el Nilo.'},
            {'day': 7, 'title': 'Asuan - El Cairo', 'description': 'Desayuno a bordo y check-out. Vuelo domestico de regreso a El Cairo. Traslado al hotel. Opcional: Excursion diurna a Abu Simbel.'},
            {'day': 8, 'title': 'El Cairo - Menfis y Saqqara', 'description': 'Desayuno. Visita al sitio al aire libre de Menfis y a Saqqara para ver la Piramide Escalonada del Faraon Djoser. Almuerzo en restaurante local. Parada en una escuela de alfombras artesanales.'},
            {'day': 9, 'title': 'El Cairo Copto, Islamico y Museo NMEC', 'description': 'Desayuno. Visita al Barrio Copto con la Iglesia Colgante. Continuacion al Cairo Islamico con la Ciudadela de Saladino y la Mezquita de Mohamed Ali. Almuerzo. Visita al Museo Nacional de la Civilizacion Egipcia.'},
            {'day': 10, 'title': 'El Cairo - Dubai', 'description': 'Check-out y traslado al aeropuerto de El Cairo para su vuelo a Dubai. Llegada, recepcion y traslado al hotel. Por la tarde, city tour con subida al Burj Khalifa y visita al Dubai Frame.'},
            {'day': 11, 'title': 'Dubai - Abu Dabi', 'description': 'Desayuno. Excursion de dia completo a Abu Dabi. Visita a la Gran Mezquita Sheikh Zayed, Heritage Village y Qasr Al Watan. Almuerzo en restaurante local. Regreso a Dubai.'},
            {'day': 12, 'title': 'Dubai - Dia Libre', 'description': 'Dia enteramente libre en Dubai para actividades independientes, compras o descanso.'},
            {'day': 13, 'title': 'Dubai - City Tour y Safari en el Desierto', 'description': 'Desayuno. Por la manana, city tour por los Zocos de Oro y Especias, con paseo en abra y por la zona de Jumeirah. Por la tarde, Safari en el Desierto en 4x4 con cena tipica y espectaculo.'},
            {'day': 14, 'title': 'Dubai - Partida', 'description': 'Desayuno y check-out. Traslado al Aeropuerto Internacional de Dubai para su vuelo de regreso. Fin de nuestros servicios.'},
        ]
    },
    'The Best of Luxor and Aswan': {
        'name_es': 'Lo Mejor de Luxor y Asuan',
        'short_description_es': '5 dias para descubrir lo mejor del Sur de Egipto. Alojamiento en hoteles en lugar de crucero, con visitas a Luxor, Edfu, Kom Ombo y Asuan con mas libertad y comodidad.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a Luxor - Luxor Oeste y Este', 'description': 'Llegada a Luxor. Visita al Valle de los Reyes, Colosos de Memnon y Templo de Hatshepsut. Por la tarde, visita al Templo de Luxor. Check-in en el hotel. Cena.'},
            {'day': 2, 'title': 'Luxor - Templo de Karnak', 'description': 'Desayuno. Visita al grandioso Templo de Karnak, el mayor complejo religioso del mundo antiguo. Tarde libre. Cena en el hotel.'},
            {'day': 3, 'title': 'Luxor - Edfu - Kom Ombo - Asuan', 'description': 'Desayuno y check-out. Viaje hacia Asuan con paradas para visitar el Templo de Horus en Edfu y el Templo de Kom Ombo. Check-in en el hotel de Asuan. Cena.'},
            {'day': 4, 'title': 'Asuan - Isla de File - Presa - Faluca', 'description': 'Desayuno. Visita al Templo de Isis en la Isla de File y a la Gran Presa de Asuan. Por la tarde, paseo en Faluca por el Nilo y visita al Jardin Botanico. Cena en el hotel.'},
            {'day': 5, 'title': 'Asuan - Partida', 'description': 'Desayuno y check-out. Traslado al aeropuerto de Asuan para su vuelo de salida. Fin de nuestros servicios. Opcional: Excursion a Abu Simbel por la manana.'},
        ]
    },
    'The Path of Moses': {
        'name_es': 'El Camino de Moises',
        'short_description_es': '7 dias de viaje transformador que te invita a vivir una experiencia de fe e historia, siguiendo los pasos de Moises en Egipto. Lugares sagrados del Cristianismo, Monte Sinai y descanso en Sharm El Sheikh.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al Aeropuerto de El Cairo. Recepcion por nuestro representante para facilitar los tramites de entrada. Traslado al hotel y check-in. Resto del dia libre para descansar.'},
            {'day': 2, 'title': 'El Cairo - Piramides de Guiza - Barrio Copto', 'description': 'Desayuno. Visita a las Piramides de Guiza, el Templo del Valle y la Esfinge. Almuerzo. Por la tarde, visita al Barrio Copto con la Iglesia Colgante, la Iglesia de San Sergio y la Gruta de la Sagrada Familia.'},
            {'day': 3, 'title': 'El Cairo - Monte Sinai (Santa Catalina)', 'description': 'Desayuno y check-out. Viaje por carretera hacia la region del Monte Sinai. Parada en las Fuentes de Moises. Llegada a la Reserva de Santa Catalina. Check-in y cena incluida.'},
            {'day': 4, 'title': 'Monte Sinai - Sharm El Sheikh', 'description': 'Opcional: Ascenso al Monte Sinai para ver el amanecer. Desayuno y check-out. Traslado a Sharm El Sheikh. Check-in en el resort con regimen Soft Todo Incluido.'},
            {'day': 5, 'title': 'Sharm El Sheikh - Dia Libre', 'description': 'Desayuno. Dia libre en el resort o la playa de Sharm El Sheikh para disfrutar del Mar Rojo. Almuerzo y Cena incluidos en el hotel.'},
            {'day': 6, 'title': 'Sharm El Sheikh - El Cairo', 'description': 'Desayuno y check-out. Traslado al aeropuerto de Sharm El Sheikh para el vuelo interno a El Cairo. Traslado al hotel.'},
            {'day': 7, 'title': 'El Cairo - Partida', 'description': 'Desayuno y check-out. Traslado al aeropuerto de El Cairo para el vuelo internacional de regreso. Fin de nuestros servicios.'},
        ]
    },
    'Three Cultural Pearls of Egypt: Cairo, Alexandria and Luxor': {
        'name_es': 'Tres Perlas Culturales de Egipto: El Cairo, Alejandria y Luxor',
        'short_description_es': '9 dias por El Cairo, Luxor y Alejandria. Travesia unica con guia especializado y alojamiento, recorriendo los encantos de las antiguas capitales milenarias. Incluye 2 vuelos domesticos.',
        'itinerary_es': [
            {'day': 1, 'title': 'Llegada a El Cairo', 'description': 'Llegada al aeropuerto internacional de El Cairo. Recepcion y asistencia por nuestro representante local para los tramites del visado. Traslado al hotel seleccionado. Check-in y resto del dia libre.'},
            {'day': 2, 'title': 'El Cairo - Menfis - Saqqara', 'description': 'Desayuno. Visita al sitio al aire libre de Menfis con la colosal Estatua de Ramses II. Continuacion a Saqqara para visitar la Piramide Escalonada del Faraon Djoser, la Piramide del Rey Unas y mastabas decoradas. Almuerzo en restaurante local.'},
            {'day': 3, 'title': 'El Cairo - Luxor', 'description': 'Desayuno y check-out. Vuelo domestico a Luxor. Visita a la Margen Occidental: Valle de los Reyes, Templo de Hatshepsut y Colosos de Memnon. Traslado al hotel. Por la tarde, visita al Templo de Karnak. Cena en el hotel.'},
            {'day': 4, 'title': 'Luxor - El Cairo', 'description': 'Desayuno y check-out. Vuelo domestico de regreso a El Cairo. Traslado al hotel. Tarde libre. Opcional: Paseo en Globo sobre Luxor al amanecer.'},
            {'day': 5, 'title': 'El Cairo - Piramides de Guiza - Museo Egipcio', 'description': 'Desayuno. Visita a la meseta de Guiza para admirar las Grandes Piramides y la Esfinge. Parada en una galeria de Papiro. Almuerzo en restaurante local. Por la tarde, visita al Museo Egipcio de El Cairo.'},
            {'day': 6, 'title': 'El Cairo - Alejandria - El Cairo', 'description': 'Desayuno. Excursion de dia completo a Alejandria. Visita al Museo Nacional, Biblioteca de Alejandria y Ciudadela de Qaitbay. Almuerzo en restaurante local con vistas al Mediterraneo. Paseo por el Puente Stanley. Regreso a El Cairo.'},
            {'day': 7, 'title': 'El Cairo Cristiano e Islamico', 'description': 'Desayuno. Visita al Barrio Copto con la Iglesia Colgante y la Iglesia de San Sergio. Continuacion al Cairo Islamico: Ciudadela de Saladino y Mezquita de Mohamed Ali. Tiempo para compras en el mercado Khan el-Khalili. Almuerzo.'},
            {'day': 8, 'title': 'El Cairo - Dia Libre', 'description': 'Desayuno. Dia enteramente libre en El Cairo para actividades independientes, compras o descanso. Opcional: Visita al Museo Nacional de la Civilizacion Egipcia y subida a la Torre de El Cairo.'},
            {'day': 9, 'title': 'El Cairo - Partida', 'description': 'Desayuno. Check-out. Traslado al aeropuerto internacional de El Cairo para embarcar en su vuelo de regreso. Fin de nuestros servicios.'},
        ]
    },
}

def add_spanish_translations():
    print("\n=== Adding Spanish Translations ===\n")
    updated_count = 0

    for tour_name, translations in TRANSLATIONS.items():
        try:
            tour = Tour.objects.get(name=tour_name)

            # Update tour fields
            tour.name_es = translations['name_es']
            tour.short_description_es = translations['short_description_es']
            tour.save()

            # Update itinerary
            for item in translations['itinerary_es']:
                try:
                    itinerary = TourItinerary.objects.get(tour=tour, day_number=item['day'])
                    itinerary.title_es = item['title']
                    itinerary.description_es = item['description']
                    itinerary.save()
                except TourItinerary.DoesNotExist:
                    print(f"  Warning: Day {item['day']} not found for {tour_name}")

            print(f"  Updated: {tour_name}")
            updated_count += 1

        except Tour.DoesNotExist:
            print(f"  Tour not found: {tour_name}")

    print(f"\n=== Updated {updated_count} tours with Spanish translations ===")

if __name__ == '__main__':
    add_spanish_translations()
