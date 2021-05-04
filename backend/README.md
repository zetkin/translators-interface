# Translators Interface Backend

## System Requirements

- Python 3.8
- virtualenv

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
```

## Stack

- [Django](https://docs.djangoproject.com/en/3.2/)
