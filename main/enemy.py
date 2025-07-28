import math
import pygame
from config import *
from healthbar import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.healthbar = HealthBar(game, x, y, self)
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.dx = 0
        self.dy = 0

        self.image = self.game.enemy_spritesheet.get_image(63, 167, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.maxSteps = random.choice(range(20, 120, 10))
        self.currSteps = 0
        
        self.state = "moving"
        self.animationCounter = 0

        self.health = ENEMY_HEALTH

        self.shootCountner = 0
        self.waitShoot = random.choice(range(10, 91, 10))
        self.shootState = 'halt'

    def shoot(self):
        self.shootCountner += 1
        if self.shootCountner >= self.waitShoot and self.playerInRange():
            self.shootState = "shoot"
            self.shootCountner = 0
            self.waitShoot = random.choice(range(10, 91, 10))
    
    def playerInRange(self):
        pX = self.game.player.rect.x
        pY = self.game.player.rect.y
        diffX = abs(self.rect.x - pX)
        diffY = abs(self.rect.y - pY)

        return diffX < ENEMY_DETECTION_RANGE * TILESIZE and diffY < ENEMY_DETECTION_RANGE * TILESIZE
    
    def move(self):
        if self.state == "moving":
            if self.direction == 'left':
                self.dx -= ENEMY_STEPS
                self.currSteps += 1
            elif self.direction == 'right':
                self.dx += ENEMY_STEPS
                self.currSteps += 1
            elif self.direction == 'up':
                self.dy -= ENEMY_STEPS
                self.currSteps += 1
            elif self.direction == 'down':
                self.dy += ENEMY_STEPS
                self.currSteps += 1
            
            if self.shootState == 'shoot':
                Enemy_Projectile(self.game, self.rect.x, self.rect.y)
                self.shootState = 'halt'

        elif self.state == "stalling":
            self.currSteps += 1
            if self.currSteps == self.maxSteps:
                self.state = "moving"
                self.currSteps = 0
                self.direction = random.choice(['left', 'right', 'up', 'down'])

    def update(self):
        self.move()
        self.animation()
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.dx = 0
        self.dy = 0

        if self.currSteps == self.maxSteps:
            if self.state != "stalling":
                self.currSteps = 0
        
            self.maxSteps = random.choice(range(20, 120, 10))
            self.state = "stalling"

        self.collide_blocks()
        self.collide_player()
        self.shoot()
    
    def animation(self):
        rightAnimation = [self.game.enemy_spritesheet.get_image(125, 70, self.width, self.height)]
        leftAnimation = [pygame.transform.flip(self.game.enemy_spritesheet.get_image(31, 72, self.width, self.height), True, False)]
        upAnimation = [self.game.enemy_spritesheet.get_image(160, 41, self.width, self.height)]
        downAnimation = [self.game.enemy_spritesheet.get_image(31, 38, self.width, self.height)]
        
        if self.direction == "right":
            if self.dx == 0:
                self.image = rightAnimation[0]
            else:
                self.image = rightAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.1

                if self.animationCounter >= len(rightAnimation):
                    self.animationCounter = 0
        elif self.direction == "left":
            if self.dx == 0:
                self.image = leftAnimation[0]
            else:
                self.image = leftAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.1

                if self.animationCounter >= len(leftAnimation):
                    self.animationCounter = 0
        elif self.direction == "up":
            if self.dy == 0:
                self.image = upAnimation[0]
            else:
                self.image = upAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.1

                if self.animationCounter >= len(upAnimation):
                    self.animationCounter = 0
        elif self.direction == "down":
            if self.dy == 0:
                self.image = downAnimation[0]
            else:
                self.image = downAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.1

                if self.animationCounter >= len(downAnimation):
                    self.animationCounter = 0

    def collide_blocks(self):
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
        
        if collide:
            if self.direction == "left":
                self.rect.x += PLAYER_STEPS
                self.direction = "right"
            elif self.direction == "right":
                self.rect.x -= PLAYER_STEPS
                self.direction = "left"
            elif self.direction == "up":
                self.rect.y += PLAYER_STEPS
                self.direction = "down"
            elif self.direction == "down":
                self.rect.y -= PLAYER_STEPS
                self.direction = "up"
    
    def collide_player(self):
        collide = pygame.sprite.spritecollide(self, self.game.main_player, True)

        if collide:
            self.game.running = False

    def damage(self, amount):
        self.health = self.health - amount

        if self.health <= 0:
            self.kill()
            self.healthbar.kill()
        else:
            self.healthbar.damage(ENEMY_HEALTH, self.health)