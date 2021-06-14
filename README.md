# Translator Interface

Monorepo for the full stack implementation of the Zetkin Translator Interface.

[Django Backend](./backend)

[React Next Frontend](./frontend)

## Running locally for development using docker-compose

Requires:

-   Docker
-   docker-compose

To start the dev environment with docker for the first time:

1. Copy `.env.development-sample` to `.env` and enter API access tokens as needed.

2. Update your hosts file at `/etc/hosts` to map `django` to 127.0.0.1

3. Run the following code in the terminal.

```sh
# Build and start
docker-compose up --build -d

# See the logs for all services
docker-compose logs -f

# Set up database
docker-compose exec django python manage.py migrate

# Create a superuser for Django Admin
docker-compose exec django python manage.py createsuperuser
```

## Features

-   Django Admin
    -   Admin Model Pages
        -   Project
            -   Sync project
                -   Imports translation objects from a project
            -   Export translation files
                -   Download a zip file of the generated YAML locale files for a project with the latest translations.
            -   CRUD operations for project model
        -   Language
            -   CRUD operations for language model
        -   Translation
            -   CRUD operations for translation model
        -   Users
            -   User management for access to the admin interface
-   Web Application
    -   Projects page
        -   View all projects
        -   Click through to project detail and edit translations page
    -   Project detail page
        -   View project details and click through to edit translations page for each language
    -   Edit translations page
        -   Shows the dotpath and "base" translations (always English)
        -   Lists
