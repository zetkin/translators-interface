#!/usr/bin/env bash

if [[ $ENVIRONMENT == 'dev' ]]; then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn -b 0.0.0.0:8000 app.wsgi:application
fi