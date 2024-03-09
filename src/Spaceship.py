import pygame
# from src.Colors import colors
# from random import randrange
from src.Bullet import Bullet

"""Abstract class spaceships (including enemy, boss and hero)"""
class Spaceship:
    def __init__(self):
        self.image = pygame.image.load("images/spaceship_red.png").convert_alpha()
        self.spaceShipObject = pygame.transform.rotate(pygame.transform.scale(self.image, (50, 50)), 180)
        self.X = 0
        self.Y = 420

    def fire(self) -> Bullet:
        # color_code = self.__color_list[randrange(0, len(self.__color_list))]
        bullet = Bullet(self.X, self.Y)
        # bullet = {"color": color_code, "shape": pygame.Rect(self.X + 20, self.Y - 25, 10, 10)}
        return bullet

    def detect_collision(self, bullet:Bullet, wall):
        for brick in wall.queue:
            if bullet["shape"].colliderect(pygame.Rect(brick.x, brick.y, brick.width, brick.height)) \
                    and bullet["color"] == brick.color:
                return brick
