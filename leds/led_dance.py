# Light LEDs at 'random' and make them fade over time
#
# Usage:
#
#    led_dance(speed)
#
# 'speed' is the time between each new LED being turned on. Note that the
# random number is actually based on time and so the speed will determine
# the pattern (and it is not really random).
#
# Hold button 'A' pressed to stop new LEDs being turned on.

import pyb

def led_dance(delay):
    dots = {}
    control = pyb.Switch(1)
    while True:
        if not control.value():
            dots[pyb.millis() % 25] = 16
        for d in dots:
            pyb.pixel(d, dots[d])
            if dots[d] == 0:
                del(dots[d])
            else:
                dots[d] = int(dots[d]/2)
        pyb.delay(delay)

led_dance(101)
