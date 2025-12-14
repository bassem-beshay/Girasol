"""
Contact serializers for API.
"""
from rest_framework import serializers
from .models import Inquiry, Newsletter, FAQ, Office


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
    class Meta:
        model = Newsletter
        fields = ['email', 'name', 'interests', 'source']

    def create(self, validated_data):
        email = validated_data['email']
        # Update if exists, create if not
        newsletter, created = Newsletter.objects.update_or_create(
            email=email,
            defaults={
                'name': validated_data.get('name', ''),
                'interests': validated_data.get('interests', ''),
                'source': validated_data.get('source', 'website'),
                'is_active': True
            }
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
