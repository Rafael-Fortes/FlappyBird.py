import pygame


class Overlay:
    def __init__(self):
        # loads the overlay image
        self.overlay = pygame.transform.scale2x(pygame.image.load("assets/sprites/message.png"))

    
    def draw(self, screen):
        #draws the overlay images
        screen.blit(self.overlay, (70, 200))
    