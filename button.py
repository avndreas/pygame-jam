import pygame
import sys

class Button():
    def __init__(self, image, pos, text_input, font, base_colour, hovering_colour):
        self.image = image
        self.pos = pos
        self.base_colour = base_colour
        self.hovering_colour = hovering_colour
        self.rect = self.image.get_rect(center = (self.pos[0], self.pos[1]))
        self.font = font
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_colour)
        self.text_rect = self.text.get_rect(center = (self.pos[0], self.pos[1]))
        
        
    
    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
    
    def changeColour(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_colour)
        else:
            self.text = self.font.render(self.text_input, True, self.base_colour)

