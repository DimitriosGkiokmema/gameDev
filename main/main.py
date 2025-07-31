from config import *
from tiles import *
from enemy import *
from player import *
from weapons import *
from spritesheet import *
import sys
import pygame
import scipy.io.wavfile as wav
import sounddevice as sd
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font('assets/fonts/pixel.ttf', 30)
        pygame.display.set_caption('Land of Lost')
        self.clock = pygame.time.Clock()

        self.running = True
        self.enemyCollided = False
        self.blockCollided = False
        self.score = 0
        self.gold = 0
    
    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)

                if column == 'M':
                    Block(self, j, i)
                elif column == 'P':
                    self.player = Player(self, j, i)
                elif column == 'E':
                    self.enemy = Enemy(self, j, i)
                elif column == 'W':
                    Water(self, j, i)
                elif column == 'T':
                    Tree(self, j, i)
                elif column == 'S':
                    Weapon(self, j, i)
                elif column == 'C':
                    Coin(self, j, i)
                elif column == 'F':
                    Fruit(self, j, i)
                elif column == 'B' or column == '.':
                    edge = False
                    side = 'ground'

                    if j > 0 and tilemap[i][j - 1] == 'W':
                        side = 'left'
                        if i > 0 and tilemap[i - 1][j] == 'W': # up-left
                            edge = True
                        elif i < len(tilemap) - 1 and tilemap[i + 1][j] == 'W': # down-left
                            side = 'down'
                            edge = True
                    elif j < len(tilemap[0]) - 1 and tilemap[i][j + 1] == 'W':
                        side = 'right'
                        if i < len(tilemap) - 1 and tilemap[i + 1][j] == 'W': # down-right
                            edge = True
                        elif i > 0 and tilemap[i - 1][j] == 'W': # up-right
                            side = 'up'
                            edge = True
                    elif i > 0 and tilemap[i - 1][j] == 'W':
                        side = 'up'
                    elif i < len(tilemap) - 1 and tilemap[i + 1][j] == 'W':
                        side = 'down'
                    
                    if side != 'ground':
                        Cliff(self, j, i, side, edge)


    def create(self):
        # Layers
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.main_player = pygame.sprite.LayeredUpdates()
        self.weapons = pygame.sprite.LayeredUpdates()
        self.projectiles = pygame.sprite.LayeredUpdates()
        self.healthbars = pygame.sprite.LayeredUpdates()
        self.coins = pygame.sprite.LayeredUpdates()
        self.fruits = pygame.sprite.LayeredUpdates()

        # Spritesheets
        self.terrain_spritesheet = Spritesheet('terrain')
        self.terrain_spritesheet.load_sheet('assets/images/overworld.png')
        self.player_spritesheet = Spritesheet('knight')
        self.player_spritesheet.load_sheet('assets/images/player.png')
        self.enemy_spritesheet = Spritesheet('slime_green')
        self.enemy_spritesheet.load_sheet('assets/images/slime_green.png')
        self.weapons_spritesheet = Spritesheet('sword')
        self.weapons_spritesheet.load_sheet('assets/images/swords.png')
        self.projectile_spritesheet = Spritesheet('fireball')
        self.projectile_spritesheet.load_sheet('assets/images/fireball.png')
        self.coin_spritesheet = Spritesheet('coin')
        self.coin_spritesheet.load_sheet('assets/images/coin.png')
        self.fruit_spritesheet = Spritesheet('fruit')
        self.fruit_spritesheet.load_sheet('assets/images/fruit.png')

        self.createTileMap()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(OCEAN)
        self.all_sprites.draw(self.screen) 
        self.clock.tick(FPS)

        # Displays score
        txt = self.font.render('score: ' + str(self.score), True, 'black')
        self.screen.blit(txt, (SCORE_X, SCORE_Y))

        # Display gold
        txt = self.font.render(str(self.gold), True, 'black')
        self.screen.blit(txt, (GOLD_X, GOLD_Y))
        gold_img = []
        self.coin_spritesheet.parse_sprite('idle', gold_img)
        gold_img = pygame.transform.scale(gold_img[0], (TILESIZE, TILESIZE))
        self.screen.blit(gold_img, (GOLD_X - TILESIZE * 1.1, GOLD_Y))

        pygame.display.update()

    def camera(self):
        if self.enemyCollided == False and self.blockCollided == False:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y -= PLAYER_STEPS
    
    def play_sound(self, filename):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '..', 'assets', 'sounds', filename)
        sample_rate, data = wav.read(file_path)
        sd.play(data, samplerate=sample_rate)

    def run_game(self):
        while self.running:
            self.events()
            self.camera()
            self.update()
            self.draw()

game = Game()
game.create()
game.run_game()

pygame.quit()
sys.exit()