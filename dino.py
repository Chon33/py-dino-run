#!/usr/bin/python

#&############################### IMPORTS ##############################################
from imports.dinoClass import Dino
import getopt
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    import pygame
except:
    print("Necesitas \"pygame\".\n \
    Usa \"pip install pygame\" para instalarlo.\n\n \
    Si no tienes pip, puedes instalarlo con \"sudo apt install python3-pip\".\n")

pygame.init()
#&######################################################################################

#&###################### WINDOW ############################
size = (width, height) = 600, 240
speed = [0, 0]
bg = (123, 162, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Py Dino Run")

grass_rect = pygame.Rect(0, height - 35, 600, 35)
grass_color = (107, 255, 116)
#&##########################################################

#&####################### LOGIC ############################
clock = pygame.time.Clock
dino = Dino(5, 3, "daniel", screen)


running = dino.running
while running:
    dt = clock().tick(60)
    running = dino.running    
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dino.running = False

    if pressed_keys[pygame.K_q]:
        dino.running = False

    screen.fill(bg)
    pygame.draw.rect(screen, grass_color, grass_rect)
    dino.update(screen, pressed_keys)

    pygame.display.update()

#&###########################################################
