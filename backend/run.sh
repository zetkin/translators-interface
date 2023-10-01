#!/usr/bin/env bash

if [[ $ENVIRONMENT == 'production' ]]; 
then
    gunicorn -b 0.0.0.0:8000 --timeout 60 app.wsgi:application
else
    python manage.py runserver 0.0.0.0:8000
fi
