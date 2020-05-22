from rainbowhat_app.itv_pic import ScrollingGraphics

graphics = ScrollingGraphics()


def run_graphics(shouldRun):
    print("status: " + str(shouldRun))
    graphics.run() if shouldRun else graphics.stop()
