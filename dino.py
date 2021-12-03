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

#&##################### FUNCTIONS ##########################
help_msg = "python3 dino.py -n Daniel -s doux\n \
            -n, --name     Nombre tu dinosaurio\n \
            -s, --skin     Cambia el color de tu dinosaurio\n \
                             skins: doux, mort, tard, vita\n \
            -h, --help     Muestra este mensaje\n"


def main(argv):
    global name, skin
    name, skin = "", ""
    try:
        opts, args = getopt.getopt(argv, "hn:s:", ["name", "skin"])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help_msg)
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-s", "--skin"):
            skin = arg

    if not name or not skin:
        print(help_msg)
        sys.exit(2)
    else:
        print(f"Nombre: {name}")
        print(f"Skin:   {skin}")


# main(sys.argv[1:])
#&##########################################################

#&###################### WINDOW ############################
size = (width, height) = 600, 240
speed = [0, 0]
bg = (123, 162, 255)
screen = pygame.display.set_mode(size)
#&##########################################################

#&####################### GRASS ############################
grass_rect = pygame.Rect(0, height - 35, 600, 35)
grass_color = (107, 255, 116)
#&##########################################################

#&####################### LOGIC ############################
clock = pygame.time.Clock
dino = Dino(3, 3, "daniel", screen)

pygame.display.set_caption(f"{dino.name}")

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
