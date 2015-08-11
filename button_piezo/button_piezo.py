# Usage:
#
# To play a note with frequency 250 Hz (i.e. 1000/4)
#
#     button_piezo(2)
#
# Note, the argument can only be an integer so the range of notes is very
# restrictive and approximate:
#
#   Note     Frequency    Argument
#   B4       493.88 Hz ->    1
#   B3       246.94 Hz ->    2
#   E3       164.81 Hz ->    3
#   B2       123.47 Hz ->    4
#   G2        98.00 Hz ->    5
#   (or G#2  103.83 Hz)
#   E2        82.41 Hz ->    6

import pyb

def button_piezo(d):
    p1 = pyb.Pin(2, pyb.Pin.OUT_PP)
    p2 = pyb.Pin(1, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
    while True:
        if p2.value() == 1:
            p1.high()
            pyb.delay(d)
            p1.low()
            pyb.delay(d)

button_piezo(1)
