import pygame, time, sys, math, placeview, font
from pygame.math import *
from button import Button
from textbox import TextBox


MAP_SPEED = 1000

def run(screen):
    pygame.init()
    screenInfo = pygame.display.Info()
    screenWidth = screenInfo.current_w 
    screenHeight = screenInfo.current_h 
    # screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Kingdom of Bread")
    pygame.display.flip()
    MAIN_FONT = font.MAIN_FONT
    BG = pygame.image.load("assets\map.png")
    # BG = pygame.transform.scale(BG, (screenWidth, screenHeight))
    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1
    # ----------- Boilerplate above ------------

    # bacil = Location()
    # farms = Location()

    bacil = Location("Bacil", Vector2(652, 645))
    farms = Location("Farms", Vector2(652, 2000))
    temp = Location("Temp", Vector2(1200, 1000))
    bacil.set_values(south = farms)
    farms.set_values(north = bacil, east = temp)
    temp.set_values(west = farms)

    locations = [bacil, farms]#, BFERRY, RFERRY, RYE]

    player = Player(bacil.coordinates.copy(), bacil, bacil)

    while running:
        screen.blit(BG, ((screenWidth / 2) - player.get_coordinates()[0], 
                         (screenHeight / 2) - player.get_coordinates()[1]))
        mouse_pos = pygame.mouse.get_pos()

        # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not player.get_moving() and player.location.cleared:
                    if player.location.north != None:
                        player.destination = player.location.north
                if event.key == pygame.K_d and not player.get_moving() and player.location.cleared:
                    if player.location.east != None:
                        player.destination = player.location.east
                if event.key == pygame.K_s and not player.get_moving() and player.location.cleared:
                    if player.location.south != None:
                        player.destination = player.location.south
                if event.key == pygame.K_a and not player.get_moving() and player.location.cleared:
                    if player.location.west != None:
                        player.destination = player.location.west
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    if not player.location.cleared:
                        placeview.run(screen, player.location)

        
        # ------- Movement -----------
        if player.destination != player.location:
            player.set_moving(True)
            #vec = [a - b for a, b in zip(list(destination.coordinates), list(current_location.coordinates))]
            vec = player.destination.coordinates - player.get_coordinates()
            mag = Vector2.magnitude(vec)
            normvec = Vector2.normalize(vec)
            if mag < 10: # Arrived at location
                player.set_coordinates(player.destination.coordinates)
                player.location = player.destination
                player.set_moving(False)
            else:
                player.set_coordinates(player.coordinates + normvec * MAP_SPEED * delta_time)
        else: # At location
            #locationBox = TextBox(Vector2(300, 100), Vector2(screenWidth / 2, screenHeight * 2 / 5), player.location.name, "Test text", "white", "black", pygame.font.SysFont("cambria", 50))
            boxDimensions = Vector2(300, 200)
            locationBox = TextBox(boxDimensions, Vector2(boxDimensions.x, boxDimensions.y - (font.MAIN_FONT_SIZE + 10)), player.location.name, "Test text", "white", "black", pygame.font.SysFont("cambria", 50))

            locationBox.render(screen)

        # --------------- Maintenance stuff ------------------
        for button in []:
            button.changeColour(mouse_pos)
            button.update(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))


class Location():
    def __init__(self, name = None, coordinates = None, north = None, east = None, south = None, west = None, cleared = False):
        self.name = name
        self.coordinates = coordinates
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.cleared = cleared
    
    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return self.name == other.name and self.coordinates == other.coordinates
    
    def set_values(self, name = None, coordinates = None, north = None, east = None, south = None, west = None, cleared = False):
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
        if cleared:
            self.cleared = False


class Player():
    def __init__(self, coordinates, location, destination, moving = False):
        self.coordinates = coordinates
        self.location = location
        self.destination = destination
        self.moving = moving

    def get_coordinates(self):
        return self.coordinates.copy()

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates.copy() # Important lesson on why you should use setter functions
    
    def get_moving(self):
        return self.moving
    
    def set_moving(self, moving):
        self.moving = moving
    
