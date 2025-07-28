import math
from tiles import *
from config import *
import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_image(48, 128, 100, 100)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.animationCounter = 0
    
    def animation(self):
        animate = [self.game.weapons_spritesheet.get_image(171, 273, 205, 390),
                   self.game.weapons_spritesheet.get_image(465, 800, 260, 570)]

        for i in range(len(animate)):
            animate[i] = pygame.transform.scale(animate[i], (TILESIZE, TILESIZE))

        if self.animationCounter >= len(animate):
            self.animationCounter = 0
        
        self.image = animate[math.floor(self.animationCounter)]
        self.animationCounter += 0.05

    def update(self):
        self.animation()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction, isPlayer):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.projectiles
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.projectile_spritesheet.get_image(0, 0, 100, 100)
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = PROJECTILE_DAMAGE
        self.isPlayer = isPlayer

        if (direction == "player"):
            self.direction = self.game.player.direction
        else:
            self.direction = direction
    
    def move(self):
        if self.direction == "right":
            self.rect.x += PROJECTILE_STEPS
        elif self.direction == "left":
            self.rect.x -= PROJECTILE_STEPS
        elif self.direction == "up":
            self.rect.y -= PROJECTILE_STEPS
        elif self.direction == "down":
            self.rect.y += PROJECTILE_STEPS   

    def update(self):
        self.move()
        self.collide_block()
        self.collide_entity()

    def collide_block(self):
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False)

        if collide:
            self.kill()
    
    def collide_entity(self):
        if self.isPlayer:
            collide = pygame.sprite.spritecollide(self, self.game.enemies, False)
            
            if collide:
                collide[0].damage(self.damage)
                self.kill()
        else:
            collide = pygame.sprite.spritecollide(self, self.game.main_player, False)

            if collide:
                self.game.player.damage(self.damage)
                self.kill()
