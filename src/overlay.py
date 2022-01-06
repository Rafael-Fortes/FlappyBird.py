import pygame


class Overlay:
    def __init__(self):
        self.overlay = pygame.transform.scale2x(pygame.image.load("assets/sprites/message.png"))

    
    def draw(self, screen):
        screen.blit(self.overlay, (70, 200))
    