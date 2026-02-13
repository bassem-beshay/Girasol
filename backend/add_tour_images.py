"""
Script to add images to tours from Unsplash.
"""
import os
import sys
import django
import requests
from io import BytesIO
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import Tour, TourImage

# Egypt-related Unsplash image IDs for tours
EGYPT_IMAGES = [
    # Pyramids & Giza
    {'id': 'pyramids-1', 'url': 'https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?w=1200', 'caption': 'The Great Pyramids of Giza', 'caption_es': 'Las Grandes Pirámides de Giza', 'caption_pt': 'As Grandes Pirâmides de Gizé'},
    {'id': 'pyramids-2', 'url': 'https://images.unsplash.com/photo-1539650116574-8efeb43e2750?w=1200', 'caption': 'Sphinx and Pyramid at sunset', 'caption_es': 'Esfinge y Pirámide al atardecer', 'caption_pt': 'Esfinge e Pirâmide ao pôr do sol'},
    {'id': 'pyramids-3', 'url': 'https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=1200', 'caption': 'Camel ride near the Pyramids', 'caption_es': 'Paseo en camello cerca de las Pirámides', 'caption_pt': 'Passeio de camelo perto das Pirâmides'},

    # Luxor & Temples
    {'id': 'luxor-1', 'url': 'https://images.unsplash.com/photo-1553913861-c0fddf2619ee?w=1200', 'caption': 'Luxor Temple at night', 'caption_es': 'Templo de Luxor de noche', 'caption_pt': 'Templo de Luxor à noite'},
    {'id': 'karnak-1', 'url': 'https://images.unsplash.com/photo-1565967511849-76a60a516170?w=1200', 'caption': 'Karnak Temple columns', 'caption_es': 'Columnas del Templo de Karnak', 'caption_pt': 'Colunas do Templo de Karnak'},

    # Nile
    {'id': 'nile-1', 'url': 'https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=1200', 'caption': 'Felucca sailing on the Nile', 'caption_es': 'Feluca navegando por el Nilo', 'caption_pt': 'Feluca navegando no Nilo'},
    {'id': 'nile-2', 'url': 'https://images.unsplash.com/photo-1572252009286-268acec5ca0a?w=1200', 'caption': 'Nile River cruise at sunset', 'caption_es': 'Crucero por el Nilo al atardecer', 'caption_pt': 'Cruzeiro no Nilo ao pôr do sol'},

    # Desert
    {'id': 'desert-1', 'url': 'https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=1200', 'caption': 'Sahara Desert landscape', 'caption_es': 'Paisaje del desierto del Sahara', 'caption_pt': 'Paisagem do deserto do Saara'},
    {'id': 'desert-2', 'url': 'https://images.unsplash.com/photo-1451337516015-6b6e9a44a8a3?w=1200', 'caption': 'Desert dunes at golden hour', 'caption_es': 'Dunas del desierto en la hora dorada', 'caption_pt': 'Dunas do deserto na hora dourada'},

    # Red Sea
    {'id': 'redsea-1', 'url': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1200', 'caption': 'Red Sea coral reef', 'caption_es': 'Arrecife de coral del Mar Rojo', 'caption_pt': 'Recife de coral do Mar Vermelho'},
    {'id': 'redsea-2', 'url': 'https://images.unsplash.com/photo-1559827291-72ee739d0d9a?w=1200', 'caption': 'Crystal clear waters of Red Sea', 'caption_es': 'Aguas cristalinas del Mar Rojo', 'caption_pt': 'Águas cristalinas do Mar Vermelho'},

    # Cairo
    {'id': 'cairo-1', 'url': 'https://images.unsplash.com/photo-1572252009286-268acec5ca0a?w=1200', 'caption': 'Cairo cityscape', 'caption_es': 'Paisaje urbano de El Cairo', 'caption_pt': 'Paisagem urbana do Cairo'},
    {'id': 'mosque-1', 'url': 'https://images.unsplash.com/photo-1553913861-c0fddf2619ee?w=1200', 'caption': 'Historic mosque in Cairo', 'caption_es': 'Mezquita histórica en El Cairo', 'caption_pt': 'Mesquita histórica no Cairo'},

    # Abu Simbel
    {'id': 'abusimbel-1', 'url': 'https://images.unsplash.com/photo-1568322445389-f64ac2515020?w=1200', 'caption': 'Abu Simbel Temple', 'caption_es': 'Templo de Abu Simbel', 'caption_pt': 'Templo de Abu Simbel'},

    # Alexandria
    {'id': 'alex-1', 'url': 'https://images.unsplash.com/photo-1539650116574-8efeb43e2750?w=1200', 'caption': 'Alexandria Mediterranean coast', 'caption_es': 'Costa mediterránea de Alejandría', 'caption_pt': 'Costa mediterrânea de Alexandria'},
]


def download_image(url):
    """Download image from URL and return as ContentFile."""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return ContentFile(response.content)
    except Exception as e:
        print(f"    Error downloading: {e}")
    return None


def add_images_to_tours():
    """Add images to tours that don't have any."""
    tours_without_images = Tour.objects.filter(images__isnull=True).distinct()
    total = tours_without_images.count()

    print("="*60)
    print("ADDING IMAGES TO TOURS")
    print("="*60)
    print(f"Tours without images: {total}")

    if total == 0:
        print("All tours already have images!")
        return

    image_index = 0
    added_count = 0

    for i, tour in enumerate(tours_without_images, 1):
        print(f"\n[{i}/{total}] {tour.name[:50]}")

        # Add 3-4 images per tour
        num_images = 3
        for j in range(num_images):
            img_data = EGYPT_IMAGES[image_index % len(EGYPT_IMAGES)]
            image_index += 1

            print(f"  Downloading image {j+1}...", end=" ")

            content = download_image(img_data['url'])
            if content:
                tour_image = TourImage(
                    tour=tour,
                    caption=img_data['caption'],
                    caption_es=img_data['caption_es'],
                    caption_pt=img_data['caption_pt'],
                    alt_text=img_data['caption'],
                    alt_text_es=img_data['caption_es'],
                    alt_text_pt=img_data['caption_pt'],
                    sort_order=j,
                )
                filename = f"tour_{tour.id}_img_{j+1}.jpg"
                tour_image.image.save(filename, content, save=True)
                print("OK")
            else:
                print("FAILED")

        added_count += 1

    print(f"\n{'='*60}")
    print(f"COMPLETED! Added images to {added_count} tours")
    print("="*60)


if __name__ == '__main__':
    add_images_to_tours()
