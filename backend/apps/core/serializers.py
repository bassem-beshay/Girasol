"""
Core serializer mixins for language support.
"""
from rest_framework import serializers


class MultiLanguageSerializerMixin:
    """
    Mixin to automatically select the correct language field based on Accept-Language header.

    Usage:
    1. Add this mixin to your serializer class
    2. Define TRANSLATABLE_FIELDS = ['name', 'description', ...] in your serializer

    The mixin will:
    - Read the Accept-Language header from the request
    - For each field in TRANSLATABLE_FIELDS, return the localized version
    - Fallback to English (base field) if translation not available
    """

    # Define which fields have translations (_es, _pt suffixes)
    TRANSLATABLE_FIELDS = []

    def to_representation(self, instance):
        """Override to include localized fields."""
        data = super().to_representation(instance)

        # Get language from request context
        request = self.context.get('request')
        language = 'en'

        if request:
            # Try Accept-Language header first
            accept_lang = request.headers.get('Accept-Language', 'en')
            if accept_lang in ['es', 'pt', 'en']:
                language = accept_lang

        # If language is English, no changes needed (base fields are in English)
        if language == 'en':
            # Remove the language suffixed fields from response
            for field in self.TRANSLATABLE_FIELDS:
                data.pop(f'{field}_es', None)
                data.pop(f'{field}_pt', None)
            return data

        # For other languages, replace base field with translated version
        for field in self.TRANSLATABLE_FIELDS:
            localized_field = f'{field}_{language}'

            # Get the localized value
            localized_value = getattr(instance, localized_field, None)

            # If translation exists and is not empty, use it
            if localized_value:
                data[field] = localized_value

            # Remove the language suffixed fields from response
            data.pop(f'{field}_es', None)
            data.pop(f'{field}_pt', None)

        return data


class LocalizedSerializer(MultiLanguageSerializerMixin, serializers.ModelSerializer):
    """
    Base serializer class with language support built-in.
    Extend this instead of ModelSerializer for models with translations.
    """
    pass
