import pygame
from config import *
from weapons import *

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, game, x, y, entity):
        self.game = game
        self.entity = entity
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.healthbars
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = 10

        self.dx = 0
        self.dy = 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y - TILESIZE / 2

    def move(self):
        self.rect.x = self.entity.rect.x
        self.rect.y = self.entity.rect.y - TILESIZE / 2

    def kill_healthbar(self):
        self.kill()

    def damage(self, totalHealth, health):
        self.image.fill(RED)
        width = self.rect.width * health / totalHealth

        pygame.draw.rect(self.image, GREEN, (0, 0, width, self.height), 0)
    
    def update(self):
        self.move()