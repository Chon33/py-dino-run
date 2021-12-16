from pygame import key
from imports.lang import *
from typing import Sequence
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class UItext:
    """Displays text on screen:
        - Name
        - Score
        - Start
    """

    def __init__(self, name: str, screen: pygame.Surface):
        self.started = False
        self.name = name
        self.screen = screen
        self.w, self.h = self.screen.get_width(), self.screen.get_height()
        self.selectedLanguage = 1
        self.points = 0
        self.rfont = pygame.font.Font("assets/misc/P22Bangersfield-Regular.ttf", 25)
        self.bfont = pygame.font.Font("assets/misc/P22Bangersfield-Bold.ttf", 25)
        
        self.mainMenuOptions = [lang["singleplayer"], lang["settings"], lang["exit"]]
        self.selectedOption = 0
        self.settingsIndex = 0
        self.inMainMenu = True
        self.mainMenuPadding = 85
        self.openSettingsMenu = False
        self.closeSettingsMenu = True
        self.inSettingsMenu = False

        self.btn1 = False
        self.btn2 = False
        self.btn3 = False
        self.btn4 = False
        self.btn5 = False
        self.btn6 = False

        self.btn7 = False
        self.btn8 = False
    
    def update(self, pressed_keys: Sequence[bool], dino, events):
        if not self.started:
            self.mainMenu(pressed_keys, dino)
            self.settingsMenu(pressed_keys, events)
        else:
            self.draw()

    def settingsMenu(self, pressed_keys: Sequence[bool], events):
        settingsOptions = [lang["name"] + self.name, lang["language"] + available_langs[self.selectedLanguage], lang["back"]]

        if self.inSettingsMenu:
            if self.settingsIndex == 0:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]  # ? We remove the last char
                        elif event.key == pygame.K_RETURN:
                            save("name", self.name)
                        else:
                            self.name += event.unicode  # ? We add the new char
            
            if self.settingsIndex == 1:
                if pressed_keys[pygame.K_RIGHT] and not self.btn7:
                    self.selectedLanguage = (self.selectedLanguage - 1) % len(available_langs)
                    self.btn7 = True
                elif not pressed_keys[pygame.K_RIGHT]:
                    self.btn7 = False

                if pressed_keys[pygame.K_LEFT] and not self.btn8:
                    self.selectedLanguage = (self.selectedLanguage + 1) % len(available_langs)
                    self.btn8 = True
                elif not pressed_keys[pygame.K_LEFT]:
                    self.btn8 = False

                if pressed_keys[pygame.K_RETURN]:
                    save("lang", self.selectedLanguage)
                

            if pressed_keys[pygame.K_UP] and not self.btn5:
                self.settingsIndex = (self.settingsIndex - 1) % len(settingsOptions)
                self.btn5 = True
            elif not pressed_keys[pygame.K_UP]:
                self.btn5 = False

            if pressed_keys[pygame.K_DOWN] and not self.btn6:
                self.settingsIndex = (self.settingsIndex + 1) % len(settingsOptions)
                self.btn6 = True
            elif not pressed_keys[pygame.K_DOWN]:
                self.btn6 = False

            for i,option in enumerate(settingsOptions):
                if self.settingsIndex == i:
                    text = self.bfont.render(f"> {option}", True, (255, 255, 255))
                    self.screen.blit(text, (self.w/2 + 0, self.h/3 + i*30))
                else:
                    text = self.rfont.render(f"  {option}", True, (255, 255, 255))
                    self.screen.blit(text, (self.w/2 + 0, self.h/3 + i*30))

    def mainMenu(self, pressed_keys: Sequence[bool], dino): 
        if self.inMainMenu:
            if not self.inSettingsMenu:
                if pressed_keys[pygame.K_UP] and not self.btn1:
                    self.selectedOption = (self.selectedOption - 1) % len(self.mainMenuOptions)
                    self.btn1 = True
                elif not pressed_keys[pygame.K_UP]:
                    self.btn1 = False

                if pressed_keys[pygame.K_DOWN] and not self.btn2:
                    self.selectedOption = (self.selectedOption + 1) % len(self.mainMenuOptions)
                    self.btn2 = True
                elif not pressed_keys[pygame.K_DOWN]:
                    self.btn2 = False

                if pressed_keys[pygame.K_RIGHT] and not self.btn3:
                    skinIndex = (dino.skinIndex + 1) % len(dino.skin_list)
                    dino.changeSkin(skinIndex)
                    self.btn3 = True
                elif not pressed_keys[pygame.K_RIGHT]:
                    self.btn3 = False

                if pressed_keys[pygame.K_LEFT] and not self.btn4:
                    skinIndex = (dino.skinIndex - 1) % len(dino.skin_list)
                    dino.changeSkin(skinIndex)
                    self.btn4 = True
                elif not pressed_keys[pygame.K_LEFT]:
                    self.btn4 = False

            for i, option in enumerate(self.mainMenuOptions):
                if self.selectedOption == i:
                    text = self.bfont.render(f"> {option}", True, (255, 255, 255))
                    self.screen.blit(text, (self.w/2 + self.mainMenuPadding, self.h/3 + i*30))

                else:
                    text = self.rfont.render(f"  {option}", True, (255, 255, 255))
                    self.screen.blit(text, (self.w/2 + self.mainMenuPadding, self.h/3 + i*30))

    def draw(self):
        if self.started:
            text = self.rfont.render(self.name, True, (255, 255, 255))
            self.screen.blit(text, (10, 10))

            text2 = self.rfont.render(str(self.points), True, (255, 255, 255))
            self.screen.blit(
                text2, (self.screen.get_width() - 10 - text2.get_width(), 10))

    def start(self):
        if not self.started:
            self.started = True
            self.points = 0
