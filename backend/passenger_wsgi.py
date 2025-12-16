import os
import sys

# Get the directory of this file
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the backend directory to the path
sys.path.insert(0, BACKEND_DIR)

# Try to add virtualenv site-packages if exists
VENV_SITE_PACKAGES = os.path.join(BACKEND_DIR, 'venv', 'lib', 'python3.9', 'site-packages')
if os.path.exists(VENV_SITE_PACKAGES):
    sys.path.insert(0, VENV_SITE_PACKAGES)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.shared_hosting')

# Import and setup Django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
