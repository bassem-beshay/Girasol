"""
Shared Hosting settings for Girasol Tours.
Simple configuration for cPanel/shared hosting.
"""
import pymysql
pymysql.install_as_MySQLdb()

from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS for production
ALLOWED_HOSTS = [
    'girasoltours.com',
    'www.girasoltours.com',
    'api.girasoltours.com',
    'girasoltours.com.eg',
    'www.girasoltours.com.eg',
    'localhost',
    '127.0.0.1',
]

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

# Cache - Local memory (no Redis needed)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
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
STATIC_URL = '/static/'
# Override STATICFILES_DIRS - don't require 'static' folder on shared hosting
STATICFILES_DIRS = []

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

# CSRF Trusted Origins (required for Django 4.0+, safe for Django 3.2)
CSRF_TRUSTED_ORIGINS = [
    'https://girasoltours.com',
    'https://www.girasoltours.com',
    'http://girasoltours.com',
    'http://www.girasoltours.com',
]

# Logging for debugging on shared hosting
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django_error.log',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
