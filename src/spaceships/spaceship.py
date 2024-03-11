import pygame
from pygame import Surface
from src.bullet import Bullet

"""Abstract class spaceships (including enemy, boss and hero)"""
class Spaceship:
    def __init__(self, name:str, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
        self.name:str = name
        self._dimension: dict = {
            "hero":(50,50),
            "enemy":(25,25),
            "boss": (80,80)
        }
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
        # if keys[pygame.K_RIGHT] and self.x < 400 - 50: # 400 is the SCREEN_WIDTH and 50 is the width of the spaceship
        #    self.x += 10
        # if keys[pygame.K_LEFT] and self.x > 0:
        #     self.x -= 10
        pass