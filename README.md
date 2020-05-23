# Rainbowhat Service

## Description
This service helps displaying graphics on an RGB led HAT (Rainbow HAT) attached to a Raspberry PI through a web interface

Simple Python 3 + Flask app with a long running task runner.

The task runner implements a solution with Celery and RabbitMQ

## RabbitMQ

### Install RabbitMQ

`$ sudo apt-get install rabbitmq-server`

### OR Run it with Docker

`$ docker run -d -p 5672:5672 rabbitmq`

### Install Docker
Download Docker  
`curl -fsSL https://get.docker.com -o get-docker.sh`  
Install  
`sudo sh get-docker.sh`  
Add the Pi user to the Docker user group  
`sudo usermod -aG docker Pi`

## Celery

#### Install Celery

`pipenv install celery`

#### Running Celery

`pipenv run celery -A rainbowhat_app.celery worker`

This starts a worker node. The worker instance object is in `rainbowhat_app.celery` with the configuration.

## Running it on Raspberry Pi

### Supervisor config

Copy `infra/rainbowhat_service.conf` from the project to `/etc/supervisor/conf.d/` on the PI

### Nginx config
Copy `infra/rainbowhat-app.conf` to `/etc/nginx/sites-enabled/rainbowhat-app.conf`

And restart Nginx  
`service nginx restart`

### Client computer config
edit the `/etc/host` file and add

```shell script
192.1681.205 meeting.status;
```

### Deployment

add symlink to the `infra/deploy.sh` from the Raspberry PI service folder.

Run the deploy script

the deploy script 
- cd to deployment
- pulls the latest code
- installs dependencies
- restart celery
- restart supervisor
- assumes Rabbit MQ is running in docker


