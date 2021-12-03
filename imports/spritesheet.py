import json
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class Spritesheet:
    """Divide un spritesheet en frames definidos en un archivo json con le mismo nombre que la imagen"""

    def __init__(self, skin: str):
        self.skin = f"assets/skins/{skin}.png"
        self.sprite_sheet = pygame.image.load(self.skin).convert()
        # ? conver() => se usa por si la ventana y el sprite no se "entienden", (ahorra las cuenas necesarias en cada frame, las hace solo una vez)
        #self.meta_data = self.skin.replace('png', 'json')
        self.meta_data = f"assets/skins/metadata.json"
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x: int, y: int, w: int, h: int):
        sprite = pygame.Surface((w, h))  # ? blank space
        sprite.set_colorkey((0, 0, 0))  # ? for transparency
        # ? paste an image in the blank spcae
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))

        return sprite

    def parse_sprite(self, animation: str, n: int, multiply_scale: int):
        sprite = self.data['frames'][animation][f"{animation}{n}"]['frame']
        (x, y, w, h) = (sprite["x"], sprite["y"], sprite["w"], sprite["h"])
        image = self.get_sprite(x, y, w, h)
        image = pygame.transform.scale(
            image, (multiply_scale*w, multiply_scale*h)
        )

        return image
