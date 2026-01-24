#!/usr/bin/env python
"""
Script to add missing blog posts and tours from girasoltours.com
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.utils import timezone
from apps.blog.models import Post, Category, Tag
from apps.tours.models import Tour, TourCategory, TourType, TourItinerary, TourInclusion, TourHighlight
from apps.destinations.models import Destination


def get_or_create_blog_category(name):
    """Get or create a blog category."""
    category, created = Category.objects.get_or_create(
        name=name,
        defaults={
            'description': f'Articles about {name}',
            'is_active': True
        }
    )
    if created:
        print(f"  Created blog category: {name}")
    return category


def get_or_create_tour_category(name):
    """Get or create a tour category."""
    category, created = TourCategory.objects.get_or_create(
        name=name,
        defaults={
            'description': f'{name} tours',
            'is_active': True
        }
    )
    if created:
        print(f"  Created tour category: {name}")
    return category


def get_or_create_tour_type(name):
    """Get or create a tour type."""
    tour_type, created = TourType.objects.get_or_create(
        name=name,
        defaults={
            'description': f'{name} tours',
            'is_active': True
        }
    )
    if created:
        print(f"  Created tour type: {name}")
    return tour_type


def get_or_create_destination(name):
    """Get or create a destination."""
    destination, created = Destination.objects.get_or_create(
        name=name,
        defaults={
            'description': f'Explore the beauty of {name}',
            'is_active': True
        }
    )
    if created:
        print(f"  Created destination: {name}")
    return destination


def seed_missing_blog_posts():
    """Add missing blog posts from girasoltours.com."""
    print("\n=== Adding Missing Blog Posts ===\n")

    # Define the missing blog posts with full content
    missing_posts = [
        {
            'title': 'Dahab City and Resort',
            'title_es': 'Ciudad y Resort de Dahab',
            'title_pt': 'Cidade e Resort de Dahab',
            'category': 'Destinations',
            'excerpt': 'Dahab city is the best coastal city in South Sinai. You can expect excellent services of its resorts and hotels with stunning Red Sea views.',
            'excerpt_es': 'Dahab es la mejor ciudad costera del sur del Sinaí. Puedes esperar excelentes servicios de sus resorts y hoteles.',
            'excerpt_pt': 'Dahab é a melhor cidade costeira do Sul do Sinai. Você pode esperar excelentes serviços de seus resorts e hotéis.',
            'content': '''
<h2>Discover Dahab: The Jewel of South Sinai</h2>

<p>Dahab, meaning "gold" in Arabic, is one of Egypt's most beloved coastal destinations. Located on the southeast coast of the Sinai Peninsula, this former Bedouin fishing village has transformed into a world-renowned destination for diving, snorkeling, and relaxation.</p>

<h3>Why Visit Dahab?</h3>

<p><strong>World-Class Diving:</strong> Dahab is home to the famous Blue Hole, one of the most spectacular dive sites in the world. The coral reefs here are pristine and teeming with marine life.</p>

<p><strong>Laid-Back Atmosphere:</strong> Unlike the bustling resorts of Sharm El Sheikh, Dahab maintains a relaxed, bohemian vibe that attracts backpackers, yoga enthusiasts, and those seeking a more authentic experience.</p>

<p><strong>Adventure Activities:</strong> Beyond diving, Dahab offers excellent windsurfing and kitesurfing conditions, desert safaris, and camel treks into the Sinai mountains.</p>

<h3>Best Resorts in Dahab</h3>

<ul>
<li>Le Méridien Dahab Resort</li>
<li>Hilton Dahab Resort</li>
<li>Swiss Inn Resort Dahab</li>
<li>Tropitel Dahab Oasis</li>
</ul>

<h3>What to Do in Dahab</h3>

<ol>
<li>Dive or snorkel at the Blue Hole</li>
<li>Visit the Lighthouse beach</li>
<li>Take a desert safari to the Colored Canyon</li>
<li>Enjoy fresh seafood at waterfront restaurants</li>
<li>Experience a Bedouin dinner under the stars</li>
</ol>

<p>Whether you're an experienced diver or simply looking for a peaceful retreat by the sea, Dahab offers an unforgettable Egyptian experience.</p>
''',
            'reading_time': 5,
            'tags': ['Dahab', 'Diving', 'Beach', 'Sinai']
        },
        {
            'title': 'What to Buy and What to Shop in Egypt',
            'title_es': 'Qué Comprar en Egipto',
            'title_pt': 'O Que Comprar no Egito',
            'category': 'Travel Tips',
            'excerpt': 'A comprehensive guide to shopping in Egypt, from traditional souvenirs to unique handicrafts and precious items you should bring home.',
            'excerpt_es': 'Una guía completa para comprar en Egipto, desde recuerdos tradicionales hasta artesanías únicas.',
            'excerpt_pt': 'Um guia completo para compras no Egito, desde souvenirs tradicionais até artesanatos únicos.',
            'content': '''
<h2>The Ultimate Shopping Guide for Egypt</h2>

<p>Egypt offers a treasure trove of unique items that make perfect souvenirs and gifts. From ancient-inspired artifacts to traditional crafts, here's what you should look for during your Egyptian adventure.</p>

<h3>Traditional Souvenirs</h3>

<h4>1. Papyrus Art</h4>
<p>Authentic papyrus paintings depicting ancient Egyptian scenes are a classic souvenir. Be sure to buy from reputable shops to avoid banana leaf imitations.</p>

<h4>2. Alabaster Items</h4>
<p>Luxor is famous for its alabaster workshops. You can find beautiful vases, statues, and decorative items carved from this translucent stone.</p>

<h4>3. Cartouche Jewelry</h4>
<p>Have your name written in hieroglyphics on gold or silver jewelry. A personalized cartouche makes a meaningful keepsake.</p>

<h3>Textiles and Fabrics</h3>

<ul>
<li><strong>Egyptian Cotton:</strong> World-renowned for its quality, Egyptian cotton products like sheets, towels, and clothing are must-buys.</li>
<li><strong>Scarves and Shawls:</strong> Beautiful silk and cotton scarves in vibrant colors.</li>
<li><strong>Bedouin Rugs:</strong> Handwoven rugs and kilims with traditional patterns.</li>
</ul>

<h3>Spices and Food Items</h3>

<ul>
<li>Hibiscus tea (Karkade)</li>
<li>Egyptian spice blends (Dukkah)</li>
<li>Dates and dried fruits</li>
<li>Saffron and cumin</li>
</ul>

<h3>Where to Shop</h3>

<p><strong>Khan El Khalili, Cairo:</strong> The most famous bazaar in Egypt, perfect for souvenirs, jewelry, and spices.</p>

<p><strong>Aswan Souk:</strong> Known for spices, Nubian crafts, and colorful fabrics.</p>

<p><strong>Luxor's West Bank:</strong> Alabaster factories and antique shops.</p>

<h3>Bargaining Tips</h3>

<ol>
<li>Always start at half the asking price</li>
<li>Be friendly and patient</li>
<li>Walk away if the price isn't right - they often call you back</li>
<li>Compare prices at multiple shops before buying</li>
</ol>
''',
            'reading_time': 7,
            'tags': ['Shopping', 'Tips', 'Egypt']
        },
        {
            'title': 'Brief History of Cairo',
            'title_es': 'Breve Historia de El Cairo',
            'title_pt': 'Breve História do Cairo',
            'category': 'Egyptian History',
            'excerpt': 'Explore Cairo\'s fascinating origins from the ancient Egyptian era through the Greek period to the Roman conquest and beyond.',
            'excerpt_es': 'Explora los fascinantes orígenes de El Cairo desde la era del antiguo Egipto hasta la conquista romana.',
            'excerpt_pt': 'Explore as origens fascinantes do Cairo desde a era do antigo Egito até a conquista romana.',
            'content': '''
<h2>The Rich History of Cairo: City of a Thousand Minarets</h2>

<p>Cairo, the capital of Egypt, is one of the oldest and most historically significant cities in the world. Its history spans over 5,000 years, from ancient Memphis to the modern metropolis we see today.</p>

<h3>Ancient Origins</h3>

<p>The area around modern Cairo has been inhabited since ancient times. Memphis, the ancient capital of Egypt, was located just south of present-day Cairo. The famous pyramids of Giza, built during the Old Kingdom (2686-2181 BC), stand as eternal monuments to this ancient civilization.</p>

<h3>Greco-Roman Period</h3>

<p>After Alexander the Great conquered Egypt in 332 BC, the Ptolemaic dynasty established Greek rule. The city of Babylon, a Roman fortress in what is now Old Cairo, became an important military and commercial center.</p>

<p>When the Roman Empire conquered Egypt in 30 BC, Babylon continued to thrive. The remnants of this fortress can still be seen in the Coptic area of Cairo today.</p>

<h3>Islamic Cairo</h3>

<p>The Arab conquest of Egypt in 641 AD marked a turning point. General Amr ibn al-As founded Fustat, the first Islamic capital of Egypt. In 969 AD, the Fatimid dynasty established Al-Qahira (Cairo), meaning "The Victorious," which eventually gave the city its modern name.</p>

<h3>Medieval Cairo</h3>

<p>Under the Mamluks (1250-1517), Cairo became one of the largest and wealthiest cities in the world. Magnificent mosques, madrasas, and caravanserais were built during this golden age. The famous Al-Azhar University, one of the oldest in the world, was founded during this period.</p>

<h3>Modern Cairo</h3>

<p>Today, Cairo is Africa's largest city and the Arab world's cultural capital. It seamlessly blends ancient monuments with modern developments, making it a fascinating destination for travelers from around the world.</p>

<h3>Key Historical Sites</h3>

<ul>
<li>The Egyptian Museum</li>
<li>The Citadel of Saladin</li>
<li>Islamic Cairo and Al-Azhar Mosque</li>
<li>Coptic Cairo and the Hanging Church</li>
<li>Khan El Khalili Bazaar</li>
</ul>
''',
            'reading_time': 6,
            'tags': ['Cairo', 'History', 'Egypt']
        },
        {
            'title': 'National Park of Gabal Elba',
            'title_es': 'Parque Nacional de Gabal Elba',
            'title_pt': 'Parque Nacional de Gabal Elba',
            'category': 'Adventure',
            'excerpt': 'Located 250 km south of Marsa Alam in Egypt\'s Eastern Desert near the Sudan border, Gabal Elba is a unique biodiversity hotspot.',
            'excerpt_es': 'Ubicado a 250 km al sur de Marsa Alam, Gabal Elba es un punto de biodiversidad único.',
            'excerpt_pt': 'Localizado a 250 km ao sul de Marsa Alam, Gabal Elba é um hotspot de biodiversidade único.',
            'content': '''
<h2>Gabal Elba: Egypt's Hidden Natural Paradise</h2>

<p>The Gabal Elba National Park is one of Egypt's most remote and pristine wilderness areas. Located in the far southeastern corner of Egypt, near the border with Sudan, this protected area is a biodiversity hotspot unlike any other in the country.</p>

<h3>Location and Access</h3>

<p>Gabal Elba is situated approximately 250 km south of Marsa Alam in Egypt's Eastern Desert. Due to its sensitive location near the Sudanese border, <strong>visitors need special permission</strong> from Egyptian authorities to visit this area.</p>

<h3>Unique Ecosystem</h3>

<p>What makes Gabal Elba special is its unique microclimate. The mountain (1,435 meters high) captures moisture from Red Sea winds, creating conditions that support vegetation and wildlife found nowhere else in Egypt.</p>

<h4>Flora</h4>
<ul>
<li>Over 458 plant species</li>
<li>Many endemic species found only here</li>
<li>Dense vegetation including acacia forests</li>
<li>Mangrove ecosystems along the coast</li>
</ul>

<h4>Fauna</h4>
<ul>
<li>Rare Nubian ibex</li>
<li>Dorcas gazelles</li>
<li>Over 40 bird species</li>
<li>Various reptiles and insects</li>
</ul>

<h3>The Bisharin People</h3>

<p>The park is home to the Bisharin, a nomadic Beja tribe who have lived in this region for centuries. They maintain their traditional pastoral lifestyle, herding camels and goats across the rugged terrain.</p>

<h3>Visiting Gabal Elba</h3>

<p>Due to security considerations and conservation efforts, tourism is limited. Visitors must:</p>

<ol>
<li>Obtain special permits from Egyptian authorities</li>
<li>Travel with authorized guides</li>
<li>Follow strict environmental guidelines</li>
<li>Respect local Bisharin communities</li>
</ol>

<p>For adventurous travelers seeking truly off-the-beaten-path experiences, Gabal Elba represents one of Egypt's last frontiers.</p>
''',
            'reading_time': 5,
            'tags': ['Desert', 'Nature', 'Adventure']
        },
        {
            'title': 'Travel to Egypt During Ramadan',
            'title_es': 'Viajar a Egipto Durante el Ramadán',
            'title_pt': 'Viajar para o Egito Durante o Ramadã',
            'category': 'Travel Tips',
            'excerpt': 'Traveling to Egypt during Ramadan is a unique experience that offers insights into Egyptian culture and traditions.',
            'excerpt_es': 'Viajar a Egipto durante el Ramadán es una experiencia única que ofrece información sobre la cultura egipcia.',
            'excerpt_pt': 'Viajar para o Egito durante o Ramadã é uma experiência única que oferece insights sobre a cultura egípcia.',
            'content': '''
<h2>Experiencing Egypt During Ramadan</h2>

<p>Ramadan, the holy month of fasting for Muslims, transforms Egypt into a unique cultural experience. While some travelers might hesitate to visit during this time, those who do are rewarded with an authentic glimpse into Egyptian traditions and hospitality.</p>

<h3>What is Ramadan?</h3>

<p>Ramadan is the ninth month of the Islamic calendar when Muslims fast from dawn to sunset. It's a time of spiritual reflection, increased devotion, and community gatherings.</p>

<h3>What to Expect</h3>

<h4>Daytime</h4>
<ul>
<li>Some restaurants and cafes may be closed during daylight hours</li>
<li>Tourist sites remain open but may have modified hours</li>
<li>The pace of life slows down considerably</li>
<li>It's respectful to avoid eating or drinking in public</li>
</ul>

<h4>Evening (After Iftar)</h4>
<ul>
<li>Cities come alive after sunset</li>
<li>Streets are decorated with Ramadan lanterns (fanoos)</li>
<li>Special Ramadan tents serve traditional foods</li>
<li>Live music and entertainment in many areas</li>
</ul>

<h3>Benefits of Visiting During Ramadan</h3>

<ol>
<li><strong>Cultural Immersion:</strong> Experience Egyptian traditions at their most authentic</li>
<li><strong>Fewer Tourists:</strong> Major attractions are less crowded</li>
<li><strong>Festive Atmosphere:</strong> Evenings are magical with celebrations</li>
<li><strong>Hospitality:</strong> Egyptians are especially welcoming during this time</li>
<li><strong>Special Foods:</strong> Try traditional Ramadan dishes like konafa and qatayef</li>
</ol>

<h3>Tips for Travelers</h3>

<ul>
<li>Hotels and tourist restaurants typically remain open</li>
<li>Book tours in the morning or late afternoon</li>
<li>Join an Iftar dinner for an authentic experience</li>
<li>Be patient with modified schedules</li>
<li>Dress modestly out of respect</li>
</ul>

<h3>Eid al-Fitr</h3>

<p>If your visit coincides with Eid al-Fitr (the celebration marking the end of Ramadan), you'll experience Egypt at its most festive. Families gather, special meals are prepared, and a joyous atmosphere fills the country.</p>
''',
            'reading_time': 6,
            'tags': ['Tips', 'Egypt', 'Culture']
        },
        {
            'title': 'Sharm El Sheikh',
            'title_es': 'Sharm El Sheikh',
            'title_pt': 'Sharm El Sheikh',
            'category': 'Destinations',
            'excerpt': 'Sharm El Sheikh is a premier diving and snorkeling destination featuring crystal-clear waters displaying coral and colorful marine life.',
            'excerpt_es': 'Sharm El Sheikh es un destino de buceo con aguas cristalinas y colorida vida marina.',
            'excerpt_pt': 'Sharm El Sheikh é um destino de mergulho com águas cristalinas e vida marinha colorida.',
            'content': '''
<h2>Sharm El Sheikh: Egypt's Red Sea Paradise</h2>

<p>Sharm El Sheikh, often called the "City of Peace," is Egypt's premier resort destination on the southern tip of the Sinai Peninsula. With world-class diving, luxurious resorts, and stunning natural beauty, it's no wonder millions of visitors flock here each year.</p>

<h3>World-Class Diving and Snorkeling</h3>

<p>Sharm El Sheikh is consistently rated among the world's top diving destinations. The Red Sea's crystal-clear waters offer visibility of up to 30 meters, revealing:</p>

<ul>
<li>Over 250 species of coral</li>
<li>More than 1,000 species of fish</li>
<li>Famous dive sites like Ras Mohammed, Tiran Island, and the SS Thistlegorm wreck</li>
<li>Opportunities for beginners and advanced divers alike</li>
</ul>

<h3>Top Attractions</h3>

<h4>Ras Mohammed National Park</h4>
<p>Egypt's first national park, offering some of the best diving and snorkeling in the world with dramatic underwater walls and abundant marine life.</p>

<h4>Naama Bay</h4>
<p>The heart of Sharm El Sheikh's nightlife and shopping, with restaurants, cafes, and entertainment venues lining the promenade.</p>

<h4>Old Market (Sharm El Maya)</h4>
<p>A more traditional Egyptian experience with souvenirs, spices, and local crafts.</p>

<h3>Beyond the Beach</h3>

<ul>
<li><strong>Desert Safaris:</strong> Quad biking and camel rides into the Sinai desert</li>
<li><strong>Mount Sinai:</strong> Sunrise trek to the sacred mountain (2-hour drive)</li>
<li><strong>St. Catherine's Monastery:</strong> One of the oldest Christian monasteries in the world</li>
<li><strong>Colored Canyon:</strong> Stunning rock formations in the Sinai interior</li>
</ul>

<h3>Best Time to Visit</h3>

<p>Sharm El Sheikh enjoys year-round sunshine with over 300 sunny days per year. The best time for diving is spring (March-May) and autumn (September-November) when water temperatures are ideal and visibility is at its best.</p>

<h3>Luxury Resorts</h3>

<p>Sharm El Sheikh is home to some of Egypt's finest resorts, including Four Seasons, Ritz-Carlton, and many all-inclusive options perfect for families and couples alike.</p>
''',
            'reading_time': 6,
            'tags': ['Sharm El Sheikh', 'Diving', 'Beach']
        },
        {
            'title': 'Siwa Oasis',
            'title_es': 'Oasis de Siwa',
            'title_pt': 'Oásis de Siwa',
            'category': 'Destinations',
            'excerpt': 'Siwa Oasis is one of Egypt\'s most isolated and enchanting destinations, located in the Western Desert near the Libyan border.',
            'excerpt_es': 'El Oasis de Siwa es uno de los destinos más aislados y encantadores de Egipto.',
            'excerpt_pt': 'O Oásis de Siwa é um dos destinos mais isolados e encantadores do Egito.',
            'content': '''
<h2>Siwa Oasis: Egypt's Desert Paradise</h2>

<p>Hidden in Egypt's Western Desert, just 50 kilometers from the Libyan border, lies Siwa Oasis – one of the most isolated and magical places in Egypt. This ancient oasis has preserved its unique culture, language, and traditions for thousands of years.</p>

<h3>A Place Touched by History</h3>

<p>Siwa's history stretches back to at least the 10th millennium BC. Its most famous moment came in 331 BC when Alexander the Great made the arduous journey across the desert to consult the Oracle of Amun at Siwa. The oracle allegedly confirmed him as the son of Zeus-Amun, legitimizing his divine status.</p>

<h3>What to See and Do</h3>

<h4>Temple of the Oracle (Temple of Amun)</h4>
<p>The ancient temple where Alexander the Great received his famous prophecy. Though partially ruined, it remains an atmospheric site with stunning views.</p>

<h4>Shali Fortress</h4>
<p>The ruins of the 13th-century mud-brick fortress that was the heart of old Siwa. Climb to the top for panoramic views of the oasis.</p>

<h4>Cleopatra's Bath</h4>
<p>A natural spring pool where, according to legend, Cleopatra herself once swam. Today it's a popular spot for a refreshing dip.</p>

<h4>The Great Sand Sea</h4>
<p>Experience the endless dunes of the Sahara on a desert safari. Watch the sunset over the sand sea for an unforgettable experience.</p>

<h3>Siwan Culture</h3>

<p>The Siwans have their own distinct:</p>
<ul>
<li><strong>Language:</strong> Siwi, a Berber language unlike Arabic</li>
<li><strong>Architecture:</strong> Traditional kershef buildings made from salt and mud</li>
<li><strong>Crafts:</strong> Beautiful silver jewelry and embroidered garments</li>
<li><strong>Cuisine:</strong> Unique dishes featuring dates, olives, and local produce</li>
</ul>

<h3>Natural Hot Springs</h3>

<p>Siwa is famous for its therapeutic hot springs, including:</p>
<ul>
<li>Bir Wahed (hot spring in the desert)</li>
<li>Fatnas Island spring</li>
<li>Numerous springs throughout the oasis</li>
</ul>

<h3>Getting There</h3>

<p>Siwa is located about 560 km from Cairo (8-9 hours by bus) or 300 km from Marsa Matruh (4 hours). The journey is part of the adventure!</p>
''',
            'reading_time': 7,
            'tags': ['Desert', 'Siwa', 'Egypt']
        },
        {
            'title': 'Kharga Oasis',
            'title_es': 'Oasis de Kharga',
            'title_pt': 'Oásis de Kharga',
            'category': 'Destinations',
            'excerpt': 'El Kharga Oasis is one of the most charming sites in the world with a rich history and various temples built over centuries.',
            'excerpt_es': 'El Oasis de Kharga es uno de los sitios más encantadores del mundo con una rica historia.',
            'excerpt_pt': 'O Oásis de Kharga é um dos locais mais encantadores do mundo com uma história rica.',
            'content': '''
<h2>Kharga Oasis: The Southernmost Oasis of Egypt's Western Desert</h2>

<p>El Kharga, meaning "the outer" in Arabic, is the largest and most accessible of Egypt's five major oases. Located in the New Valley Governorate, this ancient oasis offers a fascinating journey through thousands of years of history.</p>

<h3>Historical Significance</h3>

<p>Kharga has been inhabited since the Stone Age and was an important stop on the "Forty Days Road" – the ancient trade route that connected sub-Saharan Africa with Egypt. The Romans, Persians, and various Egyptian dynasties all left their marks here.</p>

<h3>Key Attractions</h3>

<h4>Temple of Hibis</h4>
<p>The best-preserved temple in Egypt's oases, dating to the 6th century BC during the Persian period. Dedicated to Amun-Ra, it features beautiful reliefs and has remained remarkably intact.</p>

<h4>Necropolis of Bagawat</h4>
<p>One of the oldest and best-preserved Christian cemeteries in the world, with over 260 mud-brick chapels dating from the 3rd to 7th centuries AD. The painted frescoes inside are extraordinary.</p>

<h4>Temple of Nadura</h4>
<p>A Roman-era temple sitting atop a hill, offering panoramic views of the oasis and the surrounding desert.</p>

<h4>Qasr El Ghueita</h4>
<p>A fortress and temple complex 25 km south of Kharga town, dating to the 25th Dynasty and later periods.</p>

<h3>Modern Kharga</h3>

<p>Today, Kharga is the capital of the New Valley Governorate and a growing agricultural center. Despite modernization, it retains its oasis charm with:</p>

<ul>
<li>Palm groves and gardens</li>
<li>Traditional markets</li>
<li>Warm, welcoming locals</li>
<li>A slower pace of life</li>
</ul>

<h3>Getting There</h3>

<p>Kharga is the most accessible of Egypt's oases:</p>
<ul>
<li>232 km from Asyut via a good asphalt road</li>
<li>600 km from Cairo</li>
<li>Daily buses from Cairo and Asyut</li>
<li>A small airport with occasional flights</li>
</ul>

<h3>Best Time to Visit</h3>

<p>The best time to visit is from October to April when temperatures are pleasant. Summer months can be extremely hot with temperatures exceeding 45°C.</p>
''',
            'reading_time': 6,
            'tags': ['Desert', 'Egypt', 'History']
        },
        {
            'title': 'Khan El Khalili Bazaar',
            'title_es': 'Bazar Khan El Khalili',
            'title_pt': 'Bazar Khan El Khalili',
            'category': 'Culture & History',
            'excerpt': 'Khan El Khalili is a historic marketplace in Cairo\'s El-Hussin district near Al-Azhar Mosque, founded in 970 AD.',
            'excerpt_es': 'Khan El Khalili es un mercado histórico en el distrito El-Hussin de El Cairo.',
            'excerpt_pt': 'Khan El Khalili é um mercado histórico no distrito de El-Hussin do Cairo.',
            'content': '''
<h2>Khan El Khalili: Cairo's Historic Bazaar</h2>

<p>Khan El Khalili is one of the oldest and most famous bazaars in the Middle East. Located in the heart of Islamic Cairo, this labyrinthine marketplace has been a center of trade and commerce for over 600 years.</p>

<h3>History of the Khan</h3>

<p>The bazaar was established in 1382 by Emir Djaharks el-Khalili during the Mamluk era. However, the area's commercial significance dates back even further – to the founding of Cairo by the Fatimid dynasty in 970 AD.</p>

<p>Originally built as a caravanserai (travelers' inn) for merchants traveling along ancient trade routes, Khan El Khalili grew into the sprawling marketplace we see today, where generations of families have run their shops.</p>

<h3>What to Buy</h3>

<ul>
<li><strong>Gold and Silver Jewelry:</strong> The gold souk is famous for quality craftsmanship</li>
<li><strong>Spices:</strong> Aromatic spices and herbs of every variety</li>
<li><strong>Perfumes:</strong> Traditional Egyptian perfume oils</li>
<li><strong>Antiques:</strong> Genuine and reproduction antiques</li>
<li><strong>Textiles:</strong> Cotton, silk scarves, and traditional clothing</li>
<li><strong>Souvenirs:</strong> Papyrus, alabaster, and brass items</li>
<li><strong>Shisha Pipes:</strong> Decorative and functional hookahs</li>
</ul>

<h3>Must-Visit Spots</h3>

<h4>El Fishawi Café</h4>
<p>The oldest café in Cairo (established 1773), where Nobel Prize-winning author Naguib Mahfouz wrote many of his works. Open 24/7 for over 200 years!</p>

<h4>Al-Azhar Mosque</h4>
<p>One of the oldest mosques in Cairo and home to Al-Azhar University, the world's second-oldest continuously operating university.</p>

<h4>Al-Hussein Mosque</h4>
<p>A sacred site believed to contain the head of Hussein ibn Ali, the grandson of Prophet Muhammad.</p>

<h3>Tips for Visiting</h3>

<ol>
<li><strong>Bargain:</strong> Prices are never fixed – negotiating is expected and part of the experience</li>
<li><strong>Visit in the evening:</strong> The bazaar comes alive after sunset, especially during Ramadan</li>
<li><strong>Wear comfortable shoes:</strong> The narrow, winding alleys can be challenging to navigate</li>
<li><strong>Keep valuables secure:</strong> As in any crowded marketplace</li>
<li><strong>Take your time:</strong> Getting lost is half the fun!</li>
</ol>

<h3>Getting There</h3>

<p>Khan El Khalili is located in Islamic Cairo, easily accessible by taxi or Uber. The nearest metro station is Ataba or El-Hussin.</p>
''',
            'reading_time': 6,
            'tags': ['Cairo', 'Shopping', 'Culture']
        },
        {
            'title': 'Climate of Egypt',
            'title_es': 'Clima de Egipto',
            'title_pt': 'Clima do Egito',
            'category': 'Travel Tips',
            'excerpt': 'The climate of Egypt differs based on regions of Mediterranean, Deserts and Upper Egypt. Overall, it is moderate either winter or summer.',
            'excerpt_es': 'El clima de Egipto difiere según las regiones del Mediterráneo, los desiertos y el Alto Egipto.',
            'excerpt_pt': 'O clima do Egito difere com base nas regiões do Mediterrâneo, desertos e Alto Egito.',
            'content': '''
<h2>Understanding Egypt's Climate: A Traveler's Guide</h2>

<p>Egypt's climate varies significantly across its different regions, from the Mediterranean coast to the desert interior and the tropical south. Understanding these variations will help you plan the perfect trip.</p>

<h3>Climate Zones</h3>

<h4>1. Mediterranean Coast (Alexandria, Marsa Matruh)</h4>
<ul>
<li><strong>Winter (Dec-Feb):</strong> 12-18°C, occasional rain</li>
<li><strong>Summer (Jun-Aug):</strong> 25-30°C, humid but cooled by sea breezes</li>
<li>This is Egypt's wettest region, though still relatively dry by global standards</li>
</ul>

<h4>2. Cairo and the Nile Delta</h4>
<ul>
<li><strong>Winter:</strong> 10-20°C, cool mornings and evenings</li>
<li><strong>Summer:</strong> 28-35°C, hot and dry</li>
<li>Occasional rain in winter; virtually none in summer</li>
</ul>

<h4>3. Upper Egypt (Luxor, Aswan)</h4>
<ul>
<li><strong>Winter:</strong> 15-25°C, pleasant and dry</li>
<li><strong>Summer:</strong> 35-45°C, extremely hot</li>
<li>Almost no rainfall throughout the year</li>
</ul>

<h4>4. Western Desert (Siwa, Bahariya)</h4>
<ul>
<li><strong>Winter:</strong> Cold nights (can drop below 10°C), warm days</li>
<li><strong>Summer:</strong> Extremely hot (up to 50°C)</li>
<li>Large temperature swings between day and night</li>
</ul>

<h4>5. Red Sea Coast (Hurghada, Sharm El Sheikh)</h4>
<ul>
<li><strong>Winter:</strong> 18-25°C, warm and pleasant</li>
<li><strong>Summer:</strong> 30-40°C, hot but with sea breezes</li>
<li>Perfect for year-round beach holidays</li>
</ul>

<h3>Best Time to Visit</h3>

<table>
<tr><th>Region</th><th>Best Months</th></tr>
<tr><td>Cairo & Pyramids</td><td>October - April</td></tr>
<tr><td>Luxor & Aswan</td><td>October - March</td></tr>
<tr><td>Red Sea Resorts</td><td>Year-round (March-May, Sep-Nov ideal)</td></tr>
<tr><td>Western Desert</td><td>October - April</td></tr>
<tr><td>Mediterranean</td><td>May - October</td></tr>
</table>

<h3>What to Pack</h3>

<ul>
<li><strong>Year-round:</strong> Sunscreen, sunglasses, hat</li>
<li><strong>Summer:</strong> Light, loose clothing; modest dress for religious sites</li>
<li><strong>Winter:</strong> Layers, including a jacket for cool evenings</li>
<li><strong>Desert trips:</strong> Warm clothing for cold nights</li>
</ul>

<h3>Khamaseen Winds</h3>

<p>In spring (March-May), Egypt experiences the Khamaseen – hot, dry, dusty winds from the Sahara. These can cause sandstorms and reduce visibility. If you visit during this period, carry a scarf to cover your face if needed.</p>
''',
            'reading_time': 5,
            'tags': ['Tips', 'Egypt', 'Weather']
        }
    ]

    posts_created = 0

    for post_data in missing_posts:
        # Check if post already exists
        if Post.objects.filter(title=post_data['title']).exists():
            print(f"  Post already exists: {post_data['title']}")
            continue

        # Get or create category
        category = get_or_create_blog_category(post_data['category'])

        # Create post
        post = Post.objects.create(
            title=post_data['title'],
            title_es=post_data.get('title_es', ''),
            title_pt=post_data.get('title_pt', ''),
            excerpt=post_data['excerpt'],
            excerpt_es=post_data.get('excerpt_es', ''),
            excerpt_pt=post_data.get('excerpt_pt', ''),
            content=post_data['content'],
            category=category,
            reading_time=post_data.get('reading_time', 5),
            is_published=True,
            is_featured=False,
            published_at=timezone.now(),
            featured_image='blog/posts/default.jpg'
        )

        # Add tags
        for tag_name in post_data.get('tags', []):
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        posts_created += 1
        print(f"  Created post: {post_data['title']}")

    print(f"\nTotal blog posts created: {posts_created}")
    return posts_created


def seed_missing_tours():
    """Add missing tour packages from girasoltours.com."""
    print("\n=== Adding Missing Tour Packages ===\n")

    # Get or create destinations
    cairo = get_or_create_destination('Cairo')
    luxor = get_or_create_destination('Luxor')
    aswan = get_or_create_destination('Aswan')
    hurghada = get_or_create_destination('Hurghada')
    sharm = get_or_create_destination('Sharm El Sheikh')
    alexandria = get_or_create_destination('Alexandria')
    jordan = get_or_create_destination('Jordan')
    morocco = get_or_create_destination('Morocco')

    # Define missing tours
    missing_tours = [
        {
            'name': 'Egypt with Abu Simbel and Hurghada',
            'name_es': 'Egipto con Abu Simbel y Hurghada',
            'name_pt': 'Egito com Abu Simbel e Hurghada',
            'short_description': '13 days exploring Egypt\'s treasures with Abu Simbel and Red Sea relaxation in Hurghada.',
            'short_description_es': '13 días explorando los tesoros de Egipto con Abu Simbel y relajación en Hurghada.',
            'short_description_pt': '13 dias explorando os tesouros do Egito com Abu Simbel e relaxamento em Hurghada.',
            'description': '''
Experience the best of Egypt in this comprehensive 13-day tour. Start in Cairo with the iconic Pyramids of Giza and the Egyptian Museum, then cruise down the Nile on a luxurious ship visiting Luxor and Aswan's magnificent temples. Witness the awe-inspiring Abu Simbel temples at sunrise, and conclude your journey with relaxation at Hurghada's pristine Red Sea beaches.

This tour includes:
- 3 nights on a full-board Nile Cruise
- Guided sightseeing at all major sites
- Abu Simbel excursion
- Beach relaxation in Hurghada
- All accommodations in 4-5 star hotels
- Professional English-speaking Egyptologist guide
''',
            'category': 'Classic Egypt Tours',
            'tour_type': 'Multi-Day Package',
            'days': 13,
            'nights': 12,
            'price': 2299,
            'destinations': [cairo, luxor, aswan, hurghada],
            'is_featured': True,
            'is_best_seller': True,
            'highlights': [
                'Pyramids of Giza and Sphinx',
                '3-Night Nile Cruise',
                'Abu Simbel Temples',
                'Valley of the Kings',
                'Hurghada Beach Resort'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Welcome to Egypt! Meet and assist at Cairo International Airport. Transfer to your hotel.'},
                {'day': 2, 'title': 'Pyramids & Egyptian Museum', 'description': 'Visit the Pyramids of Giza, Sphinx, and the Egyptian Museum with its treasures of Tutankhamun.'},
                {'day': 3, 'title': 'Fly to Aswan', 'description': 'Morning flight to Aswan. Visit the High Dam, Unfinished Obelisk, and Philae Temple. Board Nile Cruise.'},
                {'day': 4, 'title': 'Abu Simbel Excursion', 'description': 'Early morning excursion to Abu Simbel to see the magnificent temples of Ramses II.'},
                {'day': 5, 'title': 'Nile Cruise - Kom Ombo & Edfu', 'description': 'Sail to Kom Ombo Temple, then continue to Edfu to visit the Temple of Horus.'},
                {'day': 6, 'title': 'Nile Cruise - Luxor', 'description': 'Arrive in Luxor. Visit Karnak Temple and Luxor Temple.'},
                {'day': 7, 'title': 'West Bank Luxor', 'description': 'Explore the Valley of the Kings, Hatshepsut Temple, and the Colossi of Memnon.'},
                {'day': 8, 'title': 'Transfer to Hurghada', 'description': 'Private transfer to Hurghada. Afternoon free for beach relaxation.'},
                {'day': 9, 'title': 'Hurghada - Free Day', 'description': 'Full day at leisure. Optional activities: snorkeling, diving, or desert safari.'},
                {'day': 10, 'title': 'Hurghada - Free Day', 'description': 'Another day to enjoy Hurghada\'s beaches and water activities.'},
                {'day': 11, 'title': 'Hurghada - Free Day', 'description': 'Continue enjoying your Red Sea paradise.'},
                {'day': 12, 'title': 'Return to Cairo', 'description': 'Transfer back to Cairo. Free time for last-minute shopping at Khan El Khalili.'},
                {'day': 13, 'title': 'Departure', 'description': 'Transfer to Cairo International Airport for your departure flight.'}
            ]
        },
        {
            'name': 'Splendid Pharaonic Egypt',
            'name_es': 'Espléndido Egipto Faraónico',
            'name_pt': 'Esplêndido Egito Faraônico',
            'short_description': '10 days discovering Cairo, Alexandria, and a 4-night Nile Cruise from Luxor to Aswan.',
            'short_description_es': '10 días descubriendo El Cairo, Alejandría y un crucero por el Nilo de 4 noches.',
            'short_description_pt': '10 dias descobrindo Cairo, Alexandria e um cruzeiro de 4 noites pelo Nilo.',
            'description': '''
Discover the splendors of ancient Egypt on this 10-day journey through time. Begin in Cairo exploring the Pyramids and Egyptian Museum, then venture to the Mediterranean city of Alexandria with its Greek and Roman heritage. Conclude with a relaxing 4-night Nile Cruise from Luxor to Aswan, visiting magnificent temples along the way.

Highlights include:
- Cairo and the Pyramids of Giza
- Alexandria's Greco-Roman history
- 4-night luxury Nile Cruise
- Temples of Edfu and Kom Ombo
- Valley of the Kings in Luxor
''',
            'category': 'Classic Egypt Tours',
            'tour_type': 'Multi-Day Package',
            'days': 10,
            'nights': 9,
            'price': 1799,
            'destinations': [cairo, alexandria, luxor, aswan],
            'is_featured': True,
            'is_best_seller': False,
            'highlights': [
                'Pyramids and Sphinx',
                'Alexandria Day Trip',
                '4-Night Nile Cruise',
                'Temple of Karnak',
                'Philae Temple'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Welcome to Egypt! Airport meet and greet, transfer to hotel.'},
                {'day': 2, 'title': 'Cairo Sightseeing', 'description': 'Full day visiting the Pyramids of Giza, Sphinx, and the Egyptian Museum.'},
                {'day': 3, 'title': 'Alexandria Day Trip', 'description': 'Day trip to Alexandria visiting Catacombs, Pompey\'s Pillar, and the new Bibliotheca Alexandrina.'},
                {'day': 4, 'title': 'Fly to Luxor - Nile Cruise', 'description': 'Morning flight to Luxor. Visit Karnak and Luxor Temples. Board your Nile Cruise.'},
                {'day': 5, 'title': 'Luxor West Bank', 'description': 'Visit Valley of the Kings, Hatshepsut Temple, and Colossi of Memnon. Sail towards Edfu.'},
                {'day': 6, 'title': 'Edfu Temple', 'description': 'Visit the magnificent Temple of Horus at Edfu. Continue sailing to Kom Ombo.'},
                {'day': 7, 'title': 'Kom Ombo - Aswan', 'description': 'Visit Kom Ombo Temple dedicated to Sobek and Horus. Sail to Aswan.'},
                {'day': 8, 'title': 'Aswan Sightseeing', 'description': 'Visit Aswan High Dam, Unfinished Obelisk, and the beautiful Philae Temple.'},
                {'day': 9, 'title': 'Fly to Cairo', 'description': 'Disembark cruise. Flight to Cairo. Afternoon free for shopping.'},
                {'day': 10, 'title': 'Departure', 'description': 'Transfer to airport for your departure flight.'}
            ]
        },
        {
            'name': 'Queen Isis Route',
            'name_es': 'Ruta de la Reina Isis',
            'name_pt': 'Rota da Rainha Ísis',
            'short_description': '12 days following the goddess Isis through Egypt\'s most sacred sites including Abydos and Dendera.',
            'short_description_es': '12 días siguiendo a la diosa Isis por los sitios más sagrados de Egipto.',
            'short_description_pt': '12 dias seguindo a deusa Ísis pelos locais mais sagrados do Egito.',
            'description': '''
Follow in the footsteps of the goddess Isis on this spiritual journey through Egypt's most sacred sites. This 12-day tour takes you beyond the usual tourist trail to visit Abydos and Dendera - two of Egypt's most important religious centers.

Special features:
- 2 domestic flights included
- Visit to Abydos Temple (cult center of Osiris)
- Dendera Temple (best-preserved temple in Egypt)
- Nile Cruise with all sightseeing
- Alexandria's ancient wonders
- Luxury accommodations throughout
''',
            'category': 'Cultural & Historical',
            'tour_type': 'Multi-Day Package',
            'days': 12,
            'nights': 11,
            'price': 2499,
            'destinations': [cairo, alexandria, luxor, aswan],
            'is_featured': True,
            'is_best_seller': False,
            'highlights': [
                'Abydos Temple',
                'Dendera Temple of Hathor',
                'Nile Cruise',
                'Valley of the Kings',
                'Alexandria'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Welcome to Egypt! Transfer to your luxury hotel.'},
                {'day': 2, 'title': 'Pyramids & Saqqara', 'description': 'Visit Giza Pyramids, Sphinx, and the Step Pyramid at Saqqara.'},
                {'day': 3, 'title': 'Egyptian Museum & Old Cairo', 'description': 'Morning at the Egyptian Museum. Afternoon visit Coptic Cairo and Islamic Cairo.'},
                {'day': 4, 'title': 'Alexandria', 'description': 'Day trip to Alexandria. Visit the Library, Catacombs, and Mediterranean waterfront.'},
                {'day': 5, 'title': 'Fly to Luxor', 'description': 'Morning flight to Luxor. Board Nile Cruise. Visit Karnak Temple.'},
                {'day': 6, 'title': 'Abydos & Dendera', 'description': 'Full day excursion to Abydos Temple and Dendera\'s Temple of Hathor.'},
                {'day': 7, 'title': 'Luxor West Bank', 'description': 'Valley of the Kings, Hatshepsut Temple, Colossi of Memnon. Sail to Esna.'},
                {'day': 8, 'title': 'Edfu Temple', 'description': 'Visit Temple of Horus at Edfu. Continue sailing south.'},
                {'day': 9, 'title': 'Kom Ombo & Aswan', 'description': 'Morning visit to Kom Ombo. Arrive in Aswan, visit Philae Temple.'},
                {'day': 10, 'title': 'Aswan', 'description': 'High Dam, Unfinished Obelisk. Optional felucca ride around Elephantine Island.'},
                {'day': 11, 'title': 'Return to Cairo', 'description': 'Fly back to Cairo. Free afternoon for shopping.'},
                {'day': 12, 'title': 'Departure', 'description': 'Transfer to Cairo Airport for departure.'}
            ]
        },
        {
            'name': 'Pleasing Sharm El Sheikh with Cairo',
            'name_es': 'Placentero Sharm El Sheikh con El Cairo',
            'name_pt': 'Agradável Sharm El Sheikh com Cairo',
            'short_description': '7 days combining Red Sea relaxation in Sharm El Sheikh with Cairo\'s ancient wonders.',
            'short_description_es': '7 días combinando relajación en el Mar Rojo con las maravillas del Cairo.',
            'short_description_pt': '7 dias combinando relaxamento no Mar Vermelho com as maravilhas do Cairo.',
            'description': '''
The perfect blend of ancient history and beach relaxation! This 7-day tour combines the must-see attractions of Cairo with the stunning Red Sea resort of Sharm El Sheikh.

Enjoy:
- Pyramids of Giza and Egyptian Museum
- 4 nights in Sharm El Sheikh resort
- Optional diving and snorkeling excursions
- Free time to relax on pristine beaches
- All transfers included
''',
            'category': 'Beach & Diving',
            'tour_type': 'Multi-Day Package',
            'days': 7,
            'nights': 6,
            'price': 999,
            'destinations': [cairo, sharm],
            'is_featured': True,
            'is_best_seller': False,
            'highlights': [
                'Pyramids of Giza',
                'Egyptian Museum',
                'Sharm El Sheikh Resort',
                'Red Sea Beaches',
                'Optional Diving/Snorkeling'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Welcome to Egypt! Transfer to your Cairo hotel.'},
                {'day': 2, 'title': 'Cairo Sightseeing', 'description': 'Full day visiting Pyramids of Giza, Sphinx, and the world-famous Egyptian Museum.'},
                {'day': 3, 'title': 'Fly to Sharm El Sheikh', 'description': 'Morning flight to Sharm El Sheikh. Check in to your beach resort. Afternoon at leisure.'},
                {'day': 4, 'title': 'Sharm El Sheikh', 'description': 'Free day to enjoy the beach, pool, or optional excursions.'},
                {'day': 5, 'title': 'Sharm El Sheikh', 'description': 'Another day of relaxation. Optional snorkeling at Ras Mohammed or diving trip.'},
                {'day': 6, 'title': 'Sharm El Sheikh', 'description': 'Last full day in paradise. Optional desert safari or glass-bottom boat trip.'},
                {'day': 7, 'title': 'Departure', 'description': 'Transfer to Sharm El Sheikh Airport for your departure flight.'}
            ]
        },
        {
            'name': 'The Journey of Moses',
            'name_es': 'El Viaje de Moisés',
            'name_pt': 'A Jornada de Moisés',
            'short_description': '10 days following the biblical journey through Egypt and Jordan including Mount Sinai and Petra.',
            'short_description_es': '10 días siguiendo el viaje bíblico a través de Egipto y Jordania.',
            'short_description_pt': '10 dias seguindo a jornada bíblica através do Egito e Jordânia.',
            'description': '''
Trace the footsteps of Moses on this spiritual 10-day journey through Egypt and Jordan. From the land of the Pharaohs to Mount Sinai where Moses received the Ten Commandments, and on to Petra and the Holy Land of Jordan.

This biblical tour includes:
- Cairo and the Pyramids
- Sunrise trek to Mount Sinai
- St. Catherine's Monastery
- Petra - the Rose-Red City
- Amman and Madaba
- Professional religious guide
''',
            'category': 'Religious & Spiritual',
            'tour_type': 'Multi-Country Tour',
            'days': 10,
            'nights': 9,
            'price': 2199,
            'destinations': [cairo, sharm, jordan],
            'is_featured': True,
            'is_best_seller': False,
            'is_multi_destination': True,
            'highlights': [
                'Mount Sinai Sunrise Trek',
                'St. Catherine\'s Monastery',
                'Petra - World Wonder',
                'Pyramids of Giza',
                'Amman Citadel'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival in Cairo', 'description': 'Welcome to Egypt! Transfer to hotel.'},
                {'day': 2, 'title': 'Cairo Sightseeing', 'description': 'Visit Pyramids, Sphinx, and Egyptian Museum.'},
                {'day': 3, 'title': 'Coptic Cairo', 'description': 'Visit Coptic Churches, Hanging Church, and Ben Ezra Synagogue. Transfer to Sinai.'},
                {'day': 4, 'title': 'Mount Sinai Sunrise', 'description': 'Pre-dawn climb to Mount Sinai for sunrise. Visit St. Catherine\'s Monastery.'},
                {'day': 5, 'title': 'Sharm El Sheikh', 'description': 'Free day at Red Sea resort. Relax or optional snorkeling.'},
                {'day': 6, 'title': 'Cross to Jordan', 'description': 'Ferry to Aqaba, Jordan. Transfer to Petra.'},
                {'day': 7, 'title': 'Petra Full Day', 'description': 'Explore the ancient rose-red city of Petra, one of the New Seven Wonders.'},
                {'day': 8, 'title': 'Wadi Rum', 'description': 'Morning in Wadi Rum desert. Jeep safari through the stunning landscape.'},
                {'day': 9, 'title': 'Mount Nebo & Amman', 'description': 'Visit Mount Nebo where Moses saw the Promised Land. Continue to Amman.'},
                {'day': 10, 'title': 'Departure', 'description': 'Transfer to Amman Airport for departure.'}
            ]
        },
        {
            'name': 'Exceptional Egypt',
            'name_es': 'Egipto Excepcional',
            'name_pt': 'Egito Excepcional',
            'short_description': '13 days experiencing ancient Egyptian attractions, Red Sea beaches, and Mediterranean treasures.',
            'short_description_es': '13 días experimentando las atracciones del antiguo Egipto, el Mar Rojo y el Mediterráneo.',
            'short_description_pt': '13 dias experimentando atrações do antigo Egito, Mar Vermelho e Mediterrâneo.',
            'description': '''
The ultimate Egypt experience! This exceptional 13-day tour covers all of Egypt's highlights - from the ancient monuments of Cairo and the Nile Valley to the beaches of both the Red Sea and Mediterranean.

Your exceptional journey includes:
- Complete Cairo experience
- Alexandria and the Mediterranean
- Luxurious Nile Cruise
- Hurghada beach relaxation
- All domestic flights
- Luxury accommodations
''',
            'category': 'Luxury Tours',
            'tour_type': 'Multi-Day Package',
            'days': 13,
            'nights': 12,
            'price': 2899,
            'destinations': [cairo, alexandria, luxor, aswan, hurghada],
            'is_featured': True,
            'is_best_seller': True,
            'highlights': [
                'Pyramids and Sphinx',
                'Alexandria Day Trip',
                'Nile Cruise',
                'Valley of the Kings',
                'Hurghada Beach'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival Cairo', 'description': 'Welcome to Egypt! VIP airport meet and greet.'},
                {'day': 2, 'title': 'Pyramids & Saqqara', 'description': 'Visit Giza Pyramids, Sphinx, and the ancient burial grounds of Saqqara.'},
                {'day': 3, 'title': 'Egyptian Museum & Cairo', 'description': 'Egyptian Museum, Old Cairo, Khan El Khalili bazaar.'},
                {'day': 4, 'title': 'Alexandria', 'description': 'Full day in the Mediterranean city of Alexander the Great.'},
                {'day': 5, 'title': 'Fly to Luxor', 'description': 'Flight to Luxor. Board your luxury Nile cruise. Visit Luxor Temple.'},
                {'day': 6, 'title': 'West Bank Luxor', 'description': 'Valley of the Kings, Hatshepsut Temple, Colossi of Memnon.'},
                {'day': 7, 'title': 'Edfu', 'description': 'Sail to Edfu. Visit the Temple of Horus.'},
                {'day': 8, 'title': 'Kom Ombo - Aswan', 'description': 'Kom Ombo Temple. Arrive Aswan. Felucca ride at sunset.'},
                {'day': 9, 'title': 'Aswan', 'description': 'High Dam, Philae Temple, Unfinished Obelisk.'},
                {'day': 10, 'title': 'Transfer to Hurghada', 'description': 'Scenic drive to Hurghada. Check in to beach resort.'},
                {'day': 11, 'title': 'Hurghada', 'description': 'Free day for beach and water activities.'},
                {'day': 12, 'title': 'Hurghada', 'description': 'Another day of Red Sea relaxation.'},
                {'day': 13, 'title': 'Departure', 'description': 'Transfer to Hurghada or Cairo airport.'}
            ]
        },
        {
            'name': 'The Best of Egypt and Morocco',
            'name_es': 'Lo Mejor de Egipto y Marruecos',
            'name_pt': 'O Melhor do Egito e Marrocos',
            'short_description': '14 days exploring the cultural heritage of two incredible North African destinations.',
            'short_description_es': '14 días explorando el patrimonio cultural de dos increíbles destinos del norte de África.',
            'short_description_pt': '14 dias explorando o patrimônio cultural de dois destinos incríveis do norte da África.',
            'description': '''
Experience the best of North Africa on this epic 14-day journey through Egypt and Morocco. From the Pyramids of Giza to the medinas of Marrakech, this tour combines two of the world's most fascinating destinations.

Includes:
- 2 domestic flights
- Cairo, Luxor, and Aswan
- Marrakech, Fes, and Casablanca
- Sahara Desert experience
- Expert local guides in both countries
- All transfers between cities
''',
            'category': 'Multi-Country Tours',
            'tour_type': 'Multi-Country Tour',
            'days': 14,
            'nights': 13,
            'price': 3299,
            'destinations': [cairo, luxor, aswan, morocco],
            'is_featured': True,
            'is_best_seller': False,
            'is_multi_destination': True,
            'highlights': [
                'Pyramids of Giza',
                'Nile Cruise',
                'Marrakech Medina',
                'Fes Medina',
                'Sahara Desert'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival Cairo', 'description': 'Welcome to Egypt! Transfer to hotel.'},
                {'day': 2, 'title': 'Cairo Sightseeing', 'description': 'Pyramids, Sphinx, Egyptian Museum.'},
                {'day': 3, 'title': 'Fly to Aswan', 'description': 'Flight to Aswan. Board Nile Cruise.'},
                {'day': 4, 'title': 'Nile Cruise', 'description': 'Sail from Aswan towards Luxor with temple visits.'},
                {'day': 5, 'title': 'Nile Cruise - Luxor', 'description': 'Valley of the Kings, Karnak Temple.'},
                {'day': 6, 'title': 'Fly to Cairo, then Casablanca', 'description': 'International flight to Morocco.'},
                {'day': 7, 'title': 'Casablanca - Rabat', 'description': 'Hassan II Mosque. Drive to Rabat.'},
                {'day': 8, 'title': 'Fes', 'description': 'Drive to Fes. Explore the ancient medina.'},
                {'day': 9, 'title': 'Fes', 'description': 'Full day in Fes - tanneries, madrasas, souks.'},
                {'day': 10, 'title': 'Sahara Desert', 'description': 'Journey to Merzouga. Camel trek into the Sahara.'},
                {'day': 11, 'title': 'Dades Valley', 'description': 'Drive through the dramatic Dades Gorges.'},
                {'day': 12, 'title': 'Marrakech', 'description': 'Arrive in Marrakech. Evening in Djemaa el-Fna square.'},
                {'day': 13, 'title': 'Marrakech', 'description': 'Full day exploring Marrakech - palaces, gardens, souks.'},
                {'day': 14, 'title': 'Departure', 'description': 'Transfer to Marrakech airport.'}
            ]
        },
        {
            'name': 'Promotional Package to Egypt',
            'name_es': 'Paquete Promocional a Egipto',
            'name_pt': 'Pacote Promocional para o Egito',
            'short_description': '8 days experiencing Cairo, Giza, and a 4-night Nile Cruise at an exceptional value.',
            'short_description_es': '8 días experimentando El Cairo, Giza y un crucero por el Nilo de 4 noches.',
            'short_description_pt': '8 dias experimentando Cairo, Giza e um cruzeiro de 4 noites pelo Nilo.',
            'description': '''
Our best-value package to Egypt! Experience the highlights of this ancient land in 8 unforgettable days. This promotional package includes Cairo sightseeing and a 4-night Nile Cruise - all at an exceptional price.

What's included:
- 3 nights in Cairo (4-star hotel)
- 4 nights on Nile Cruise (full board)
- All sightseeing with Egyptologist guide
- Airport transfers
- Domestic flight Cairo-Luxor
''',
            'category': 'Classic Egypt Tours',
            'tour_type': 'Multi-Day Package',
            'days': 8,
            'nights': 7,
            'price': 1199,
            'destinations': [cairo, luxor, aswan],
            'is_featured': False,
            'is_best_seller': True,
            'has_discount': True,
            'discount_percentage': 15,
            'highlights': [
                'Pyramids of Giza',
                'Egyptian Museum',
                '4-Night Nile Cruise',
                'Valley of the Kings',
                'Aswan Temples'
            ],
            'itinerary': [
                {'day': 1, 'title': 'Arrival Cairo', 'description': 'Airport transfer to hotel. Welcome meeting.'},
                {'day': 2, 'title': 'Pyramids & Museum', 'description': 'Full day: Pyramids, Sphinx, Egyptian Museum.'},
                {'day': 3, 'title': 'Fly to Luxor', 'description': 'Flight to Luxor. Board cruise. Karnak Temple.'},
                {'day': 4, 'title': 'West Bank Luxor', 'description': 'Valley of the Kings, Hatshepsut Temple.'},
                {'day': 5, 'title': 'Edfu & Kom Ombo', 'description': 'Visit both temples as you sail south.'},
                {'day': 6, 'title': 'Aswan', 'description': 'High Dam, Philae Temple, Unfinished Obelisk.'},
                {'day': 7, 'title': 'Return to Cairo', 'description': 'Fly back to Cairo. Free afternoon.'},
                {'day': 8, 'title': 'Departure', 'description': 'Transfer to airport.'}
            ]
        }
    ]

    tours_created = 0

    for tour_data in missing_tours:
        # Check if tour already exists
        if Tour.objects.filter(name=tour_data['name']).exists():
            print(f"  Tour already exists: {tour_data['name']}")
            continue

        # Get or create category and type
        category = get_or_create_tour_category(tour_data['category'])
        tour_type = get_or_create_tour_type(tour_data['tour_type'])

        # Create tour
        tour = Tour.objects.create(
            name=tour_data['name'],
            name_es=tour_data.get('name_es', ''),
            name_pt=tour_data.get('name_pt', ''),
            short_description=tour_data['short_description'],
            short_description_es=tour_data.get('short_description_es', ''),
            short_description_pt=tour_data.get('short_description_pt', ''),
            description=tour_data['description'],
            category=category,
            tour_type=tour_type,
            days=tour_data['days'],
            nights=tour_data['nights'],
            price=tour_data['price'],
            is_featured=tour_data.get('is_featured', False),
            is_best_seller=tour_data.get('is_best_seller', False),
            is_multi_destination=tour_data.get('is_multi_destination', False),
            has_discount=tour_data.get('has_discount', False),
            discount_percentage=tour_data.get('discount_percentage'),
            is_published=True,
            published_at=timezone.now(),
            featured_image='tours/default.jpg',
            difficulty_level='easy'
        )

        # Add destinations
        for dest in tour_data.get('destinations', []):
            tour.destinations.add(dest)

        # Add highlights
        for i, highlight in enumerate(tour_data.get('highlights', [])):
            TourHighlight.objects.create(
                tour=tour,
                title=highlight,
                sort_order=i
            )

        # Add itinerary
        for item in tour_data.get('itinerary', []):
            TourItinerary.objects.create(
                tour=tour,
                day_number=item['day'],
                title=item['title'],
                description=item['description'],
                sort_order=item['day']
            )

        # Add standard inclusions
        inclusions = [
            'Accommodation in 4-5 star hotels',
            'Daily breakfast',
            'Airport transfers',
            'Professional Egyptologist guide',
            'All entrance fees',
            'Air-conditioned transportation'
        ]
        exclusions = [
            'International flights',
            'Travel insurance',
            'Personal expenses',
            'Tipping'
        ]

        for i, item in enumerate(inclusions):
            TourInclusion.objects.create(tour=tour, item=item, is_included=True, sort_order=i)

        for i, item in enumerate(exclusions):
            TourInclusion.objects.create(tour=tour, item=item, is_included=False, sort_order=i + len(inclusions))

        tours_created += 1
        print(f"  Created tour: {tour_data['name']}")

    print(f"\nTotal tours created: {tours_created}")
    return tours_created


if __name__ == '__main__':
    print("=" * 60)
    print("Adding Missing Content from girasoltours.com")
    print("=" * 60)

    posts = seed_missing_blog_posts()
    tours = seed_missing_tours()

    print("\n" + "=" * 60)
    print(f"Summary: Created {posts} blog posts and {tours} tours")
    print("=" * 60)
