import pygame


class BackGround:
    def __init__(self):
        """Loads the background image stretched."""
        self.image = pygame.transform.scale2x(pygame.image.load("assets/sprites/background.png"))
    

    def draw(self, screen):
        """Draws the image on screen surface."""
        screen.blit(self.image, (0, 0))