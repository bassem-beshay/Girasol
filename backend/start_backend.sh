#!/bin/bash
cd /home/bassem/Girasol/backend
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=config.settings.production
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2
