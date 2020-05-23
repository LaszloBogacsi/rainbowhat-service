from rainbowhat_app import celery
from rainbowhat_app.itv_pic import ScrollingGraphics

graphics = ScrollingGraphics()


@celery.task
def run_graphics():
    print("Running task")
    graphics.run()
