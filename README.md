# Translator Interface

Monorepo for the full stack implementation of the Zetkin Translator Interface.

[Django Backend](./backend)

[React Next Frontend](./frontend)

## Running locally for development

There are 2 ways to run in development:

1. Follow the instructions in each directory, and start the local dev environments for each service that way.
2. Use docker-compose to run everything in docker containers.

### Using docker-compose

Requires:

- Docker
- docker-compose

To start the dev environment with docker for the first time:

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

If using docker-compose, you need to update your hosts file at `/etc/hosts` to map `django` to 127.0.0.1.
