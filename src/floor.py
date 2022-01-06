import pygame


class Floor:
    def __init__(self, y):
        self.floor = pygame.transform.scale2x(pygame.image.load("assets/sprites/base.png"))
             
        self.y = y
        self.x1 = 0
        self.x2 = 576
    

    def draw(self, screen):
        screen.blit(self.floor, (self.x1, self.y))
        screen.blit(self.floor, (self.x2, self.y))


    def move(self):
        self.x1 -= 5
        self.x2 -= 5

        if self.x1 <= -576:
            self.x1 = 576
        elif self.x2 <= -576:
            self.x2 = 576
    