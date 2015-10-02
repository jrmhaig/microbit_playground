import microbit

w = microbit.io.P0
short = 250
long = 500

w.set_digital_value(0)
while True:
    if microbit.button_a.is_pressed():
        w.set_digital_value(1)
        microbit.sleep(short)
        w.set_digital_value(0)
        microbit.display.print('A')
    if microbit.button_b.is_pressed():
        w.set_digital_value(1)
        microbit.sleep(long)
        w.set_digital_value(0)
        microbit.display.print('B')
    microbit.sleep(10)
