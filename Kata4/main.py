# python -m pip install pygame

import pygame, random

# Variables
screen_width = 1280
screen_height = 960

# Colors
white_color = (200, 200, 200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width,screen_height))

def mover_rectangulo():
    global speed

    if rectangulo.top + 50 < screen_height:
        rectangulo.top += speed



def start_bola():
    global speed_bola_x, speed_bola_y

    if bola.left + 50 > screen_width:
        bola.top = screen_height // 2
        bola.left = screen_width // 2

        speed_bola_x
        speed_bola_y

def mover_bola():
    global speed_bola_x, speed_bola_y

    if bola.top + 50 > screen_height or bola_top < 0:
        speed_bola_x = -speed_bola_x

    if bola.left < 10 and rectangulo.top < bola.top < rectangulo:
        speed_bola_x = -speed_bola_x

    start_bola()

    bola.top += speed_bola_x
    bola_left += speed_bola_y

rectangulo = pygame.Rect(10,10,50,50)
bola=pygame.Rect(50,10,50,50)

speed = 0
speed_bola_x = 3
speed_bola_y = 3


while True:
    screen.fill(light_gray)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3
            elif event.key == pygame.K_DOWN:
                speed = 3
        elif event.type == pygame.KEYUP:
            speed = 0

    mover_rectangulo()

    pygame.draw.rect(screen, white_color, rectangulo)

    pygame.display.flip()
    clock.tick(60)