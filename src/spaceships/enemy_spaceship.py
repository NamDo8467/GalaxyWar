from .spaceship import Spaceship
import pygame
from pygame import Surface
class EnemySpaceship(Spaceship):
	def __init__(self, name = "enemy", x = 200, y = 40) -> None:
		super().__init__(name, x, y)
		self.spaceship_surface: Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_red.png").convert_alpha(), (20, 20)), 0)
		
	def draw(self, screen)->None:
		super().draw(screen, self.spaceship_surface)