#!/bin/bash
ls
cd app
ls
# Запуск миграций Django
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate

daphne app.asgi:application --port 8000 --bind 0.0.0.0

# python manage.py runserver 0.0.0.0:8000