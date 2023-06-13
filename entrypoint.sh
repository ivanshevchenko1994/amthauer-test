#!/bin/bash
poetry run python manage.py makemigrations --noinput
poetry run python manage.py migrate --noinput
poetry run python manage.py collectstatic --noinput
poetry run uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload