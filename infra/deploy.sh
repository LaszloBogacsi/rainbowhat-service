#!/bin/bash -e

pushd ./deployment > /dev/null
git reset --hard
git pull origin master
pipenv install
pipenv run celery control shutdown
pipenv run celery -A rainbowhat_app.celery worker

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl avail
sudo supervisorctl restart rainbowhat_service