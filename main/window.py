import pygame

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Super Cool Game')
background_colour = (200, 80, 50)
screen.fill(background_colour)
pygame.display.flip()

running = True

# game loop
while running:
    for event in pygame.event.get():
    
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

