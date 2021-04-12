# Create a clicker game in Python using Pygame Library. 
# Game description: Animated ( coins, diamonds, chocolates etc or anything of your choice) 
#   objects falling down from the top of the window.
# Player can click on the falling objects to increase the score. Display the score.

import pygame
import random
pygame.font.init()

pygame.init()

score = 0

width = 600 # width of the surface of pygame
height = 600 # height of the surface of pygame

coin_width = 30
coin_height = 30

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clicker Game")
fps = 60 # frames per second
bg = pygame.image.load(r'./GitHub/Python/ClickerGame/bg1.png')
background = pygame.transform.scale(bg, (width, height))

score_font = pygame.font.SysFont('comicsans', 40)

coin_image = pygame.image.load(r'./GitHub/Python/ClickerGame/coin.png')
coin = pygame.transform.scale(coin_image,(coin_width, coin_height))
coin_space = pygame.Rect(random.randint(50,550), 20, coin_width, coin_height)

def updateCoin():
    window.blit(coin, (coin_space.x, coin_space.y))
    if coin_space.y <= 500:
        coin_space.y += 3

clock = pygame.time.Clock()
run = True
while run:
    clock.tick((fps)) # to control the speed of while loop
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if coin_space.collidepoint(x, y):
                score += 1
                coin_space = pygame.Rect(random.randint(50,550), 20, coin_width, coin_height)
                #print("clicked")

    if coin_space.y <= 500:
        updateCoin()
    else:
        coin_space = pygame.Rect(random.randint(50,550), 20, coin_width, coin_height)

    draw_text = score_font.render("Score: " + str(score), 1, 'black')
    window.blit(draw_text, (5, 5))
    
    pygame.display.update()


pygame.quit()