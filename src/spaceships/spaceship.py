import pygame
from pygame import Surface
from src.bullet import Bullet

"""Abstract class spaceships (including enemy, boss and hero)"""
class Spaceship:
    def __init__(self, name:str, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
        self.name:str = name
        # if self.name == "hero":
        #     self.spaceShipSurface: Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_yellow.png").convert_alpha(), (50, 50)), 180)
        
    def draw(self, screen:Surface, spaceship_surface) -> None:
        screen.blit(spaceship_surface, (self.x, self.y))
        
    def move(self,keys) -> None:
        # if keys[pygame.K_RIGHT] and self.x < 400 - 50: # 400 is the SCREEN_WIDTH and 50 is the width of the spaceship
        #    self.x += 10
        # if keys[pygame.K_LEFT] and self.x > 0:
        #     self.x -= 10
        pass