from time import sleep
import os

i = -1


class ScrollingGraphics():
    import rainbowhat as rainbow
    rainbow.set_layout(rainbow.AUTO)
    rainbow.set_layout(rainbow.HAT)
    rainbow.rotation(180)
    rainbow.brightness(0.2)
    width, height = rainbow.get_shape()

    # Every line needs to be exactly 8 characters
    # but you can have as many lines as you like.

    status: bool
    ASCIIPIC = [
         "        "
        ,"i tttv v"
        ,"i  t v v"
        ,"i  t v v"
        ,"i  t v v"
        ,"i  t  v "
        ,"        "
        ]

    def step(self):
        global i
        i = 0 if i >= 100 * len(self.ASCIIPIC) else i + 1  # avoid overflow
        for h in range(self.height):
            for w in range(self.width):
                h_pos = (i+h) % len(self.ASCIIPIC)
                char = self.ASCIIPIC[h_pos][w]
                if char == 'i':
                    self.rainbow.set_pixel(w, h, 25, 190, 200)
                elif char == 't':
                    self.rainbow.set_pixel(w, h, 134, 122, 36)
                elif char == 'v':
                    self.rainbow.set_pixel(w, h, 255, 170, 0)
                else:
                    self.rainbow.set_pixel(w, h, 0, 0, 0)
        self.rainbow.show()

    def run(self):
        print("Starting")

        self.status = True
        while self.check_status():
            self.step()
            sleep(0.2)

    def stop(self):
        print("Stopping")
        self.status = False

    def check_status(self) -> bool:
        return self.status




