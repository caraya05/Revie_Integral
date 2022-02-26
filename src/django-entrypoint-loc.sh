#!/bin/bash
echo "Waiting for postgres..."
while ! nc -z postgres 5432; do
  sleep 0.5
done
echo "PostgreSQL started"
python manage.py runserver 0.0.0.0:8000
exec "$@"