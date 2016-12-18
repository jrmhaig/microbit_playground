import serial
import pygame
import sys
import math
import time
from random import randrange

ser = [
        serial.Serial(
            '/dev/ttyACM0',
            baudrate=115200,
            timeout = 0.0001
        ),
        serial.Serial(
            '/dev/ttyACM1',
            baudrate=115200,
            timeout = 0.0001
        )
    ]

positions = [
        [ 100, 120 ],
        [ 600, 400 ]
    ]

colours = [
        ( 0, 255, 0 ),
        ( 0, 0, 255 )
    ]

speed = 5

ball_position = [ 200, 200 ]
ball_velocity = [ 5, 5 ]
ball_radius = 10

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode((width, height), 0)

in_game = False

font = pygame.font.SysFont('sanserif', 40)

t_start = 0
t_end = 0

for s in ser:
    s.flushInput()

def intersect(a, b, c, r):
    # Distance from a to b
    lab = math.sqrt( (b[0] - a[0])**2 + (b[1] - a[1])**2 )

    # Direction from a to b
    d = [ (b[0] - a[0])/lab, (b[1] - a[1]) /lab ]

    # Line equation: x = d[0]*t + a[0], y = d[1] * t + a[0]
    # Value of t for closest point to c
    t = d[0]*(c[0] - a[0]) + d[1]*(c[1] - a[1])

    # Coordinates of this point
    e = [ t * d[0] + a[0], t * d[1] + a[1] ]

    # Distance from this point to c
    lec = math.sqrt( (e[0] - c[0])**2 + (e[1] - c[1])**2 )

    # True if lec is less than the radius and t is between a and b
    return ( t > 0 and t < lab and lec < r )

def playing():
    global in_game, t_end
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((55,55,50))
    line = 0
    for i in range(2):
        comm = ser[i].read()
        if comm == 'r' and positions[i][0] < width:
            positions[i][0] += speed
        elif comm == 'l' and positions[i][0] > 0:
            positions[i][0] -= speed
        elif comm == 'u' and positions[i][1] < height:
            positions[i][1] -= speed
        elif comm == 'd' and positions[i][1] > 0:
            positions[i][1] += speed
        pygame.draw.circle(screen, colours[i], positions[i], 10)
        ser[i].flushInput()
    pygame.draw.line(screen, (255, 0, 0), positions[0], positions[1])

    for i in range(2):
        new = ball_position[i] + ball_velocity[i]
        if new > size[i] - ball_radius or new < ball_radius:
            ball_velocity[i] *= -1
            new = ball_position[i] + ball_velocity[i]
        ball_position[i] = new

    if intersect(positions[0], positions[1], ball_position, ball_radius):
        ball_colour = ( 255, 0, 0 )
        t_end = time.time()
        in_game = False
    else:
        ball_colour = ( 255, 255,255 )

    pygame.draw.circle(screen, ball_colour, ball_position, ball_radius)
    return in_game

def show_message():
    global in_game, ball_position, t_start, t_end, positions
    if t_end > 0:
        score = font.render("You lasted %d seconds" % int(t_end - t_start), 1, (255, 255, 0))
        screen.blit(score, (200, 100))
    label = font.render("Press Space to start", 1, (255, 255, 0))
    screen.blit(label, (200, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_position = [ randrange(width), randrange(height) ]
                positions = [
                        [ 100, 120 ],
                        [ 600, 400 ]
                    ]

                t_start = time.time()
                for s in ser:
                    s.flushInput()
                in_game = True
    return in_game

while True:
    if in_game:
        in_game = playing()
    else:
        in_game = show_message()
    pygame.display.update()
    pygame.time.Clock().tick(10)
