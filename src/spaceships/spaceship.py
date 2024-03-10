import pygame
from pygame import Surface
from src.bullet import Bullet

"""Abstract class spaceships (including enemy, boss and hero)"""
class Spaceship:
    def __init__(self, name:str, x:int, y:int) -> None:
        self.X:int = x
        self.Y:int = y
        self.name:str = name
        # if self.name == "hero":
        #     self.spaceShipSurface: Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_yellow.png").convert_alpha(), (50, 50)), 180)
        
    def draw(self, screen:Surface, spaceship_surface) -> None:
        screen.blit(spaceship_surface, (self.X, self.Y))
        
    def move(self,keys) -> None:
        if keys[pygame.K_RIGHT] and self.X < 400 - 50: # 400 is the SCREEN_WIDTH and 50 is the width of the spaceship
           self.X += 10
        if keys[pygame.K_LEFT] and self.X > 0:
            self.X -= 10