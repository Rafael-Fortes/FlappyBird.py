import pygame
from src import bird, pipes, background, floor, text, overlay
from sys import exit


class Game:
    def __init__(self, width, height):
        # initialize all objects and variables

        self.screen = pygame.display.set_mode((width, height))
        self.bg = background.BackGround()
        self.floor = floor.Floor(height-150)
        self.overlay = overlay.Overlay()

        self.bird = bird.Bird(100, height // 2)

        self.pipes = pipes.Pipe()
        self.pipes.create_pipes(first=True)

        self.score = 0
        self.score_text = text.Text()

        self.running = False
        

    def draw(self):
        # draws all objects

        self.bg.draw(self.screen)
        self.pipes.draw(self.screen)
        self.floor.draw(self.screen)

        if self.running:
            self.bird.draw(self.screen)
            self.score_text.draw(self.screen, f"score {self.score}", (400, 40), True)   
        else:
            self.overlay.draw(self.screen)

        


    def update(self):
        # updates all objects

        if self.running:
            self.floor.move()
            self.pipes.move()
            self.bird.move()

        if self.pipes.queue[0][0] <= -100:
            self.pipes.delete_pipes()
            self.pipes.create_pipes()

        if self.check_collision():
            self.running = False
            self.reset()

        # detect when the bird pass between the pipes and add 1 point to score
        if self.pipes.queue[0][0] == 100:
            self.score += 1
    

    def check_collision(self):
        # check if the bird's rect collided with a pipe
        x = self.pipes.queue[0][0]
        y = self.pipes.queue[0][1]

        pipe_bottom_rect = self.pipes.bottom_pipe_surface.get_rect(x=x, y=y)
        pipe_top_rect = self.pipes.top_pipe_surface.get_rect(x=x, y=y-900)

        if pipe_bottom_rect.colliderect(self.bird.bird_rect) or pipe_top_rect.colliderect(self.bird.bird_rect):
            return True
        elif self.bird.bird_rect.centery >= 780:
            return True
        else:
            return False
    

    def reset(self):
        # reset the game
        self.pipes.queue.clear()
        self.pipes.create_pipes(True)
        self.bird.bird_rect.centery = 450
        self.score = 0


