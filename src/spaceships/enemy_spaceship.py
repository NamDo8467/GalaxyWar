from .spaceship import Spaceship
import pygame
from pygame import Surface
class EnemySpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 0, name:str = "enemy") -> None:
		super().__init__(x,y,name)
		
		
	def draw(self, screen)->None:
		super().draw(screen)

	def move_x_and_y(self, key = None)->None:
		if self.x > 170: #170 is the boundary. If the enemy spaceship x-coordinate is bigger then the x-coordinate will be decreasing
			self.x -= 2.5
		else:
			self.x += 2.5
		self.y += 1.5
	def move_x(self) -> None:
		self.x += 2.5
	def move_y(self) -> None:
		self.y += 1.5