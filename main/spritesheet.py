import pygame
import json

class Spritesheet:
    def __init__(self, character):
        self.character = character

        with open("data/sprites.json") as f:
            self.data = json.load(f)
        f.close()

    def load_sheet(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, action, lst):
        for frame in self.data[self.character][action]:
            sprite = self.data[self.character][action][frame]['frame']
            x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
            image = self.get_sprite(x, y, w, h)
            lst.append(image)