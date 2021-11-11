import pygame
from random import randint


class Pipe:
    def __init__(self):
        self.pipes_surface = [pygame.transform.scale2x(pygame.image.load("assets/sprites/pipe-green.png")),
                            pygame.transform.scale2x(pygame.image.load("assets/sprites/pipe-green.png"))]

        self.bottom_pipe_surface = self.pipes_surface [0]
        self.top_pipe_surface = pygame.transform.rotate(self.pipes_surface[1], 180)

        self.queue = []



    def draw(self, screen):
        for pipe in self.queue:
            screen.blit(self.bottom_pipe_surface, (pipe[0], pipe[1]))
            screen.blit(self.top_pipe_surface, (pipe[0], pipe[1] - 900))
    

    def create_pipes(self, first=False):
        if first:
            for i in range(3):
                y = randint(350, 580)
                x = 700 + (i * 330)

                self.queue.append([x, y])
        else:
            y = randint(350, 580)
            x = 900

            self.queue.append([x, y])
    

    def delete_pipes(self):
        self.queue.pop(0)

    
    def move(self):
        for pipe in self.queue:
            pipe[0] -= 5
