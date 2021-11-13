import pygame


class Bird:
    def __init__(self, x, y):
        # Loads the Bird sprites.
        self.birds = [pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-upflap.png")),
                    pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-midflap.png")),
                    pygame.transform.scale2x(pygame.image.load("assets/sprites/yellowbird-downflap.png"))]

        self.i = 1  # controls the sprite index.
        self.bird_surface = self.birds[self.i]  # It's the current bird sprite
        self.bird_rect = self.bird_surface.get_rect(center=(x, y))  # Creates a rect arround the bird sprite to control the position.

        # controls the bird's movements.
        self.gravity = 0.25
        self.movement = 0


    def draw(self, screen):
        # draws the bird on screen surface.
        screen.blit(self.rotated_bird, self.bird_rect)
    

    def move(self):
        """makes the bird move."""

        # prevents the bird from passing the height limit.
        if self.bird_rect.y <= 0:
            self.bird_rect.y = 0
            self.movement += self.gravity * 2

        # updtaes the bird's movement.
        self.movement += self.gravity
        self.bird_rect.centery += self.movement

        # creates a new bird's rotationed surface to give a feeling of fligh.
        self.rotated_bird = pygame.transform.rotozoom(self.bird_surface, -self.movement * 3, 1)
    

    def change_sprite(self):
        """animates the bird by change the sprite in a cycle."""

        # changes the sprite index.
        if self.i < 2:
            self.i += 1
        else:
            self.i = 0

        # updates the bird surface to current index.
        self.bird_surface = self.birds[self.i]        
    

    def jump(self):
        """makes the bird jump."""
        self.movement = 0
        self.movement -= 9
