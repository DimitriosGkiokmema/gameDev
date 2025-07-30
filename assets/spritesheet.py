import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open("assets/sprites.json") as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, entity, action, lst):
        print(self.data[entity][action])
        for frame in self.data[entity][action]:
            print(frame)
            sprite = self.data[entity][action][frame]['frame']
            x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
            image = self.get_sprite(x, y, w, h)
            lst.append(image)
            print(sprite)
            print("\n")