#!/usr/bin/env python
"""
Script to add 10 new tour packages from Word documents.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.utils import timezone
from apps.tours.models import Tour, TourCategory, TourType, TourItinerary, TourInclusion, TourHighlight
from apps.destinations.models import Destination


def get_or_create_destination(name):
    dest, created = Destination.objects.get_or_create(
        name=name,
        defaults={'description': f'Explore {name}', 'is_active': True}
    )
    if created:
        print(f"  Created destination: {name}")
    return dest


def get_or_create_category(name):
    cat, created = TourCategory.objects.get_or_create(
        name=name,
        defaults={'description': f'{name} tours', 'is_active': True}
    )
    if created:
        print(f"  Created category: {name}")
    return cat


def get_or_create_tour_type(name):
    tt, created = TourType.objects.get_or_create(
        name=name,
        defaults={'description': f'{name}', 'is_active': True}
    )
    if created:
        print(f"  Created tour type: {name}")
    return tt


def create_tour(data):
    """Create a tour with all related data."""
    if Tour.objects.filter(name=data['name']).exists():
        print(f"  Tour already exists: {data['name']}")
        return None

    category = get_or_create_category(data['category'])
    tour_type = get_or_create_tour_type(data['tour_type'])

    tour = Tour.objects.create(
        name=data['name'],
        short_description=data['short_description'],
        description=data['description'],
        category=category,
        tour_type=tour_type,
        days=data['days'],
        nights=data['nights'],
        price=data.get('price', 0),
        is_featured=data.get('is_featured', True),
        is_best_seller=data.get('is_best_seller', False),
        is_multi_destination=data.get('is_multi_destination', False),
        is_published=True,
        published_at=timezone.now(),
        difficulty_level='easy',
        featured_image='tours/default.jpg'
    )

    # Add destinations
    for dest_name in data.get('destinations', []):
        dest = get_or_create_destination(dest_name)
        tour.destinations.add(dest)

    # Add highlights
    for i, hl in enumerate(data.get('highlights', [])):
        TourHighlight.objects.create(tour=tour, title=hl, sort_order=i)

    # Add itinerary
    for item in data.get('itinerary', []):
        TourItinerary.objects.create(
            tour=tour,
            day_number=item['day'],
            title=item['title'],
            description=item['description'],
            sort_order=item['day']
        )

    # Add inclusions
    for i, inc in enumerate(data.get('inclusions', [])):
        TourInclusion.objects.create(tour=tour, item=inc, is_included=True, sort_order=i)

    for i, exc in enumerate(data.get('exclusions', [])):
        TourInclusion.objects.create(tour=tour, item=exc, is_included=False, sort_order=i + 20)

    print(f"  Created tour: {data['name']}")
    return tour


def seed_tours():
    print("\n=== Adding 10 New Tour Packages ===\n")

    tours_data = [
        # 1. Magic of the White Desert
        {
            'name': 'Magic of the White Desert with Cairo and Alexandria',
            'short_description': '9 days of discovery combining Cairo\'s historical grandeur with the surreal magic of Egypt\'s Western Desert oases.',
            'description': '''Discover Egypt beyond the pyramids with an exclusive journey that combines the historical grandeur of Cairo and Alexandria with the surreal magic of the oases and deserts of the Egyptian West.

This 9-day package has been carefully designed to offer an immersive and diverse experience, ideal for travelers seeking adventure, culture, and authenticity.

Explore the iconic monuments of Giza and Saqqara, dive into the Greco-Roman heritage of Alexandria, and adventure through the unique landscapes of the White Desert, Black Desert, and Crystal Mountain. Sleep under a starry sky in a Bedouin camp in the White Desert and get to know the Bahariya and Farafra oases, where life blossoms in the middle of the desert.

Route: Cairo → Giza → Bahariya Oasis → Farafra Oasis → White Desert → Black Desert → Cairo → Alexandria → Cairo''',
            'category': 'Desert Adventures',
            'tour_type': 'Multi-Day Package',
            'days': 9,
            'nights': 8,
            'price': 1899,
            'is_featured': True,
            'is_best_seller': False,
            'destinations': ['Cairo', 'Alexandria', 'Bahariya Oasis', 'White Desert'],
            'highlights': [
                'Pyramids of Giza and the Sphinx',
                'Grand Egyptian Museum (GEM)',
                'White Desert camping under the stars',
                'Black Desert and Crystal Mountain',
                'Alexandria\'s Greco-Roman heritage',
                'Bahariya and Farafra Oases',
                '4x4 desert adventure'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo International Airport. Our representative will assist with entry formalities and luggage collection. Transfer to the hotel. Overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids of Giza and Grand Egyptian Museum', 'description': 'Visit the Giza Plateau with the famous Pyramids of Khufu, Khafre, and Menkaure, the Valley Temple and the Sphinx. Stop at a papyrus gallery. Lunch at a local restaurant. Visit the Grand Egyptian Museum (GEM). Overnight in Cairo.'},
                {'day': 3, 'title': 'Cairo to Alexandria', 'description': 'Journey to Alexandria (221 km). Visit the Roman Amphitheatre, National Museum, Modern Library of Alexandria, and Qaitbay Citadel. Stroll on Stanley Bridge. Return to Cairo. Overnight in Cairo.'},
                {'day': 4, 'title': 'Memphis and Saqqara', 'description': 'Visit the Open Court of Memphis with the Colossus of Ramses II and the Memphis Sphinx. Continue to Saqqara to see the Step Pyramid complex, Pyramid of Unas, and mastabas. Visit the Imhotep Museum. Overnight in Cairo.'},
                {'day': 5, 'title': 'Cairo to White Desert', 'description': 'Departure to El Heiz Oasis (350 km). Continue to the Black Desert and Crystal Mountain. Transfer to Shahrazad Camp in the White Desert. Dinner and overnight at the camp.'},
                {'day': 6, 'title': 'White Desert Exploration', 'description': 'Full day exploring the White Desert, one of Egypt\'s most stunning natural reserves. Guided walk among white limestone rocks. Picnic lunch in the desert. Return to camp for dinner and overnight under starry sky.'},
                {'day': 7, 'title': 'Return to Cairo', 'description': 'After breakfast, begin return to Cairo (approx. 4 hours). Stop for lunch on the way. Check-in at hotel in Cairo. Overnight in Cairo.'},
                {'day': 8, 'title': 'Free Day in Cairo', 'description': 'Free day for shopping or optional tour to Christian Coptic Cairo and Islamic Cairo including the Citadel of Saladin and Alabaster Mosque. Overnight in Cairo.'},
                {'day': 9, 'title': 'Departure', 'description': 'Breakfast. Transfer to Cairo airport for your departure flight. End of services.'}
            ],
            'inclusions': [
                '7 nights accommodation in Cairo (5-star hotel)',
                '2 nights in luxury camp in the White Desert',
                'Half board in Cairo and Alexandria (breakfast + lunch)',
                'Full board in the White Desert',
                'English-speaking Egyptologist guide',
                'Air-conditioned transportation',
                '4x4 vehicle for desert exploration',
                'All entrance fees as per itinerary'
            ],
            'exclusions': [
                'International airfare',
                'Egypt entry visa',
                'Optional tours',
                'Tips and gratuities',
                'Personal expenses',
                'Travel insurance'
            ]
        },

        # 2. Best of Millennial Egypt with Abu Simbel and Dendera
        {
            'name': 'Best of Millennial Egypt with Abu Simbel and Dendera',
            'short_description': '10 days exploring Egypt\'s treasures with Nile Cruise, Abu Simbel temples, and the magnificent Dendera Temple.',
            'description': '''The 'Best of Millennial Egypt with Abu Simbel and Dendera' package offers 10 days of immersive land experience with 2 included domestic flights.

Combine accommodation in Cairo and a Nile cruise to explore the treasures of Giza, Luxor, Dendera, Edfu, Kom Ombo, Aswan, and majestic Abu Simbel.

This unique package includes the "unmissable but seldom offered" temples: Abu Simbel (a wonder of Pharaonic engineering, saved from the Nile waters!) + Dendera (Temple of Hathor with the famous Dendera Zodiac).

Route: Cairo → Giza → Luxor → Dendera → Nile Cruise (5 days/4 nights) → Aswan → Abu Simbel → Cairo''',
            'category': 'Classic Egypt Tours',
            'tour_type': 'Multi-Day Package',
            'days': 10,
            'nights': 9,
            'price': 2299,
            'is_featured': True,
            'is_best_seller': True,
            'destinations': ['Cairo', 'Luxor', 'Aswan', 'Abu Simbel'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                'Egyptian Museum of Cairo',
                'Coptic and Islamic Cairo',
                'Dendera Temple of Hathor',
                '5-star Nile Cruise (4 nights)',
                'Valley of the Kings',
                'Karnak and Luxor Temples',
                'Abu Simbel Temples',
                'Philae Temple'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo airport. Reception and assistance with entry formalities. Transfer to the hotel. Check-in. Overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids of Giza and Egyptian Museum', 'description': 'Visit the Giza Complex with the three Great Pyramids, Valley Temple, and the Sphinx. Lunch at a local restaurant. Visit the Egyptian Museum of Cairo with its marvelous artifacts. Overnight in Cairo.'},
                {'day': 3, 'title': 'Coptic and Islamic Cairo', 'description': 'Visit Christian Cairo including the Hanging Church and Church of Saint Sergius built on the Holy Family Grotto. Lunch. Continue to the Citadel of Saladin and the Alabaster Mosque. Overnight in Cairo.'},
                {'day': 4, 'title': 'Free Day in Cairo', 'description': 'Free day in Cairo. Optional visits to Saqqara and Memphis or the Grand Egyptian Museum (GEM). Overnight in Cairo.'},
                {'day': 5, 'title': 'Fly to Luxor - Nile Cruise Begins', 'description': 'Flight to Luxor. Transfer to your 5-star Nile Cruise. Visit the fabulous Karnak Temple and magnificent Luxor Temple. Dinner on board. Overnight on Cruise.'},
                {'day': 6, 'title': 'Valley of the Kings and Sailing', 'description': 'Visit the Valley of the Kings (3 royal tombs), Temple of Hatshepsut, and Colossi of Memnon. Optional: Visit Dendera Temple. Sail through Esna Lock towards Edfu. Overnight on Cruise.'},
                {'day': 7, 'title': 'Edfu and Kom Ombo', 'description': 'Visit the Temple of Horus in Edfu, one of the best-preserved temples. Sail to Kom Ombo. Visit the unique dual temple dedicated to Sobek and Horus. Sail to Aswan. Overnight on Cruise.'},
                {'day': 8, 'title': 'Aswan - Philae and High Dam', 'description': 'Visit the Aswan High Dam and the beautiful Temple of Isis on Philae Island. Felucca ride on the Nile. Overnight on Cruise.'},
                {'day': 9, 'title': 'Abu Simbel and Fly to Cairo', 'description': 'Early morning transfer to Abu Simbel (265 km). Visit the magnificent temples of Ramses II and Nefertari. Return to Aswan. Flight to Cairo. Overnight in Cairo.'},
                {'day': 10, 'title': 'Departure', 'description': 'Breakfast. Check-out and transfer to Cairo International Airport. End of services.'}
            ],
            'inclusions': [
                '5 nights in Cairo (5-star hotel)',
                '4 nights on 5-star Nile Cruise (full board)',
                '2 domestic flights (Cairo-Luxor, Aswan-Cairo)',
                'Abu Simbel excursion by road',
                'All tours with Egyptologist guide',
                'All entrance fees',
                'Meals as per itinerary'
            ],
            'exclusions': [
                'International airfare',
                'Egypt entry visa ($25)',
                'Optional tours',
                'Tips ($65-75 per person recommended)',
                'Travel insurance'
            ]
        },

        # 3. Classic Egypt with Nile Cruise
        {
            'name': 'Classic Egypt with Nile Cruise',
            'short_description': '10 days exploring Cairo\'s wonders and cruising the Nile from Luxor to Aswan with stops at ancient temples.',
            'description': '''This "Classic Egypt with Nile Cruise" package offers a comprehensive 10-day, 9-night land itinerary, perfect for those wishing to explore the wonders of Ancient Egypt in complete comfort.

The package includes two domestic flights, selected accommodation in Cairo, and a charming cruise on the Nile River, along with visits to the most important historical sites in Luxor and Aswan.

An enriching experience that combines culture, comfort, and unforgettable discoveries.

Route: Cairo → Giza → Luxor → Nile Cruise (4 nights) → Aswan → Cairo''',
            'category': 'Nile Cruises',
            'tour_type': 'Multi-Day Package',
            'days': 10,
            'nights': 9,
            'price': 1999,
            'is_featured': True,
            'is_best_seller': True,
            'destinations': ['Cairo', 'Luxor', 'Aswan'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                'Egyptian Museum',
                'Coptic and Islamic Cairo',
                '4-night Nile Cruise',
                'Valley of the Kings',
                'Temple of Hatshepsut',
                'Karnak and Luxor Temples',
                'Edfu and Kom Ombo Temples',
                'Philae Temple'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo International Airport. Welcome and assistance with visa formalities. Transfer to hotel. Overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids of Giza and Egyptian Museum', 'description': 'Visit the Giza Plateau with the Great Pyramids, Valley Temple, and the Sphinx. Visit a Papyrus gallery. Lunch at a local restaurant. Visit the Egyptian Museum in Tahrir Square. Overnight in Cairo.'},
                {'day': 3, 'title': 'Christian and Islamic Cairo', 'description': 'Visit the Coptic Quarter with the Hanging Church and Church of St. Sergius. Lunch. Visit the Citadel of Saladin and Mohamed Ali Mosque. Overnight in Cairo.'},
                {'day': 4, 'title': 'Free Day in Cairo', 'description': 'Free day to explore at your own pace. Optional tour to Memphis and Saqqara available. Overnight in Cairo.'},
                {'day': 5, 'title': 'Fly to Luxor - Cruise Begins', 'description': 'Flight to Luxor. Transfer to 5-star Nile Cruise. Lunch on board. Visit Karnak Temple and Luxor Temple. Dinner on board. Overnight on Cruise.'},
                {'day': 6, 'title': 'Luxor West Bank - Sailing to Edfu', 'description': 'Visit Valley of the Kings (3 tombs), Colossi of Memnon, and Temple of Hatshepsut. Lunch on board. Sail to Edfu through Esna Lock. Overnight on Cruise.'},
                {'day': 7, 'title': 'Edfu and Kom Ombo - Aswan', 'description': 'Visit the Temple of Horus in Edfu. Sail to Kom Ombo. Visit the dual temple of Kom Ombo. Continue to Aswan. Overnight on Cruise.'},
                {'day': 8, 'title': 'Aswan - Philae Temple', 'description': 'Visit Philae Island with the Temple of Isis. Enjoy a felucca sailboat ride on the Nile. Overnight on Cruise.'},
                {'day': 9, 'title': 'Fly to Cairo', 'description': 'Disembark after breakfast. Transfer to Aswan Airport. Flight to Cairo. Free time. Optional: Abu Simbel excursion. Overnight in Cairo.'},
                {'day': 10, 'title': 'Departure', 'description': 'Breakfast. Check-out. Transfer to Cairo International Airport. End of services.'}
            ],
            'inclusions': [
                '5 nights in Cairo (5-star hotel)',
                '4 nights on 5-star Nile Cruise (full board)',
                '2 domestic flights',
                'Half board in Cairo',
                'English-speaking Egyptologist guide',
                'All transfers and entrance fees'
            ],
            'exclusions': [
                'International airfare',
                'Egypt entry visa',
                'Optional tours',
                'Tips for guide, driver, and cruise staff',
                'Travel insurance'
            ]
        },

        # 4. Cultural Cairo and Marsa Alam
        {
            'name': 'Cultural Cairo and Marsa Alam on the Red Sea',
            'short_description': '8 days combining Cairo\'s millennia-old history with absolute relaxation on Marsa Alam\'s pristine Red Sea coast.',
            'description': '''Discover the hidden gem of the Red Sea, Marsa Alam, and dive into the grandeur of Cairo with an 8-day land package in Egypt.

This unique journey combines the fascinating millennia-old history of the pharaohs with absolute relaxation on one of the country's most preserved coastlines.

Known for its untouched coral reefs and golden sand beaches, Marsa Alam is a paradise for snorkeling, diving, and absolute relaxation.

Route: Cairo → Marsa Alam → Cairo''',
            'category': 'Beach & Diving',
            'tour_type': 'Multi-Day Package',
            'days': 8,
            'nights': 7,
            'price': 1499,
            'is_featured': True,
            'is_best_seller': False,
            'destinations': ['Cairo', 'Marsa Alam'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                'Egyptian Museum',
                'Marsa Alam pristine beaches',
                'Red Sea coral reefs',
                'Snorkeling and diving opportunities',
                'All-inclusive resort experience'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo International Airport. Personalized assistance with immigration and visa. Transfer to hotel. Check-in and rest.'},
                {'day': 2, 'title': 'Pyramids of Giza and Egyptian Museum', 'description': 'Visit the Giza Plateau with the Great Pyramids and the Sphinx. Lunch at a local restaurant. Explore the Egyptian Museum. Return to hotel for dinner. Overnight in Cairo.'},
                {'day': 3, 'title': 'Fly to Marsa Alam', 'description': 'Breakfast and check-out. Domestic flight to Marsa Alam. Transfer to 4-star resort. Check-in on Soft All-inclusive basis. Free time to enjoy the Red Sea.'},
                {'day': 4, 'title': 'Marsa Alam - Free Day', 'description': 'Full day at leisure. Enjoy the pools, golden sand beach, and crystal-clear waters perfect for snorkeling. All meals and drinks included at the resort.'},
                {'day': 5, 'title': 'Marsa Alam - Free Day', 'description': 'Second free day. Optional boat trip to coral reefs, water park visit, or simply relax by the sea. All-inclusive meals.'},
                {'day': 6, 'title': 'Marsa Alam - Free Day', 'description': 'Third free day. Optional scuba diving or desert safari activities. All-inclusive meals at the resort.'},
                {'day': 7, 'title': 'Return to Cairo', 'description': 'Breakfast. Free time until transfer to Marsa Alam Airport. Flight to Cairo. Transfer to hotel. Dinner included. Overnight in Cairo.'},
                {'day': 8, 'title': 'Departure', 'description': 'Breakfast. Check-out. Transfer to Cairo International Airport. End of services.'}
            ],
            'inclusions': [
                '3 nights in Cairo (5-star hotel)',
                '4 nights in Marsa Alam (5-star resort, Soft All-Inclusive)',
                '2 domestic flights',
                'Full board in Cairo',
                'Cairo tours with English-speaking guide',
                'All transfers'
            ],
            'exclusions': [
                'International airfare',
                'Egypt entry visa',
                'Personal extras and alcoholic beverages',
                'Tips',
                'Travel insurance'
            ]
        },

        # 5. Egypt in 8 Days (Cairo, Alexandria, Sharm)
        {
            'name': 'Egypt in 8 Days: Cairo, Alexandria and Sharm El Sheikh',
            'short_description': '8 days discovering Cairo\'s ancient wonders, Alexandria\'s Mediterranean charm, Mount Sinai\'s spirituality, and Sharm El Sheikh\'s beaches.',
            'description': '''Embark on an essential journey that brings together Egypt's most iconic destinations in one optimized 8-day, 7-night tour.

Experience the grandeur of Cairo with the enigmatic Pyramids and the rich collection of the Egyptian Museum. Travel through history to Alexandria, the jewel of the Mediterranean. Then, immerse yourself in a spiritual experience in the sacred Mount Sinai region. Finally, surrender to well-deserved relaxation in the turquoise waters and beaches of Sharm El Sheikh.

A perfect combination for those seeking a complete and balanced adventure.

Route: Cairo → Alexandria → Mount Sinai (St. Catherine) → Sharm El Sheikh → Cairo''',
            'category': 'Classic Egypt Tours',
            'tour_type': 'Multi-Day Package',
            'days': 8,
            'nights': 7,
            'price': 1599,
            'is_featured': True,
            'is_best_seller': False,
            'destinations': ['Cairo', 'Alexandria', 'Sharm El Sheikh', 'Mount Sinai'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                'Egyptian Museum',
                'Alexandria\'s Greco-Roman heritage',
                'Mount Sinai and St. Catherine',
                'Sharm El Sheikh beaches',
                'Red Sea relaxation'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo International Airport. Reception and assistance with visa. Transfer to hotel. Check-in and overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids of Giza and Egyptian Museum', 'description': 'Visit the Giza Plateau with the Great Pyramids and Sphinx. Visit a papyrus gallery. Lunch at a local restaurant. Explore the Egyptian Museum. Return to hotel.'},
                {'day': 3, 'title': 'Cairo to Mount Sinai', 'description': 'Breakfast and check-out. Overland journey to Mount Sinai region (448 km). Pass through Ahmed Hamdi Tunnel under the Suez Canal. Stop at the Fountains of Moses. Arrival at St. Catherine. Check-in. Dinner included.'},
                {'day': 4, 'title': 'St. Catherine to Sharm El Sheikh', 'description': 'Breakfast and check-out. Transfer to Sharm El Sheikh. Check-in at 4-star resort on Soft All-inclusive basis. Free time to enjoy the crystal-clear Red Sea.'},
                {'day': 5, 'title': 'Sharm El Sheikh - Free Day', 'description': 'Full day free to relax at the resort, enjoy the beach, or participate in optional diving or snorkeling activities. All-inclusive meals.'},
                {'day': 6, 'title': 'Fly to Cairo', 'description': 'Breakfast and check-out. Transfer to Sharm El Sheikh Airport. Domestic flight to Cairo. Transfer to hotel. Check-in. Free afternoon. Overnight in Cairo.'},
                {'day': 7, 'title': 'Alexandria Day Trip', 'description': 'Breakfast. Full-day excursion to Alexandria (221 km). Visit the Roman Theatre, National Museum, and Library of Alexandria. Lunch at local restaurant. See Qaitbay Citadel and Stanley Bridge. Return to Cairo.'},
                {'day': 8, 'title': 'Departure', 'description': 'Breakfast and check-out. Transfer to Cairo International Airport. End of services.'}
            ],
            'inclusions': [
                '4 nights in Cairo (4-star hotel)',
                '1 night in St. Catherine (3-star regional lodge)',
                '2 nights in Sharm El Sheikh (4-star resort, Soft All-Inclusive)',
                '1 domestic flight',
                'Half board in Cairo and St. Catherine',
                'English-speaking guide',
                'All entrance fees'
            ],
            'exclusions': [
                'International airfare',
                'Egypt entry visa',
                'Optional tours',
                'Tips',
                'Travel insurance'
            ]
        },

        # 6. Incredible Egypt Package
        {
            'name': 'Incredible Egypt Package: Cairo, Luxor and Hurghada',
            'short_description': '9 days of magic combining Cairo\'s pyramids, Luxor\'s pharaonic temples, and Hurghada\'s Red Sea paradise.',
            'description': '''Live Egypt in 9 days with the Incredible Egypt Trip! A land package (no cruise) with tours in Cairo (pyramids), Luxor (Pharaonic temples), and a seaside resort stay in Hurghada.

History, culture, and relaxation in a single journey!

This non-cruise itinerary is perfect for those who prefer staying in hotels while exploring the best of Ancient Egypt and enjoying Red Sea beach relaxation.

Route: Cairo → Giza → Luxor → Hurghada → Cairo''',
            'category': 'Classic Egypt Tours',
            'tour_type': 'Multi-Day Package',
            'days': 9,
            'nights': 8,
            'price': 1699,
            'is_featured': True,
            'is_best_seller': False,
            'destinations': ['Cairo', 'Luxor', 'Hurghada'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                'Egyptian Museum',
                'Valley of the Kings',
                'Temple of Hatshepsut',
                'Karnak and Luxor Temples',
                'Hurghada beach resort',
                'Red Sea relaxation'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo airport. Reception and assistance with entry formalities. Transfer to hotel. Overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids of Giza and Egyptian Museum', 'description': 'Visit the Giza Complex with the three Great Pyramids, Valley Temple, and the Sphinx. Visit a papyrus gallery. Lunch at local restaurant. Continue to the Egyptian Museum. Return to hotel.'},
                {'day': 3, 'title': 'Fly to Luxor - Full Day Touring', 'description': 'Flight to Luxor. Visit the Valley of the Kings (3 royal tombs), Colossi of Memnon, and Temple of Hatshepsut. Check-in at hotel. In the afternoon, visit Karnak Temple and Luxor Temple. Dinner at hotel.'},
                {'day': 4, 'title': 'Transfer to Hurghada', 'description': 'Breakfast. Check-out. Transfer to Hurghada (305 km). Check-in at beach resort on Full Board All-Inclusive basis. Rest of day free.'},
                {'day': 5, 'title': 'Hurghada - Free Day', 'description': 'Free day for personal activities at the resort, diving, or beach relaxation. All meals included at the resort.'},
                {'day': 6, 'title': 'Hurghada - Free Day', 'description': 'Another free day in Hurghada\'s diving paradise. All meals included at the resort.'},
                {'day': 7, 'title': 'Fly to Cairo', 'description': 'Breakfast. Check-out. Transfer to airport for domestic flight to Cairo. Transfer to hotel. Free afternoon. Overnight in Cairo.'},
                {'day': 8, 'title': 'Free Day in Cairo', 'description': 'Breakfast at hotel. Free day. Optional: Saqqara tour, Coptic Cairo, and Citadel of Saladin. Overnight in Cairo.'},
                {'day': 9, 'title': 'Departure', 'description': 'Check-out. Transfer to Cairo airport for departure. End of services.'}
            ],
            'inclusions': [
                '4 nights in Cairo (4-star hotel)',
                '2 nights in Luxor (4-star hotel, half board)',
                '3 nights in Hurghada (4-star resort, Full Board Soft All-Inclusive)',
                '2 domestic flights (Cairo-Luxor, Hurghada-Cairo)',
                'Tours with English-speaking guide',
                'All entrance fees'
            ],
            'exclusions': [
                'International airfare',
                'Egypt entry visa',
                'Optional tours',
                'Tips',
                'Travel insurance'
            ]
        },

        # 7. Best of Egypt with Dubai and Abu Dhabi
        {
            'name': 'Best of Egypt with Dubai and Abu Dhabi',
            'short_description': '14 days combining Ancient Egypt\'s wonders with Dubai and Abu Dhabi\'s modern luxury.',
            'description': '''Discover Egypt with the stunning "The Best of Egypt with Dubai and Abu Dhabi" itinerary: a 14-day package through historical wonders and the modernity of the Emirates.

This unique journey combines the grandeur of Ancient Egypt with the futuristic boldness of Dubai and Abu Dhabi. Enjoy a luxury 5-star Nile Cruise, explore the Pyramids and temples, then experience the modern wonders of the UAE including Burj Khalifa, Dubai Mall, and the Sheikh Zayed Grand Mosque.

Route: Cairo → Giza → Luxor → Nile Cruise → Aswan → Cairo → Dubai → Abu Dhabi → Dubai''',
            'category': 'Multi-Country Tours',
            'tour_type': 'Multi-Country Tour',
            'days': 14,
            'nights': 13,
            'price': 3499,
            'is_featured': True,
            'is_best_seller': True,
            'is_multi_destination': True,
            'destinations': ['Cairo', 'Luxor', 'Aswan', 'Dubai', 'Abu Dhabi'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                '5-star Nile Cruise (4 nights)',
                'Valley of the Kings',
                'Abu Simbel Temples (optional)',
                'Burj Khalifa observation deck',
                'Sheikh Zayed Grand Mosque',
                'Dubai Desert Safari',
                'Dubai city tour'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo International Airport. Reception and visa assistance. Transfer to hotel. Overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids and Egyptian Museum', 'description': 'Visit Giza Plateau with Pyramids and Sphinx. Stop at Papyrus gallery. Lunch. Visit the Egyptian Museum. Overnight in Cairo.'},
                {'day': 3, 'title': 'Fly to Luxor - Cruise Begins', 'description': 'Flight to Luxor. Visit Karnak Temple. Transfer to 5-star Nile Cruise. Visit Luxor Temple at sunset. Overnight on Cruise.'},
                {'day': 4, 'title': 'Luxor West Bank - Sailing to Edfu', 'description': 'Visit Valley of the Kings, Colossi of Memnon, and Temple of Hatshepsut. Sail through Esna Lock towards Edfu. Overnight on Cruise.'},
                {'day': 5, 'title': 'Edfu and Kom Ombo - Aswan', 'description': 'Visit Temple of Horus in Edfu. Sail to Kom Ombo and visit the dual temple. Continue to Aswan. Overnight on Cruise.'},
                {'day': 6, 'title': 'Aswan - High Dam and Philae', 'description': 'Visit Aswan High Dam and Philae Temple. Felucca ride on the Nile. Overnight on Cruise.'},
                {'day': 7, 'title': 'Fly to Cairo', 'description': 'Disembark cruise. Flight to Cairo. Transfer to hotel. Optional: Abu Simbel excursion. Overnight in Cairo.'},
                {'day': 8, 'title': 'Memphis, Saqqara and NMEC Museum', 'description': 'Visit Memphis and Saqqara with the Step Pyramid. Lunch. Visit the National Museum of Egyptian Civilization with Royal Mummies. Overnight in Cairo.'},
                {'day': 9, 'title': 'Coptic and Islamic Cairo', 'description': 'Visit Coptic Quarter with Hanging Church. Continue to Citadel of Saladin and Alabaster Mosque. Lunch. Overnight in Cairo.'},
                {'day': 10, 'title': 'Fly to Dubai', 'description': 'Transfer to Cairo airport. Flight to Dubai (not included). Arrival, transfer to hotel. Afternoon city tour: Burj Khalifa and Dubai Frame. Overnight in Dubai.'},
                {'day': 11, 'title': 'Abu Dhabi Day Trip', 'description': 'Full-day excursion to Abu Dhabi. Visit Sheikh Zayed Grand Mosque, Heritage Village, and Qasr Al Watan palace. Lunch at local restaurant. Return to Dubai.'},
                {'day': 12, 'title': 'Dubai - Free Day', 'description': 'Free day in Dubai for independent activities, shopping, or rest. Overnight in Dubai.'},
                {'day': 13, 'title': 'Dubai City Tour and Desert Safari', 'description': 'Morning city tour: Gold and Spice Souks, abra ride, Jumeirah area. Afternoon: Desert Safari in 4x4 with Bedouin camp activities and dinner with show.'},
                {'day': 14, 'title': 'Departure from Dubai', 'description': 'Check-out. Transfer to Dubai International Airport. End of services.'}
            ],
            'inclusions': [
                '3 nights in Cairo (5-star hotel)',
                '4 nights on 5-star Nile Cruise (full board)',
                '3 nights in Dubai (4-star hotel)',
                '2 domestic flights in Egypt',
                'Half board in Cairo',
                'Abu Dhabi tour with lunch',
                'Desert Safari with dinner',
                'English-speaking guides',
                'All entrance fees'
            ],
            'exclusions': [
                'International flights',
                'Cairo-Dubai flight',
                'Egypt and UAE visas',
                'Dubai Tourism Dirham Fee (~$5.5/night)',
                'Tips',
                'Travel insurance'
            ]
        },

        # 8. The Best of Luxor and Aswan
        {
            'name': 'The Best of Luxor and Aswan',
            'short_description': '5 days discovering Southern Egypt\'s ancient wonders in Luxor, Edfu, Kom Ombo, and Aswan without a cruise.',
            'description': '''This is a journey to Southern Egypt to discover the best of Luxor and Aswan in 5 days.

This package includes visits to the ancient wonders of Egyptian culture located in the south of the country. It is a perfect option for those who prefer to stay in hotels instead of taking a Nile cruise, enjoying the tours in Luxor, Edfu, Kom Ombo, and Aswan with more freedom and comfort.

Unlike traditional cruise itineraries, here you stay in comfortable hotels on dry land, enjoying tours with more freedom, tranquility, and comfort.

Route: Luxor → Edfu → Kom Ombo → Aswan''',
            'category': 'Cultural & Historical',
            'tour_type': 'Multi-Day Package',
            'days': 5,
            'nights': 4,
            'price': 899,
            'is_featured': False,
            'is_best_seller': False,
            'destinations': ['Luxor', 'Aswan'],
            'highlights': [
                'Valley of the Kings',
                'Temple of Hatshepsut',
                'Karnak Temple',
                'Luxor Temple',
                'Edfu Temple',
                'Kom Ombo Temple',
                'Philae Temple',
                'Aswan High Dam',
                'Felucca ride on the Nile'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Luxor', 'description': 'Arrival in Luxor. Visit the West Bank: Valley of the Kings, Colossi of Memnon, and Temple of Hatshepsut. Transfer to hotel. In the afternoon, visit Luxor Temple. Dinner at hotel. Overnight in Luxor.'},
                {'day': 2, 'title': 'Karnak Temple', 'description': 'Breakfast. Visit the magnificent Karnak Temple, the largest religious complex of the ancient world. Free afternoon. Dinner at hotel. Overnight in Luxor.'},
                {'day': 3, 'title': 'Luxor to Aswan via Edfu and Kom Ombo', 'description': 'Breakfast and check-out. Drive to Edfu to visit the Temple of Horus. Continue to Kom Ombo to visit the dual temple. Continue to Aswan. Check-in at hotel. Dinner. Overnight in Aswan.'},
                {'day': 4, 'title': 'Aswan Sightseeing', 'description': 'Breakfast. Visit Philae Island with the Temple of Isis. Visit Aswan High Dam. Enjoy a Felucca ride on the Nile. Visit the Botanical Garden. Dinner at hotel. Overnight in Aswan.'},
                {'day': 5, 'title': 'Departure from Aswan', 'description': 'Breakfast. Optional: Abu Simbel excursion (by road or flight). Transfer to Aswan Airport. End of services.'}
            ],
            'inclusions': [
                '2 nights in Luxor (4 or 5-star hotel)',
                '2 nights in Aswan (4 or 5-star hotel)',
                'Half board (breakfast + dinner)',
                'English-speaking guide',
                'All entrance fees',
                'All transfers by air-conditioned vehicle',
                '1 bottle of water per person per day'
            ],
            'exclusions': [
                'Domestic flights (Cairo-Luxor, Aswan-Cairo)',
                'Egypt entry visa',
                'Abu Simbel tour',
                'Tutankhamun tomb entry',
                'Tips',
                'Travel insurance'
            ]
        },

        # 9. The Path of Moses
        {
            'name': 'The Path of Moses',
            'short_description': '7 days following in the footsteps of Moses through Egypt\'s sacred sites, Mount Sinai, and Red Sea beaches.',
            'description': '''A transformative journey that invites you to live an experience of faith and history, following in the footsteps of Moses in Egypt.

Discover sacred Christian sites, ascend the majestic Mount Sinai, explore the cultural riches of Cairo, and complete this spiritual and cultural journey with moments of rest and contemplation on the beautiful beaches of Sharm El Sheikh on the Red Sea.

This package is perfect for pilgrims, faith groups, and those seeking a spiritual experience in the Holy Land of Egypt.

Route: Cairo → Giza → Mount Sinai (St. Catherine) → Sharm El Sheikh → Cairo''',
            'category': 'Religious & Spiritual',
            'tour_type': 'Multi-Day Package',
            'days': 7,
            'nights': 6,
            'price': 1299,
            'is_featured': True,
            'is_best_seller': False,
            'destinations': ['Cairo', 'Mount Sinai', 'Sharm El Sheikh'],
            'highlights': [
                'Pyramids of Giza and Sphinx',
                'Coptic Cairo churches',
                'Holy Family Grotto',
                'Mount Sinai sunrise trek',
                'St. Catherine\'s Monastery',
                'Sharm El Sheikh beaches',
                'Red Sea relaxation'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo Airport. Reception and visa assistance. Transfer to hotel. Check-in and rest. Overnight in Cairo.'},
                {'day': 2, 'title': 'Pyramids and Coptic Cairo', 'description': 'Visit the Pyramids of Giza, Valley Temple, and Sphinx. Continue to Coptic Cairo: Hanging Church, Church of St. Sergius with Holy Family Grotto, and Ben Ezra Synagogue. Lunch at local restaurant. Overnight in Cairo.'},
                {'day': 3, 'title': 'Cairo to Mount Sinai', 'description': 'Breakfast and check-out. Overland journey to Mount Sinai region passing through the Suez Canal tunnel. Stop at the Fountains of Moses. Arrival at St. Catherine. Dinner and overnight at regional hotel.'},
                {'day': 4, 'title': 'Mount Sinai to Sharm El Sheikh', 'description': 'Early morning optional trek to Mount Sinai for sunrise (accompanied by Bedouin guide). Visit St. Catherine\'s Monastery. Transfer to Sharm El Sheikh. Check-in at resort on Soft All-Inclusive. Free time. Overnight in Sharm El Sheikh.'},
                {'day': 5, 'title': 'Sharm El Sheikh - Free Day', 'description': 'Free day to enjoy the resort and Red Sea beaches. All meals included. Overnight in Sharm El Sheikh.'},
                {'day': 6, 'title': 'Fly to Cairo', 'description': 'Breakfast and check-out. Transfer to Sharm El Sheikh Airport. Flight to Cairo (included). Transfer to hotel. Free afternoon. Overnight in Cairo.'},
                {'day': 7, 'title': 'Departure', 'description': 'Breakfast and check-out. Transfer to Cairo Airport. End of services.'}
            ],
            'inclusions': [
                '3 nights in Cairo (4-star hotel)',
                '1 night in Mount Sinai (regional hotel, half board)',
                '2 nights in Sharm El Sheikh (4-star resort, Soft All-Inclusive)',
                '1 domestic flight (Sharm-Cairo)',
                'Tours with English-speaking guide',
                'Entrance fees to Pyramids and St. Catherine',
                'All transfers'
            ],
            'exclusions': [
                'International flights',
                'Egypt entry visa',
                'Optional tours',
                'Mount Sinai trek guide fee',
                'Tips',
                'Travel insurance'
            ]
        },

        # 10. Three Cultural Pearls of Egypt
        {
            'name': 'Three Cultural Pearls of Egypt: Cairo, Alexandria and Luxor',
            'short_description': '9 days exploring Egypt\'s three golden capitals: Cairo, Alexandria, and Luxor with 2 domestic flights.',
            'description': '''Discover Egypt with the stunning "Three Golden Capitals" itinerary: a 9-day package through Cairo, Luxor, and Alexandria.

Embark on a unique journey with an English-speaking specialist guide and accommodation, exploring the wonders of the ancient millennial capitals: Cairo, Thebes (modern Luxor), and Alexandria.

This land-only itinerary is perfect for exploring freely, with included domestic flights ensuring comfort and maximum sightseeing time.

Route: Cairo → Alexandria → Luxor → Cairo''',
            'category': 'Cultural & Historical',
            'tour_type': 'Multi-Day Package',
            'days': 9,
            'nights': 8,
            'price': 1799,
            'is_featured': True,
            'is_best_seller': False,
            'destinations': ['Cairo', 'Alexandria', 'Luxor'],
            'highlights': [
                'Memphis and Saqqara',
                'Valley of the Kings',
                'Temple of Hatshepsut',
                'Karnak Temple',
                'Pyramids of Giza and Sphinx',
                'Egyptian Museum',
                'Alexandria\'s Library and Citadel',
                'Coptic and Islamic Cairo'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Arrival at Cairo International Airport. Reception and visa assistance. Transfer to hotel. Check-in and rest. Overnight in Cairo.'},
                {'day': 2, 'title': 'Memphis and Saqqara', 'description': 'Visit the open-air site of Memphis with the Colossus of Ramses II. Continue to Saqqara with the Step Pyramid of Djoser, Pyramid of Unas, and decorated mastabas. Visit Imhotep Museum. Lunch at local restaurant. Overnight in Cairo.'},
                {'day': 3, 'title': 'Fly to Luxor', 'description': 'Flight to Luxor. Visit the West Bank: Valley of the Kings (3 tombs), Temple of Hatshepsut, and Colossi of Memnon. Transfer to hotel. Visit Karnak Temple. Dinner at hotel. Overnight in Luxor.'},
                {'day': 4, 'title': 'Fly to Cairo', 'description': 'Breakfast and check-out. Optional: Hot air balloon ride over Luxor at sunrise. Transfer to Luxor Airport. Flight to Cairo. Transfer to hotel. Free afternoon. Overnight in Cairo.'},
                {'day': 5, 'title': 'Pyramids of Giza and Egyptian Museum', 'description': 'Visit the Giza Plateau with the Great Pyramids and Sphinx. Stop at Papyrus gallery. Lunch. Visit the Egyptian Museum in Tahrir Square. Overnight in Cairo.'},
                {'day': 6, 'title': 'Alexandria Day Trip', 'description': 'Full-day excursion to Alexandria. Visit the National Museum, Library of Alexandria, and Qaitbay Citadel (exterior). Lunch at local restaurant. Walk along Stanley Bridge. Return to Cairo.'},
                {'day': 7, 'title': 'Christian and Islamic Cairo', 'description': 'Visit Coptic Quarter with Hanging Church and St. Sergius Church. Continue to Islamic Cairo: Citadel of Saladin and Mohammed Ali Mosque. Visit Khan El-Khalili bazaar. Lunch. Overnight in Cairo.'},
                {'day': 8, 'title': 'Free Day in Cairo', 'description': 'Free day for independent activities, shopping, or rest. Optional: Visit National Museum of Egyptian Civilization (NMEC) with Royal Mummies. Overnight in Cairo.'},
                {'day': 9, 'title': 'Departure', 'description': 'Breakfast. Check-out. Transfer to Cairo International Airport. End of services.'}
            ],
            'inclusions': [
                '7 nights in Cairo (4-star hotel)',
                '1 night in Luxor (5-star hotel, with dinner)',
                '2 domestic flights (Cairo-Luxor, Luxor-Cairo)',
                'All tours with lunch included',
                'English-speaking guide',
                'All entrance fees',
                'All transfers'
            ],
            'exclusions': [
                'International flights',
                'Egypt entry visa',
                'Optional tours',
                'Tips',
                'Travel insurance'
            ]
        }
    ]

    created_count = 0
    for tour_data in tours_data:
        tour = create_tour(tour_data)
        if tour:
            created_count += 1

    print(f"\n=== Created {created_count} new tours ===\n")
    return created_count


if __name__ == '__main__':
    seed_tours()
