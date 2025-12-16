#!/home4/girasolt/girasol/backend/venv/bin/python3
import os
import sys

# Add the backend directory to the path
sys.path.insert(0, '/home4/girasolt/girasol/backend')
sys.path.insert(0, '/home4/girasolt/girasol/backend/venv/lib/python3.9/site-packages')

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.shared_hosting')

# Setup Django BEFORE importing WSGI application
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
