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
python src/manage.py makemigrations
```

Once you have your new migration files, you should apply them to your database to make sure they work as expected:

``` python
python src/manage.py migrate
```

Set the STATIC_ROOT setting to the directory from which you’d like to serve these files, for example:

``` python
STATIC_ROOT = ROOT_DIR / "support_an/staticfiles"
```

Run the collectstatic management command:

```python
python src/manage.py collectstatic
```

## Celery and Redis

Here's an example of how to use Celery in a Django API:

1. Install Celery and Redis: You can install Celery using Pipenv by running the following command in your project directory:

    ```code
    pipenv install celery redis
    ```

2. Create a Celery app: Create a new file named celery.py in your project directory with the following contents:

    ``` python
    import os
    from time import sleep

    from celery import Celery

    # Set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    celery_app = Celery('config')

    # Using a string here means the worker doesn't have to serialize
    # the configuration object to child processes.
    # - namespace='CELERY' means all celery-related configuration keys
    #   should have a 'CELERY_' prefix.
    celery_app.config_from_object('django.conf:settings', namespace='CELERY')

    # Load task modules from all registered Django app configs.
    celery_app.autodiscover_tasks()

    @celery_app.task(bind=True)
    def debug_task(self):
        sleep(7)
        print(f'Request: {self.request!r}')
    ```

3. Create a new file named __init__.py in your project directory with the following contents:

    ```python
    from config.celery import celery_app

    __all__ = ("celery_app",)
    ```

4. Configure Django to use Redis: In your Django project's settings.py file, add the following lines to configure Django to use Redis as the message broker and result backend for Celery:

    ```python
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    ```

5. Create a docker-compose.yml file: Create a new file named docker-compose.yml in your project directory with the following contents:

    ```code
    services:
        redis:
        image: redis
        container_name: "support_redis"
        ports:
            - "6379:6379"
    ```

6. Use the task in your views: In one of your Django views, import the Celery task and call it using the delay method. For example:

    ```python
     def list(self, request, *args, **kwargs) -> Response:

        # This task bloks I/O
        hello_task.delay()

        if request.user.role == Role.ADMIN:
            queryset = self.get_queryset()
        elif request.user.role == Role.MANAGER:
            queryset = Ticket.objects.filter(manager=request.user)
        else:
            queryset = Ticket.objects.filter(customer=request.user)

        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)
    ```

7. Start the Celery worker: In a separate terminal window, start the Celery worker by running the following command in your project directory:

    ```code
    celery -A myproject worker -l info
    ```

    This command starts the Celery worker, which will process any tasks that you call using the delay method.
