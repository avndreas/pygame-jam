import pygame, time, sys, math, placeview, json
from pygame.math import *
from button import Button

def run(screen, location, fighter):

    # Enemy initialization
    enemy = None
    with open("assets/characters.json", "r") as f:
        data = json.load(f)
    for item in data['characters']:
        if item['name'] == fighter:
            enemy = item
    print("Fighting ", enemy['name'])
    if enemy == None:
        print("I have no enemies...")
        return

    # Screen and sprite setup
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
    ENEMY = pygame.image.load(enemy['image'])

    # Physics setup
    velocity = 0
    max_velocity = 2000
    strength = 50
    stab_depth = 150
    stab_cooldown = False
    repulsion_force = 800
    stab_range = 20 # pixels

    # Clock setup
    running = True
    x = 0
    clock = pygame.time.Clock()
    delta_time = 0.1

    # Positioning stage
    knife_dimensions = Vector2(KNIFE.get_width(), KNIFE.get_height())
    knife_position = Vector2(screenWidth / 2 - knife_dimensions.x / 2, screenHeight / 2 - knife_dimensions.y / 2)
    knife_point = knife_position + Vector2(0, KNIFE.get_height())

    enemy_dimensions = Vector2(ENEMY.get_width(), ENEMY.get_height())
    enemy_position = Vector2((screenWidth / 2), (3 * screenHeight / 4))
    enemy_weak_spots = [(Vector2(100 * x / enemy['weak_spots'] * (ENEMY.get_width() / 100) - (ENEMY.get_width() / 2) + enemy_position.x  , knife_position.y + (KNIFE.get_height() / 2) + stab_depth))
                        for x in range(1, enemy['weak_spots'])]
    print("100 * x / ", enemy['weak_spots'], " + ", enemy_position.x, " - ", (ENEMY.get_width() / 2))
    for spot in enemy_weak_spots:
        print("Weak spot at ", spot)


    # Functions
    def check_stab(point):
        for spot in enemy_weak_spots:
            if (point - spot).magnitude() <= stab_range:
                print("Hit at ", spot)
                enemy_weak_spots.remove(spot)
                if len(enemy_weak_spots) == 0:
                    print("Enemy defeated!")
                    # location.cleared = True
                    # running = False
                return True
            else: 
                # print("Missed at ", point)
                return False
    def get_bounds(sprite, position): # This assumes the position is the center of the sprite, it's up to the rest of the code to ensure it's rendered that way
        dimensions = Vector2(sprite.get_width(), sprite.get_height())
        top_left = position - dimensions / 2
        bottom_right = position + dimensions / 2
        top_right = top_left + Vector2(dimensions.x, 0)
        bottom_left = top_left + Vector2(0, dimensions.y)
        return (top_left, top_right, bottom_left, bottom_right)

    def render():
        screen.blit(BG, (0, 0))
        screen.blit(KNIFE, knife_position - knife_dimensions / 2)
        screen.blit(ENEMY, enemy_position - enemy_dimensions / 2)
        pygame.draw.circle(screen, (0, 0, 255), knife_point, 10)
        for spot in enemy_weak_spots:
            pygame.draw.circle(screen, (255, 0, 0), spot, 10)
        pygame.display.flip()

    def stab(knife_position, knife_point):
        stab_cooldown = True
        startpos = knife_position.y
        x = 1
        while knife_position.y <= startpos + stab_depth:
            knife_position.y += 40/x
            x += 1
            render()
        knife_point.y += stab_depth
        pygame.time.delay(50)

    def unstab(knife_position, knife_point):
        knife_point.y -= stab_depth
        startpos = knife_position.y
        x = 1
        while knife_position.y >= startpos - stab_depth:
            knife_position.y -= 40/x
            x += 1
            render()
        stab_cooldown = False

    # Game loop
    while running:
        render()
        pressed = pygame.key.get_pressed()
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
                    check_stab(knife_point)
                    unstab(knife_position, knife_point)
                    render()
                    pass
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()

        if pressed[pygame.K_d] and not pressed[pygame.K_a]:
            if velocity < max_velocity:
                velocity += strength
            if velocity < 0:
                velocity *= 0.8
        elif pressed[pygame.K_a] and not pressed[pygame.K_d]:
            if velocity > -max_velocity:
                velocity -= strength
            if velocity > 0:
                velocity *= 0.8
        else:
            velocity *= 0.8
            if abs(velocity) < 10:
                velocity = 0
        

        # Collisions
        if knife_position.x - knife_dimensions.x / 2 < 0:
            knife_position.x = knife_dimensions.x / 2
            velocity = -velocity
        if knife_position.x + knife_dimensions.x / 2 > screenWidth:
            knife_position.x = screenWidth - knife_dimensions.x / 2
            velocity = -velocity
        leftSideHit = get_bounds(KNIFE, knife_position)[1].x >= get_bounds(ENEMY, enemy_position)[0].x and get_bounds(KNIFE, knife_position)[1].x <= enemy_position.x
        rightSideHit = get_bounds(KNIFE, knife_position)[0].x <= get_bounds(ENEMY, enemy_position)[1].x and get_bounds(KNIFE, knife_position)[0].x >= enemy_position.x

        if (leftSideHit or rightSideHit) and abs(velocity) <= max_velocity * 3 / 4:
            if leftSideHit:
                velocity -= repulsion_force
            elif rightSideHit:
                velocity += repulsion_force

        # Update positions     
        knife_position.x += velocity * delta_time
        knife_point = knife_position + Vector2(0, KNIFE.get_height()/ 2)

        # --------------- Maintenance stuff ------------------
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
