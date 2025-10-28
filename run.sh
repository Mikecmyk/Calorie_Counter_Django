#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --no-input

echo "Starting Gunicorn server..."
exec gunicorn calorie_counter_project.wsgi