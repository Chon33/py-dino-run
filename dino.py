#!/usr/bin/python

#&############################### IMPORTS ##############################################
from imports.dinoClass import Dino
from imports.lang import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    import pygame
except:
    print(lang['pygame_error'])

pygame.init()
#&######################################################################################

#&###################### WINDOW ############################
size = (width, height) = 600, 240
bg = (123, 162, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Py Dino Run")

grass_rect = pygame.Rect(0, height - 35, 600, 35)
grass_color = (107, 255, 116)
#&##########################################################

#&####################### LOGIC ############################
clock = pygame.time.Clock
dino = Dino(5, 3, settings["name"], screen)


running = dino.running
while running:
    dt = clock().tick(60)
    running = dino.running    
    pressed_keys = pygame.key.get_pressed()

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            dino.running = False

    if pressed_keys[pygame.K_q]:
        dino.running = False

    screen.fill(bg)
    pygame.draw.rect(screen, grass_color, grass_rect)
    dino.update(screen, pressed_keys, events)

    pygame.display.update()

#&###########################################################
