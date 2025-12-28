"""
Contact serializers for API.
"""
from rest_framework import serializers
from .models import Inquiry, Newsletter, FAQ, Office, Statistic


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            'name', 'email', 'phone', 'country',
            'inquiry_type', 'subject', 'message',
            'tour', 'travel_date', 'travelers', 'budget',
            'source', 'utm_source', 'utm_medium', 'utm_campaign'
        ]


class NewsletterSerializer(serializers.ModelSerializer):
    """
    Serializer for newsletter subscription.
    Creates new subscribers with is_confirmed=False for Double Opt-In.
    """
    class Meta:
        model = Newsletter
        fields = ['email', 'name', 'interests', 'source']

    def validate_email(self, value):
        """Normalize email to lowercase."""
        return value.lower().strip()

    def create(self, validated_data):
        """
        Create new subscriber with is_confirmed=False.
        The confirmation email will be sent separately via Celery.
        """
        email = validated_data['email']

        # Create new subscriber (not confirmed yet)
        newsletter = Newsletter.objects.create(
            email=email,
            name=validated_data.get('name', ''),
            interests=validated_data.get('interests', ''),
            source=validated_data.get('source', 'website'),
            is_confirmed=False,  # Will be confirmed via email
            is_active=True
        )

        return newsletter


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = [
            'id', 'question', 'question_es', 'question_pt',
            'answer', 'answer_es', 'answer_pt', 'category'
        ]


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = [
            'id', 'name', 'city', 'address', 'phone', 'email', 'whatsapp',
            'latitude', 'longitude', 'working_hours', 'is_headquarters'
        ]


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = [
            'id', 'value', 'label', 'label_es', 'label_pt',
            'icon', 'description', 'sort_order'
        ]
