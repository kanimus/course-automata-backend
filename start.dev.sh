#!/bin/bash
sleep 10 # sleep 10s to init db
echo "Apply database migrations"
python manage.py migrate
echo "Starting server"
python manage.py runserver 0.0.0.0:8000