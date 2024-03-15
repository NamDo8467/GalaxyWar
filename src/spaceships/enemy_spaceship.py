from .spaceship import Spaceship
import pygame
from pygame import Surface
class EnemySpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 0, name:str = "enemy", row:int = 1) -> None:
		super().__init__(x,y,name)
		self.row = row
		
		
	def draw(self, screen)->None:
		super().draw(screen)

	def move_x_and_y(self, distance:float = 2.2)->None:
		if self.x > 225: #225 is the boundary (middle point of the screen width). If the enemy spaceship x-coordinate is bigger then the x-coordinate will be decreasing
			self.x -= distance
		else:
			self.x += distance
		self.y += 2.2
	def move_x(self) -> None:
		self.x += 2.5
	def move_y(self) -> None:
		self.y += 2.2

	def move_x_by(self, distance:float) -> None:
		if self.x > 225: #225 is the boundary (middle point of the screen width). If the enemy spaceship x-coordinate is bigger then the x-coordinate will be decreasing
			self.x -= distance
		else:
			self.x += distance
	def move_y_by(self, distance:float) -> None:
		self.y += distance