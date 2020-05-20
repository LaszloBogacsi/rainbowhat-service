#!/usr/bin/env python

from time import sleep

import rainbowhat as rainbow
import os
#rainbow.set_layout(rainbow.AUTO)
rainbow.set_layout(rainbow.HAT)
rainbow.rotation(180)
rainbow.brightness(0.2)
width,height=rainbow.get_shape()

# Every line needs to be exactly 8 characters
# but you can have as many lines as you like.
ASCIIPIC = [
     "        "
    ,"i tttv v"
    ,"i  t v v"
    ,"i  t v v"
    ,"i  t v v"
    ,"i  t  v "
    ,"        "
    ]
i = -1

print(os.getpid())

def step():
    global i
    i = 0 if i>=100*len(ASCIIPIC) else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % len(ASCIIPIC)
            chr = ASCIIPIC[hPos][w]
            if chr == 'i':
                rainbow.set_pixel(w, h, 25, 190, 200)
            elif chr == 't':
                rainbow.set_pixel(w, h, 134, 122, 36)
            elif chr == 'v':
                rainbow.set_pixel(w, h, 255, 170, 0)
            else:
                rainbow.set_pixel(w, h, 0, 0, 0)
    rainbow.show()

while True:
    step()
    sleep(0.2)