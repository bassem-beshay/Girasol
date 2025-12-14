import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()

from apps.tours.models import Tour
from apps.destinations.models import Destination

print('Total tours:', Tour.objects.count())
print('Published tours:', Tour.objects.filter(is_published=True).count())
print('')

for t in Tour.objects.all():
    print(f'- {t.name}: is_published={t.is_published}')
