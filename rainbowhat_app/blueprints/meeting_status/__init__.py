from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from rainbowhat_app.graphics_runner import run_graphics

meeting_status = Blueprint('meeting_status', __name__,
                           template_folder='templates')

result = None


@meeting_status.route('/meeting', methods=['GET'])
def show_meeting_status():
    try:
        return render_template('meeting/index.html', status="on" if result is not None else "off")
    except TemplateNotFound:
        abort(404)


@meeting_status.route('/meeting/<status>')
def meeting_on(status: str):
    global result

    if to_state(status) and result is None:
        result = run_graphics.delay()
    elif not to_state(status) and result is not None:
        result.revoke(terminate=True, signal='SIGUSR1')
        result = None
    return render_template('meeting/index.html', status=status)


def to_state(status) -> bool:
    return status.lower() == "on"
