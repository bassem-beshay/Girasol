"""
Download images for Multi-Destination Tours from Unsplash
"""
import os
import sys
import urllib.request
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.core.files.base import ContentFile
from apps.destinations.models import Destination
from apps.tours.models import Tour

# Unsplash image URLs (free to use)
IMAGES = {
    # Destinations
    'jordan': 'https://images.unsplash.com/photo-1548786811-dd6e453ccca7?w=1200',  # Petra Jordan
    'dubai': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1200',   # Dubai skyline

    # Tours
    'egypt-jordan': 'https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=1200',  # Petra Treasury
    'egypt-dubai': 'https://images.unsplash.com/photo-1518684079-3c830dcef090?w=1200',      # Dubai Burj Khalifa
}

def download_image(url, filename):
    """Download image from URL"""
    print(f"  Downloading {filename}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read()
    except Exception as e:
        print(f"  Error downloading {filename}: {e}")
        return None


def update_destinations():
    """Update destination images"""
    print("\n[Destinations] Updating Images...")

    # Jordan
    jordan = Destination.objects.filter(slug='jordan').first()
    if jordan and not jordan.featured_image:
        image_data = download_image(IMAGES['jordan'], 'jordan.jpg')
        if image_data:
            jordan.featured_image.save('jordan-petra.jpg', ContentFile(image_data), save=True)
            print(f"  [OK] Jordan image saved")

    # Dubai
    dubai = Destination.objects.filter(slug='dubai').first()
    if dubai and not dubai.featured_image:
        image_data = download_image(IMAGES['dubai'], 'dubai.jpg')
        if image_data:
            dubai.featured_image.save('dubai-skyline.jpg', ContentFile(image_data), save=True)
            print(f"  [OK] Dubai image saved")


def update_tours():
    """Update tour images"""
    print("\n[Tours] Updating Images...")

    # Egypt & Jordan
    tour1 = Tour.objects.filter(slug='egypt-jordan-discovery').first()
    if tour1 and not tour1.featured_image:
        image_data = download_image(IMAGES['egypt-jordan'], 'egypt-jordan.jpg')
        if image_data:
            tour1.featured_image.save('egypt-jordan-discovery.jpg', ContentFile(image_data), save=True)
            print(f"  [OK] Egypt & Jordan tour image saved")

    # Egypt & Dubai
    tour2 = Tour.objects.filter(slug='egypt-dubai-luxury').first()
    if tour2 and not tour2.featured_image:
        image_data = download_image(IMAGES['egypt-dubai'], 'egypt-dubai.jpg')
        if image_data:
            tour2.featured_image.save('egypt-dubai-luxury.jpg', ContentFile(image_data), save=True)
            print(f"  [OK] Egypt & Dubai tour image saved")


def main():
    print("=" * 50)
    print("Downloading Images for Multi-Destination Content")
    print("=" * 50)

    update_destinations()
    update_tours()

    print("\n" + "=" * 50)
    print("[DONE] All images downloaded!")
    print("=" * 50)

    # Verify
    print("\nVerification:")
    for dest in Destination.objects.filter(slug__in=['jordan', 'dubai']):
        print(f"  {dest.name}: {dest.featured_image.url if dest.featured_image else 'No image'}")

    for tour in Tour.objects.filter(is_multi_destination=True):
        print(f"  {tour.name}: {tour.featured_image.url if tour.featured_image else 'No image'}")


if __name__ == '__main__':
    main()
