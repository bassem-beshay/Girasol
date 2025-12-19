"""
Seed Data Script for Girasol Egypt Tourism Platform
This script populates the database with realistic fake data for testing and development.
Run with: python seed_data.py
"""

import os
import sys
import django
from decimal import Decimal
from datetime import date, datetime, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

from apps.destinations.models import Destination, DestinationImage, Activity
from apps.tours.models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight,
    TourItinerary, TourInclusion, TourPricing, TourDeparture, TourFAQ
)
from apps.blog.models import Category as BlogCategory, Tag, Post, Comment
from apps.reviews.models import Review, Testimonial
from apps.contact.models import FAQ, Office, Newsletter, Inquiry
from apps.bookings.models import PromoCode

User = get_user_model()

print("=" * 60)
print("GIRASOL EGYPT - Database Seeder")
print("=" * 60)

# ============================================================
# DESTINATIONS DATA
# ============================================================
print("\n[1/7] Creating Destinations...")

destinations_data = [
    {
        "name": "Cairo",
        "name_ar": "القاهرة",
        "tagline": "The City of a Thousand Minarets",
        "description": """Cairo, the sprawling capital of Egypt, is a vibrant metropolis where ancient history meets modern life. Home to the iconic Pyramids of Giza and the Sphinx, Cairo offers visitors an unparalleled journey through time.

The city pulses with energy from its bustling bazaars, magnificent mosques, and world-class museums. The Egyptian Museum houses the world's most extensive collection of Pharaonic antiquities, including the treasures of Tutankhamun.

From the medieval Islamic architecture of Old Cairo to the modern skyscrapers along the Nile, Cairo presents a fascinating tapestry of cultures and eras. The Khan el-Khalili bazaar offers an authentic shopping experience, while the Nile corniche provides stunning sunset views.

Whether you're exploring ancient tombs, savoring traditional Egyptian cuisine, or experiencing the legendary Egyptian hospitality, Cairo promises an unforgettable adventure.""",
        "description_ar": "القاهرة، العاصمة المترامية الأطراف لمصر، هي مدينة نابضة بالحياة حيث يلتقي التاريخ القديم بالحياة الحديثة.",
        "country": "Egypt",
        "region": "Greater Cairo",
        "latitude": Decimal("30.0444"),
        "longitude": Decimal("31.2357"),
        "best_time_to_visit": "October to April offers the most pleasant weather. Winters are mild and perfect for sightseeing.",
        "getting_there": "Cairo International Airport (CAI) is the main gateway, served by major international airlines.",
        "climate_info": "Cairo has a hot desert climate. Summers are hot and dry (35-40°C), while winters are mild (10-20°C).",
        "is_featured": True,
        "is_active": True,
    },
    {
        "name": "Luxor",
        "name_ar": "الأقصر",
        "tagline": "The World's Greatest Open-Air Museum",
        "description": """Luxor, ancient Thebes, stands as one of the world's most remarkable archaeological sites. This city on the banks of the Nile was the glorious capital of Egypt during the New Kingdom.

The East Bank houses the magnificent Karnak Temple Complex, the largest religious building ever constructed, and the elegant Luxor Temple. The West Bank reveals the Valley of the Kings with 63 royal tombs, including Tutankhamun's famous tomb.

The Temple of Hatshepsut rises dramatically against limestone cliffs, while the Colossi of Memnon stand guard over the Theban necropolis. Luxor offers an intimate glimpse into the lives of pharaohs who lived over 3,000 years ago.""",
        "description_ar": "الأقصر، طيبة القديمة، تقف كواحدة من أبرز المواقع الأثرية في العالم.",
        "country": "Egypt",
        "region": "Upper Egypt",
        "latitude": Decimal("25.6872"),
        "longitude": Decimal("32.6396"),
        "best_time_to_visit": "October to April is ideal. Winter months offer comfortable temperatures for exploring outdoor sites.",
        "getting_there": "Luxor International Airport receives domestic and some international flights. Many visitors arrive by Nile cruise.",
        "climate_info": "Luxor has an extremely hot desert climate. Summers are scorching (40-45°C), while winters are warm (15-25°C).",
        "is_featured": True,
        "is_active": True,
    },
    {
        "name": "Aswan",
        "name_ar": "أسوان",
        "tagline": "Gateway to Nubia and Ancient Wonders",
        "description": """Aswan, Egypt's sunniest southern city, offers a more relaxed pace and stunning natural beauty. Set along the most picturesque stretch of the Nile, Aswan has been a frontier town since ancient times.

The city serves as the gateway to Nubian culture, with colorful villages and warm hospitality. Key attractions include the majestic Philae Temple dedicated to Isis, the Aswan High Dam, and the ancient granite quarries with the Unfinished Obelisk.

A short flight away lies Abu Simbel, where Ramesses II's colossal temples were relocated in a remarkable UNESCO rescue operation.""",
        "description_ar": "أسوان، أكثر مدن مصر الجنوبية إشراقاً، تقدم إيقاعاً أكثر استرخاءً وجمالاً طبيعياً مذهلاً.",
        "country": "Egypt",
        "region": "Upper Egypt",
        "latitude": Decimal("24.0889"),
        "longitude": Decimal("32.8998"),
        "best_time_to_visit": "November to March offers the best weather for visiting.",
        "getting_there": "Aswan International Airport has domestic flights from Cairo. Popular endpoint for Nile cruises.",
        "climate_info": "Aswan has one of the driest climates in the world. Summer temperatures reach 40-45°C, winters are warm (20-25°C).",
        "is_featured": True,
        "is_active": True,
    },
    {
        "name": "Alexandria",
        "name_ar": "الإسكندرية",
        "tagline": "The Pearl of the Mediterranean",
        "description": """Alexandria, founded by Alexander the Great in 331 BC, was once the intellectual capital of the ancient world. Today, Egypt's second-largest city retains its cosmopolitan character and Mediterranean charm.

The stunning Bibliotheca Alexandrina has revived the city's scholarly tradition. The Catacombs of Kom el-Shoqafa and the Citadel of Qaitbay offer glimpses into different historical periods.

Alexandria's corniche stretches for miles along the seafront, and the city is famous for its fresh seafood and nostalgic European atmosphere.""",
        "description_ar": "الإسكندرية، التي أسسها الإسكندر الأكبر عام 331 قبل الميلاد، كانت يوماً العاصمة الفكرية للعالم القديم.",
        "country": "Egypt",
        "region": "Mediterranean Coast",
        "latitude": Decimal("31.2001"),
        "longitude": Decimal("29.9187"),
        "best_time_to_visit": "May to October for beach weather, though the city is pleasant year-round.",
        "getting_there": "Borg El Arab International Airport serves Alexandria. Easy access from Cairo by train (2.5 hours).",
        "climate_info": "Mediterranean climate with mild, wet winters and hot, humid summers (25-30°C).",
        "is_featured": True,
        "is_active": True,
    },
    {
        "name": "Sharm El Sheikh",
        "name_ar": "شرم الشيخ",
        "tagline": "Red Sea Riviera Paradise",
        "description": """Sharm El Sheikh, at the southern tip of the Sinai Peninsula, is Egypt's premier beach resort destination. Known for world-class diving, stunning beaches, and year-round sunshine.

The Red Sea's crystal-clear waters offer incredible diving and snorkeling at Ras Mohammed National Park. Beyond beaches, visitors can explore the Sinai desert, climb Mount Sinai, or visit St. Catherine's Monastery.

Naama Bay is the vibrant heart of the resort with restaurants, shops, and nightlife.""",
        "description_ar": "شرم الشيخ، الواقعة في الطرف الجنوبي لشبه جزيرة سيناء، هي وجهة مصر الشاطئية الأولى.",
        "country": "Egypt",
        "region": "South Sinai",
        "latitude": Decimal("27.9158"),
        "longitude": Decimal("34.3300"),
        "best_time_to_visit": "Year-round destination. October to May offers perfect weather.",
        "getting_there": "Sharm El Sheikh International Airport receives flights from major European cities and Cairo.",
        "climate_info": "Hot desert climate moderated by sea breezes. Summer 35-40°C, winters mild 20-25°C.",
        "is_featured": True,
        "is_active": True,
    },
    {
        "name": "Hurghada",
        "name_ar": "الغردقة",
        "tagline": "Red Sea Adventure Hub",
        "description": """Hurghada stretches along 40 kilometers of Red Sea coastline, transformed from a fishing village into a popular beach destination. Perfect combination of beach relaxation, water sports, and easy access to ancient sites.

Giftun Islands National Park offers pristine beaches and vibrant reefs. The location makes it excellent for visiting Luxor on day trips. Desert safaris and dolphin watching are popular activities.

With consistent sunshine and warm waters, Hurghada appeals to families, couples, and adventure enthusiasts.""",
        "description_ar": "الغردقة، الممتدة على طول 40 كيلومتراً من ساحل البحر الأحمر، تحولت من قرية صيد صغيرة إلى واحدة من أشهر الوجهات الشاطئية.",
        "country": "Egypt",
        "region": "Red Sea",
        "latitude": Decimal("27.2579"),
        "longitude": Decimal("33.8116"),
        "best_time_to_visit": "Year-round. Spring and autumn are ideal. Summers hot but excellent for water activities.",
        "getting_there": "Hurghada International Airport has connections to major European cities and Cairo.",
        "climate_info": "Hot desert climate with abundant sunshine. Summer 35-40°C, winters mild 18-25°C.",
        "is_featured": False,
        "is_active": True,
    },
]

