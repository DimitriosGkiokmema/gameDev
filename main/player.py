import math
import pygame
from config import *
from healthbar import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.healthbar = HealthBar(game, x, y, self)
        self.groups = self.game.all_sprites, self.game.main_player
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.dx = 0
        self.dy = 0

        self.image = self.game.player_spritesheet.get_image(30, 29, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = "right"
        self.animationCounter = 0
        self.swordEquipped = False
        self.counter = 0
        self.coolDown = 20
        self.canShoot = True
        self.health = PLAYER_HEALTH

    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.dx -= PLAYER_STEPS

            if self.direction != "left":
                self.animationCounter = 0

            self.direction = "left"
        elif pressed[pygame.K_RIGHT]:
            self.dx += PLAYER_STEPS

            if self.direction != "right":
                self.animationCounter = 0

            self.direction = "right"
        elif pressed[pygame.K_UP]:
            self.dy -= PLAYER_STEPS

            if self.direction != "up":
                self.animationCounter = 0

            self.direction = "up"
        elif pressed[pygame.K_DOWN]:
            self.dy += PLAYER_STEPS

            if self.direction != "down":
                self.animationCounter = 0

            self.direction = "down"

    def update(self):
        self.move()
        self.animation()
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.collide_blocks()
        self.collide_enemies()
        self.collide_weapon()
        self.shoot_fireball()
        self.shootCooldown()

        self.dx = 0
        self.dy = 0

    def animation(self):
        rightAnimation = [self.game.player_spritesheet.get_image(30, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(130, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(220, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(320, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(410, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(500, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(610, 29, self.width, self.height),
                         self.game.player_spritesheet.get_image(705, 29, self.width, self.height)]
        leftAnimation = [self.game.player_spritesheet.get_image(30, 29, self.width, self.height)]
        upAnimation = [self.game.player_spritesheet.get_image(30, 29, self.width, self.height)]
        downAnimation = [self.game.player_spritesheet.get_image(30, 29, self.width, self.height)]
        
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
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False, pygame.sprite.collide_rect_ratio(0.85))

        if collide:
            self.game.blockCollided = True
            if pressed[pygame.K_LEFT]:
                self.rect.x += PLAYER_STEPS
            if pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
            if pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS
            if pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS
        else:
            self.game.blockCollided = False
    
    def collide_enemies(self):
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self, self.game.enemies, False, pygame.sprite.collide_rect_ratio(0.85))

        if collide:
            self.game.enemyCollided = True
            if pressed[pygame.K_LEFT]:
                self.rect.x += PLAYER_STEPS
            if pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
            if pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS
            if pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS
        else:
            self.game.enemyCollided = False

    def collide_weapon(self):
        collide = pygame.sprite.spritecollide(self, self.game.weapons, True)
        
        if collide:
            self.swordEquipped = True

    def shoot_fireball(self):
        pressed = pygame.key.get_pressed()

        if self.swordEquipped and self.canShoot:
            if pressed[pygame.K_SPACE]:
                Projectile(self.game, self.rect.x, self.rect.y)
                self.canShoot = False
    
    def shootCooldown(self):
        if not self.canShoot:
            self.counter += 1

            if self.counter >= self.coolDown:
                self.counter = 0
                self.canShoot = True

    def damage(self, amount):
        self.health -= amount
        self.healthbar.damage(PLAYER_HEALTH, self.health)

        if self.health <= 0:
            self.kill()
            self.healthbar.kill_healthbar()
            # self.running = False