#!/bin/sh

python3 manage.py migrate

gunicorn Airdev.wsgi:application --bind 0.0.0.0:8000