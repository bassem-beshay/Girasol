"""
One-time script to update statistic labels for ES/PT translations.
Run from backend directory with: python manage.py shell < update_stats.py
"""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django.setup()

from apps.contact.models import Statistic

# Mapping: English label -> (Spanish label, Portuguese label)
label_updates = {
    'Years of Experience': ('Años de Experiencia', 'Anos de Experiência'),
    'Happy Travelers': ('Viajeros Felices', 'Viajantes Felizes'),
    'Satisfaction Rate': ('Tasa de Satisfacción', 'Taxa de Satisfação'),
    'Average Rating': ('Calificación Promedio', 'Avaliação Média'),
    'Tour Packages': ('Paquetes de Tours', 'Pacotes de Tours'),
    'Partner Countries': ('Países Socios', 'Países Parceiros'),
    'Destinations': ('Destinos', 'Destinos'),
    'Local Offices': ('Oficinas Locales', 'Escritórios Locais'),
}

updated = 0
for stat in Statistic.objects.all():
    label = stat.label.strip()
    if label in label_updates:
        es, pt = label_updates[label]
        stat.label_es = es
        stat.label_pt = pt
        stat.save()
        print(f"Updated: {label} -> ES: {es}, PT: {pt}")
        updated += 1
    else:
        print(f"Skipped (no mapping): {label} (current ES: {stat.label_es}, PT: {stat.label_pt})")

print(f"\nDone. Updated {updated} statistics.")
