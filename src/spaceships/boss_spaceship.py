import pygame
from .spaceship import Spaceship
from .spaceship_dimension import dimension
from src.bullet import Bullet

class BossSpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 0, name:str = "boss") -> None:
		super().__init__(x,y,name)
		# self.row = row
		self.width:float = dimension["boss"][0]
		self.height:float = dimension["boss"][1]

		
	def draw(self, screen)->None:
		super().draw(screen)

	def fire(self) -> Bullet:
		return super().fire()
	
	def detect_collision(self, bullet:Bullet, hero_spaceship) -> bool:
		if bullet.shape.colliderect(pygame.Rect(hero_spaceship.x, hero_spaceship.y, hero_spaceship.width, hero_spaceship.height)):
			return True
		else: 
			return False