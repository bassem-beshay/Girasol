import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.tours.models import Tour
from django.conf import settings

print("Database settings:", settings.DATABASES['default']['NAME'])
print("")

# Check all tours
tours = Tour.objects.all()
print(f"All Tours ({tours.count()}):")
for t in tours:
    print(f"  - {t.name}: published={t.is_published}")

print("")

# Check published tours
published = Tour.objects.filter(is_published=True)
print(f"Published Tours ({published.count()}):")
for t in published:
    print(f"  - {t.name}")
