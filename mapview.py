import pygame, time, sys, math
from pygame.math import *
from button import Button


MAP_SPEED = 1000

def run(screen):
    pygame.init()
    screenInfo = pygame.display.Info()
    screenWidth = screenInfo.current_w 
    screenHeight = screenInfo.current_h 
    # screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Kingdom of Bread")
    pygame.display.flip()
    main_font = pygame.font.SysFont("cambria", 50)
    BG = pygame.image.load("assets\map.png")
    # BG = pygame.transform.scale(BG, (screenWidth, screenHeight))
    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1
    # ----------- Boilerplate above ------------

    bacil = Location()
    farms = Location()

    bacil = Location("Bacil", Vector2(652, 645), None, None, farms, None)
    farms = Location("Farms", Vector2(652, 2000), bacil, None, None, None)

    locations = [bacil, farms]#, BFERRY, RFERRY, RYE]
    current_location = bacil
    destination = bacil

    while running:
        # x += 50 * delta_time
        screen.blit(BG, (-(current_location.coordinates[0] - (screenWidth / 2)), -(current_location.coordinates[1] - (screenHeight / 2))))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    destination = farms
                    print("Moved to farms")
        if destination != current_location:
            #vec = [a - b for a, b in zip(list(destination.coordinates), list(current_location.coordinates))]
            vec = destination.coordinates - current_location.coordinates
            mag = Vector2.magnitude(vec)
            normvec = Vector2.normalize(vec)
            if mag < 30:
                current_location.coordinates = destination.coordinates
                current_location = destination
            else:
                current_location.coordinates += normvec * MAP_SPEED * delta_time


        # --------------- Maintenance stuff below ------------------
        for button in []:
            button.changeColour(mouse_pos)
            button.update(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))


class Location():
    def __init__(self, name = None, coordinates = None, north = None, east = None, south = None, west = None):
        self.name = name
        self.coordinates = coordinates
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    
    def set_values(self, name = None, coordinates = None, north = None, east = None, south = None, west = None):
        if name != None:
            self.name = name
        if coordinates != None:
            self.coordinates = coordinates
        if north != None:
            self.north = north
        if east != None:
            self.east = east
        if south != None:
            self.south = south
        if west != None:
            self.west = west

    