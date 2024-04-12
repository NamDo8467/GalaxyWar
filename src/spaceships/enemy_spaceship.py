import pygame
from .spaceship import Spaceship
from pygame import Surface
from .spaceship_dimension import dimension
from src.bullet import Bullet

class EnemySpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 0, name:str = "enemy") -> None:
		super().__init__(x,y,name)
		self.width:float = dimension["enemy"][0]
		self.height:float = dimension["enemy"][1]

		
	def draw(self, screen)->None:
		super().draw(screen)

	def fire(self) -> Bullet:
		return super().fire()
	
	def detect_collision(self, bullet:Bullet, hero_spaceship) -> bool:
		if pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height).colliderect(pygame.Rect(hero_spaceship.x, hero_spaceship.y, hero_spaceship.width, hero_spaceship.height)):
			return True
		else: 
			return False

	def move_x_and_y(self, distance:float = 2.2)->None:
		if self.x > 225: #225 is the boundary (middle point of the screen width). If the enemy spaceship x-coordinate is bigger then the x-coordinate will be decreasing
			self.x -= distance
		else:
			self.x += distance
		self.y += 2.2

	def move_x_by(self, distance:float) -> None:
		self.x += distance
	def move_y_by(self, distance:float) -> None:
		self.y += distance