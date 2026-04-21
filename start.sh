#!/usr/bin/env bash

python manage.py migrate

echo "Creating superuser if not exists..."

python manage.py shell << END
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print("Superuser created")
    else:
        print("Superuser already exists")
END

gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT




#!/usr/bin/env bash

#python manage.py migrate

# echo "from django.contrib.auth import get_user_model;
# User = get_user_model();
# User.objects.filter(username='Yogesh').exists() or
# User.objects.create_superuser('Yogesh', 'yogesh@gmail.com', 'yogesh@123')" | python manage.py shell

# gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
