import pygame, time, sys, math, placeview
from pygame.math import *
from button import Button


MAP_SPEED = 1000

def run(screen, location):
    pygame.init()
    screenInfo = pygame.display.Info()
    screenWidth = screenInfo.current_w 
    screenHeight = screenInfo.current_h 
    pygame.display.set_caption("Kingdom of Bread")
    pygame.display.flip()
    main_font = pygame.font.SysFont("cambria", 50)
    BG = pygame.image.load("assets/green_mountains.png")
    BG = pygame.transform.scale(BG, (screenWidth, screenHeight))
    # BG = pygame.transform.scale(BG, (screenWidth, screenHeight))
    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1
    # ----------- Boilerplate above ------------

    while running:
        # x += 50 * delta_time
        screen.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    location.cleared = True
                    running = False
                # if event.key == pygame.K_w and not player.get_moving():
                #     pass
                # if event.key == pygame.K_d and not player.get_moving():
                #     pass
                # if event.key == pygame.K_s and not player.get_moving():
                #     pass
                # if event.key == pygame.K_a and not player.get_moving():
                #     pass
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()

        
        # ------- Movement -----------
        # if player.destination != player.location:
        #     player.set_moving(True)
        #     #vec = [a - b for a, b in zip(list(destination.coordinates), list(current_location.coordinates))]
        #     vec = player.destination.coordinates - player.get_coordinates()
        #     mag = Vector2.magnitude(vec)
        #     normvec = Vector2.normalize(vec)
        #     if mag < 10:
        #         player.set_coordinates(player.destination.coordinates)
        #         player.location = player.destination
        #         player.set_moving(False)
        #     else:
        #         player.set_coordinates(player.coordinates + normvec * MAP_SPEED * delta_time)
        # else:
        #     pass

        # --------------- Maintenance stuff ------------------
        for button in []:
            button.changeColour(mouse_pos)
            button.update(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))


