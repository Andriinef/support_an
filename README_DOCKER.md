# Setting up a Django API with Pipenv, Docker

This repository contains the code and configuration files to set up a Django API server using Pipenv, Docker, Docker Compose, Gunicorn, and Celery running on Amazon SQS.

## Prerequisites

Before you begin, make sure you have the following installed:

* Docker

    ```html
    https://docs.docker.com/engine/install/
    ```

* Docker Compose

    ```html
    https://docs.docker.com/compose/install/
    ```

* Pipenv

    ```html
    https://pipenv.pypa.io/en/latest/install/
    ```

* An Amazon Web Services (AWS) account with permissions to create an Amazon SQS queue and access keys with the appropriate permissions.

## Getting Started

1. Clone this repository to your local machine.

    ```code
    git clone git@github.com:Andriinef/support_an.git
    ```

2. Change into the project directory.

    ```code
    cd support_an
    ```

3. Install the project dependencies using Pipenv.

    ```code
    pipenv install
    ```

4. Copy the .env.default file and rename it to .env.

    ```code
    cp .env.default .env
    ```

5. Run the Docker Compose command to start the Django API server, Gunicorn, and Celery worker.

    ```code
    docker-compose up -d --build
    ```

6. You should now be able to access the API at "http://0.0.0.0:8000."

## Deployment

To deploy the API to a production environment, follow the steps described in the file README_DEPLOY.md