for dest_data in destinations_data:
    # Remove unsupported fields
    clean_data = {k: v for k, v in dest_data.items() if k not in ['name_ar']}
    dest, created = Destination.objects.update_or_create(
        slug=slugify(clean_data["name"]),
        defaults=clean_data
    )
    status = "Created" if created else "Updated"
    print(f"  {status}: {dest.name}")

    # Add Activities for each destination
    activities_data = {
        "Cairo": [
            {"name": "Pyramid Tour", "description": "Guided tour of the Giza Pyramids and Sphinx with expert Egyptologist.", "price_from": Decimal("45"), "price_to": Decimal("120"), "duration": "4-5 hours"},
            {"name": "Egyptian Museum Visit", "description": "Explore 5,000 years of Egyptian history including Tutankhamun's treasures.", "price_from": Decimal("30"), "price_to": Decimal("80"), "duration": "3-4 hours"},
            {"name": "Nile Dinner Cruise", "description": "Evening cruise with dinner, belly dancing, and traditional music.", "price_from": Decimal("50"), "price_to": Decimal("100"), "duration": "3 hours"},
            {"name": "Khan el-Khalili Shopping", "description": "Guided tour of Cairo's famous medieval bazaar.", "price_from": Decimal("25"), "price_to": Decimal("50"), "duration": "2-3 hours"},
            {"name": "Islamic Cairo Walking Tour", "description": "Explore medieval mosques, madrasas, and historic streets.", "price_from": Decimal("35"), "price_to": Decimal("70"), "duration": "3-4 hours"},
        ],
        "Luxor": [
            {"name": "Valley of the Kings", "description": "Visit the royal tombs including option for Tutankhamun's tomb.", "price_from": Decimal("40"), "price_to": Decimal("100"), "duration": "3-4 hours"},
            {"name": "Hot Air Balloon Ride", "description": "Sunrise balloon flight over the West Bank temples and tombs.", "price_from": Decimal("80"), "price_to": Decimal("150"), "duration": "1 hour flight"},
            {"name": "Karnak Temple Tour", "description": "Comprehensive tour of the largest ancient religious complex.", "price_from": Decimal("35"), "price_to": Decimal("75"), "duration": "2-3 hours"},
            {"name": "Felucca Sunset Sail", "description": "Traditional sailing boat trip on the Nile at sunset.", "price_from": Decimal("20"), "price_to": Decimal("40"), "duration": "1-2 hours"},
        ],
        "Aswan": [
            {"name": "Abu Simbel Excursion", "description": "Day trip to Ramesses II's magnificent rock temples.", "price_from": Decimal("80"), "price_to": Decimal("180"), "duration": "Full day"},
            {"name": "Philae Temple Visit", "description": "Boat ride to the island temple of the goddess Isis.", "price_from": Decimal("35"), "price_to": Decimal("70"), "duration": "2-3 hours"},
            {"name": "Nubian Village Visit", "description": "Experience Nubian culture, food, and hospitality.", "price_from": Decimal("30"), "price_to": Decimal("60"), "duration": "3-4 hours"},
            {"name": "Felucca to Elephantine", "description": "Sail to Elephantine Island and the Botanical Gardens.", "price_from": Decimal("25"), "price_to": Decimal("50"), "duration": "2-3 hours"},
        ],
        "Alexandria": [
            {"name": "Bibliotheca Tour", "description": "Guided tour of the modern Library of Alexandria.", "price_from": Decimal("20"), "price_to": Decimal("45"), "duration": "2 hours"},
            {"name": "Catacombs Exploration", "description": "Descend into the mysterious Roman-era burial chambers.", "price_from": Decimal("25"), "price_to": Decimal("50"), "duration": "1-2 hours"},
            {"name": "Seafood Dining Experience", "description": "Guided food tour of Alexandria's best seafood restaurants.", "price_from": Decimal("40"), "price_to": Decimal("80"), "duration": "3 hours"},
        ],
        "Sharm El Sheikh": [
            {"name": "Scuba Diving", "description": "Discover world-class reefs with certified instructors.", "price_from": Decimal("50"), "price_to": Decimal("120"), "duration": "Half day"},
            {"name": "Snorkeling Trip", "description": "Visit multiple snorkeling spots including Ras Mohammed.", "price_from": Decimal("35"), "price_to": Decimal("70"), "duration": "Full day"},
            {"name": "Mount Sinai Sunrise", "description": "Night trek to summit for spectacular sunrise views.", "price_from": Decimal("60"), "price_to": Decimal("100"), "duration": "Overnight"},
            {"name": "Quad Bike Safari", "description": "Desert adventure on quad bikes with Bedouin tea.", "price_from": Decimal("40"), "price_to": Decimal("80"), "duration": "3-4 hours"},
        ],
        "Hurghada": [
            {"name": "Giftun Island Trip", "description": "Full day at pristine beaches with snorkeling.", "price_from": Decimal("35"), "price_to": Decimal("70"), "duration": "Full day"},
            {"name": "Dolphin Watching", "description": "Boat trip to spot dolphins in their natural habitat.", "price_from": Decimal("45"), "price_to": Decimal("90"), "duration": "Half day"},
            {"name": "Desert Safari", "description": "Jeep safari with Bedouin dinner under the stars.", "price_from": Decimal("50"), "price_to": Decimal("100"), "duration": "Half day"},
            {"name": "Luxor Day Trip", "description": "Visit Valley of the Kings and Karnak from Hurghada.", "price_from": Decimal("80"), "price_to": Decimal("150"), "duration": "Full day"},
        ],
    }

    if dest.name in activities_data:
        for activity_data in activities_data[dest.name]:
            Activity.objects.update_or_create(
                destination=dest,
                name=activity_data["name"],
                defaults=activity_data
            )

