import microbit

key_delay = 100
acc = microbit.accelerometer
a = microbit.button_a
b = microbit.button_b
img = microbit.display.image

while True:
    microbit.display.clear()
    x = acc.get_x()
    y = acc.get_y()
    if x > 300:
        print('r')
        img.set_pixel_value(4, 2, 1)
    elif x < -300:
        print('l')
        img.set_pixel_value(0, 2, 1)

    if y > 300:
        print('d')
        img.set_pixel_value(2, 4, 1)
    elif y < -300:
        print('u')
        img.set_pixel_value(2, 0, 1)

    if a.is_pressed():
        print('a')
        img.set_pixel_value(1, 2, 1)

    if b.is_pressed():
        print('b')
        img.set_pixel_value(3, 2, 1)

    microbit.sleep(key_delay)
