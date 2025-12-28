"""
Migration for Newsletter Double Opt-In feature.
Adds confirmation_token, unsubscribe_token, is_confirmed, and tracking fields.
"""
import uuid
from django.db import migrations, models


def generate_tokens(apps, schema_editor):
    """Generate unique tokens for existing subscribers."""
    Newsletter = apps.get_model('contact', 'Newsletter')
    for subscriber in Newsletter.objects.all():
        subscriber.confirmation_token = uuid.uuid4()
        subscriber.unsubscribe_token = uuid.uuid4()
        # Mark existing subscribers as confirmed since they were already subscribed
        subscriber.is_confirmed = True
        subscriber.save()


def reverse_tokens(apps, schema_editor):
    """Reverse migration - no action needed."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_statistic'),
    ]

    operations = [
        # Step 1: Add fields without unique constraint first
        migrations.AddField(
            model_name='newsletter',
            name='confirmation_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='unsubscribe_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='confirmed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='confirmation_sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='emails_sent',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='last_email_sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),

        # Step 2: Generate unique tokens for existing records
        migrations.RunPython(generate_tokens, reverse_tokens),

        # Step 3: Now make the fields non-nullable and unique
        migrations.AlterField(
            model_name='newsletter',
            name='confirmation_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='unsubscribe_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
