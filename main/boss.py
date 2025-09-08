import math
import pygame
from config import *
from a_star import *
from healthbar import *
import random

class Boss(pygame.sprite.Sprite):
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

        self.image = self.game.purple_slime_spritesheet.get_sprite(63, 167, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.path = []
        self.maxSteps = random.choice(range(20, 120, 10))
        self.currSteps = 0
        self.player_detected = False
        
        self.animationCounter = 0

        self.health = BOSS_HEALTH

        self.shootCounter = 0
        self.waitShoot = random.choice(range(10, 91, 10))
        self.shootState = 'halt'

        # Loading sprite frames
        self.rightAnimation = []
        self.game.purple_slime_spritesheet.parse_sprite('slime_green', 'right', self.rightAnimation)
        self.upAnimation = []
        self.game.purple_slime_spritesheet.parse_sprite('slime_green', 'up', self.upAnimation)

        self.leftAnimation = []
        for i in range(len(self.rightAnimation)):
            self.rightAnimation[i] = pygame.transform.scale(self.rightAnimation[i], (self.width, self.height))
            self.leftAnimation.append(pygame.transform.flip(self.rightAnimation[i], True, False))

        self.downAnimation = []
        for i in range(len(self.upAnimation)):
            self.upAnimation[i] = pygame.transform.scale(self.upAnimation[i], (self.width, self.height))
            self.downAnimation.append(pygame.transform.flip(self.upAnimation[i], False, True))

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

        return diffX < BOSS_DETECTION_RANGE * TILESIZE and diffY < BOSS_DETECTION_RANGE * TILESIZE
    
    def move(self):
        cords = self.cords_to_map()
        if self.path == [] or not type(self.path) == list:
            self.path = get_path(cords, self.game.player.cords_to_map())
            # self.path = get_path((5, 5), (5, 9))

        if cords[1] < self.path[0][1]:
            self.dx += ENEMY_STEPS
        else:
            self.dx -= ENEMY_STEPS
        
        if cords[0] < self.path[0][0]:
            self.dy += ENEMY_STEPS
        else:
            self.dy -= ENEMY_STEPS
        
        self.path = self.path[1:]
            
        if self.shootState == 'shoot':
            Projectile(self.game, self.rect.x, self.rect.y, self.direction, False)
            self.shootState = 'halt'

    def update(self):
        if self.playerInRange():
            self.player_detected = True
        
        if self.player_detected:
            self.move()

        self.animation()
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.dx = 0
        self.dy = 0

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
        self.game.play_sound("explosion.wav")
        self.health = self.health - amount

        if self.health <= 0:
            self.game.score += BOSS_KILL_POINTS
            self.kill()
            self.healthbar.kill()
            self.game.player.max_mana += 1
        else:
            self.healthbar.damage(BOSS_HEALTH, self.health)

    def cords_to_map(self):
        sprite = list(self.game.all_sprites)[0]
        x = ((-sprite.rect.x + self.rect.x) + TILESIZE // 2) // TILESIZE
        y = ((-sprite.rect.y + self.rect.y) + TILESIZE // 2) // TILESIZE
        return (y, x)