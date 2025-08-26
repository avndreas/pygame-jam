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
    KNIFE = pygame.image.load("assets/bread_knife.png")


    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1

    knife_position = Vector2(screenWidth / 2 - KNIFE.get_width() / 2, screenHeight / 2 - KNIFE.get_height() / 2)
    knife_point = Vector2(KNIFE.get_width(), KNIFE.get_height()) + knife_position

    velocity = 0
    max_velocity = 5000
    strength = 50

    # ----------- Boilerplate above ------------

    stab_depth = 150
    stab_cooldown = False

    def stab(knife_position, knife_point):
        stab_cooldown = True
        startpos = knife_position.y
        x = 1
        while knife_position.y <= startpos + stab_depth:
            knife_position.y += 40/x
            x += 1
            screen.blit(BG, (0, 0))
            screen.blit(KNIFE, knife_position)
            pygame.display.flip()

    def unstab(knife_position, knife_point):
        startpos = knife_position.y
        x = 1
        while knife_position.y >= startpos - stab_depth:
            knife_position.y -= 40/x
            x += 1
            screen.blit(BG, (0, 0))
            screen.blit(KNIFE, knife_position)
            pygame.display.flip()
        stab_cooldown = False

    # Game loop
    while running:
        screen.blit(BG, (0, 0))
        screen.blit(KNIFE, knife_position)
        pressed = pygame.key.get_pressed()
        #print(knife_point)

        if pressed[pygame.K_d] and not pressed[pygame.K_a]:
            velocity += strength
            if velocity < 0:
                velocity *= 0.8
        elif pressed[pygame.K_a] and not pressed[pygame.K_d]:
            if velocity > 0:
                velocity *= 0.8
            velocity -= strength
        else:
            velocity *= 0.8
            if abs(velocity) < 10:
                velocity = 0
        knife_position.x += velocity * delta_time
        knife_point = Vector2(KNIFE.get_width(), KNIFE.get_height()) + knife_position

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
                if event.key == pygame.K_SPACE and not stab_cooldown:
                    stab(knife_position, knife_point)
                    screen.blit(BG, (0, 0))
                    screen.blit(KNIFE, knife_position)
                    pygame.display.flip()
                    #pygame.time.delay(70)
                    unstab(knife_position, knife_point)
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()

        # --------------- Maintenance stuff ------------------
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))


