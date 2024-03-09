import pygame
from pygame import Surface
from src.Bullet import Bullet
from main import SCREEN_WIDTH

"""Abstract class spaceships (including enemy, boss and hero)"""
class Spaceship:
    def __init__(self, name:str, x:int, y:int) -> None:
        self.X:int = x
        self.Y:int = y
        self.name:str = name
        # self.image:Surface = pygame.image.load("images/spaceship_red.png").convert_alpha()
        if self.name == "hero":
            print("I run")
            self.spaceShipSurface: Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_yellow.png").convert_alpha(), (50, 50)), 180)
        
    def draw(self, screen:Surface) -> None:
        screen.blit(self.spaceShipSurface, (self.X, self.Y))
        
    def move(self,keys:list) -> None:
        if keys[pygame.K_RIGHT] and self.X < SCREEN_WIDTH - 50:
           self.X += 10
        if keys[pygame.K_LEFT] and self.X > 0:
            self.X -= 10
            

    # def fire(self) -> Bullet:
    #     # color_code = self.__color_list[randrange(0, len(self.__color_list))]
    #     bullet = Bullet(self.X, self.Y)
    #     # bullet = {"color": color_code, "shape": pygame.Rect(self.X + 20, self.Y - 25, 10, 10)}
    #     return bullet
    # def detect_collision(self, bullet:Bullet, wall):
    #     for brick in wall.queue:
    #         if bullet["shape"].colliderect(pygame.Rect(brick.x, brick.y, brick.width, brick.height)) \
    #                 and bullet["color"] == brick.color:
    #             return brick
