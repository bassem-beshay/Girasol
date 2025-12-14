"""
Django settings for Girasol Tours project.
"""
import os
from pathlib import Path
from datetime import timedelta
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

# Application definition
DJANGO_APPS = [
    'jazzmin',  # Admin theme (must be before django.contrib.admin)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_extensions',
]

LOCAL_APPS = [
    'apps.core',
    'apps.users',
    'apps.tours',
    'apps.destinations',
    'apps.blog',
    'apps.reviews',
    'apps.contact',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='db7'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='root'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_TZ = True

# Supported languages
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('pt', 'Portuguese'),
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'users.User'

# Sites Framework
SITE_ID = 1

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour'
    }
}

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# CORS Configuration
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:3000,http://127.0.0.1:3000',
    cast=Csv()
)
CORS_ALLOW_CREDENTIALS = True

# AllAuth Configuration (Updated for django-allauth 0.63+)
# Use the correct allauth setting names for email-only authentication
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# When using email as the USERNAME_FIELD, usernames are not required
ACCOUNT_USERNAME_REQUIRED = False
# Require email for email-based authentication
ACCOUNT_EMAIL_REQUIRED = True

# DRF Spectacular (API Docs)
SPECTACULAR_SETTINGS = {
    'TITLE': 'Girasol Tours API',
    'DESCRIPTION': 'API for Girasol Tours Egypt - Tourism Management Platform',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/',
}

# Email Configuration
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='Girasol Tours <info@girasoltours.com>')

# Celery Configuration
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND', default='redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Cache Configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://localhost:6379/1'),
    }
}

# Jazzmin Admin Theme Configuration - Professional Navy & Gold Theme
JAZZMIN_SETTINGS = {
    # Title & Branding
    'site_title': 'Girasol Egypt Admin',
    'site_header': 'Girasol Egypt',
    'site_brand': 'Girasol Egypt',
    'site_logo': 'admin/img/logo.png',
    'site_logo_classes': 'img-fluid',
    'site_icon': 'admin/img/favicon.png',
    'login_logo': 'admin/img/logo.png',
    'login_logo_dark': 'admin/img/logo.png',
    'welcome_sign': 'Welcome to Girasol Egypt Admin',
    'copyright': 'Girasol Egypt Travel and Tours',

    # Search in sidebar
    'search_model': ['users.User', 'tours.Tour', 'bookings.Booking'],

    # Top menu links
    'topmenu_links': [
        {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'View Site', 'url': '/', 'new_window': True},
    ],

    # User Menu
    'usermenu_links': [
        {'name': 'Profile', 'url': 'admin:users_user_changelist', 'icon': 'fas fa-user'},
        {'model': 'auth.user'},
    ],

    # Sidebar Configuration
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': ['auth', 'sites', 'authtoken', 'account', 'socialaccount'],
    'hide_models': [],

    # App Ordering
    'order_with_respect_to': [
        'bookings',
        'tours',
        'destinations',
        'users',
        'reviews',
        'blog',
        'contact',
    ],

    # Icons - Professional style
    'icons': {
        'users.User': 'fas fa-users',
        'users.Wishlist': 'fas fa-heart',
        'tours.Tour': 'fas fa-compass',
        'tours.TourCategory': 'fas fa-th-large',
        'tours.TourDeparture': 'fas fa-calendar-alt',
        'tours.Addon': 'fas fa-puzzle-piece',
        'destinations.Destination': 'fas fa-map-marker-alt',
        'destinations.Area': 'fas fa-globe-africa',
        'destinations.Activity': 'fas fa-hiking',
        'bookings.Booking': 'fas fa-ticket-alt',
        'bookings.PromoCode': 'fas fa-percent',
        'blog.Post': 'fas fa-newspaper',
        'blog.Category': 'fas fa-folder-open',
        'blog.Tag': 'fas fa-tags',
        'blog.Comment': 'fas fa-comments',
        'reviews.Review': 'fas fa-star',
        'reviews.Testimonial': 'fas fa-quote-right',
        'contact.Inquiry': 'fas fa-envelope-open-text',
        'contact.Newsletter': 'fas fa-mail-bulk',
        'contact.FAQ': 'fas fa-question-circle',
        'contact.Office': 'fas fa-building',
    },

    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-arrow-right',

    # Related Modal
    'related_modal_active': True,

    # Custom CSS
    'custom_css': 'admin/css/custom_admin.css',
    'custom_js': None,

    # Fonts
    'use_google_fonts_cdn': True,

    # UI Builder
    'show_ui_builder': False,

    # Change View
    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {
        'tours.Tour': 'vertical_tabs',
        'bookings.Booking': 'vertical_tabs',
        'destinations.Destination': 'vertical_tabs',
    },

    # Language
    'language_chooser': False,
}

# Jazzmin UI Tweaks - Professional Navy Theme
JAZZMIN_UI_TWEAKS = {
    # Text sizes
    'navbar_small_text': False,
    'footer_small_text': True,
    'body_small_text': False,
    'brand_small_text': False,

    # Navbar
    'brand_colour': 'navbar-dark',
    'accent': 'accent-warning',
    'navbar': 'navbar-dark',
    'no_navbar_border': True,

    # Layout
    'navbar_fixed': True,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,

    # Sidebar - Dark Navy theme
    'sidebar': 'sidebar-dark-warning',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': True,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,

    # Theme - Using default (will be overridden by custom CSS)
    'theme': 'default',
    'dark_mode_theme': None,

    # Buttons - Professional colors
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-primary',
    },

    # Actions
    'actions_sticky_top': True,
}

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
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
            'level': config('DJANGO_LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
    },
}
