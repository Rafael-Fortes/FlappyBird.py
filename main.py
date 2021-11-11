import pygame
from sys import exit
from src import game


game = game.Game(500, 900)
clock = pygame.time.Clock()

CHANGE_SPRITE = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_SPRITE, 200)

pygame.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.bird.jump()
        
        if event.type == CHANGE_SPRITE:
            game.bird.change_sprite()
    
    
    game.update()
    game.draw()

    pygame.display.update()
    clock.tick(75)
