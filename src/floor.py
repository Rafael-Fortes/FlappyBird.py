import pygame


class Floor:
    def __init__(self, y):
        # loads the floor sprite
        self.floor = pygame.transform.scale2x(pygame.image.load("assets/sprites/base.png"))
             
        self.y = y
        self.x1 = 0
        self.x2 = 576
    

    def draw(self, screen):
        # draws two floor images in diferents x position
        screen.blit(self.floor, (self.x1, self.y))
        screen.blit(self.floor, (self.x2, self.y))


    def move(self):
        """moves both floor in the same time and when one floor disappear from screen, 
        it gets a new x position behind the second floor making a loop."""
        
        self.x1 -= 5
        self.x2 -= 5

        if self.x1 <= -576:
            self.x1 = 576
        elif self.x2 <= -576:
            self.x2 = 576
    