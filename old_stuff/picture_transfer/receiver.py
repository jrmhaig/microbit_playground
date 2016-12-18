import microbit

r = microbit.io.P0
cutoff = 400

img = microbit.display.image

i = j = 0
while j < 5:
    while r.get_digital_value() == 0:
        pass

    t = microbit.system_time()

    while r.get_digital_value() == 1:
        pass

    if microbit.system_time() - t < cutoff:
        img.set_pixel_value(i, j, 255)
    else:
        img.set_pixel_value(i, j, 0)

    i = i + 1
    if i >= 5:
        i = 0
        j = j + 1
