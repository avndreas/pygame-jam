import pygame
import sys

# pygame.init()
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption("Button")
# main_font = pygame.font.SysFont("cambria", 50)

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

# button_surface = pygame.image.load("assets/play_button.png")
# button_surface = pygame.transform.scale(button_surface, (400, 150))

# button = Button(button_surface, 400, 300, "Button text")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             button.checkForInput(pygame.mouse.get_pos())
#         screen.fill("white")

#         button.update()
#         button.changeColour(pygame.mouse.get_pos())

#         pygame.display.update()