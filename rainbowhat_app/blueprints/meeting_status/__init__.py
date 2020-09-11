from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from rainbowhat_app.graphics_runner import run_graphics

meeting_status = Blueprint('meeting_status', __name__,
                           template_folder='templates')

result = None


@meeting_status.route('/meeting', methods=['GET'])
def show_meeting_status():
    try:

        return render_template('meeting/index.html', active_status="on" if result is not None else "off")
    except TemplateNotFound:
        abort(404)


@meeting_status.route('/meeting/<status>')
def meeting_on(status: str):
    global result
    from flask import current_app
    if to_state(status) and result is None:
        result = run_graphics.delay()
    elif not to_state(status) and result is not None:
        current_app.logger.info(result)
        current_app.logger.info("Terminating process")
        result.revoke(terminate=True, signal='SIGINT')
        result = None
    return render_template('meeting/index.html', active_status=status)


def to_state(status) -> bool:
    return status.lower() == "on"