print(f"  Total Destinations: {Destination.objects.count()}")

# ============================================================
# TOUR CATEGORIES
# ============================================================
print("\n[2/7] Creating Tour Categories...")

categories_data = [
    {"name": "Classic Egypt Tours", "name_ar": "جولات مصر الكلاسيكية", "description": "Traditional tours covering Egypt's most iconic sites.", "icon": "fas fa-landmark", "is_active": True},
    {"name": "Nile Cruises", "name_ar": "رحلات نيلية", "description": "Luxurious cruise experiences along the Nile River.", "icon": "fas fa-ship", "is_active": True},
    {"name": "Day Tours", "name_ar": "جولات يومية", "description": "Single-day excursions to major attractions.", "icon": "fas fa-sun", "is_active": True},
    {"name": "Beach & Diving", "name_ar": "شواطئ وغوص", "description": "Red Sea adventures including diving and snorkeling.", "icon": "fas fa-umbrella-beach", "is_active": True},
    {"name": "Desert Adventures", "name_ar": "مغامرات صحراوية", "description": "Safari trips, oasis visits, and desert camping.", "icon": "fas fa-campground", "is_active": True},
    {"name": "Luxury Tours", "name_ar": "جولات فاخرة", "description": "Premium experiences with 5-star accommodations.", "icon": "fas fa-crown", "is_active": True},
    {"name": "Family Tours", "name_ar": "جولات عائلية", "description": "Family-friendly itineraries with activities for all ages.", "icon": "fas fa-users", "is_active": True},
]

for cat_data in categories_data:
    clean_data = {k: v for k, v in cat_data.items() if k not in ['name_ar']}
    cat, created = TourCategory.objects.update_or_create(
        slug=slugify(clean_data["name"]),
        defaults=clean_data
    )
    print(f"  {'Created' if created else 'Updated'}: {cat.name}")

# ============================================================
# TOURS
# ============================================================
print("\n[3/7] Creating Tours...")

# Get destinations and categories
cairo = Destination.objects.get(slug="cairo")
luxor = Destination.objects.get(slug="luxor")
aswan = Destination.objects.get(slug="aswan")
alexandria = Destination.objects.get(slug="alexandria")
sharm = Destination.objects.get(slug="sharm-el-sheikh")
hurghada = Destination.objects.get(slug="hurghada")

classic_cat = TourCategory.objects.get(slug="classic-egypt-tours")
nile_cat = TourCategory.objects.get(slug="nile-cruises")
day_cat = TourCategory.objects.get(slug="day-tours")
beach_cat = TourCategory.objects.get(slug="beach-diving")
desert_cat = TourCategory.objects.get(slug="desert-adventures")
luxury_cat = TourCategory.objects.get(slug="luxury-tours")
family_cat = TourCategory.objects.get(slug="family-tours")

