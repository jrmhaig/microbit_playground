import microbit

r = microbit.io.P0
long = 500
short = 250

while True:
    while r.get_digital_value() == 0:
        pass

    t = microbit.system_time()

    while r.get_digital_value() == 1:
        pass

    if microbit.system_time() - t < 400:
        microbit.display.print('A')
    else:
        microbit.display.print('B')
