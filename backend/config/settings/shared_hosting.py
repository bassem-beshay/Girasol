"""
Shared Hosting settings for Girasol Tours.
Simple configuration for cPanel/shared hosting.
"""
from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)

# Database - SQLite for shared hosting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Allow both HTTP and HTTPS during development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files - local storage
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Email - console for now (can configure SMTP later)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS - allow frontend domain
CORS_ALLOWED_ORIGINS = [
    'https://girasoltours.com',
    'https://www.girasoltours.com',
    'http://girasoltours.com',
    'http://www.girasoltours.com',
]

CORS_ALLOW_CREDENTIALS = True
