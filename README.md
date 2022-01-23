# Hillel REST API application

## Setup

## Mandatory steps

1. Install Python3.9+
2. Install Pipenv

## Setup project

Setup environment 
```bash
# Create virtual environment
pipenv install
# pipenv install --dev
pipenv shell

# On manual setup install Django, Django REST Framework
pipenv install django djangorestframework

# On setup cloned project sync virtual environment
pipenv sync
```


Start Django server
```bash
# Run migrations only on a project setup
python manage.py migrate

# Run server
python manage.py runserver
```