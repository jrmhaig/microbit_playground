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

microbit.display.set_display_mode(1)

for b in range(63, -1, -4):
    show_image(TARDIS, b)
    microbit.display.image.set_pixel_value(2, 0, 255)
    microbit.sleep(500)
    microbit.display.image.set_pixel_value(2, 0, 0)
    microbit.sleep(500)
    
microbit.display.clear()
