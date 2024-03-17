import pygame
from src.bullet import Bullet
import math 
from src.spaceships.hero_spaceship import HeroSpaceship
from src.spaceships.enemy_spaceship import EnemySpaceship
from src.spaceships.spaceship_dimension import dimension
pygame.init()
clock = pygame.time.Clock()

TITLE = "GAME"
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 500
SPACESHIP_X = 0
SPACESHIP_Y = 420
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
background = pygame.image.load("images\\spaceBackground.jpg").convert()


running = True

game_level = 1
is_created_game_opening = False

total_rows = 2

hero_spaceship =  HeroSpaceship()
enemy_spaceship_1 = EnemySpaceship(0, 0)
enemy_spaceship_2 = EnemySpaceship(SCREEN_WIDTH/2-(dimension["enemy"][0]/2), 0)
enemy_spaceship_3 = EnemySpaceship(SCREEN_WIDTH-dimension["enemy"][0],0)

# enemy_fleet: deque[EnemySpaceship] = deque()
enemy_fleet: list[EnemySpaceship] = []

enemy_position: dict = {
    "x": 30,
    "y": 80
}
enemy_position_offset = 0

bullets: list[Bullet] = []

brick_to_remove = None

scroll = 0

tiles = math.ceil(SCREEN_HEIGHT / background.get_height()) + 1

def create_an_enemy(x:float, y:float, row:int) -> EnemySpaceship:
    enemy = EnemySpaceship(x,y, "enemy", row)
    return enemy

def create_enemies_for_level(level: int) -> None:
    number_of_enemy:int = 0
    x_coordinate:float = SCREEN_WIDTH/6 + 25
    y_coordinate:float = 0
    distance_to_the_next_spaceship = 1
    global total_rows

    if level == 1: # 4 enemies
        number_of_enemy = 4
        for i in range(0, number_of_enemy):
            enemy_fleet.append(create_an_enemy(x_coordinate + (SCREEN_WIDTH/6)*i, 130, total_rows))
            # distance_to_the_next_spaceship += 1
            # x_coordinate += (SCREEN_WIDTH/6)
    elif level == 2: # 7 enemies
        distance_to_the_next_spaceship = 1
        number_of_enemy = 8
        for i in range(0, number_of_enemy):
            if i > (3+4*(total_rows - 2)):
                # x_coordinate = SCREEN_WIDTH/6 + 25
                # x_coordinate += (SCREEN_WIDTH/6) * distance_to_the_next_spaceship
                enemy_fleet.append(create_an_enemy(x_coordinate + (SCREEN_WIDTH/6)*i-(4*(total_rows-1)*(SCREEN_WIDTH/6)),90, total_rows))
            else:
                pass
                enemy_fleet.append(create_an_enemy(x_coordinate + (SCREEN_WIDTH/6)*i,130, total_rows))
                # x_coordinate += (SCREEN_WIDTH/6)
            # if distance_to_the_next_spaceship + 1 > 3:
            #     distance_to_the_next_spaceship = 0
            # else:
            #     distance_to_the_next_spaceship += 1
            
def create_enemies_for_level_recursively(number_of_rows: int, y_coordinate:int = 130) -> None: # number_of_rows is equal to game level
    if number_of_rows < 1:
        return
    number_of_enemy: int = 4
    x_coordinate:float = SCREEN_WIDTH/6 + 25
    create_enemies_for_level_recursively(number_of_rows - 1 , y_coordinate - (dimension["enemy"][0]+20))
    for i in range(0, number_of_enemy):
        enemy_fleet.append(create_an_enemy(x_coordinate + (SCREEN_WIDTH/6)*i, y_coordinate, number_of_rows))

is_enemy_in_position: bool = False


def draw_window_and_object():
    screen.blit(background, (0, 0))

    screen.blit(hero_spaceship.spaceShipObject, (hero_spaceship.X, hero_spaceship.Y))

    # for brick in wall.queue:
    #     pygame.draw.rect(screen, brick.color, pygame.Rect(brick.x, brick.y, brick.width, brick.height), 0, 3)

    # wall.addLayerOfBricks()


def handle_bullets_collision() -> None:
    # global wall
    # global brick_to_remove

    if len(bullets) == 0:
        return
    for b in bullets:
        b.draw(screen)        # pygame.draw.rect(screen, b.color, b.shape)
        # pygame.draw.rect(screen, b["color"], b["shape"])
        # brick_to_remove = None
        enemy_to_remove = hero_spaceship.detect_collision(b, enemy_fleet)
        if enemy_to_remove:
            bullets.remove(b)
            enemy_fleet.remove(enemy_to_remove)
        b.shape.y = b.shape.y - 3
        # print(len(bullets))
        if b.shape.y < 0:
            bullets.remove(b)
            # print(len(bullets))



# def handle_movement(keys:list)->None:
#     if keys[pygame.K_RIGHT] and spaceShip.X < SCREEN_WIDTH - 50:
#         spaceShip.X += 10
#     if keys[pygame.K_LEFT] and spaceShip.X > 0:
#         spaceShip.X -= 10

while running:
    clock.tick(45)
    for i in range(0,tiles):
        screen.blit(background, (0, background.get_height() * (-i) + scroll))
    scroll += 2
    if abs(scroll) > background.get_height(): 
        scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_COMMA:
                print("haha")
                bullet = hero_spaceship.fire()
                # bullet = 0
                bullets.append(bullet)

    keys_pressed = pygame.key.get_pressed()
    hero_spaceship.draw(screen)
    hero_spaceship.move(keys_pressed)
    # enemy_spaceship_3.draw(screen)
    if is_created_game_opening == False:
        create_enemies_for_level_recursively(game_level)
        is_created_game_opening = True
    for enemy_spaceship in enemy_fleet:
        # print(enemy_fleet[0].x, enemy_fleet[0].y)
        enemy_spaceship.draw(screen)
    # if is_enemy_in_position == False:
    #     for enemy in enemy_fleet:
    #         enemy.move_x_by(1.5)
    #         enemy.move_x_by(-2.5)
    #             pass
    # else:
    #     for enemy_spaceship in enemy_fleet:
    #         enemy_spaceship.draw(screen)
    
    # print(len(enemy_fleet))
    handle_bullets_collision()        
    pygame.display.update()


pygame.quit()
