import pygame
from config import *

class Button():
    def __init__(self, game, x, y, height, width, state, txt):
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topleft = (x, y)
        self.state = state
        self.txt = txt
        self.draw()
    
    def draw(self):
        # Button background
        pygame.draw.rect(self.game.screen, RED, self.rect)

        # Button text
        txt = self.game.font.render(self.txt, True, 'white')
        self.game.screen.blit(txt, (self.rect.x, self.rect.y))

    def checkClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.game.game_state = self.state