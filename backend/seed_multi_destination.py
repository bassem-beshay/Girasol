"""
Seed script for Multi-Destination Tours (Egypt & Jordan, Egypt & Dubai)
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.destinations.models import Destination
from apps.tours.models import Tour, TourCategory, TourHighlight, TourItinerary, TourInclusion
from decimal import Decimal

def create_destinations():
    """Create Jordan and Dubai destinations"""

    # Jordan
    jordan, created = Destination.objects.get_or_create(
        slug='jordan',
        defaults={
            'name': 'Jordan',
            'name_es': 'Jordania',
            'name_pt': 'Jordânia',
            'country': 'Jordan',
            'region': 'Middle East',
            'tagline': 'Discover Petra & the Dead Sea',
            'description': '''Jordan is a land of ancient wonders and natural beauty. Home to the legendary city of Petra,
one of the New Seven Wonders of the World, Jordan offers an unforgettable journey through history.
Float in the Dead Sea, explore the desert landscapes of Wadi Rum, and experience warm Bedouin hospitality.''',
            'best_time_to_visit': 'March to May, September to November',
            'climate_info': 'Mediterranean climate with hot, dry summers and cool, wet winters.',
            'getting_there': 'Queen Alia International Airport in Amman is the main gateway.',
            'is_featured': True,
            'is_active': True,
            'sort_order': 10,
        }
    )
    print(f"{'Created' if created else 'Found'} destination: Jordan")

    # Dubai
    dubai, created = Destination.objects.get_or_create(
        slug='dubai',
        defaults={
            'name': 'Dubai',
            'name_es': 'Dubái',
            'name_pt': 'Dubai',
            'country': 'UAE',
            'region': 'Middle East',
            'tagline': 'Where Future Meets Tradition',
            'description': '''Dubai is a dazzling metropolis that seamlessly blends ultra-modern architecture with rich Arabian heritage.
Experience the world's tallest building, luxury shopping, desert safaris, and pristine beaches.
From the historic Al Fahidi district to the futuristic Palm Jumeirah, Dubai offers endless adventures.''',
            'best_time_to_visit': 'November to March',
            'climate_info': 'Desert climate with very hot summers and warm winters.',
            'getting_there': 'Dubai International Airport is one of the busiest in the world with connections to everywhere.',
            'is_featured': True,
            'is_active': True,
            'sort_order': 11,
        }
    )
    print(f"{'Created' if created else 'Found'} destination: Dubai")

    return jordan, dubai


def create_egypt_jordan_tour(jordan_dest):
    """Create Egypt & Jordan multi-destination tour"""

    # Get Egypt destinations
    cairo = Destination.objects.filter(slug='cairo').first()
    luxor = Destination.objects.filter(slug='luxor').first()

    # Get or create category
    category, _ = TourCategory.objects.get_or_create(
        slug='multi-country',
        defaults={
            'name': 'Multi-Country Tours',
            'name_es': 'Tours Multi-País',
            'name_pt': 'Tours Multi-País',
            'description': 'Explore multiple countries in one amazing journey',
            'is_active': True,
            'sort_order': 1,
        }
    )

    tour, created = Tour.objects.get_or_create(
        slug='egypt-jordan-discovery',
        defaults={
            'name': 'Egypt & Jordan Discovery',
            'name_es': 'Descubrimiento de Egipto y Jordania',
            'name_pt': 'Descoberta do Egito e Jordânia',
            'short_description': 'Experience the best of two ancient civilizations - Pyramids of Giza and the legendary Petra',
            'description': '''Embark on an extraordinary 10-day journey through two of the world's most fascinating destinations.

This carefully crafted tour combines the ancient wonders of Egypt with the rose-red city of Petra in Jordan.
Begin in Cairo, where you'll marvel at the Great Pyramids and the Sphinx, explore the treasures of the Egyptian Museum,
and wander through the vibrant Khan El Khalili bazaar.

Continue to Luxor, the world's greatest open-air museum, where you'll discover the Valley of the Kings,
Karnak Temple, and the majestic Luxor Temple.

Then fly to Amman, Jordan's capital, before heading to the UNESCO World Heritage site of Petra.
Walk through the Siq canyon to witness the iconic Treasury, explore ancient tombs and temples,
and experience the magic of Petra by night.

End your journey floating in the Dead Sea, the lowest point on Earth, before returning home with memories to last a lifetime.''',
            'category': category,
            'days': 10,
            'nights': 9,
            'price': Decimal('2499.00'),
            'currency': 'USD',
            'min_group_size': 2,
            'max_group_size': 16,
            'departure_city': 'Cairo',
            'is_published': True,
            'is_featured': True,
            'is_multi_destination': True,
            'difficulty_level': 'moderate',
            'languages': 'English, Arabic',
            'average_rating': Decimal('4.9'),
            'review_count': 47,
        }
    )

    if created:
        # Add destinations
        if cairo:
            tour.destinations.add(cairo)
        if luxor:
            tour.destinations.add(luxor)
        tour.destinations.add(jordan_dest)

        # Add highlights
        highlights = [
            ('Pyramids of Giza', 'Marvel at the last surviving wonder of the ancient world', 'pyramid'),
            ('Petra by Night', 'Experience the Treasury illuminated by thousands of candles', 'moon'),
            ('Valley of the Kings', 'Explore the tombs of ancient pharaohs', 'crown'),
            ('Dead Sea Float', 'Float effortlessly in the lowest point on Earth', 'waves'),
            ('Wadi Rum Desert', 'Optional jeep safari in the Martian-like landscape', 'mountain'),
        ]
        for i, (title, desc, icon) in enumerate(highlights):
            TourHighlight.objects.create(tour=tour, title=title, description=desc, icon=icon, sort_order=i)

        # Add itinerary
        itinerary = [
            (1, 'Arrival in Cairo', 'Welcome to Egypt! Transfer to your hotel and evening orientation.', 'Cairo', '', 'Cairo 5-star hotel'),
            (2, 'Pyramids & Sphinx', 'Full day exploring Giza Pyramids, Sphinx, and Egyptian Museum.', 'Giza, Cairo', 'Breakfast, Lunch', 'Cairo 5-star hotel'),
            (3, 'Cairo to Luxor', 'Fly to Luxor. Visit Karnak Temple and Luxor Temple.', 'Luxor', 'Breakfast, Dinner', 'Luxor 5-star hotel'),
            (4, 'Valley of the Kings', 'West Bank tour: Valley of Kings, Hatshepsut Temple, Colossi of Memnon.', 'Luxor West Bank', 'Breakfast, Lunch', 'Luxor 5-star hotel'),
            (5, 'Fly to Amman', 'Morning flight to Amman, Jordan. City tour and welcome dinner.', 'Amman', 'Breakfast, Dinner', 'Amman 5-star hotel'),
            (6, 'Petra Full Day', 'Full day exploring the ancient city of Petra. Walk through the Siq to the Treasury.', 'Petra', 'Breakfast, Lunch', 'Petra hotel'),
            (7, 'Petra & Little Petra', 'Morning in Petra, afternoon visit to Little Petra. Optional Petra by Night.', 'Petra', 'Breakfast', 'Petra hotel'),
            (8, 'Wadi Rum', 'Drive to Wadi Rum for desert jeep safari. Bedouin camp experience.', 'Wadi Rum', 'Breakfast, Dinner', 'Wadi Rum camp'),
            (9, 'Dead Sea', 'Drive to Dead Sea. Afternoon floating and spa treatments.', 'Dead Sea', 'Breakfast, Lunch', 'Dead Sea resort'),
            (10, 'Departure', 'Transfer to Amman airport for departure.', 'Amman', 'Breakfast', ''),
        ]
        for day, title, desc, locations, meals, accommodation in itinerary:
            TourItinerary.objects.create(
                tour=tour, day_number=day, title=title, description=desc,
                locations=locations, meals_included=meals, accommodation=accommodation, sort_order=day
            )

        # Add inclusions
        inclusions = [
            ('All international flights (Cairo-Luxor, Luxor-Amman)', True),
            ('9 nights accommodation in 5-star hotels', True),
            ('All transfers in air-conditioned vehicles', True),
            ('Professional English-speaking guides', True),
            ('All entrance fees to sites mentioned', True),
            ('Meals as specified (B=9, L=4, D=3)', True),
            ('Jordan visa assistance', True),
            ('Personal expenses', False),
            ('Travel insurance', False),
            ('Tips for guides and drivers', False),
        ]
        for i, (item, included) in enumerate(inclusions):
            TourInclusion.objects.create(tour=tour, item=item, is_included=included, sort_order=i)

    print(f"{'Created' if created else 'Found'} tour: Egypt & Jordan Discovery")
    return tour


def create_egypt_dubai_tour(dubai_dest):
    """Create Egypt & Dubai multi-destination tour"""

    # Get Egypt destinations
    cairo = Destination.objects.filter(slug='cairo').first()

    # Get or create category
    category = TourCategory.objects.filter(slug='multi-country').first()

    tour, created = Tour.objects.get_or_create(
        slug='egypt-dubai-luxury',
        defaults={
            'name': 'Egypt & Dubai Luxury Experience',
            'name_es': 'Experiencia de Lujo en Egipto y Dubái',
            'name_pt': 'Experiência de Luxo no Egito e Dubai',
            'short_description': 'From ancient Pyramids to futuristic skyscrapers - the ultimate luxury journey',
            'description': '''Experience the perfect blend of ancient wonders and modern marvels on this 8-day luxury journey.

Begin in Cairo, where 5,000 years of history await. Stand before the Great Pyramids of Giza,
gaze upon the golden mask of Tutankhamun, and sail the Nile at sunset. Experience Egyptian hospitality
at its finest in world-class hotels.

Then jet to Dubai, where the future has already arrived. Ascend the world's tallest building, Burj Khalifa,
shop in spectacular malls, and experience a desert safari under the stars. From traditional souks to
palm-shaped islands, Dubai offers luxury beyond imagination.

This tour combines the best of both worlds - ancient history and cutting-edge modernity -
all wrapped in 5-star comfort and personalized service.''',
            'category': category,
            'days': 8,
            'nights': 7,
            'price': Decimal('2899.00'),
            'currency': 'USD',
            'min_group_size': 2,
            'max_group_size': 12,
            'departure_city': 'Cairo',
            'is_published': True,
            'is_featured': True,
            'is_best_seller': True,
            'is_multi_destination': True,
            'difficulty_level': 'easy',
            'languages': 'English, Arabic',
            'average_rating': Decimal('4.8'),
            'review_count': 63,
        }
    )

    if created:
        # Add destinations
        if cairo:
            tour.destinations.add(cairo)
        tour.destinations.add(dubai_dest)

        # Add highlights
        highlights = [
            ('Pyramids of Giza', 'Private tour of the last ancient wonder', 'pyramid'),
            ('Burj Khalifa', 'Sunset views from the world\'s tallest building', 'building'),
            ('Nile Dinner Cruise', 'Elegant dinner sailing past illuminated Cairo', 'ship'),
            ('Desert Safari', 'Thrilling dune bashing and Bedouin BBQ', 'sun'),
            ('Dubai Mall & Fountain', 'World\'s largest mall and spectacular fountain show', 'shopping-bag'),
            ('Palm Jumeirah', 'Visit the iconic man-made island', 'palm-tree'),
        ]
        for i, (title, desc, icon) in enumerate(highlights):
            TourHighlight.objects.create(tour=tour, title=title, description=desc, icon=icon, sort_order=i)

        # Add itinerary
        itinerary = [
            (1, 'Arrival in Cairo', 'VIP airport meet & greet. Transfer to 5-star hotel. Welcome dinner.', 'Cairo', 'Dinner', 'Four Seasons Cairo'),
            (2, 'Pyramids & Museum', 'Private tour of Pyramids, Sphinx. Afternoon at Grand Egyptian Museum.', 'Giza, Cairo', 'Breakfast, Lunch', 'Four Seasons Cairo'),
            (3, 'Cairo Highlights', 'Old Cairo, Citadel, Khan El Khalili. Evening Nile dinner cruise.', 'Cairo', 'Breakfast, Dinner', 'Four Seasons Cairo'),
            (4, 'Fly to Dubai', 'Morning flight to Dubai. Afternoon Dubai Mall and Burj Khalifa sunset.', 'Dubai', 'Breakfast, Dinner', 'Atlantis The Palm'),
            (5, 'Dubai City Tour', 'Old Dubai, Gold Souk, Dubai Frame, Jumeirah Beach.', 'Dubai', 'Breakfast, Lunch', 'Atlantis The Palm'),
            (6, 'Desert Safari', 'Free morning. Afternoon desert safari with BBQ dinner.', 'Dubai Desert', 'Breakfast, Dinner', 'Atlantis The Palm'),
            (7, 'Abu Dhabi Day Trip', 'Visit Sheikh Zayed Mosque, Louvre Abu Dhabi, Corniche.', 'Abu Dhabi', 'Breakfast, Lunch', 'Atlantis The Palm'),
            (8, 'Departure', 'Leisure morning. Transfer to Dubai International Airport.', 'Dubai', 'Breakfast', ''),
        ]
        for day, title, desc, locations, meals, accommodation in itinerary:
            TourItinerary.objects.create(
                tour=tour, day_number=day, title=title, description=desc,
                locations=locations, meals_included=meals, accommodation=accommodation, sort_order=day
            )

        # Add inclusions
        inclusions = [
            ('Flight Cairo to Dubai', True),
            ('7 nights in 5-star luxury hotels', True),
            ('Private air-conditioned transportation', True),
            ('Private English-speaking guides', True),
            ('All entrance fees', True),
            ('Meals as specified', True),
            ('Burj Khalifa tickets (At the Top)', True),
            ('Desert safari with BBQ', True),
            ('Nile dinner cruise', True),
            ('UAE visa for eligible nationalities', True),
            ('International flights to Cairo/from Dubai', False),
            ('Personal expenses and shopping', False),
            ('Travel insurance', False),
            ('Tips and gratuities', False),
        ]
        for i, (item, included) in enumerate(inclusions):
            TourInclusion.objects.create(tour=tour, item=item, is_included=included, sort_order=i)

    print(f"{'Created' if created else 'Found'} tour: Egypt & Dubai Luxury Experience")
    return tour


def main():
    print("=" * 50)
    print("Creating Multi-Destination Tours Data")
    print("=" * 50)

    # Create destinations
    jordan, dubai = create_destinations()

    # Create tours
    egypt_jordan = create_egypt_jordan_tour(jordan)
    egypt_dubai = create_egypt_dubai_tour(dubai)

    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  - Destinations created/found: Jordan, Dubai")
    print(f"  - Tours created/found:")
    print(f"    1. Egypt & Jordan Discovery (10 days) - ${egypt_jordan.price}")
    print(f"    2. Egypt & Dubai Luxury Experience (8 days) - ${egypt_dubai.price}")
    print("=" * 50)

    # Verify
    multi_tours = Tour.objects.filter(is_multi_destination=True)
    print(f"\nTotal multi-destination tours: {multi_tours.count()}")


if __name__ == '__main__':
    main()
