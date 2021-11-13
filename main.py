import pygame
from sys import exit
from src import game


game = game.Game(500, 900)
clock = pygame.time.Clock()
running = True


CHANGE_SPRITE = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_SPRITE, 200)

pygame.display.set_caption("FlappyBird.py")
pygame.display.set_icon(pygame.image.load("assets/sprites/yellowbird-midflap.png"))

pygame.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.running:
                game.bird.jump()

            elif event.key == pygame.K_SPACE and not game.running:
                game.running = True
                game.bird.jump()
            
        
        if event.type == CHANGE_SPRITE:
            game.bird.change_sprite()
    
    
    game.update()
    game.draw()

    pygame.display.update()
    clock.tick(75)
