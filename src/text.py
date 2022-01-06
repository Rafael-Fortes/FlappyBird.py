import pygame


class Text:
    def __init__(self):
        pygame.font.init()

        self.font = pygame.font.Font("assets/font/fb_font.TTF", 42)
        

    def draw(self, screen, text, pos, shadow=False):
        self.font_text = self.font.render(text, True, (225, 225, 225))
        self.font_rect = self.font_text.get_rect(center=pos)

        if shadow:
            self.font_shadow = self.font.render(text, True, (0, 0, 0))
            screen.blit(self.font_shadow, (self.font_rect.x+2, self.font_rect.y+2))

        screen.blit(self.font_text, self.font_rect)
