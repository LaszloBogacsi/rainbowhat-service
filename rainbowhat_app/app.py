import os

from flask import Flask
from celery import Celery

root_folder = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(root_folder, 'static')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_folder=static_folder, root_path=root_folder)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.update(
        CELERY_BROKER_URL='amqp://localhost:5672',
        CELERY_RESULT_BACKEND='amqp://localhost:5672'
    )

    return app

 # TODO: Remove Celery from the project along with RabbitMQ from the PI
def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask

    return celery


