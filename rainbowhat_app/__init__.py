from rainbowhat_app.app import create_app, make_celery

app = create_app()
celery = make_celery(app)

from rainbowhat_app.blueprints.meeting_status import meeting_status

app.register_blueprint(meeting_status)
