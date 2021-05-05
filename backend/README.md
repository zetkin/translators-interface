# Translators Interface Backend

## System Requirements

- Python 3.8
- virtualenv

## Stack

- [Django](https://docs.djangoproject.com/en/3.2/)

## Setup

```bash
## Create virtual env
python3 -m venv venv
## Activate virtual env
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Setup database
python manage.py migrate

## Run dev server
python manage.py runserver
```

### Admin Interface

The admin interface is used to manage the creation of projects and languages, manage access to the admin interface, and trigger syncing.

To setup an admin account:

```bash
## Create superuser
python manage.py createsuperuser
## Run the dev server
python manage.py runserver
```

Then navigate to `localhost:8000/admin` and log in with the superuser credentials.

### Translation Sync

#### Dotpath generation

Dotpaths, (the path that is used in the frontend of a project to find the localisation string, formatted like `homePage.title`) are generated dynamically from the folder and their location within the object in that folder.

The file path should be formatted like this `./path/to/file/se.yaml`. The object path should be formatted like javascript dot notation: `path.to.key`.