tours_data = [
    {
        "name": "Pyramids & Ancient Egypt Explorer",
        "name_ar": "مستكشف الأهرامات ومصر القديمة",
        "short_description": "Discover the wonders of ancient Egypt from Cairo to Luxor in this comprehensive 8-day journey.",
        "description": """Embark on an unforgettable 8-day journey through Egypt's most iconic ancient sites.

**Highlights:**
- Great Pyramids of Giza and the Sphinx
- Egyptian Museum with Tutankhamun's treasures
- Karnak and Luxor Temples
- Valley of the Kings
- Philae Temple in Aswan
- Optional Abu Simbel excursion

**What's Included:**
- Expert Egyptologist guides
- 4-star hotel accommodations
- All entrance fees
- Daily breakfast and select meals
- Air-conditioned transportation
- Domestic flights as per itinerary""",
        "category": classic_cat,
        "tour_type": "package",
        "days": 8,
        "nights": 7,
        "price": Decimal("1299.00"),
        "price_single_supplement": Decimal("350.00"),
        "child_price": Decimal("899.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 16,
        "is_featured": True,
        "is_best_seller": True,
        "has_discount": True,
        "discount_percentage": 15,
        "average_rating": Decimal("4.8"),
        "review_count": 127,
        "difficulty_level": "easy",
        "departure_city": "Cairo",
        "languages": "English, Spanish, German, French",
        "is_published": True,
        "destinations": [cairo, luxor, aswan],
    },
    {
        "name": "Luxury Nile Cruise Experience",
        "name_ar": "تجربة رحلة نيلية فاخرة",
        "short_description": "Sail in 5-star luxury along the Nile from Luxor to Aswan.",
        "description": """Experience the timeless beauty of the Nile aboard a luxurious 5-star cruise ship.

**Temples Along the Way:**
- Luxor Temple (evening visit)
- Karnak Temple Complex
- Edfu Temple (Temple of Horus)
- Kom Ombo Double Temple
- Philae Temple

**On Board:**
- Spacious cabins with Nile views
- Gourmet dining
- Swimming pool and spa
- Evening entertainment
- All meals included (full board)""",
        "category": nile_cat,
        "tour_type": "nile_cruise",
        "days": 5,
        "nights": 4,
        "price": Decimal("899.00"),
        "price_single_supplement": Decimal("250.00"),
        "child_price": Decimal("599.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 50,
        "is_featured": True,
        "is_best_seller": True,
        "has_discount": False,
        "average_rating": Decimal("4.9"),
        "review_count": 89,
        "difficulty_level": "easy",
        "departure_city": "Luxor",
        "languages": "English, German, French, Italian",
        "is_published": True,
        "destinations": [luxor, aswan],
    },
    {
        "name": "Cairo & Alexandria Discovery",
        "name_ar": "اكتشاف القاهرة والإسكندرية",
        "short_description": "Explore Egypt's two great cities - ancient Cairo and Mediterranean Alexandria.",
        "description": """Discover the contrasting wonders of Egypt's two greatest cities.

**Cairo Highlights:**
- Giza Pyramids and the Great Sphinx
- Egyptian Museum
- Khan el-Khalili bazaar
- Coptic Cairo
- Islamic Cairo mosques

**Alexandria Highlights:**
- Bibliotheca Alexandrina
- Catacombs of Kom el-Shoqafa
- Citadel of Qaitbay
- Pompey's Pillar
- Mediterranean seafood lunch""",
        "category": classic_cat,
        "tour_type": "package",
        "days": 5,
        "nights": 4,
        "price": Decimal("699.00"),
        "price_single_supplement": Decimal("200.00"),
        "child_price": Decimal("450.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 16,
        "is_featured": True,
        "is_best_seller": False,
        "has_discount": True,
        "discount_percentage": 10,
        "average_rating": Decimal("4.7"),
        "review_count": 64,
        "difficulty_level": "easy",
        "departure_city": "Cairo",
        "languages": "English, Spanish, French",
        "is_published": True,
        "destinations": [cairo, alexandria],
    },
    {
        "name": "Red Sea Diving Adventure",
        "name_ar": "مغامرة الغوص في البحر الأحمر",
        "short_description": "World-class diving in the Red Sea with stays in Sharm El Sheikh and Hurghada.",
        "description": """Explore the underwater wonders of the Red Sea on this 7-day diving adventure.

**Sharm El Sheikh (3 nights):**
- Ras Mohammed National Park
- Tiran Island reefs
- Night dive experience

**Hurghada (3 nights):**
- Giftun Islands snorkeling
- Abu Ramada reef diving
- Dolphin house visit

**Included:**
- 6 guided dive days (2 dives per day)
- All diving equipment
- PADI certified instructors
- Beach resort accommodations""",
        "category": beach_cat,
        "tour_type": "package",
        "days": 7,
        "nights": 6,
        "price": Decimal("999.00"),
        "price_single_supplement": Decimal("280.00"),
        "child_price": Decimal("699.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 12,
        "is_featured": True,
        "is_best_seller": False,
        "has_discount": False,
        "average_rating": Decimal("4.8"),
        "review_count": 52,
        "difficulty_level": "moderate",
        "departure_city": "Sharm El Sheikh",
        "languages": "English, German",
        "is_published": True,
        "destinations": [sharm, hurghada],
    },
    {
        "name": "Complete Egypt Grand Tour",
        "name_ar": "جولة مصر الكبرى الكاملة",
        "short_description": "The ultimate 14-day Egypt experience covering Cairo, Luxor, Aswan, and the Red Sea.",
        "description": """Experience the very best of Egypt on this comprehensive 14-day journey.

**Days 1-3: Cairo**
- Great Pyramids and Sphinx
- Egyptian Museum
- Islamic Cairo and Khan el-Khalili

**Days 4-7: Nile Cruise**
- Karnak and Luxor Temples
- Valley of the Kings
- Edfu and Kom Ombo Temples

**Days 8-9: Aswan**
- Abu Simbel excursion
- Philae Temple
- Nubian village visit

**Days 10-14: Hurghada**
- Beach relaxation
- Snorkeling trips
- Desert safari option""",
        "category": luxury_cat,
        "tour_type": "package",
        "days": 14,
        "nights": 13,
        "price": Decimal("2799.00"),
        "price_single_supplement": Decimal("650.00"),
        "child_price": Decimal("1899.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 16,
        "is_featured": True,
        "is_best_seller": True,
        "has_discount": True,
        "discount_percentage": 20,
        "average_rating": Decimal("4.9"),
        "review_count": 156,
        "difficulty_level": "easy",
        "departure_city": "Cairo",
        "languages": "English, Spanish, German, French, Italian",
        "is_published": True,
        "destinations": [cairo, luxor, aswan, hurghada],
    },
    {
        "name": "Pyramids of Giza Day Tour",
        "name_ar": "جولة يوم واحد لأهرامات الجيزة",
        "short_description": "Full-day tour of the Giza Pyramids, Sphinx, and Egyptian Museum.",
        "description": """Discover Cairo's ancient wonders on this comprehensive full-day tour.

**Morning - Giza Plateau:**
- Great Pyramid of Khufu
- Pyramid of Khafre
- Pyramid of Menkaure
- The Great Sphinx
- Valley Temple

**Lunch:** Egyptian restaurant with Pyramid views

**Afternoon - Egyptian Museum:**
- Tutankhamun's treasures
- Royal Mummy Hall (optional)
- Ancient artifacts

**Included:**
- Hotel pickup and drop-off
- Licensed Egyptologist guide
- Lunch
- All entrance fees""",
        "category": day_cat,
        "tour_type": "day_tour",
        "days": 1,
        "nights": 0,
        "price": Decimal("89.00"),
        "price_single_supplement": Decimal("0.00"),
        "child_price": Decimal("55.00"),
        "currency": "USD",
        "min_group_size": 1,
        "max_group_size": 15,
        "is_featured": False,
        "is_best_seller": True,
        "has_discount": False,
        "average_rating": Decimal("4.7"),
        "review_count": 234,
        "difficulty_level": "easy",
        "departure_city": "Cairo",
        "languages": "English, Spanish, German, French, Arabic",
        "is_published": True,
        "destinations": [cairo],
    },
    {
        "name": "Luxor West Bank Day Tour",
        "name_ar": "جولة يوم واحد للبر الغربي بالأقصر",
        "short_description": "Explore the Valley of the Kings, Temple of Hatshepsut, and Colossi of Memnon.",
        "description": """Journey to Luxor's West Bank, the ancient City of the Dead.

**Valley of the Kings:**
- Visit 3 royal tombs
- See intricate wall paintings
- Learn about mummification

**Temple of Hatshepsut:**
- Egypt's female pharaoh's mortuary temple
- Dramatic cliff-side architecture

**Colossi of Memnon:**
- Massive stone statues of Amenhotep III

**Included:**
- Hotel pickup and drop-off
- Expert Egyptologist guide
- Lunch
- Entrance fees (3 tombs)""",
        "category": day_cat,
        "tour_type": "day_tour",
        "days": 1,
        "nights": 0,
        "price": Decimal("75.00"),
        "price_single_supplement": Decimal("0.00"),
        "child_price": Decimal("45.00"),
        "currency": "USD",
        "min_group_size": 1,
        "max_group_size": 15,
        "is_featured": False,
        "is_best_seller": False,
        "has_discount": False,
        "average_rating": Decimal("4.8"),
        "review_count": 98,
        "difficulty_level": "easy",
        "departure_city": "Luxor",
        "languages": "English, German, French",
        "is_published": True,
        "destinations": [luxor],
    },
    {
        "name": "Abu Simbel Day Trip from Aswan",
        "name_ar": "رحلة يوم واحد لأبو سمبل من أسوان",
        "short_description": "Visit the magnificent rock temples of Ramesses II at Abu Simbel.",
        "description": """Journey to Abu Simbel, one of Egypt's most awe-inspiring monuments.

**The Great Temple:**
- Four colossal statues (20m high)
- Stunning interior reliefs
- Battle of Kadesh depictions

**Temple of Nefertari:**
- Dedicated to Ramesses' queen
- Beautiful goddess Hathor statues

**Travel Options:**
- By road (4:00 AM departure)
- By air (30-minute scenic flight)

**Included:**
- Transportation
- Egyptologist guide
- Entrance fees
- Bottled water""",
        "category": day_cat,
        "tour_type": "day_tour",
        "days": 1,
        "nights": 0,
        "price": Decimal("95.00"),
        "price_single_supplement": Decimal("0.00"),
        "child_price": Decimal("65.00"),
        "currency": "USD",
        "min_group_size": 1,
        "max_group_size": 20,
        "is_featured": False,
        "is_best_seller": False,
        "has_discount": True,
        "discount_percentage": 10,
        "average_rating": Decimal("4.9"),
        "review_count": 145,
        "difficulty_level": "easy",
        "departure_city": "Aswan",
        "languages": "English, German, French, Spanish",
        "is_published": True,
        "destinations": [aswan],
    },
    {
        "name": "Egypt Family Adventure",
        "name_ar": "مغامرة عائلية في مصر",
        "short_description": "A family-friendly 10-day adventure designed for travelers of all ages.",
        "description": """Create unforgettable family memories on this 10-day Egypt adventure.

**Cairo (Days 1-3):**
- Pyramids with camel rides
- Egyptian Museum treasure hunt
- Papyrus making workshop

**Nile Cruise (Days 4-7):**
- Pool time on cruise ship
- Hieroglyphic writing class
- Temple explorations

**Hurghada (Days 8-10):**
- Beach time and swimming
- Glass-bottom boat ride
- Dolphin watching

**Family-Friendly Features:**
- Specially trained guides
- Kid-friendly meals
- Connecting rooms available""",
        "category": family_cat,
        "tour_type": "package",
        "days": 10,
        "nights": 9,
        "price": Decimal("1599.00"),
        "price_single_supplement": Decimal("400.00"),
        "child_price": Decimal("999.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 20,
        "is_featured": True,
        "is_best_seller": False,
        "has_discount": True,
        "discount_percentage": 15,
        "average_rating": Decimal("4.8"),
        "review_count": 78,
        "difficulty_level": "easy",
        "departure_city": "Cairo",
        "languages": "English, German",
        "is_published": True,
        "destinations": [cairo, luxor, aswan, hurghada],
    },
    {
        "name": "Desert Safari & Oasis Adventure",
        "name_ar": "رحلة سفاري صحراوية وواحات",
        "short_description": "Explore Egypt's Western Desert, including the White Desert and Bahariya Oasis.",
        "description": """Venture into Egypt's spectacular Western Desert.

**Day 1: Cairo to Bahariya**
- Black Desert exploration
- Golden Mummies Museum
- Hot spring relaxation

**Day 2: White Desert**
- Crystal Mountain
- White Desert sunset
- Camp under the stars

**Day 3: Desert Exploration**
- Sunrise photography
- Mushroom rock formations
- Traditional Bedouin dinner

**Day 4: Return to Cairo**

**Included:**
- 4x4 jeep transportation
- Camping equipment
- All meals
- Desert guide""",
        "category": desert_cat,
        "tour_type": "package",
        "days": 4,
        "nights": 3,
        "price": Decimal("449.00"),
        "price_single_supplement": Decimal("100.00"),
        "child_price": Decimal("350.00"),
        "currency": "USD",
        "min_group_size": 2,
        "max_group_size": 12,
        "is_featured": False,
        "is_best_seller": False,
        "has_discount": False,
        "average_rating": Decimal("4.7"),
        "review_count": 45,
        "difficulty_level": "moderate",
        "departure_city": "Cairo",
        "languages": "English",
        "is_published": True,
        "destinations": [cairo],
    },
]

for tour_data in tours_data:
    destinations = tour_data.pop("destinations")
    clean_data = {k: v for k, v in tour_data.items() if k not in ['name_ar']}
    tour, created = Tour.objects.update_or_create(
        slug=slugify(clean_data["name"]),
        defaults=clean_data
    )
    tour.destinations.set(destinations)
    print(f"  {'Created' if created else 'Updated'}: {tour.name}")

    # Add Inclusions
    inclusions = [
        ("Professional Egyptologist guide", True),
        ("All entrance fees", True),
        ("Air-conditioned transportation", True),
        ("Hotel accommodations", True),
        ("Meals as per itinerary", True),
        ("Airport transfers", True),
        ("International flights", False),
        ("Personal expenses", False),
        ("Travel insurance", False),
        ("Tips and gratuities", False),
    ]

    for item, is_included in inclusions:
        TourInclusion.objects.update_or_create(
            tour=tour,
            item=item,
            defaults={"is_included": is_included}
        )

    # Add Highlights
    highlights = [
        {"title": "Expert Guides", "description": "Licensed Egyptologist guides", "icon": "fas fa-user-graduate"},
        {"title": "Small Groups", "description": "Intimate group sizes", "icon": "fas fa-users"},
        {"title": "Quality Hotels", "description": "Hand-picked accommodations", "icon": "fas fa-hotel"},
    ]

    for i, highlight in enumerate(highlights):
        TourHighlight.objects.update_or_create(
            tour=tour,
            title=highlight["title"],
            defaults={**highlight, "sort_order": i}
        )

    # Add Departures
    base_date = date.today() + timedelta(days=30)
    for i in range(6):
        dep_date = base_date + timedelta(days=i*14)
        TourDeparture.objects.update_or_create(
            tour=tour,
            departure_date=dep_date,
            defaults={
                "return_date": dep_date + timedelta(days=tour.days - 1),
                "price": tour.price,
                "available_spots": random.randint(5, 15),
                "is_guaranteed": i < 3,
                "status": "available"
            }
        )

print(f"  Total Tours: {Tour.objects.count()}")

# ============================================================
# BLOG
# ============================================================
print("\n[4/7] Creating Blog Content...")

blog_categories_data = [
    {"name": "Travel Tips", "name_ar": "نصائح السفر", "description": "Practical advice for traveling in Egypt"},
    {"name": "Egyptian History", "name_ar": "التاريخ المصري", "description": "Deep dives into Egypt's fascinating past"},
    {"name": "Culture & Food", "name_ar": "الثقافة والطعام", "description": "Egyptian traditions and cuisine"},
    {"name": "Destinations", "name_ar": "الوجهات", "description": "Guides to Egypt's best places"},
]

for cat_data in blog_categories_data:
    clean_data = {k: v for k, v in cat_data.items() if k not in ['name_ar']}
    cat, created = BlogCategory.objects.update_or_create(
        slug=slugify(clean_data["name"]),
        defaults={**clean_data, "is_active": True}
    )
    print(f"  {'Created' if created else 'Updated'} Category: {cat.name}")

# Tags
tags_list = ["pyramids", "luxor", "cairo", "nile", "diving", "desert", "food", "culture", "history", "tips"]
for tag_name in tags_list:
    Tag.objects.update_or_create(slug=slugify(tag_name), defaults={"name": tag_name.title()})

# Blog Posts
travel_tips_cat = BlogCategory.objects.get(slug="travel-tips")
history_cat = BlogCategory.objects.get(slug="egyptian-history")
culture_cat = BlogCategory.objects.get(slug="culture-food")
destinations_cat = BlogCategory.objects.get(slug="destinations")

posts_data = [
    {
        "title": "10 Essential Tips for Your First Trip to Egypt",
        "excerpt": "Planning your first Egyptian adventure? Here's everything you need to know.",
        "content": """Egypt is a destination like no other. Here are essential tips for your first visit:

## 1. Best Time to Visit
October to April offers the most pleasant weather for sightseeing.

## 2. Visa Requirements
Most nationalities can obtain a visa on arrival for $25 USD.

## 3. What to Pack
Comfortable, modest clothing, sun protection, and comfortable walking shoes.

## 4. Money Matters
ATMs are widely available. Keep small bills for tips.

## 5. Tipping Culture
Tipping (baksheesh) is expected. Keep small bills handy.

## 6. Stay Hydrated
Drink plenty of bottled water.

## 7. Bargaining
Expected in markets like Khan el-Khalili.

## 8. Photography
Ask permission before photographing people.

## 9. Safety
Egypt is generally safe for tourists.

## 10. Embrace the Experience
Egyptian hospitality is legendary!""",
        "category": travel_tips_cat,
        "author_name": "Ahmed Hassan",
        "is_featured": True,
        "is_published": True,
        "reading_time": 8,
        "view_count": 1523,
    },
    {
        "title": "The Mysteries of the Great Pyramid",
        "excerpt": "Explore the enduring mysteries of the Great Pyramid of Giza.",
        "content": """The Great Pyramid has fascinated humanity for over 4,500 years.

## Construction Facts
- Height: Originally 146.5 meters
- Blocks: About 2.3 million limestone blocks
- Construction time: Approximately 20 years

## The Mystery of Construction
How did ancient Egyptians move blocks weighing up to 80 tonnes?

## Hidden Chambers
Modern technology continues to reveal secrets, including a large void discovered in 2017.

## Precision Engineering
- Aligned to true north with only 0.05% error
- Base is level to within 2.1 centimeters

The Great Pyramid remains one of humanity's greatest achievements.""",
        "category": history_cat,
        "author_name": "Dr. Sarah Mitchell",
        "is_featured": True,
        "is_published": True,
        "reading_time": 12,
        "view_count": 2847,
    },
    {
        "title": "A Food Lover's Guide to Egyptian Cuisine",
        "excerpt": "Discover the delicious flavors of Egyptian cuisine.",
        "content": """Egyptian cuisine is a delicious blend of Mediterranean and Middle Eastern influences.

## Must-Try Dishes

### Koshari
Egypt's national dish - rice, lentils, macaroni, chickpeas, and crispy onions.

### Ful Medames
Slow-cooked fava beans - the traditional Egyptian breakfast.

### Ta'meya
Egyptian falafel made with fava beans.

### Molokhia
Green soup made from jute leaves.

## Sweet Treats

### Konafa
Shredded phyllo with cream or nuts in sweet syrup.

### Om Ali
Egyptian bread pudding with nuts and milk.

## Drinks
- Sahlab (warm, creamy drink)
- Karkade (hibiscus tea)
- Fresh sugarcane juice

Egyptian cuisine offers something for everyone!""",
        "category": culture_cat,
        "author_name": "Fatma Abdullah",
        "is_featured": False,
        "is_published": True,
        "reading_time": 10,
        "view_count": 1876,
    },
    {
        "title": "Complete Guide to Visiting Luxor",
        "excerpt": "Everything you need to know about exploring ancient Thebes.",
        "content": """Luxor contains more monuments than anywhere else in Egypt.

## East Bank Highlights

### Karnak Temple
The largest religious building ever constructed. Allow 3 hours.

### Luxor Temple
Beautiful when illuminated at night.

## West Bank Highlights

### Valley of the Kings
63 royal tombs. Standard ticket includes 3 tombs.

### Temple of Hatshepsut
Dramatic cliff-side mortuary temple.

### Colossi of Memnon
Massive statues of Amenhotep III.

## Getting Around
- Ferry across the Nile
- Taxi or private driver
- Bicycle on the West Bank

## Best Time to Visit
October to April for comfortable temperatures.

Luxor is truly extraordinary!""",
        "category": destinations_cat,
        "author_name": "Mohamed Ibrahim",
        "is_featured": True,
        "is_published": True,
        "reading_time": 15,
        "view_count": 3241,
    },
    {
        "title": "Diving the Red Sea: A Complete Guide",
        "excerpt": "The Red Sea offers world-class diving for all levels.",
        "content": """The Red Sea is ranked among the world's top diving destinations.

## Why the Red Sea?
- Visibility often exceeds 30 meters
- Water temperature 21-28°C year-round
- Over 1,200 fish species

## Best Diving Spots

### Sharm El Sheikh
- Ras Mohammed National Park
- Tiran Island reefs
- SS Thistlegorm wreck

### Hurghada
- Giftun Islands
- Abu Ramada
- El Fanadir

## What You'll See
- Colorful coral gardens
- Tropical fish
- Sea turtles
- Dolphins
- Reef sharks

## Getting Certified
PADI Open Water courses available (3-4 days).

The underwater world here is truly magical!""",
        "category": destinations_cat,
        "author_name": "Klaus Werner",
        "is_featured": False,
        "is_published": True,
        "reading_time": 12,
        "view_count": 1654,
    },
]

for post_data in posts_data:
    post, created = Post.objects.update_or_create(
        slug=slugify(post_data["title"][:50]),
        defaults={**post_data, "published_at": timezone.now() - timedelta(days=random.randint(1, 60))}
    )
    post.tags.set(Tag.objects.order_by('?')[:4])
    print(f"  {'Created' if created else 'Updated'}: {post.title[:40]}...")

print(f"  Total Posts: {Post.objects.count()}")

# ============================================================
# REVIEWS & TESTIMONIALS
# ============================================================
print("\n[5/7] Creating Reviews & Testimonials...")

testimonials_data = [
    {"name": "Maria Garcia", "country": "Spain", "quote": "Our trip to Egypt with Girasol was absolutely magical! Our guide Ahmed was incredibly knowledgeable. We'll definitely be back!", "rating": 5},
    {"name": "John & Sarah Thompson", "country": "United States", "quote": "Best vacation we've ever taken! From the pyramids at sunrise to the temples of Luxor, every moment was special.", "rating": 5},
    {"name": "Hans Mueller", "country": "Germany", "quote": "Ich war sehr beeindruckt von der Professionalität. Die Tour war perfekt organisiert. Highly recommended!", "rating": 5},
    {"name": "Yuki Tanaka", "country": "Japan", "quote": "Beautiful experience from start to finish. The guides were excellent and very knowledgeable.", "rating": 5},
    {"name": "Sophie Laurent", "country": "France", "quote": "Une expérience inoubliable! The combination of ancient history and modern comfort was perfect.", "rating": 5},
    {"name": "Ahmed Al-Rashid", "country": "UAE", "quote": "Excellent service! I appreciated the cultural sensitivity and Arabic-speaking guides.", "rating": 5},
    {"name": "Emma Wilson", "country": "Australia", "quote": "We traveled all the way from Sydney and it was worth every hour! The Red Sea diving was world-class.", "rating": 5},
    {"name": "Roberto Rossi", "country": "Italy", "quote": "Servizio eccellente! The food, the history, the hospitality - everything was bellissimo!", "rating": 5},
    {"name": "Chen Wei", "country": "China", "quote": "我们全家都非常满意这次旅行。组织得很好。The Chinese-speaking guide was greatly appreciated.", "rating": 5},
    {"name": "Anna Kowalski", "country": "Poland", "quote": "The hot air balloon ride over Luxor was the highlight - absolutely breathtaking!", "rating": 5},
]

tours = list(Tour.objects.filter(is_published=True))
for i, test_data in enumerate(testimonials_data):
    test, created = Testimonial.objects.update_or_create(
        name=test_data["name"],
        defaults={
            **test_data,
            "tour": random.choice(tours) if tours else None,
            "is_active": True,
            "sort_order": i
        }
    )
    print(f"  {'Created' if created else 'Updated'}: Testimonial from {test.name}")

print(f"  Total Testimonials: {Testimonial.objects.count()}")

# ============================================================
# FAQS & CONTACT
# ============================================================
print("\n[6/7] Creating FAQs & Contact Info...")

faqs_data = [
    {"category": "booking", "question": "How do I book a tour?", "answer": "You can book directly through our website or contact us via email or phone."},
    {"category": "booking", "question": "What payment methods do you accept?", "answer": "We accept Visa, MasterCard, American Express, PayPal, and bank transfers."},
    {"category": "booking", "question": "What is your cancellation policy?", "answer": "Free cancellation up to 30 days before departure. 50% refund 15-29 days. No refund within 14 days."},
    {"category": "travel", "question": "Do I need a visa to visit Egypt?", "answer": "Most nationalities can obtain a visa on arrival ($25 USD) or apply for an e-visa online."},
    {"category": "travel", "question": "What should I pack for Egypt?", "answer": "Comfortable, modest clothing, sun protection, and comfortable walking shoes."},
    {"category": "travel", "question": "Is Egypt safe for tourists?", "answer": "Egypt is generally very safe for tourists. Tourist areas are well-policed."},
    {"category": "tours", "question": "What is included in tour prices?", "answer": "Accommodations, transportation, entrance fees, guides, and meals as specified."},
    {"category": "tours", "question": "Can tours be customized?", "answer": "Absolutely! We specialize in tailor-made tours. Contact us with your preferences."},
    {"category": "tours", "question": "What languages do your guides speak?", "answer": "English, Spanish, German, French, Italian, Arabic, and Chinese."},
    {"category": "general", "question": "What is the best time to visit Egypt?", "answer": "October to April for comfortable sightseeing weather."},
]

for i, faq_data in enumerate(faqs_data):
    faq, created = FAQ.objects.update_or_create(
        question=faq_data["question"],
        defaults={**faq_data, "is_active": True, "sort_order": i}
    )
    print(f"  {'Created' if created else 'Updated'}: FAQ")

# Office
office_data = {
    "name": "Girasol Egypt Headquarters",
    "city": "Cairo",
    "address": "Panorama Pyramids Tower, Al Haram, Giza, Egypt",
    "phone": "+20 2 3771 5511",
    "email": "info@girasolegypt.com",
    "whatsapp": "+20 100 123 4567",
    "latitude": Decimal("29.9773"),
    "longitude": Decimal("31.1325"),
    "working_hours": "Sun-Thu: 9AM-6PM, Fri-Sat: 10AM-4PM",
    "is_headquarters": True,
    "is_active": True,
}

office, created = Office.objects.update_or_create(
    name=office_data["name"],
    defaults=office_data
)
print(f"  {'Created' if created else 'Updated'}: Office")

print(f"  Total FAQs: {FAQ.objects.count()}")

# ============================================================
# PROMO CODES & ADDONS
# ============================================================
print("\n[7/7] Creating Promo Codes & Add-ons...")

promo_codes = [
    {"code": "WELCOME10", "description": "10% off for new customers", "discount_type": "percentage", "discount_value": Decimal("10"), "valid_from": timezone.now(), "valid_until": timezone.now() + timedelta(days=365), "is_active": True},
    {"code": "SUMMER2025", "description": "Summer special - $100 off", "discount_type": "fixed", "discount_value": Decimal("100"), "minimum_order": Decimal("500"), "valid_from": timezone.now(), "valid_until": timezone.now() + timedelta(days=180), "is_active": True},
    {"code": "FAMILY15", "description": "15% off family tours", "discount_type": "percentage", "discount_value": Decimal("15"), "valid_from": timezone.now(), "valid_until": timezone.now() + timedelta(days=365), "is_active": True},
]

for promo_data in promo_codes:
    promo, created = PromoCode.objects.update_or_create(
        code=promo_data["code"],
        defaults=promo_data
    )
    print(f"  {'Created' if created else 'Updated'}: Promo Code - {promo.code}")


# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("DATABASE SEEDING COMPLETE!")
print("=" * 60)
print(f"""
Summary:
- Destinations: {Destination.objects.count()}
- Tour Categories: {TourCategory.objects.count()}
- Tours: {Tour.objects.count()}
- Blog Categories: {BlogCategory.objects.count()}
- Blog Posts: {Post.objects.count()}
- Testimonials: {Testimonial.objects.count()}
- FAQs: {FAQ.objects.count()}
- Promo Codes: {PromoCode.objects.count()}

Your Girasol Egypt database is now populated!
""")
