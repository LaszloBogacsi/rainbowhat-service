from time import sleep
import rainbowhat as rainbow

i = -1


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
    , "i tttv v"
    , "i  t v v"
    , "i  t v v"
    , "i  t v v"
    , "i  t  v "
    , "        "
]


def step():
    global i, width, height
    
    i = 0 if i >= 100 * len(ASCIIPIC) else i + 1  # avoid overflow
    for h in range(height):
        for w in range(width):
            h_pos = (i + h) % len(ASCIIPIC)
            char = ASCIIPIC[h_pos][w]
            if char == 'i':
                rainbow.set_pixel(w, h, 25, 190, 200)
            elif char == 't':
                rainbow.set_pixel(w, h, 134, 122, 36)
            elif char == 'v':
                rainbow.set_pixel(w, h, 255, 170, 0)
            else:
                rainbow.set_pixel(w, h, 0, 0, 0)
    rainbow.show()
    

def run():
    print("Starting")
    global status
    status = True
    while check_status():
        step()
        sleep(0.2)


def stop():
    print("Stopping")
    global status
    status = False


def check_status() -> bool:
    return status


run()
