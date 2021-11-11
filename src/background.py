import pygame


class BackGround:
    def __init__(self):
        self.image = pygame.transform.scale2x(pygame.image.load("assets/sprites/background.png"))
    

    def draw(self, screen):
        screen.blit(self.image, (0, 0))