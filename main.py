import pygame
from src.bullet import Bullet
import math 
from src.spaceships.hero_spaceship import HeroSpaceship
from src.spaceships.enemy_spaceship import EnemySpaceship
from src.spaceships.spaceship_dimension import dimension
from src.colors import colors
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

score = 0
font = pygame.font.Font('freesansbold.ttf', 18)
scoreFont = font.render(f'Score: {score}', True, colors["green"])

scoreRect = scoreFont.get_rect()
scoreRect.x = SCREEN_WIDTH - scoreRect.width - 25
scoreRect.y = 25

def create_an_enemy(x:float, y:float, row:int) -> EnemySpaceship:
    enemy = EnemySpaceship(x,y, "enemy", row)
    return enemy
            
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


def handle_bullets_collision() -> None:
    global score
    global scoreFont
    global font

    if len(bullets) == 0:
        return
    for b in bullets:
        b.draw(screen)
        enemy_to_remove = hero_spaceship.detect_collision(b, enemy_fleet)
        if enemy_to_remove:
            bullets.remove(b)
            enemy_fleet.remove(enemy_to_remove)
            score += 10
            scoreFont = font.render(f'Score: {score}', True, colors["green"])
        b.shape.y = b.shape.y - 3
        # print(len(bullets))
        if b.shape.y < 0:
            bullets.remove(b)
            
def handle_level_up()->None:
    global game_level
    global is_created_game_opening
    if len(enemy_fleet) == 0:
        game_level += 1
        is_created_game_opening = False

while running:
    clock.tick(45)
    for i in range(0,tiles):
        screen.blit(background, (0, background.get_height() * (-i) + scroll))
    scroll += 2
    if abs(scroll) > background.get_height(): 
        scroll = 0
    screen.blit(scoreFont, scoreRect)
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
    if is_created_game_opening == False:
        create_enemies_for_level_recursively(game_level)
        is_created_game_opening = True
    for enemy_spaceship in enemy_fleet:
        enemy_spaceship.draw(screen)
    handle_bullets_collision()        
    handle_level_up()    
    # print(len(enemy_fleet))
    pygame.display.update()


pygame.quit()
