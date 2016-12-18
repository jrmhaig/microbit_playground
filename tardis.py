import radio
import microbit
import random

id = 0
bits = 1
has_tardis = False


def n_except(n, i):
    j = i
    while j == i:
        j = random.randint(0, n-1)
    return j


ts = []
for j in range(0, 10, 3):
    body = '0%d%d%d0' % (j, j, j)
    t = microbit.Image('000000:' + ':'.join([body, body, body, body]))
    flash = []
    for i in range(0, 10):
        s = t.copy()
        s.set_pixel(2, 0, i)
        flash.append(s)
    ts = ts + flash
    if j < 9:
        flash.reverse()
        ts = ts + flash

flash_speed = 20

while not microbit.button_a.is_pressed():
    pass

radio.on()

# Can I be the master???
key_send = random.randint(0, 10000)
microbit.display.scroll('Sending %d' % key_send)
radio.send('Hi %d' % key_send)
t = microbit.running_time()
while microbit.running_time() - t < 1000:
    incoming = radio.receive()
    if incoming:
        split = incoming.split()
        if split[0] == 'Ho' and int(split[1]) == key_send:
            id = int(split[2])
            break

if id == 0:
    microbit.display.show(ts, flash_speed)
    has_tardis = True
else:
    microbit.display.show('S')

if id == 0:
    while True:
        incoming = radio.receive()
        if incoming:
            split = incoming.split()
            if id == 0 and split[0] == 'Hi':
                radio.send('Ho %s %d' % (split[1], bits))
                microbit.display.show(str(bits))
                bits = bits + 1
            elif split[0] == 'Jump_from':
                to = n_except(bits, int(split[1]))
                if to == 0:
                    microbit.display.show(ts, flash_speed)
                    has_tardis = True
                else:
                    radio.send('Jump_to %d' % to)
        if has_tardis and microbit.button_a.is_pressed():
            has_tardis = False
            to = n_except(bits, 0)
            radio.send('Jump_to %d' % to)
            microbit.display.show(reversed(ts), flash_speed)
else:
    while True:
        incoming = radio.receive()
        if incoming:
            split = incoming.split()
            if split[0] == 'Jump_to' and int(split[1]) == id:
                microbit.display.show(ts, flash_speed)
                has_tardis = True
        if has_tardis and microbit.button_a.is_pressed():
            has_tardis = False
            radio.send('Jump_from %d' % id)
            microbit.display.show(reversed(ts), flash_speed)
