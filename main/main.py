from config import *
from tiles import *
from enemy import *
from player import *
from weapons import *
from spritesheet import *
import sys
import pygame
import scipy.io.wavfile as wavfile
import sounddevice as sd
import os

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Super Cool Game')
        self.clock = pygame.time.Clock()

        # Creating Spritesheet objects
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
        
        self.running = True
        self.enemyCollided = False
        self.blockCollided = False
    
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
                elif column == 'B':
                    if j < ISLAND_SIDE_EDGE and i < ISLAND_TB_EDGE:
                        Cliff(self, j, i, "left", True)
                    elif j >= len(tilemap[0]) - ISLAND_SIDE_EDGE and i < ISLAND_TB_EDGE:
                        Cliff(self, j, i, "up", True)
                    elif j >= len(tilemap[0]) - ISLAND_SIDE_EDGE and i >= len(tilemap) - ISLAND_TB_EDGE:
                        Cliff(self, j, i, "right", True)
                    elif j < ISLAND_SIDE_EDGE and i >= len(tilemap) - ISLAND_TB_EDGE:
                        Cliff(self, j, i, "down", True)
                    elif j < ISLAND_SIDE_EDGE:
                        Cliff(self, j, i, "left", False)
                    elif j >= len(tilemap[0]) - ISLAND_SIDE_EDGE:
                        Cliff(self, j, i, "right", False)
                    elif i < ISLAND_TB_EDGE:
                        Cliff(self, j, i, "up", False)
                    elif i >= len(tilemap) - ISLAND_TB_EDGE:
                        Cliff(self, j, i, "down", False)

    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.main_player = pygame.sprite.LayeredUpdates()
        self.weapons = pygame.sprite.LayeredUpdates()
        self.projectiles = pygame.sprite.LayeredUpdates()
        self.healthbars = pygame.sprite.LayeredUpdates()
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

        sample_rate, data = wavfile.read(file_path)
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