import pygame
from src.bullet import Bullet
import math 
from src.spaceships.hero_spaceship import HeroSpaceship
from src.spaceships.enemy_spaceship import EnemySpaceship
from src.spaceships.boss_spaceship import BossSpaceship
from src.spaceships.spaceship_dimension import dimension
from src.colors import colors
import random

from tkinter import *
from tkinter import messagebox


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

boss_health_point = 200

# boss: BossSpaceship = BossSpaceship(0,0, "boss")

running = True

game_level = 5

is_created_game_opening = False

hero_spaceship =  HeroSpaceship(SCREEN_WIDTH/2 - dimension["hero"][0]/2, 420, "hero")
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

enemy_bullets: list[Bullet] = []

brick_to_remove = None

scroll = 0

tiles = math.ceil(SCREEN_HEIGHT / background.get_height()) + 1

score = 0
font = pygame.font.Font('freesansbold.ttf', 18)
scoreFont = font.render(f'Score: {score}', True, colors["green"])

scoreRect = scoreFont.get_rect()
scoreRect.x = SCREEN_WIDTH - scoreRect.width - 25
scoreRect.y = 25

hit_the_left_of_screen = True
hit_the_right_of_screen = False
moving_space = 0.7

def create_an_enemy(x:float, y:float, row:int) -> EnemySpaceship:
    enemy = EnemySpaceship(x,y, "enemy", row)
    return enemy
            
def create_boss() -> BossSpaceship:
    x = SCREEN_WIDTH/2 - dimension["boss"][0]/2
    y = 90
    boss = BossSpaceship(x,y, "boss")
    return boss

def create_boss_hp_bar(health_point) -> None:
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(125, 45, 200, 20), 2) # no color-filled inside
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(125, 45, health_point, 20)) # color-filled inside
    # pass

def create_enemies_for_level_recursively(number_of_rows: int, y_coordinate:int = 130) -> None: # number_of_rows is equal to game level
    if number_of_rows == 5:
        boss = create_boss()
        enemy_fleet.append(boss)
        return
    if number_of_rows < 1:
        return
    number_of_enemy: int = 4
    x_coordinate:float = SCREEN_WIDTH/6 + 25
    create_enemies_for_level_recursively(number_of_rows - 1 , y_coordinate - (dimension["enemy"][0]+20))
    for i in range(0, number_of_enemy):
        enemy_fleet.append(create_an_enemy(x_coordinate + (SCREEN_WIDTH/6)*i, y_coordinate, number_of_rows))

is_enemy_in_position: bool = False


def handle_bullets_collision() -> None:
    global score
    global scoreFont
    global font
    global running 
    for b in enemy_bullets:
        b.draw(screen)
        hit_hero_spaceship = enemy_fleet[0].detect_collision(b, hero_spaceship) # any enemy can detect the collision
        if hit_hero_spaceship:
            enemy_bullets.remove(b)
            Tk().wm_withdraw() #to hide the main window
            messagebox.showinfo('Info','Game over')
            running = False
        else:   
            b.shape.y = b.shape.y + 3
            if b.shape.y > SCREEN_HEIGHT:
                enemy_bullets.remove(b)
    
    if len(bullets) == 0:
        return
    else:
        for b in bullets:
            b.draw(screen)
            enemy_to_remove = hero_spaceship.detect_collision(b, enemy_fleet)
            if enemy_to_remove:
                bullets.remove(b)
                if enemy_to_remove.name == "boss":
                    enemy_to_remove.health_point -= 2
                else:
                    enemy_fleet.remove(enemy_to_remove)
                score += 10
                scoreFont = font.render(f'Score: {score}', True, colors["green"])
            b.shape.y = b.shape.y - 3
            if b.shape.y < 0:
                bullets.remove(b)
    
            
def handle_level_up()->None:
    global game_level
    global is_created_game_opening
    if len(enemy_fleet) == 0:
        game_level += 1
        is_created_game_opening = False

random_enemy_index = 0
create_random = True
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
                # print("haha")
                bullet = hero_spaceship.fire()
                bullets.append(bullet)

    keys_pressed = pygame.key.get_pressed()
    hero_spaceship.draw(screen)
    hero_spaceship.move(keys_pressed)

    if is_created_game_opening == False:
        create_enemies_for_level_recursively(game_level)

        is_created_game_opening = True
        
    for enemy_spaceship in enemy_fleet:
        enemy_spaceship.y = 90
        enemy_spaceship.draw(screen)
        if enemy_spaceship.name != "boss":
            if len(enemy_bullets) == 0:
                random_enemy_index = random.randint(0, len(enemy_fleet) - 1)
                enemy_bullet = enemy_fleet[random_enemy_index].fire()
                enemy_bullets.append(enemy_bullet)
            if hit_the_left_of_screen:
                enemy_spaceship.move_x_by(moving_space) # move to the right
                if(enemy_fleet[len(enemy_fleet) - 1].x >= SCREEN_WIDTH - dimension["enemy"][0]):
                    hit_the_right_of_screen = True # that means that it should start moving to the left now
                    hit_the_left_of_screen = False
            else:
                enemy_spaceship.move_x_by(-moving_space) # move to the left
                if(enemy_fleet[0].x <= 0):
                    hit_the_left_of_screen = True # that means that it should start moving to the right now
                    hit_the_right_of_screen = False
        else:
            enemy_spaceship.draw_health_bar(screen)
            boss_bullet = enemy_spaceship.fire()
            if len(enemy_bullets) <= 6:
                enemy_bullets.append(boss_bullet)
             
    handle_bullets_collision()        
    handle_level_up()    
    pygame.display.update()

pygame.quit()
