import pygame


class Bird:
    def __init__(self, x, y):
        self.birds = [pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-upflap.png")),
                    pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-midflap.png")),
                    pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-downflap.png"))]
            
        self.i = 1
        self.bird_surface = self.birds[self.i]
        self.bird_rect = self.bird_surface.get_rect(center=(x, y))

        self.gravity = 0.25
        self.movement = 0

    
    def draw(self, screen):
        screen.blit(self.rotated_bird, self.bird_rect)
    

    def move(self):
        if self.bird_rect.y <= 0:
            self.bird_rect.y = 0
            self.movement += self.gravity * 2

        self.movement += self.gravity
        self.bird_rect.centery += self.movement

        self.rotated_bird = pygame.transform.rotozoom(self.bird_surface, -self.movement * 3, 1)
    

    def change_sprite(self):
        if self.i < 2:
            self.i += 1
        else:
            self.i = 0

        self.bird_surface = self.birds[self.i]        
    

    def jump(self):
        self.movement = 0
        self.movement -= 9
