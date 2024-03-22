import pygame
from pygame import Surface
from src.bullet import Bullet
from .spaceship_dimension import dimension

"""Abstract class spaceships (including enemy, boss and hero)"""
class Spaceship:
    def __init__(self, x:float, y:float, name:str) -> None:
        self.x:float = x
        self.y:float = y
        self.name:str = name
        self._dimension: dict = dimension
        self.spaceship_surface:Surface
        if self.name == "hero":
            self.spaceship_surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_yellow.png").convert_alpha(), self._dimension["hero"]), 180)
        elif self.name == "enemy":
            self.spaceship_surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_red.png").convert_alpha(), self._dimension["enemy"]), 0)
        elif self.name == "boss":
            self.spaceship_surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_red.png").convert_alpha(), self._dimension["boss"]), 0)
        
    def draw(self, screen:Surface) -> None:
        screen.blit(self.spaceship_surface, (self.x, self.y))
        
    def move(self, key) -> None:
        pass
    def fire(self) -> Bullet:
        bullet = Bullet(self.x, self.y, self.name)
        return bullet