from .spaceship import Spaceship
import pygame
from pygame import Surface
class EnemySpaceship(Spaceship):
	def __init__(self, name = "enemy", x = 0, y = 0) -> None:
		super().__init__(name, x, y)
		
		
	def draw(self, screen)->None:
		super().draw(screen)

	def move(self, key = None)->None:
		self.x += 2
		self.y += 2