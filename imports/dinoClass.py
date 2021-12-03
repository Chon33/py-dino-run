from typing import Sequence
from imports.spritesheet import Spritesheet
from imports.ui import UItext
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class Dino:
    """Usa los frames del Spritesheet para animar al personaje y añade funcionalidades:
            - Saltar
            - Colisionar
            - Movimiento
    """

    def __init__(self, skinIndex: int, mult: int, name: str, screen: pygame.Surface):      
        """
        try:
            self.skin = self.skin_list[self.skinIndex]
        except IndexError:
            self.skin = self.skin_list[0]

        self.spritesheet = Spritesheet(self.skin)
        """

        self.shadow = pygame.image.load("assets/misc/shadow.png")
        self.shadow = pygame.transform.scale(self.shadow, (55, 55))
        self.mult = mult
        self.name = name
        self.screen = screen
        self.i, self.k, self.elapsed, self.y, self.started = 0, 0, 0, 0, False
        self.changeSkin(skinIndex)
        self.running = True

        self.ui_text = UItext(self.name.capitalize(), screen)
        self.elap2 = 0

        self.is_jumping = False
        self.going_up = True
        self.jump_speed = 3
        self.max_jump = 65

    def changeSkin(self, skinIndex):
        self.skinIndex = skinIndex
        self.skin_list = [
            "doux",
            "trois",
            "mort",
            "notte",
            "tard",
            "rose",
            "vita",
            "giglio"
        ]
        
        try:
            self.skin = self.skin_list[self.skinIndex]
        except IndexError:
            self.skin = self.skin_list[0]
        
        self.spritesheet = Spritesheet(self.skin)

        mult = self.mult
        dino_idle = [
            self.spritesheet.parse_sprite("idle", 1, mult),
            self.spritesheet.parse_sprite("idle", 2, mult),
            self.spritesheet.parse_sprite("idle", 3, mult),
            self.spritesheet.parse_sprite("idle", 4, mult), ]
        dino_move = [
            self.spritesheet.parse_sprite("move", 1, mult),
            self.spritesheet.parse_sprite("move", 2, mult),
            self.spritesheet.parse_sprite("move", 3, mult),
            self.spritesheet.parse_sprite("move", 4, mult),
            self.spritesheet.parse_sprite("move", 5, mult),
            self.spritesheet.parse_sprite("move", 6, mult), ]
        dino_hurt = [
            self.spritesheet.parse_sprite("hurt", 1, mult),
            self.spritesheet.parse_sprite("hurt", 2, mult),
            self.spritesheet.parse_sprite("hurt", 3, mult),
            self.spritesheet.parse_sprite("hurt", 4, mult), ]
        dino_sneak = [
            self.spritesheet.parse_sprite("sneak", 1, mult),
            self.spritesheet.parse_sprite("sneak", 2, mult),
            self.spritesheet.parse_sprite("sneak", 3, mult),
            self.spritesheet.parse_sprite("sneak", 4, mult),
            self.spritesheet.parse_sprite("sneak", 5, mult), ]

        self.dino_anims = [
            dino_idle,
            dino_move,
            dino_hurt,
            dino_sneak]

    def start(self, pressed_keys: Sequence[bool]):
        if not self.started and pressed_keys[pygame.K_RETURN]:
            if self.ui_text.selectedOption == 0:
                self.started = True
                self.ui_text.start()
                self.k = 1

            elif self.ui_text.selectedOption == 2:
                self.running = False

    def update(self, screen, pressed_keys: Sequence[bool]):
        self.start(pressed_keys)
        self.jump(pressed_keys)
        self.sneak(pressed_keys)

        self.ui_text.update(pressed_keys, self)

        self.elapsed += 1
        self.elap2 +=1

        if self.elapsed > 4:
            self.i = (self.i+1) % len(self.dino_anims[self.k])        
            self.elapsed = 0
        
        if self.elap2 > 30:
            self.ui_text.points += 1
            self.elap2 = 0

        screen.blit(self.shadow, (17, 175))
        try:
            screen.blit(self.dino_anims[self.k][self.i], (10, 160 - self.y))
        except IndexError:
            self.i = 0
            screen.blit(self.dino_anims[self.k][self.i], (10, 160 - self.y))

    def jump(self, pressed_keys: Sequence[bool]):
        if self.started:
            if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]:
                if not self.is_jumping:
                    self.is_jumping = True
                    self.going_up = True

            if self.is_jumping and self.going_up:
                self.y += self.jump_speed

            if self.y >= self.max_jump:
                self.going_up = False

            if self.is_jumping and not self.going_up:
                self.y -= self.jump_speed

            if self.y <= 0:
                self.is_jumping = False
                self.going_up = True
                self.y = 0

    def sneak(self, pressed_keys: Sequence[bool]):
        if self.started:
            if self.started and pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT] or pressed_keys[pygame.K_DOWN]:
                self.k = 3
            elif not self.started:
                self.k = 0
            else:
                self.k = 1
