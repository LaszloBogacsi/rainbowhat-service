# Rainbowhat Service

## Description
This service helps displaying graphics on an RGB led HAT (Rainbow HAT) attached to a Raspberry PI.

Simple Python 3 + Flask app with a long running task runner.

The task runner is implemented with Celery and RabbitMQ

### RabbitMQ

#### Install RabbitMQ

`$ sudo apt-get install rabbitmq-server`

#### OR Run it with Docker

`$ docker run -d -p 5672:5672 rabbitmq`

### Celery

`pip install celery`

#### Running Celery

`pipenv run celery -A rainbowhat_app.celery worker`



