import os
import sys

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.shared_hosting'

# Import and setup Django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
