#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --no-input

echo "Creating superuser if not exists..."
python manage.py shell -c "
import os
from authentication.models import Author
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'bipulroy')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'bipulroy@admin.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Bipul100\$')
if not Author.objects.filter(username=username).exists():
    Author.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser {username} created.')
else:
    print(f'Superuser {username} already exists.')
"

echo "Starting Gunicorn..."
exec gunicorn first_project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
