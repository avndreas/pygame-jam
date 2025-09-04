import pygame
import sys

class TextBox():
    def __init__(self, dimensions, pos, caption_input, body_input, base_colour, text_colour, font):
        self.dimensions = dimensions
        self.pos = pos - (dimensions / 2)

        self.base_colour = base_colour
        self.text_colour = text_colour

        self.rect = pygame.Rect(self.pos, self.dimensions)
        self.font = font

        self.caption_input = caption_input
        self.caption_text = self.font.render(self.caption_input, True, self.text_colour)
        self.caption_rect = pygame.Rect(self.pos, self.dimensions / 1.5)

        # self.body_input = body_input
        # self.text = self.font.render(self.text_input, True, self.base_colour)
        # self.text_rect = self.text.get_rect(center = (self.pos[0], self.pos[1]))

    def render(self, screen):
        pygame.draw.rect(screen, self.base_colour, self.caption_rect)
        screen.blit(self.caption_text, self.pos)
    
    def update_text(self, text):
        self.text_input = text
        self.text = self.font.render(self.text_input, True, self.text_colour)
    
    def update_caption(self, caption):
        self.caption = caption
        self.caption = self.font.render(self.caption, True, self.text_colour)
    
    def changeColour(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_colour)
        else:
            self.text = self.font.render(self.text_input, True, self.base_colour)

    def clear(self):
        self.clear
