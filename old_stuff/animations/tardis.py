# Touch sensitive TARDIS
#
# Connect P0 and GND to the same pins on another microbit loaded with
# tardis_2.py to see the TARDIS move from one to another

import microbit

TARDIS = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0]
    ]

def show_image(img, brightness):
    for i in range(5):
        for j in range(5):
            microbit.display.image.set_pixel_value(i, j, img[j][i] * brightness)

def detect_motion():
    x = microbit.accelerometer.get_x()
    while abs(x - microbit.accelerometer.get_x()) < 64:
        microbit.sleep(10)

microbit.display.set_display_mode(1)
brightness = [ 0, 1, 3, 7, 15, 31, 63, 127, 255 ]
materialisation = 1
while True:
    detect_motion()
    microbit.io.P0.set_digital_value(materialisation)
    for n in range(9):
        if materialisation == 1:
            b = brightness[n]
        else:
            b = brightness[8 - n]
        show_image(TARDIS, b)
        microbit.display.image.set_pixel_value(2, 0, 255 * (1 - materialisation))
        microbit.sleep(500)
        microbit.display.image.set_pixel_value(2, 0, 255 * materialisation)
        microbit.sleep(500)
    materialisation = 1 - materialisation
