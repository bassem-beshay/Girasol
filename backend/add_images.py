"""
Add Images Script for Girasol Egypt Tourism Platform
Downloads images from Unsplash and adds them to the database.
"""

import os
import sys
import django
import urllib.request
import ssl
from io import BytesIO

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.core.files.base import ContentFile
from apps.destinations.models import Destination, DestinationImage, Activity
from apps.tours.models import Tour, TourImage, TourCategory, Addon
from apps.blog.models import Post
from apps.reviews.models import Testimonial

# Disable SSL verification for downloads
ssl._create_default_https_context = ssl._create_unverified_context

print("=" * 60)
print("GIRASOL EGYPT - Image Downloader")
print("=" * 60)

def download_image(url, filename):
    """Download image from URL and return as ContentFile."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request, timeout=30)
        image_data = response.read()
        return ContentFile(image_data, name=filename)
    except Exception as e:
        print(f"    Error downloading {filename}: {e}")
        return None

# Unsplash image URLs (free to use)
# Using specific sizes for optimization

DESTINATION_IMAGES = {
    "Cairo": {
        "featured": "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?w=1200&q=80",
        "banner": "https://images.unsplash.com/photo-1539768942893-daf53e448371?w=1920&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1553913861-c0fddf2619ee?w=800&q=80",
            "https://images.unsplash.com/photo-1608329597689-24b9fc68b993?w=800&q=80",
            "https://images.unsplash.com/photo-1562979314-bee7453e911c?w=800&q=80",
        ]
    },
    "Luxor": {
        "featured": "https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=1200&q=80",
        "banner": "https://images.unsplash.com/photo-1590253230532-a67f6bc61c9e?w=1920&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1565967511849-76a60a516170?w=800&q=80",
            "https://images.unsplash.com/photo-1600093463592-8e36ae95ef56?w=800&q=80",
            "https://images.unsplash.com/photo-1558271736-cd043ef2e855?w=800&q=80",
        ]
    },
    "Aswan": {
        "featured": "https://images.unsplash.com/photo-1569230919100-d3fd5e1132f4?w=1200&q=80",
        "banner": "https://images.unsplash.com/photo-1578271887552-5ac3a72752bc?w=1920&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1623345805780-8f01f714e65f?w=800&q=80",
            "https://images.unsplash.com/photo-1565686075576-01e0aa55cc1e?w=800&q=80",
        ]
    },
    "Alexandria": {
        "featured": "https://images.unsplash.com/photo-1572252821143-035a024857ac?w=1200&q=80",
        "banner": "https://images.unsplash.com/photo-1558271736-cd043ef2e855?w=1920&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=800&q=80",
        ]
    },
    "Sharm El Sheikh": {
        "featured": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1200&q=80",
        "banner": "https://images.unsplash.com/photo-1682687220742-aba13b6e50ba?w=1920&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=80",
            "https://images.unsplash.com/photo-1544551763-77ef2d0cfc6c?w=800&q=80",
            "https://images.unsplash.com/photo-1682687982501-1e58ab814714?w=800&q=80",
        ]
    },
    "Hurghada": {
        "featured": "https://images.unsplash.com/photo-1582967788606-a171c1080cb0?w=1200&q=80",
        "banner": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1920&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&q=80",
            "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=800&q=80",
        ]
    },
}

TOUR_IMAGES = {
    "pyramids": [
        "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?w=1200&q=80",
        "https://images.unsplash.com/photo-1539768942893-daf53e448371?w=800&q=80",
        "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?w=800&q=80",
    ],
    "nile_cruise": [
        "https://images.unsplash.com/photo-1569230919100-d3fd5e1132f4?w=1200&q=80",
        "https://images.unsplash.com/photo-1578271887552-5ac3a72752bc?w=800&q=80",
        "https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=800&q=80",
    ],
    "diving": [
        "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1200&q=80",
        "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=80",
        "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=800&q=80",
    ],
    "desert": [
        "https://images.unsplash.com/photo-1547234935-80c7145ec969?w=1200&q=80",
        "https://images.unsplash.com/photo-1509316785289-025f5b846b35?w=800&q=80",
        "https://images.unsplash.com/photo-1542401886-65d6c61db217?w=800&q=80",
    ],
    "temple": [
        "https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=1200&q=80",
        "https://images.unsplash.com/photo-1590253230532-a67f6bc61c9e?w=800&q=80",
        "https://images.unsplash.com/photo-1565967511849-76a60a516170?w=800&q=80",
    ],
}

BLOG_IMAGES = [
    "https://images.unsplash.com/photo-1539768942893-daf53e448371?w=1200&q=80",
    "https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=1200&q=80",
    "https://images.unsplash.com/photo-1590253230532-a67f6bc61c9e?w=1200&q=80",
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1200&q=80",
    "https://images.unsplash.com/photo-1547234935-80c7145ec969?w=1200&q=80",
]

# Avatar images for testimonials (using placeholder service)
AVATAR_IMAGES = [
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&q=80",
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&q=80",
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&q=80",
    "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&q=80",
    "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&q=80",
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&q=80",
    "https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=150&q=80",
    "https://images.unsplash.com/photo-1463453091185-61582044d556?w=150&q=80",
    "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&q=80",
    "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=150&q=80",
]

# ============================================================
# ADD DESTINATION IMAGES
# ============================================================
print("\n[1/4] Adding Destination Images...")

for dest_name, images in DESTINATION_IMAGES.items():
    try:
        dest = Destination.objects.get(name=dest_name)
        print(f"  Processing: {dest_name}")

        # Featured image
        if not dest.featured_image or 'unsplash' not in str(dest.featured_image):
            img = download_image(images["featured"], f"{dest.slug}_featured.jpg")
            if img:
                dest.featured_image.save(f"{dest.slug}_featured.jpg", img, save=True)
                print(f"    Added featured image")

        # Banner image
        if not dest.banner_image:
            img = download_image(images["banner"], f"{dest.slug}_banner.jpg")
            if img:
                dest.banner_image.save(f"{dest.slug}_banner.jpg", img, save=True)
                print(f"    Added banner image")

        # Gallery images
        existing_gallery = dest.images.count()
        if existing_gallery < 3:
            for i, gallery_url in enumerate(images.get("gallery", []), 1):
                img = download_image(gallery_url, f"{dest.slug}_gallery_{i}.jpg")
                if img:
                    gallery_img = DestinationImage(
                        destination=dest,
                        caption=f"{dest_name} - View {i}",
                        alt_text=f"{dest_name} tourist attraction",
                        sort_order=i
                    )
                    gallery_img.image.save(f"{dest.slug}_gallery_{i}.jpg", img, save=False)
                    gallery_img.save()
                    print(f"    Added gallery image {i}")

    except Destination.DoesNotExist:
        print(f"  Destination not found: {dest_name}")
    except Exception as e:
        print(f"  Error processing {dest_name}: {e}")

# ============================================================
# ADD TOUR IMAGES
# ============================================================
print("\n[2/4] Adding Tour Images...")

tours = Tour.objects.all()
for tour in tours:
    print(f"  Processing: {tour.name[:40]}...")

    # Determine which image set to use based on tour name/type
    if 'pyramid' in tour.name.lower() or 'giza' in tour.name.lower():
        image_set = TOUR_IMAGES['pyramids']
    elif 'cruise' in tour.name.lower() or 'nile' in tour.name.lower():
        image_set = TOUR_IMAGES['nile_cruise']
    elif 'diving' in tour.name.lower() or 'red sea' in tour.name.lower() or 'beach' in tour.name.lower():
        image_set = TOUR_IMAGES['diving']
    elif 'desert' in tour.name.lower() or 'safari' in tour.name.lower() or 'oasis' in tour.name.lower():
        image_set = TOUR_IMAGES['desert']
    else:
        image_set = TOUR_IMAGES['temple']

    try:
        # Featured image
        if not tour.featured_image or 'placeholder' in str(tour.featured_image):
            img = download_image(image_set[0], f"{tour.slug}_featured.jpg")
            if img:
                tour.featured_image.save(f"{tour.slug}_featured.jpg", img, save=True)
                print(f"    Added featured image")

        # Gallery images
        existing_gallery = tour.images.count()
        if existing_gallery < 2:
            for i, gallery_url in enumerate(image_set[1:], 1):
                img = download_image(gallery_url, f"{tour.slug}_gallery_{i}.jpg")
                if img:
                    gallery_img = TourImage(
                        tour=tour,
                        caption=f"{tour.name} - Photo {i}",
                        alt_text=f"{tour.name} tour experience",
                        sort_order=i
                    )
                    gallery_img.image.save(f"{tour.slug}_gallery_{i}.jpg", img, save=False)
                    gallery_img.save()
                    print(f"    Added gallery image {i}")

    except Exception as e:
        print(f"    Error: {e}")

# ============================================================
# ADD BLOG IMAGES
# ============================================================
print("\n[3/4] Adding Blog Post Images...")

posts = Post.objects.all()
for i, post in enumerate(posts):
    print(f"  Processing: {post.title[:40]}...")
    try:
        if not post.featured_image or 'placeholder' in str(post.featured_image):
            img_url = BLOG_IMAGES[i % len(BLOG_IMAGES)]
            img = download_image(img_url, f"{post.slug}_featured.jpg")
            if img:
                post.featured_image.save(f"{post.slug}_featured.jpg", img, save=True)
                print(f"    Added featured image")
    except Exception as e:
        print(f"    Error: {e}")

# ============================================================
# ADD TESTIMONIAL AVATARS
# ============================================================
print("\n[4/4] Adding Testimonial Avatars...")

testimonials = Testimonial.objects.all()
for i, testimonial in enumerate(testimonials):
    print(f"  Processing: {testimonial.name[:30]}...")
    try:
        if not testimonial.avatar or 'placeholder' in str(testimonial.avatar):
            img_url = AVATAR_IMAGES[i % len(AVATAR_IMAGES)]
            img = download_image(img_url, f"avatar_{testimonial.pk}.jpg")
            if img:
                testimonial.avatar.save(f"avatar_{testimonial.pk}.jpg", img, save=True)
                print(f"    Added avatar")
    except Exception as e:
        print(f"    Error: {e}")

# ============================================================
# ADD TOUR CATEGORY IMAGES
# ============================================================
print("\n[Bonus] Adding Tour Category Images...")

CATEGORY_IMAGES = {
    "Classic Egypt": "https://images.unsplash.com/photo-1539768942893-daf53e448371?w=600&q=80",
    "Nile Cruises": "https://images.unsplash.com/photo-1569230919100-d3fd5e1132f4?w=600&q=80",
    "Day Tours": "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?w=600&q=80",
    "Beach": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600&q=80",
    "Diving": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=600&q=80",
    "Desert": "https://images.unsplash.com/photo-1547234935-80c7145ec969?w=600&q=80",
    "Luxury": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600&q=80",
    "Family": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=600&q=80",
}

categories = TourCategory.objects.all()
for cat in categories:
    print(f"  Processing: {cat.name}...")
    try:
        if not cat.image:
            # Find matching image
            for key, url in CATEGORY_IMAGES.items():
                if key.lower() in cat.name.lower():
                    img = download_image(url, f"category_{cat.slug}.jpg")
                    if img:
                        cat.image.save(f"category_{cat.slug}.jpg", img, save=True)
                        print(f"    Added category image")
                    break
    except Exception as e:
        print(f"    Error: {e}")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("IMAGE DOWNLOAD COMPLETE!")
print("=" * 60)

print(f"""
Summary:
- Destinations with images: {Destination.objects.exclude(featured_image='').count()}
- Tours with images: {Tour.objects.exclude(featured_image='').count()}
- Blog posts with images: {Post.objects.exclude(featured_image='').count()}
- Testimonials with avatars: {Testimonial.objects.exclude(avatar='').count()}

Images are stored in the media/ directory.
""")
