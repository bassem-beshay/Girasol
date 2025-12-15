"""
Shared Hosting settings for Girasol Tours.
Simple configuration for cPanel/shared hosting.
"""
import pymysql
pymysql.install_as_MySQLdb()

from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)

# Database - MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'girasolt_gira',
        'USER': 'girasolt_db9',
        'PASSWORD': '852456312002Bassem*',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
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
