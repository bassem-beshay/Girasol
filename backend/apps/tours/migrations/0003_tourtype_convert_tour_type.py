# Generated manually for TourType conversion

from django.db import migrations, models
import django.db.models.deletion


def convert_tour_types(apps, schema_editor):
    """Convert old tour_type CharField values to new TourType ForeignKey."""
    Tour = apps.get_model('tours', 'Tour')
    TourType = apps.get_model('tours', 'TourType')

    # Create TourType records for existing values
    type_mapping = {
        'package': ('Package Tour', 'Paquete Turístico', 'Pacote Turístico'),
        'day_tour': ('Day Tour', 'Tour de un Día', 'Passeio de um Dia'),
        'nile_cruise': ('Nile Cruise', 'Crucero por el Nilo', 'Cruzeiro no Nilo'),
        'multi_country': ('Multi-Country Tour', 'Tour Multi-País', 'Tour Multi-País'),
    }

    # Create TourType objects
    created_types = {}
    for slug, (name, name_es, name_pt) in type_mapping.items():
        tour_type, _ = TourType.objects.get_or_create(
            slug=slug,
            defaults={
                'name': name,
                'name_es': name_es,
                'name_pt': name_pt,
                'is_active': True,
                'sort_order': list(type_mapping.keys()).index(slug)
            }
        )
        created_types[slug] = tour_type

    # Update Tour records
    for tour in Tour.objects.all():
        old_type = tour.tour_type_old
        if old_type and old_type in created_types:
            tour.tour_type_new = created_types[old_type]
            tour.save()


def reverse_convert(apps, schema_editor):
    """Reverse the conversion."""
    Tour = apps.get_model('tours', 'Tour')
    for tour in Tour.objects.all():
        if tour.tour_type_new:
            tour.tour_type_old = tour.tour_type_new.slug
            tour.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_remove_tour_description_ar_remove_tour_name_ar_and_more'),
    ]

    operations = [
        # Step 1: Create TourType model
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('name_es', models.CharField(blank=True, max_length=100, verbose_name='Name (Spanish)')),
                ('name_pt', models.CharField(blank=True, max_length=100, verbose_name='Name (Portuguese)')),
                ('description', models.TextField(blank=True)),
                ('icon', models.CharField(blank=True, help_text='Icon class name', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tour Type',
                'verbose_name_plural': 'Tour Types',
                'ordering': ['sort_order', 'name'],
            },
        ),

        # Step 2: Rename old tour_type field
        migrations.RenameField(
            model_name='tour',
            old_name='tour_type',
            new_name='tour_type_old',
        ),

        # Step 3: Add new tour_type ForeignKey field
        migrations.AddField(
            model_name='tour',
            name='tour_type_new',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='tours_new',
                to='tours.tourtype'
            ),
        ),

        # Step 4: Convert data
        migrations.RunPython(convert_tour_types, reverse_convert),

        # Step 5: Remove old field
        migrations.RemoveField(
            model_name='tour',
            name='tour_type_old',
        ),

        # Step 6: Rename new field to tour_type
        migrations.RenameField(
            model_name='tour',
            old_name='tour_type_new',
            new_name='tour_type',
        ),

        # Step 7: Update the related_name
        migrations.AlterField(
            model_name='tour',
            name='tour_type',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='tours',
                to='tours.tourtype'
            ),
        ),
    ]
