import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font('assets/fonts/pixel.ttf', 30)
screen = pygame.display.set_mode([800, 500])

run = True
while run:
    clock.tick(fps)
    screen.fill('white')
    txt = font.render('score: ', True, 'black')
    screen.blit(txt, (100, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit

