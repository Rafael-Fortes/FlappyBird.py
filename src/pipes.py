import pygame
from random import randint


class Pipe:
    def __init__(self):
        # loads two pipes image and invert one
        self.pipes_surface = [pygame.transform.scale2x(pygame.image.load("assets/sprites/pipe-green.png")),
                            pygame.transform.scale2x(pygame.image.load("assets/sprites/pipe-green.png"))]

        self.bottom_pipe_surface = self.pipes_surface [0]
        self.top_pipe_surface = pygame.transform.rotate(self.pipes_surface[1], 180)

        # creates a queue to put the pipe position
        self.queue = []



    def draw(self, screen):
        # draws the pipes on screen
        for pipe in self.queue:
            screen.blit(self.bottom_pipe_surface, (pipe[0], pipe[1]))
            screen.blit(self.top_pipe_surface, (pipe[0], pipe[1] - 900))
    

    def create_pipes(self, first=False):
        """creates to new pipes with random y position and put then in the queue
        if is the first time that is creating the pipes, this creates three and put then in the queue
        else, just put one pipe in the queue"""

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
        # remove the first pipe from the queue
        self.queue.pop(0)

    
    def move(self):
        # moves the pipe x position
        for pipe in self.queue:
            pipe[0] -= 5
