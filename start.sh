#!/usr/bin/env bash

python manage.py migrate

echo "from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.filter(username='Yogesh').exists() or
User.objects.create_superuser('Yogesh', 'admin@gmail.com', 'yogesh@123')" \
| python manage.py shell

gunicorn backend.wsgi:application