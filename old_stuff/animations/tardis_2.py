# Touch sensitive TARDIS part two
#
# To be used with tardis.py

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
    x = microbit.io.P0.get_digital_value()
    y = x
    while x == y:
        x = y
        y = microbit.io.P0.get_digital_value()
        microbit.sleep(10)

microbit.display.set_display_mode(1)
brightness = [ 0, 1, 3, 7, 15, 31, 63, 127, 255 ]
materialisation = 0
while True:
    detect_motion()
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
