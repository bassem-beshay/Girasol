"""
User serializers for API.
"""
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'bio', 'emergency_contact_name', 'emergency_contact_phone',
            'emergency_contact_relation', 'dietary_requirements',
            'medical_conditions', 'special_requests'
        ]


class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile = UserProfileSerializer(read_only=True)
    full_name = serializers.CharField(read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'full_name',
            'phone', 'country', 'avatar', 'preferred_language',
            'newsletter_subscribed', 'date_of_birth', 'nationality',
            'profile', 'created_at'
        ]
        read_only_fields = ['id', 'email', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone',
            'country', 'avatar', 'preferred_language', 'newsletter_subscribed',
            'date_of_birth', 'nationality', 'passport_number', 'profile'
        ]
        read_only_fields = ['id', 'email']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone', 'country', 'avatar',
            'preferred_language', 'newsletter_subscribed', 'date_of_birth',
            'nationality', 'passport_number'
        ]
