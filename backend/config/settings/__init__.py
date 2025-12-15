import os

# Only import base settings here
# Specific settings (local, shared_hosting, production) should be set via DJANGO_SETTINGS_MODULE
from .base import *

# Only auto-import local settings if no specific settings module is set
settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', '')
if settings_module == 'config.settings' or not settings_module:
    try:
        from .local import *
    except ImportError:
        pass
