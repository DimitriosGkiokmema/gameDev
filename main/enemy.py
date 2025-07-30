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

        self.width = TILESIZE
        self.height = TILESIZE

        self.dx = 0
        self.dy = 0

        self.image = self.game.enemy_spritesheet.get_sprite(63, 167, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.maxSteps = random.choice(range(20, 120, 10))
        self.currSteps = 0
        
        self.state = "moving"
        self.animationCounter = 0

        self.health = ENEMY_HEALTH

        self.shootCounter = 0
        self.waitShoot = random.choice(range(10, 91, 10))
        self.shootState = 'halt'

        # Loading sprite frames
        # rightAnimation = []
        # self.game.enemy_spritesheet.parse_sprite('right', rightAnimation)
        # leftAnimation = [pygame.transform.flip(self.game.enemy_spritesheet.get_sprite(31, 72, self.width, self.height), True, False)]
        # upAnimation = [self.game.enemy_spritesheet.get_sprite(160, 41, self.width, self.height)]
        # downAnimation = [self.game.enemy_spritesheet.get_sprite(31, 38, self.width, self.height)]
        self.rightAnimation = []
        self.game.enemy_spritesheet.parse_sprite('right', self.rightAnimation)
        self.upAnimation = []
        self.game.enemy_spritesheet.parse_sprite('up', self.upAnimation)

        self.leftAnimation = []
        for frame in self.rightAnimation:
            self.leftAnimation.append(pygame.transform.flip(frame, True, False))

        self.downAnimation = []
        for frame in self.upAnimation:
            self.downAnimation.append(pygame.transform.flip(frame, False, True))

    def shoot(self):
        self.shootCounter += 1
        if self.shootCounter >= self.waitShoot and self.playerInRange():
            self.shootState = "shoot"
            self.shootCounter = 0
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
                Projectile(self.game, self.rect.x, self.rect.y, self.direction, False)
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
        currAnimation = None
        change = None
        
        if self.direction == "right":
            currAnimation = self.rightAnimation
            change = self.dx
        elif self.direction == "left":
            currAnimation = self.leftAnimation
            change = self.dx
        elif self.direction == "up":
            currAnimation = self.upAnimation
            change = self.dy
        elif self.direction == "down":
            currAnimation = self.downAnimation
            self.dy
        
        if change == 0:
            self.image = currAnimation[0]
        else:
            self.image = currAnimation[math.floor(self.animationCounter)]
            self.animationCounter += 0.15

            if self.animationCounter >= len(currAnimation):
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