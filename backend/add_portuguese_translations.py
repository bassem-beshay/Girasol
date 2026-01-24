#!/usr/bin/env python
"""
Script to add Portuguese translations for the 10 new tours.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import Tour, TourItinerary

# Portuguese translations mapping
TRANSLATIONS = {
    'Magic of the White Desert with Cairo and Alexandria': {
        'name_pt': 'Encanto do Deserto Branco com Cairo e Alexandria',
        'short_description_pt': '9 dias de aventura e história combinando a grandiosidade do Cairo e Alexandria com a magia surrealista dos oásis e desertos do Oeste egípcio.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto Internacional do Cairo. Recepção e assistência nas formalidades de entrada. Traslado ao hotel. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides de Gizé e Grande Museu Egípcio', 'description': 'Visita ao Complexo de Gizé com as Pirâmides de Quéops, Quéfren e Miquerinos, Templo do Vale e Esfinge. Parada em galeria de papiro. Almoço. Visita ao Grande Museu Egípcio (GEM). Pernoite no Cairo.'},
            {'day': 3, 'title': 'Cairo para Alexandria', 'description': 'Viagem a Alexandria (221 km). Visita ao Anfiteatro Romano, Museu Nacional, Biblioteca Moderna e Fortaleza de Qaitbay. Passeio pela Ponte Stanley. Retorno ao Cairo.'},
            {'day': 4, 'title': 'Mênfis e Saqqara', 'description': 'Visita ao Museu Aberto de Mênfis com o Colosso de Ramsés II e a Esfinge de Mênfis. Continuação para Saqqara com a Pirâmide Escalonada, Pirâmide de Unas e mastabas. Visita ao Museu de Imhotep.'},
            {'day': 5, 'title': 'Cairo para o Deserto Branco', 'description': 'Partida para o Oásis de El Heiz (350 km). Continuação para o Deserto Negro e Montanha de Cristal. Transfer para o Acampamento Shahrazad no Deserto Branco. Jantar e pernoite no acampamento.'},
            {'day': 6, 'title': 'Exploração do Deserto Branco', 'description': 'Dia inteiro explorando o Deserto Branco, uma das mais deslumbrantes reservas naturais do Egito. Caminhada guiada entre rochas de calcário branco. Almoço piquenique no deserto. Jantar e pernoite sob céu estrelado.'},
            {'day': 7, 'title': 'Retorno ao Cairo', 'description': 'Após café da manhã, retorno ao Cairo (aprox. 4 horas). Parada para almoço no caminho. Check-in no hotel no Cairo. Pernoite no Cairo.'},
            {'day': 8, 'title': 'Dia Livre no Cairo', 'description': 'Dia livre para compras ou tour opcional ao Cairo Copta e Islâmico incluindo a Cidadela de Saladino e Mesquita de Alabastro. Pernoite no Cairo.'},
            {'day': 9, 'title': 'Partida', 'description': 'Café da manhã. Transfer ao aeroporto do Cairo para seu voo de partida. Fim dos serviços.'}
        ]
    },
    'Best of Millennial Egypt with Abu Simbel and Dendera': {
        'name_pt': 'O Melhor do Egito Milenar com Abu Simbel e Dandara',
        'short_description_pt': '10 dias explorando os tesouros do Egito com Cruzeiro no Nilo, templos de Abu Simbel e o magnífico Templo de Dandara.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao aeroporto do Cairo. Recepção e assistência nas formalidades de entrada. Traslado ao hotel. Check-in. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides de Gizé e Museu Egípcio', 'description': 'Visita ao Complexo de Gizé com as três Grandes Pirâmides, Templo do Vale e Esfinge. Almoço em restaurante local. Visita ao Museu Egípcio do Cairo. Pernoite no Cairo.'},
            {'day': 3, 'title': 'Cairo Copta e Islâmico', 'description': 'Visita ao Cairo Cristão incluindo a Igreja Suspensa e Igreja de São Sérgio construída sobre a Gruta da Sagrada Família. Almoço. Visita à Cidadela de Saladino e Mesquita de Alabastro. Pernoite no Cairo.'},
            {'day': 4, 'title': 'Dia Livre no Cairo', 'description': 'Dia livre no Cairo. Visitas opcionais a Saqqara e Mênfis ou ao Grande Museu Egípcio (GEM). Pernoite no Cairo.'},
            {'day': 5, 'title': 'Voo para Luxor - Início do Cruzeiro', 'description': 'Voo para Luxor. Transfer para o Cruzeiro 5 estrelas no Nilo. Visita ao Templo de Dandara. Visita ao fabuloso Templo de Karnak e ao magnífico Templo de Luxor. Jantar a bordo. Pernoite no Cruzeiro.'},
            {'day': 6, 'title': 'Vale dos Reis e Navegação', 'description': 'Visita ao Vale dos Reis (3 tumbas reais), Templo de Hatshepsut e Colossos de Memnon. Navegação pela Eclusa de Esna rumo a Edfu. Pernoite no Cruzeiro.'},
            {'day': 7, 'title': 'Edfu e Kom Ombo', 'description': 'Visita ao Templo de Hórus em Edfu. Navegação para Kom Ombo. Visita ao templo duplo dedicado a Sobek e Hórus. Navegação para Assuã. Pernoite no Cruzeiro.'},
            {'day': 8, 'title': 'Assuã - Filae e Grande Represa', 'description': 'Visita à Grande Represa de Assuã e ao belo Templo de Ísis na Ilha de Filae. Passeio de Feluca no Nilo. Pernoite no Cruzeiro.'},
            {'day': 9, 'title': 'Abu Simbel e Voo para Cairo', 'description': 'Transfer matinal para Abu Simbel (265 km). Visita aos magníficos templos de Ramsés II e Nefertari. Retorno a Assuã. Voo para o Cairo. Pernoite no Cairo.'},
            {'day': 10, 'title': 'Partida', 'description': 'Café da manhã. Check-out e transfer ao Aeroporto Internacional do Cairo. Fim dos serviços.'}
        ]
    },
    'Classic Egypt with Nile Cruise': {
        'name_pt': 'Viagem Egito Clássico com Cruzeiro no Nilo',
        'short_description_pt': '10 dias explorando as maravilhas do Cairo e navegando pelo Nilo de Luxor a Assuã com paradas em templos antigos.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto Internacional do Cairo. Recepção e assistência nas formalidades do visto. Traslado ao hotel. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides de Gizé e Museu Egípcio', 'description': 'Visita ao Planalto de Gizé com as Grandes Pirâmides, Templo do Vale e Esfinge. Visita a galeria de Papiro. Almoço. Visita ao Museu Egípcio na Praça Tahrir. Pernoite no Cairo.'},
            {'day': 3, 'title': 'Cairo Cristão e Islâmico', 'description': 'Visita ao Bairro Copta com a Igreja Suspensa e Igreja de São Sérgio. Almoço. Visita à Cidadela de Saladino e Mesquita de Mohamed Ali. Pernoite no Cairo.'},
            {'day': 4, 'title': 'Dia Livre no Cairo', 'description': 'Dia livre para explorar ao seu ritmo. Tour opcional a Mênfis e Saqqara disponível. Pernoite no Cairo.'},
            {'day': 5, 'title': 'Voo para Luxor - Início do Cruzeiro', 'description': 'Voo para Luxor. Transfer para o Cruzeiro 5 estrelas no Nilo. Almoço a bordo. Visita ao Templo de Karnak e Templo de Luxor. Jantar a bordo. Pernoite no Cruzeiro.'},
            {'day': 6, 'title': 'Luxor Oeste - Navegação para Edfu', 'description': 'Visita ao Vale dos Reis (3 tumbas), Colossos de Memnon e Templo de Hatshepsut. Almoço a bordo. Navegação para Edfu pela Eclusa de Esna. Pernoite no Cruzeiro.'},
            {'day': 7, 'title': 'Edfu e Kom Ombo - Assuã', 'description': 'Visita ao Templo de Hórus em Edfu. Navegação para Kom Ombo. Visita ao templo duplo de Kom Ombo. Continuação para Assuã. Pernoite no Cruzeiro.'},
            {'day': 8, 'title': 'Assuã - Templo de Filae', 'description': 'Visita à Ilha de Filae com o Templo de Ísis. Passeio de feluca no Nilo. Pernoite no Cruzeiro.'},
            {'day': 9, 'title': 'Voo para Cairo', 'description': 'Desembarque após café da manhã. Transfer ao Aeroporto de Assuã. Voo para o Cairo. Tempo livre. Opcional: excursão a Abu Simbel. Pernoite no Cairo.'},
            {'day': 10, 'title': 'Partida', 'description': 'Café da manhã. Check-out. Transfer ao Aeroporto Internacional do Cairo. Fim dos serviços.'}
        ]
    },
    'Cultural Cairo and Marsa Alam on the Red Sea': {
        'name_pt': 'Cairo Cultural e Marsa Alam no Mar Vermelho',
        'short_description_pt': '8 dias combinando a história milenar do Cairo com relaxamento absoluto na costa preservada de Marsa Alam no Mar Vermelho.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto Internacional do Cairo. Assistência personalizada com imigração e visto. Traslado ao hotel. Check-in e descanso.'},
            {'day': 2, 'title': 'Pirâmides de Gizé e Museu Egípcio', 'description': 'Visita ao Planalto de Gizé com as Grandes Pirâmides e a Esfinge. Almoço em restaurante local. Exploração do Museu Egípcio. Retorno ao hotel para jantar. Pernoite no Cairo.'},
            {'day': 3, 'title': 'Voo para Marsa Alam', 'description': 'Café da manhã e check-out. Voo doméstico para Marsa Alam. Transfer para resort 4 estrelas. Check-in em regime Soft All-Inclusive. Tempo livre para apreciar o Mar Vermelho.'},
            {'day': 4, 'title': 'Marsa Alam - Dia Livre', 'description': 'Dia inteiro de lazer. Aproveite as piscinas, praia de areia dourada e águas cristalinas perfeitas para snorkeling. Todas as refeições e bebidas incluídas no resort.'},
            {'day': 5, 'title': 'Marsa Alam - Dia Livre', 'description': 'Segundo dia livre. Passeio opcional de barco aos recifes de coral, visita a parque aquático ou simplesmente relaxe junto ao mar. Refeições all-inclusive.'},
            {'day': 6, 'title': 'Marsa Alam - Dia Livre', 'description': 'Terceiro dia livre. Atividades opcionais de mergulho ou safari no deserto. Refeições all-inclusive no resort.'},
            {'day': 7, 'title': 'Retorno ao Cairo', 'description': 'Café da manhã. Tempo livre até o transfer ao Aeroporto de Marsa Alam. Voo para o Cairo. Transfer ao hotel. Jantar incluído. Pernoite no Cairo.'},
            {'day': 8, 'title': 'Partida', 'description': 'Café da manhã. Check-out. Transfer ao Aeroporto Internacional do Cairo. Fim dos serviços.'}
        ]
    },
    'Egypt in 8 Days: Cairo, Alexandria and Sharm El Sheikh': {
        'name_pt': 'Egito em 8 Dias: Cairo, Alexandria e Sharm El Sheikh',
        'short_description_pt': '8 dias descobrindo as maravilhas antigas do Cairo, o charme mediterrâneo de Alexandria, a espiritualidade do Monte Sinai e as praias de Sharm El Sheikh.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto Internacional do Cairo. Recepção e assistência com visto. Traslado ao hotel. Check-in e pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides de Gizé e Museu Egípcio', 'description': 'Visita ao Planalto de Gizé com as Grandes Pirâmides e Esfinge. Visita a galeria de papiro. Almoço. Exploração do Museu Egípcio. Retorno ao hotel.'},
            {'day': 3, 'title': 'Cairo para Monte Sinai', 'description': 'Café da manhã e check-out. Viagem terrestre para a região do Monte Sinai (448 km). Passagem pelo Túnel Ahmed Hamdi sob o Canal de Suez. Parada nas Fontes de Moisés. Chegada em Santa Catarina. Check-in. Jantar incluído.'},
            {'day': 4, 'title': 'Santa Catarina para Sharm El Sheikh', 'description': 'Café da manhã e check-out. Transfer para Sharm El Sheikh. Check-in em resort 4 estrelas em regime Soft All-inclusive. Tempo livre para apreciar as águas cristalinas do Mar Vermelho.'},
            {'day': 5, 'title': 'Sharm El Sheikh - Dia Livre', 'description': 'Dia inteiro livre para relaxar no resort, aproveitar a praia ou participar de atividades opcionais de mergulho ou snorkeling. Refeições all-inclusive.'},
            {'day': 6, 'title': 'Voo para Cairo', 'description': 'Café da manhã e check-out. Transfer ao Aeroporto de Sharm El Sheikh. Voo doméstico para o Cairo. Transfer ao hotel. Check-in. Tarde livre. Pernoite no Cairo.'},
            {'day': 7, 'title': 'Excursão a Alexandria', 'description': 'Café da manhã. Excursão de dia inteiro a Alexandria (221 km). Visita ao Teatro Romano, Museu Nacional e Biblioteca de Alexandria. Almoço. Visita externa à Fortaleza de Qaitbay e Ponte Stanley. Retorno ao Cairo.'},
            {'day': 8, 'title': 'Partida', 'description': 'Café da manhã e check-out. Transfer ao Aeroporto Internacional do Cairo. Fim dos serviços.'}
        ]
    },
    'Incredible Egypt Package: Cairo, Luxor and Hurghada': {
        'name_pt': 'Pacote Egito Incrível: Cairo, Luxor e Hurghada',
        'short_description_pt': '9 dias de magia combinando as pirâmides do Cairo, os templos faraônicos de Luxor e o paraíso do Mar Vermelho em Hurghada.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao aeroporto do Cairo. Recepção e assistência nas formalidades de entrada. Traslado ao hotel. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides de Gizé e Museu Egípcio', 'description': 'Visita ao Complexo de Gizé com as três Grandes Pirâmides, Templo do Vale e Esfinge. Visita a galeria de papiro. Almoço em restaurante local. Continuação ao Museu Egípcio. Retorno ao hotel.'},
            {'day': 3, 'title': 'Voo para Luxor - Dia Completo de Passeios', 'description': 'Voo para Luxor. Visita ao Vale dos Reis (3 tumbas reais), Colossos de Memnon e Templo de Hatshepsut. Check-in no hotel. À tarde, visita ao Templo de Karnak e Templo de Luxor. Jantar no hotel.'},
            {'day': 4, 'title': 'Transfer para Hurghada', 'description': 'Café da manhã. Check-out. Transfer para Hurghada (305 km). Check-in em resort de praia em regime Full Board All-Inclusive. Resto do dia livre.'},
            {'day': 5, 'title': 'Hurghada - Dia Livre', 'description': 'Dia livre para atividades pessoais no resort, mergulho ou relaxamento na praia. Todas as refeições incluídas no resort.'},
            {'day': 6, 'title': 'Hurghada - Dia Livre', 'description': 'Mais um dia livre no paraíso do mergulho de Hurghada. Todas as refeições incluídas no resort.'},
            {'day': 7, 'title': 'Voo para Cairo', 'description': 'Café da manhã. Check-out. Transfer ao aeroporto para voo doméstico ao Cairo. Transfer ao hotel. Tarde livre. Pernoite no Cairo.'},
            {'day': 8, 'title': 'Dia Livre no Cairo', 'description': 'Café da manhã no hotel. Dia livre. Opcional: tour a Saqqara, Cairo Copta e Cidadela de Saladino. Pernoite no Cairo.'},
            {'day': 9, 'title': 'Partida', 'description': 'Check-out. Transfer ao aeroporto do Cairo para partida. Fim dos serviços.'}
        ]
    },
    'Best of Egypt with Dubai and Abu Dhabi': {
        'name_pt': 'O Melhor do Egito com Dubai e Abu Dhabi',
        'short_description_pt': '14 dias combinando as maravilhas do Egito Antigo com o luxo moderno de Dubai e Abu Dhabi.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto Internacional do Cairo. Recepção e assistência com visto. Traslado ao hotel. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides e Museu Egípcio', 'description': 'Visita ao Planalto de Gizé com Pirâmides e Esfinge. Parada em galeria de Papiro. Almoço. Visita ao Museu Egípcio. Pernoite no Cairo.'},
            {'day': 3, 'title': 'Voo para Luxor - Início do Cruzeiro', 'description': 'Voo para Luxor. Visita ao Templo de Karnak. Transfer para o Cruzeiro 5 estrelas no Nilo. Visita ao Templo de Luxor ao pôr do sol. Pernoite no Cruzeiro.'},
            {'day': 4, 'title': 'Luxor Oeste - Navegação para Edfu', 'description': 'Visita ao Vale dos Reis, Colossos de Memnon e Templo de Hatshepsut. Navegação pela Eclusa de Esna rumo a Edfu. Pernoite no Cruzeiro.'},
            {'day': 5, 'title': 'Edfu e Kom Ombo - Assuã', 'description': 'Visita ao Templo de Hórus em Edfu. Navegação para Kom Ombo e visita ao templo duplo. Continuação para Assuã. Pernoite no Cruzeiro.'},
            {'day': 6, 'title': 'Assuã - Grande Represa e Filae', 'description': 'Visita à Grande Represa de Assuã e Templo de Filae. Passeio de Feluca no Nilo. Pernoite no Cruzeiro.'},
            {'day': 7, 'title': 'Voo para Cairo', 'description': 'Desembarque do cruzeiro. Voo para o Cairo. Transfer ao hotel. Opcional: excursão a Abu Simbel. Pernoite no Cairo.'},
            {'day': 8, 'title': 'Mênfis, Saqqara e Museu NMEC', 'description': 'Visita a Mênfis e Saqqara com a Pirâmide Escalonada. Almoço. Visita ao Museu Nacional da Civilização Egípcia com as Múmias Reais. Pernoite no Cairo.'},
            {'day': 9, 'title': 'Cairo Copta e Islâmico', 'description': 'Visita ao Bairro Copta com Igreja Suspensa. Continuação à Cidadela de Saladino e Mesquita de Alabastro. Almoço. Pernoite no Cairo.'},
            {'day': 10, 'title': 'Voo para Dubai', 'description': 'Transfer ao aeroporto do Cairo. Voo para Dubai (não incluído). Chegada, transfer ao hotel. City tour: Burj Khalifa e Dubai Frame. Pernoite em Dubai.'},
            {'day': 11, 'title': 'Excursão a Abu Dhabi', 'description': 'Excursão de dia inteiro a Abu Dhabi. Visita à Grande Mesquita Sheikh Zayed, Heritage Village e Palácio Qasr Al Watan. Almoço. Retorno a Dubai.'},
            {'day': 12, 'title': 'Dubai - Dia Livre', 'description': 'Dia livre em Dubai para atividades independentes, compras ou descanso. Pernoite em Dubai.'},
            {'day': 13, 'title': 'City Tour Dubai e Safari no Deserto', 'description': 'City tour matinal: Souks de Ouro e Especiarias, passeio de abra, área de Jumeirah. À tarde: Safari no Deserto em 4x4 com atividades no acampamento beduíno e jantar com show.'},
            {'day': 14, 'title': 'Partida de Dubai', 'description': 'Check-out. Transfer ao Aeroporto Internacional de Dubai. Fim dos serviços.'}
        ]
    },
    'The Best of Luxor and Aswan': {
        'name_pt': 'O Melhor de Luxor e Assuã',
        'short_description_pt': '5 dias descobrindo as maravilhas antigas do sul do Egito em Luxor, Edfu, Kom Ombo e Assuã sem cruzeiro.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada a Luxor', 'description': 'Chegada a Luxor. Visita à Margem Oeste: Vale dos Reis, Colossos de Memnon e Templo de Hatshepsut. Transfer ao hotel. À tarde, visita ao Templo de Luxor. Jantar no hotel. Pernoite em Luxor.'},
            {'day': 2, 'title': 'Templo de Karnak', 'description': 'Café da manhã. Visita ao magnífico Templo de Karnak, o maior complexo religioso do mundo antigo. Tarde livre. Jantar no hotel. Pernoite em Luxor.'},
            {'day': 3, 'title': 'Luxor para Assuã via Edfu e Kom Ombo', 'description': 'Café da manhã e check-out. Viagem a Edfu para visitar o Templo de Hórus. Continuação para Kom Ombo para visitar o templo duplo. Continuação para Assuã. Check-in no hotel. Jantar. Pernoite em Assuã.'},
            {'day': 4, 'title': 'Passeios em Assuã', 'description': 'Café da manhã. Visita à Ilha de Filae com o Templo de Ísis. Visita à Grande Represa de Assuã. Passeio de Feluca no Nilo. Visita ao Jardim Botânico. Jantar no hotel. Pernoite em Assuã.'},
            {'day': 5, 'title': 'Partida de Assuã', 'description': 'Café da manhã. Opcional: excursão a Abu Simbel (por estrada ou voo). Transfer ao Aeroporto de Assuã. Fim dos serviços.'}
        ]
    },
    'The Path of Moses': {
        'name_pt': 'O Caminho de Moisés',
        'short_description_pt': '7 dias seguindo os passos de Moisés através dos lugares sagrados do Egito, Monte Sinai e praias do Mar Vermelho.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto do Cairo. Recepção e assistência com visto. Transfer ao hotel. Check-in e descanso. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Pirâmides e Cairo Copta', 'description': 'Visita às Pirâmides de Gizé, Templo do Vale e Esfinge. Continuação ao Cairo Copta: Igreja Suspensa, Igreja de São Sérgio com Gruta da Sagrada Família e Sinagoga Ben Ezra. Almoço em restaurante local. Pernoite no Cairo.'},
            {'day': 3, 'title': 'Cairo para Monte Sinai', 'description': 'Café da manhã e check-out. Viagem terrestre para a região do Monte Sinai passando pelo túnel do Canal de Suez. Parada nas Fontes de Moisés. Chegada a Santa Catarina. Jantar e pernoite no hotel regional.'},
            {'day': 4, 'title': 'Monte Sinai para Sharm El Sheikh', 'description': 'Subida opcional ao Monte Sinai ao amanhecer (acompanhado por guia beduíno). Visita ao Mosteiro de Santa Catarina. Transfer para Sharm El Sheikh. Check-in em resort em regime Soft All-Inclusive. Tempo livre. Pernoite em Sharm El Sheikh.'},
            {'day': 5, 'title': 'Sharm El Sheikh - Dia Livre', 'description': 'Dia livre para aproveitar o resort e as praias do Mar Vermelho. Todas as refeições incluídas. Pernoite em Sharm El Sheikh.'},
            {'day': 6, 'title': 'Voo para Cairo', 'description': 'Café da manhã e check-out. Transfer ao Aeroporto de Sharm El Sheikh. Voo para o Cairo (incluído). Transfer ao hotel. Tarde livre. Pernoite no Cairo.'},
            {'day': 7, 'title': 'Partida', 'description': 'Café da manhã e check-out. Transfer ao Aeroporto do Cairo. Fim dos serviços.'}
        ]
    },
    'Three Cultural Pearls of Egypt: Cairo, Alexandria and Luxor': {
        'name_pt': 'Três Pérolas Culturais do Egito: Cairo, Alexandria e Luxor',
        'short_description_pt': '9 dias explorando as três capitais douradas do Egito: Cairo, Alexandria e Luxor com 2 voos domésticos.',
        'itinerary_pt': [
            {'day': 1, 'title': 'Chegada ao Cairo', 'description': 'Chegada ao Aeroporto Internacional do Cairo. Recepção e assistência com visto. Transfer ao hotel. Check-in e descanso. Pernoite no Cairo.'},
            {'day': 2, 'title': 'Mênfis e Saqqara', 'description': 'Visita ao sítio aberto de Mênfis com o Colosso de Ramsés II. Continuação para Saqqara com a Pirâmide Escalonada de Djoser, Pirâmide de Unas e mastabas decoradas. Visita ao Museu de Imhotep. Almoço. Pernoite no Cairo.'},
            {'day': 3, 'title': 'Voo para Luxor', 'description': 'Voo para Luxor. Visita à Margem Oeste: Vale dos Reis (3 tumbas), Templo de Hatshepsut e Colossos de Memnon. Transfer ao hotel. Visita ao Templo de Karnak. Jantar no hotel. Pernoite em Luxor.'},
            {'day': 4, 'title': 'Voo para Cairo', 'description': 'Café da manhã e check-out. Opcional: passeio de balão sobre Luxor ao amanhecer. Transfer ao Aeroporto de Luxor. Voo para o Cairo. Transfer ao hotel. Tarde livre. Pernoite no Cairo.'},
            {'day': 5, 'title': 'Pirâmides de Gizé e Museu Egípcio', 'description': 'Visita ao Planalto de Gizé com as Grandes Pirâmides e Esfinge. Parada em galeria de Papiro. Almoço. Visita ao Museu Egípcio na Praça Tahrir. Pernoite no Cairo.'},
            {'day': 6, 'title': 'Excursão a Alexandria', 'description': 'Excursão de dia inteiro a Alexandria. Visita ao Museu Nacional, Biblioteca de Alexandria e Fortaleza de Qaitbay (exterior). Almoço. Passeio pela Ponte Stanley. Retorno ao Cairo.'},
            {'day': 7, 'title': 'Cairo Cristão e Islâmico', 'description': 'Visita ao Bairro Copta com Igreja Suspensa e Igreja de São Sérgio. Continuação ao Cairo Islâmico: Cidadela de Saladino e Mesquita de Mohammed Ali. Visita ao mercado Khan El-Khalili. Almoço. Pernoite no Cairo.'},
            {'day': 8, 'title': 'Dia Livre no Cairo', 'description': 'Dia livre para atividades independentes, compras ou descanso. Opcional: Visita ao Museu Nacional da Civilização Egípcia (NMEC) com as Múmias Reais. Pernoite no Cairo.'},
            {'day': 9, 'title': 'Partida', 'description': 'Café da manhã. Check-out. Transfer ao Aeroporto Internacional do Cairo. Fim dos serviços.'}
        ]
    }
}


def update_tours():
    print("\n=== Adding Portuguese Translations ===\n")

    updated = 0
    for en_name, data in TRANSLATIONS.items():
        try:
            tour = Tour.objects.get(name=en_name)

            # Update tour fields
            tour.name_pt = data['name_pt']
            tour.short_description_pt = data['short_description_pt']
            tour.save()

            # Update itinerary
            for item in data.get('itinerary_pt', []):
                try:
                    itin = TourItinerary.objects.get(tour=tour, day_number=item['day'])
                    itin.title_pt = item['title']
                    itin.description_pt = item['description']
                    itin.save()
                except TourItinerary.DoesNotExist:
                    print(f"  Warning: Itinerary day {item['day']} not found for {en_name}")

            updated += 1
            print(f"  Updated: {en_name}")

        except Tour.DoesNotExist:
            print(f"  Tour not found: {en_name}")

    print(f"\n=== Updated {updated} tours with Portuguese translations ===\n")
    return updated


if __name__ == '__main__':
    update_tours()
