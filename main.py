import pygame, time, sys
import mapview
from button import Button

pygame.init()
screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w / 1.6 * 1.5
screenHeight = screenInfo.current_h / 1.9 * 1.5
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Kingdom of Bread")

BG = pygame.image.load("assets/ebicgames.png")
BG = pygame.transform.scale(BG, (screenWidth, screenHeight))
screen.blit(BG, (0, 0))
pygame.display.flip()

main_font = pygame.font.SysFont("cambria", 50)

pygame.time.delay(200)



def main_menu():
    pygame.display.flip()
    pygame.display.set_caption("Kingdom of Bread - Main Menu")
    BG = pygame.image.load("assets/green_mountains.png")
    BG = pygame.transform.scale(BG, (screenWidth, screenHeight))

    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1

    play_button = Button(image = pygame.image.load("assets/play_button.png"), pos = (screenWidth / 2, screenHeight / 3 * 2), text_input = "Play", font = main_font, base_colour = "black", hovering_colour = "orange")
    while running:
        # x += 50 * delta_time
        screen.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()


        for button in [play_button]:
            button.changeColour(mouse_pos)
            button.update(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))

def play():
    pygame.display.set_caption("Kingdom of Bread")
    screen.fill("black")
    pygame.display.flip()
    print("Running mapview")
    mapview.run(screen)
    # running = True
    # while running:
    #     mouse_pos = pygame.mouse.get_pos()
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             pass
    #     pygame.display.flip()
    

def options():
    pass

main_menu()

pygame.quit()