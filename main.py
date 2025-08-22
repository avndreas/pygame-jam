import pygame, time, sys
from button import Button

pygame.init()
screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w / 1.5
screenHeight = screenInfo.current_h / 1.5
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Kingdom of Bread")

BG = pygame.image.load("assets/ebicgames.png")
BG = pygame.transform.scale(BG, (screenWidth, screenHeight))
screen.blit(BG, (0, 0))
pygame.display.flip()

main_font = pygame.font.SysFont("cambria", 50)

pygame.time.delay(3000)



def main_menu():
    pygame.display.flip()
    pygame.display.set_caption("Kingdom of Bread - Main Menu")
    bipoc_img = pygame.image.load('assets\Bipoc_eating_a_can_of_coke.jpg').convert_alpha()
    BG = pygame.image.load("assets/green_mountains.png")
    BG = pygame.transform.scale(BG, (screenWidth, screenHeight))

    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1

    while running:
        print(time.time())
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


        play_button = Button(image = pygame.image.load("assets/play_button.png"), pos = (screenWidth / 2, screenHeight / 3 * 2), text_input = "Play", font = main_font, base_colour = "black", hovering_colour = "orange")

        for button in [play_button]:
            button.changeColour(mouse_pos)
            button.update(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))

def play():
    screen.fill("black")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play()
        print("Play")
        pygame.display.flip()
    

def options():
    pass

main_menu()

pygame.quit()

    


