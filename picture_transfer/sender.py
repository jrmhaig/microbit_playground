import microbit

w = microbit.io.P0
short = 250
long = 500
gap = 100

img = microbit.display.image
flash_delay = 10

# Draw image
#   Button A for pixel on
#   Button B for pixel off
for j in range(5):
    for i in range(5):
        while not (microbit.button_a.is_pressed() or microbit.button_b.is_pressed()):
            img.set_pixel_value(i, j, 255)
            microbit.sleep(flash_delay)
            img.set_pixel_value(i, j, 0)
            microbit.sleep(flash_delay)
        if microbit.button_a.is_pressed():
            img.set_pixel_value(i, j, 255)
        else:
            img.set_pixel_value(i, j, 0)
        while microbit.button_a.is_pressed() or microbit.button_b.is_pressed():
            pass

# Send image
w.set_digital_value(0)
for j in range(5):
    for i in range(5):
        w.set_digital_value(1)
        if img.get_pixel_value(i, j):
            microbit.sleep(long)
        else:
            microbit.sleep(short)
        w.set_digital_value(0)
        microbit.sleep(gap)
