import math
import pygame
from config import *

class MapTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, ground, block):
        self.game = game

        if ground:
            self._layer = GROUND_LAYER
        else:
            self._layer = BLOCKS_LAYER
        
        if block:
            self.groups = self.game.all_sprites, self.game.blocks
        else:
            self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.animationCounter = 0

class Block(MapTile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, False, True)

        self.image = self.game.terrain_spritesheet.get_sprite(176, 46, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(MapTile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, True, False)

        self.image = self.game.terrain_spritesheet.get_sprite(86, 7, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Tree(MapTile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, True, True)

        self.image = self.game.terrain_spritesheet.get_sprite(111, 64, 16, 16)
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
class Bridge(MapTile):
    def __init__(self, game, x, y, frame, turn):
        super().__init__(game, x, y, True, False)

        frames = []
        self.game.terrain_spritesheet.parse_sprite('building', 'bridge', frames)
        self.image = pygame.transform.scale(frames[frame], (TILESIZE, TILESIZE))
        self.image = pygame.transform.rotate(self.image, turn)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Cliff(MapTile):
    def __init__(self, game, x, y, orientation, corner):
        super().__init__(game, x, y, True, True)

        if corner:
            self.image = self.game.terrain_spritesheet.get_sprite(0, 100, 10, 11)
        else:
            self.image = self.game.terrain_spritesheet.get_sprite(0, 107, 10, 22)

        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

        if orientation == "up":
            self.image = pygame.transform.rotate(self.image, -90)
        elif orientation == "right":
            self.image = pygame.transform.rotate(self.image, -180)
        elif orientation == "down":
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Water(MapTile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, True, True)

        self.image = self.game.terrain_spritesheet.get_sprite(48, 128, 16, 16)
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def animation(self):
        animate = [self.game.terrain_spritesheet.get_sprite(48, 128, 16, 16),
                   self.game.terrain_spritesheet.get_sprite(64, 128, 16, 16)]

        for i in range(len(animate)):
            animate[i] = pygame.transform.scale(animate[i], (TILESIZE, TILESIZE))

        self.image = animate[math.floor(self.animationCounter)]
        self.animationCounter += 0.01
        if self.animationCounter >= len(animate):
            self.animationCounter = 0

    def update(self):
        self.animation()    