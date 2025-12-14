# Generated manually

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_tourtype_convert_tour_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Addon',
        ),
    ]
