from src.spaceships.spaceship import Spaceship
# import pygame
from pygame import Surface
class HeroSpaceShip(Spaceship):
	def __init__(self, name="hero", x = 0, y = 420)->None:
		super().__init__(name, x, y)
		# self.image:Surface = pygame.image.load("images/spaceship_yellow.png").convert_alpha()
		# self.spaceShipSurface: Surface = pygame.transform.rotate(pygame.transform.scale(self.image, (50, 50)), 180)

	def draw(self, screen:Surface) -> None:
		super().draw(screen)

	def move(self, keys:list) -> None:
		super().move(keys)
