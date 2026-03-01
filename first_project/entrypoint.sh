#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --no-input

echo "Creating superuser if not exists..."
python manage.py shell -c "
from authentication.models import Author
if not Author.objects.filter(username='bipulroy').exists():
    Author.objects.create_superuser(username='bipulroy', email='bipulroy@admin.com', password='Bipul100\$')
    print('Superuser bipulroy created.')
else:
    print('Superuser bipulroy already exists.')
"

echo "Starting Gunicorn..."
exec gunicorn first_project.wsgi:application --bind 0.0.0.0:8000 --workers 2
