# Translators Interface Backend

## System Requirements

- Python 3.8
- virtualenv

## Stack

- [Django](https://docs.djangoproject.com/en/3.2/)
- [PyGithub](https://github.com/PyGithub/PyGithub)

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

To trigger a sync with a django management command, use `python manage.py syncproject <project_name>`. This action is also available in the admin interface.

#### Accessing Github

Accessing github requires an access token, which must be set in a `.env` file. The key for the access token is `GITHUB_ACCESS_TOKEN`.

#### Dotpath generation

Dotpaths, (the path that is used in the frontend of a project to find the localisation string, formatted like `homePage.title`) are generated dynamically from the folder and their location within the object in that folder.
