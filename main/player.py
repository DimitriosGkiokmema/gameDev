import math
import pygame
from config import *
from healthbar import *
from spritesheet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.healthbar = HealthBar(game, x, y, self)
        self.groups = self.game.all_sprites, self.game.main_player
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.width = TILESIZE
        self.height = TILESIZE

        self.dx = 0
        self.dy = 0

        self.image = self.game.player_spritesheet.get_sprite(30, 29, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.direction = "right"
        self.animationCounter = 0

        self.swordEquipped = False
        self.counter = 0
        self.coolDown = 20
        self.canShoot = True

        self.health = PLAYER_HEALTH

        # Fetching character frames
        spritesheet = Spritesheet('knight')
        spritesheet.load_sheet('assets\images\player.png')
        self.rightAnimation = []
        spritesheet.parse_sprite('right', self.rightAnimation)
        self.leftAnimation = []
        spritesheet.parse_sprite('left', self.leftAnimation)
        self.upAnimation = []
        spritesheet.parse_sprite('up', self.upAnimation)
        self.downAnimation = []
        spritesheet.parse_sprite('down', self.downAnimation)

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
            self.game.play_sound("power_up.wav")

    def shoot_fireball(self):
        pressed = pygame.key.get_pressed()

        if self.swordEquipped and self.canShoot:
            if pressed[pygame.K_SPACE]:
                Projectile(self.game, self.rect.x, self.rect.y, "player", True)
                self.canShoot = False
    
    def shootCooldown(self):
        if not self.canShoot:
            self.counter += 1

            if self.counter >= self.coolDown:
                self.counter = 0
                self.canShoot = True

    def damage(self, amount):
        self.game.play_sound("hurt.wav")
        self.health -= amount
        self.healthbar.damage(PLAYER_HEALTH, self.health)

        if self.health <= 0:
            self.kill()
            self.healthbar.kill_healthbar()
            self.running = False