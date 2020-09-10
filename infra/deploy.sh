#!/bin/bash -e

pushd ./deployment > /dev/null
echo "resetting head to and discarding changes..."
git reset --hard
echo "pulling latest master..."
git pull origin master
echo "Pipenv, install project dependencies..."
pipenv install
echo "shutting down celery..."
pipenv run celery control shutdown || true
wait
echo "starting new celery worker"
pipenv run celery -A rainbowhat_app.celery worker &

echo "Update supervisor and restart app"
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl avail
sudo supervisorctl restart rainbowhat_service