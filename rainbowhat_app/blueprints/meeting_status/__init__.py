from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# from rainbowhat_app.graphics_runner import run_graphics
from rainbowhat_app.graphics_runner import GraphicsExecutor

meeting_status = Blueprint('meeting_status', __name__,
                           template_folder='templates')

result = None


@meeting_status.route('/meeting', methods=['GET'])
def show_meeting_status():
    try:
        return render_template('meeting/index.html', active_status="on" if result is not None else "off")
    except TemplateNotFound:
        abort(404)


executor = GraphicsExecutor()


@meeting_status.route('/meeting/<status>')
def meeting_on(status: str):
    should_start = is_on(status) and not executor.is_running()
    should_stop = not is_on(status) and executor.is_running()

    if should_start:
        executor.start_graphics()
    elif should_stop:
        executor.stop_graphics()
    else:
        pass
    return render_template('meeting/index.html', active_status=status)


def is_on(status) -> bool:
    return status.lower() == "on"
