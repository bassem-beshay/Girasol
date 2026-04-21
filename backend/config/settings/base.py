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

# Allow same-origin iframes so Jazzmin related-object popups render in admin.
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Frontend URL for email links
FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:3000')

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
    'django_ckeditor_5',
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
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=False, cast=bool)
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:3000,http://127.0.0.1:3000',
    cast=Csv()
)
CORS_ALLOW_CREDENTIALS = True

# CSRF Trusted Origins (required for Django 4.0+)
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://localhost:3000,http://127.0.0.1:3000',
    cast=Csv()
)

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
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='Girasol Tours <hello@girasoltours.com>')

# Google reCAPTCHA v3 Configuration
RECAPTCHA_SITE_KEY = config('RECAPTCHA_SITE_KEY', default='')
RECAPTCHA_SECRET_KEY = config('RECAPTCHA_SECRET_KEY', default='')

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
        'BACKEND': config('CACHE_BACKEND', default='django.core.cache.backends.locmem.LocMemCache'),
        'LOCATION': config('CACHE_LOCATION', default='unique-snowflake'),
    }
}

# Jazzmin Admin Theme Configuration - Professional Navy & Gold Theme
JAZZMIN_SETTINGS = {
    # Title & Branding
    'site_title': 'Girasol Tours',
    'site_header': 'Girasol Tours',
    'site_brand': 'Girasol Tours',
    'site_logo': 'admin/img/logo.png',
    'site_logo_classes': 'img-fluid',
    'site_icon': 'admin/img/favicon.png',
    'login_logo': 'admin/img/login-logo.jpeg',
    'login_logo_dark': 'admin/img/login-logo.jpeg',
    'welcome_sign': 'Welcome to Girasol Tours Dashboard',
    'copyright': 'Girasol Egypt Travel and Tours',

    # Search
    'search_model': [],

    # Top menu
    'topmenu_links': [],

    # User Menu
    'usermenu_links': [
        {'name': 'View Site', 'url': 'https://www.girasoltours.com', 'new_window': True, 'icon': 'fas fa-globe'},
    ],

    # Sidebar
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': ['auth', 'sites', 'authtoken', 'account', 'socialaccount', 'reviews'],
    'hide_models': ['tours.TourCategory', 'blog.Comment'],

    # App Ordering - logical flow
    'order_with_respect_to': [
        'tours',
        'destinations',
        'blog',
        'contact',
        'users',
        'admin',
    ],

    # Icons
    'icons': {
        # Tours
        'tours.Tour': 'fas fa-route',
        'tours.TourCategory': 'fas fa-th-large',
        'tours.TourType': 'fas fa-tags',
        'tours.EarlyBookingOffer': 'fas fa-percentage',
        # Destinations
        'destinations.Destination': 'fas fa-map-marked-alt',
        'destinations.Activity': 'fas fa-hiking',
        # Blog
        'blog.Post': 'fas fa-pen-fancy',
        'blog.Category': 'fas fa-folder-open',
        'blog.Tag': 'fas fa-hashtag',
        'blog.Comment': 'fas fa-comments',
        # Contact
        'contact.Inquiry': 'fas fa-envelope-open-text',
        'contact.Newsletter': 'fas fa-mail-bulk',
        'contact.NewsletterCampaign': 'fas fa-paper-plane',
        'contact.FAQ': 'fas fa-question-circle',
        'contact.Office': 'fas fa-map-pin',
        'contact.Statistic': 'fas fa-chart-bar',
        # Users
        'users.User': 'fas fa-users-cog',
        # Reviews (hidden but keep icons)
        'reviews.Review': 'fas fa-star',
        'reviews.Testimonial': 'fas fa-quote-right',
        # Admin
        'admin.LogEntry': 'fas fa-history',
    },

    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-arrow-right',

    # Related Modal
    'related_modal_active': True,

    # Custom CSS/JS
    'custom_css': 'admin/css/custom_admin.css',
    'custom_js': 'admin/js/custom_admin.js',

    # Fonts
    'use_google_fonts_cdn': True,

    # UI Builder
    'show_ui_builder': False,

    # Change View
    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {
        'tours.Tour': 'horizontal_tabs',
        'destinations.Destination': 'horizontal_tabs',
        'blog.Post': 'horizontal_tabs',
    },

    'language_chooser': False,
}

# CKEditor 5 - rich text editor for admin (blog content, tour descriptions, etc.)
CKEDITOR_5_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
CKEDITOR_5_UPLOAD_FILE_TYPES = ['jpeg', 'jpg', 'png', 'gif', 'webp']
CKEDITOR_5_CUSTOM_CSS = 'admin/css/ckeditor5_custom.css'
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'underline', 'link', '|',
            'alignment', '|',
            'bulletedList', 'numberedList', 'blockQuote', '|',
            'outdent', 'indent', '|',
            'undo', 'redo',
        ],
        'alignment': {
            'options': ['left', 'right', 'center', 'justify'],
        },
        'link': {
            'addTargetToExternalLinks': True,
            'defaultProtocol': 'https://',
            'decorators': {
                'openInNewTab': {
                    'mode': 'manual',
                    'label': 'Open in new tab (external)',
                    'attributes': {'target': '_blank', 'rel': 'noopener noreferrer'},
                },
                'isInternal': {
                    'mode': 'manual',
                    'label': 'Internal link (same tab)',
                    'attributes': {'data-internal': 'true'},
                },
            },
        },
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|', 'bulletedList', 'numberedList',
            '|', 'blockQuote',
        ],
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'underline', 'strikethrough', '|',
            'fontFamily', 'fontSize', 'fontColor', 'fontBackgroundColor', '|',
            'link', 'bulletedList', 'numberedList', '|',
            'alignment', 'outdent', 'indent', '|',
            'blockQuote', 'insertImage', 'horizontalLine', '|',
            'removeFormat', 'sourceEditing', '|',
            'undo', 'redo',
        ],
        'alignment': {
            'options': ['left', 'right', 'center', 'justify'],
        },
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side'],
            'styles': ['full', 'side', 'alignLeft', 'alignRight', 'alignCenter'],
        },
        'link': {
            'addTargetToExternalLinks': True,
            'defaultProtocol': 'https://',
            'decorators': {
                'openInNewTab': {
                    'mode': 'manual',
                    'label': 'Open in new tab (external)',
                    'attributes': {'target': '_blank', 'rel': 'noopener noreferrer'},
                },
                'isInternal': {
                    'mode': 'manual',
                    'label': 'Internal link (same tab)',
                    'attributes': {'data-internal': 'true'},
                },
            },
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4'},
            ],
        },
        'fontSize': {
            'options': [9, 11, 13, 'default', 17, 19, 21, 24, 28, 32],
            'supportAllValues': True,
        },
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Lucida Sans Unicode, Lucida Grande, sans-serif',
                'Tahoma, Geneva, sans-serif',
                'Times New Roman, Times, serif',
                'Trebuchet MS, Helvetica, sans-serif',
                'Verdana, Geneva, sans-serif',
            ],
            'supportAllValues': True,
        },
    },
}

# Jazzmin UI Tweaks - Professional Navy Theme
JAZZMIN_UI_TWEAKS = {
    # Text
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
    'navbar_fixed': False,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,

    # Sidebar
    'sidebar': 'sidebar-dark-warning',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': True,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,

    # Theme
    'theme': 'default',
    'dark_mode_theme': None,

    # Buttons
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success',
    },
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
