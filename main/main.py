from tiles import *
from boss import *
from enemy import *
from config import *
from button import *
from player import *
from weapons import *
from spritesheet import *
import sys
import csv
import pygame
import scipy.io.wavfile as wav
import sounddevice as sd
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font('assets/fonts/pixel.ttf', 30)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.buttons = []

        self.running = True
        # self.game_state = 'main menu'
        self.game_state = 'Play'
        self.paused = False

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
                elif column == 'B':
                    Bridge(self, j, i, 1, 90)
                elif column == 'Z':
                    Boss(self, j, i)
                else:
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
        self.terrain_spritesheet = Spritesheet('overworld.png')
        self.player_spritesheet = Spritesheet('player.png')
        self.enemy_spritesheet = Spritesheet('slime_green.png')
        self.purple_slime_spritesheet = Spritesheet('slime_purple.png')
        self.weapons_spritesheet = Spritesheet('swords.png')
        self.projectile_spritesheet = Spritesheet('fireball.png')
        self.coin_spritesheet = Spritesheet('coin.png')
        self.fruit_spritesheet = Spritesheet('fruit.png')

        self.createTileMap() 

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.paused = not self.paused

            for btn in self.buttons:
                btn.checkClick(event)

    def draw(self):
        self.clock.tick(FPS)

        if self.game_state == 'main menu':
            self.draw_main_menu()
        elif self.game_state == 'Play':
            self.draw_game()
        elif self.game_state == 'Leaderboard':
            self.draw_leaderboard()
        elif self.game_state == 'Controls':
            self.draw_controls()
        
        if self.paused:
            self.draw_paused()

        pygame.display.update()

    def draw_game(self):
        self.screen.fill(OCEAN)
        self.all_sprites.draw(self.screen) 

        # Displays score
        txt = self.font.render('score: ' + str(self.score), True, 'black')
        self.screen.blit(txt, (SCORE_X, SCORE_Y))

        # Display gold
        txt = self.font.render(str(self.gold), True, 'black')
        self.screen.blit(txt, (GOLD_X, GOLD_Y))
        gold_img = []
        self.coin_spritesheet.parse_sprite('coin', 'idle', gold_img)
        gold_img = pygame.transform.scale(gold_img[0], (TILESIZE, TILESIZE))
        self.screen.blit(gold_img, (GOLD_X - TILESIZE * 1.1, GOLD_Y))

        # Display 'Mana:'
        if self.player.swordEquipped:
            txt = self.font.render('Mana: ', True, 'black')
            self.screen.blit(txt, (MANA_BAR_X, MANA_BAR_Y - 8))

    def draw_main_menu(self):
        self.screen.fill(OCEAN)

        # Game title
        txt = self.font.render(TITLE, True, 'white')
        self.screen.blit(txt, (SCORE_X / 2, SCORE_Y * 6))

        # Buttons
        Button(self, BTN_X, PLAY_BTN_Y, BTN_HEIGHT, BTN_WIDTH, 'Play', 'Play')
        Button(self, BTN_X, LEAD_BTN_Y, BTN_HEIGHT, BTN_WIDTH, 'Leaderboard', 'Leaderboard')
        Button(self, BTN_X, CONT_BTN_Y, BTN_HEIGHT, BTN_WIDTH, 'Controls', 'Controls')
    
    def draw_leaderboard(self):
        self.screen.fill(OCEAN)
        pygame.draw.rect(self.screen, GREY, pygame.Rect(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT))

        with open('data/leaderboard.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for i, line in enumerate(csvFile):
                name = self.font.render(line[0], True, 'black')
                points = self.font.render(line[1], True, 'black')
                self.screen.blit(name, (NAME_X, NAME_Y + i * BTN_HEIGHT))
                self.screen.blit(points, (POINTS_X, NAME_Y + i * BTN_HEIGHT))
        
        Button(self, BACK_BTN_X, BACK_BTN_Y, BTN_HEIGHT, BACK_BTN_WIDTH, 'main menu', ' X')
    
    def draw_controls(self):
        pygame.draw.rect(self.screen, GREY, pygame.Rect(PAUSE_X, PAUSE_Y, PAUSE_WIDTH, PAUSE_HEIGHT))

        # Controls
        title = self.font.render('Controls', True, 'black')
        self.screen.blit(title, (CONTROL_X, CONTROL_Y))
        arrows = self.font.render('Arrows:', True, 'black')
        self.screen.blit(arrows, (KEY_X, KEY_Y))
        movement = self.font.render('movement', True, 'black')
        self.screen.blit(movement, (KEY_X + BTN_WIDTH, KEY_Y))
        space = self.font.render('Space:', True, 'black')
        self.screen.blit(space, (KEY_X, KEY_Y + 2 * BTN_HEIGHT))
        shoot = self.font.render('shoot', True, 'black')
        self.screen.blit(shoot, (KEY_X + BTN_WIDTH, KEY_Y + 2 * BTN_HEIGHT))
        key = self.font.render('Q:', True, 'black')
        self.screen.blit(key, (KEY_X, KEY_Y + 4 * BTN_HEIGHT))
        pause = self.font.render('pause', True, 'black')
        self.screen.blit(pause, (KEY_X + BTN_WIDTH, KEY_Y + 4 * BTN_HEIGHT))

        Button(self, PAUSE_CLOSE_X, PAUSE_Y, BTN_HEIGHT, BACK_BTN_WIDTH, 'main menu', ' X')

    def draw_paused(self):
        pygame.draw.rect(self.screen, GREY, pygame.Rect(PAUSE_X, PAUSE_Y, PAUSE_WIDTH, PAUSE_HEIGHT))

        title = self.font.render('Paused', True, 'black')
        self.screen.blit(title, (WIN_WIDTH / 2 - 35, PAUSE_Y + 10))
        Button(self, RESUME_X, RESUME_Y, BTN_HEIGHT, BTN_WIDTH, 'UNPAUSE', 'Resume')
        Button(self, PAUSE_CLOSE_X, PAUSE_Y, BTN_HEIGHT, BACK_BTN_WIDTH, 'UNPAUSE', ' X')
        Button(self, RESUME_X, QUIT_Y, BTN_HEIGHT, BTN_WIDTH, 'main menu', 'Quit')

    def camera(self):
        if self.enemyCollided == False and self.blockCollided == False:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                for sprite in self.all_sprites:
                    sprite.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                for sprite in self.all_sprites:
                    sprite.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                for sprite in self.all_sprites:
                    sprite.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                for sprite in self.all_sprites:
                    sprite.rect.y -= PLAYER_STEPS
    
    def play_sound(self, filename):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '..', 'assets', 'sounds', filename)
        sample_rate, data = wav.read(file_path)
        sd.play(data, samplerate=sample_rate)

    def run(self):
        self.create()

        while self.running:
            if self.game_state == 'Play' and not self.paused:
                self.camera()
                self.update()

            self.events()
            self.draw()

game = Game()
game.run()

pygame.quit()
sys.exit()
