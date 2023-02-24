# Support service application

## Adjust the application

### Install deps

```bash
# Install pipenv
# https://pipenv.pypa.io/en/latest/
pip install pipenv
```

### Activate the environment

```bash
# Activate virtual env
pipenv shell
```

```bash
# Regenerate Pipfile.lock file
pipenv lock
```

```bash
# pipenv lock & pipenv sync
pipenv update
```

```bash
# pipenv sync
pipenv sync --dev
```

### Code quality tools

```bash
# https://pypi.org/project/flake8/
flake8

# https://pypi.org/project/black/
black

# https://pypi.org/project/isort/
isort
```

### Install framework

```bash
# https://pypi.org/project/Django/
Django
```

### Install additional packages

```bash
# https://pypi.org/project/psycopg-binary/
psycopg2-binary

# https://pypi.org/project/Pillow/
Pillow

# https://pypi.org/project/django-debug-toolbar/
django-debug-toolbar

# https://pypi.org/project/django-ckeditor/
django-ckeditor

# https://pypi.org/project/python-dotenv/
python-dotenv
```

## Creates a Django project

Create a folder src.
Creates a Django project directory structure for the given project name in the current directory or the given destination.

```bash
# https://docs.djangoproject.com/en/4.1/ref/django-admin/
django-admin startproject config src/
```

```bash
scr/
    config/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
```

### The development server

Run the following commands:

```bash
python src/manage.py runserver
```

## Creates a Django apps

Creates a Django apps

```bash
django-admin startapp exchange_rates
```

Open up config/settings.py

```bash
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# Local
"exchange_rates.apps.ExchangeRatesConfig", # new
]
```

## Workflow

Django can create migrations for you. Make changes to your models - say, add a field and remove a model - and then run makemigrations:

``` python
python manage.py makemigrations
```

Once you have your new migration files, you should apply them to your database to make sure they work as expected:

``` python
python manage.py migrate
```

Set the STATIC_ROOT setting to the directory from which you’d like to serve these files, for example:

``` python
STATIC_ROOT = ROOT_DIR / "support_an/staticfiles"
```

Run the collectstatic management command:

```python
python src/manage.py collectstatic
```
