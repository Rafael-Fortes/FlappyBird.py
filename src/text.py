import pygame


class Text:
    def __init__(self):
        # initializes the text object
        pygame.font.init()

        # importing the game font
        self.font = pygame.font.Font("assets/font/fb_font.TTF", 42)
        

    def draw(self, screen, text, pos, shadow=False):
        # creates a text surface
        self.font_text = self.font.render(text, True, (225, 225, 225))
        self.font_rect = self.font_text.get_rect(center=pos)

        # creates a shadow effect if shadow parameter is True
        if shadow:
            self.font_shadow = self.font.render(text, True, (0, 0, 0))
            screen.blit(self.font_shadow, (self.font_rect.x+2, self.font_rect.y+2))

        # draws the text surface on screen
        screen.blit(self.font_text, self.font_rect)
