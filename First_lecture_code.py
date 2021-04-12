import pygame

pygame.init()

width = 600 # width of the surface of pygame
height = 600 # height of the surface of pygame

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clicker Game")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill('white')
    pygame.display.update()

pygame.quit()