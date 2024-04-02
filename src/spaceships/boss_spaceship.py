import pygame
from .spaceship import Spaceship
from pygame import Surface
from .spaceship_dimension import dimension
from src.bullet import Bullet
from random import randint

class BossSpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 0, name:str = "boss") -> None:
		super().__init__(x,y,name)
		self.width:float = dimension["boss"][0]
		self.height:float = dimension["boss"][1]
		self.health_point:float = 200

		
	def draw(self, screen:Surface)->None:
		super().draw(screen)
		# pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.x, self.y, self.width, self.height),2)

	def fire(self) -> Bullet:
		x = randint(self.x, self.x + self.width)
		# y = randint(self.y, self.height)
		y = self.y + self.height
		bullet = Bullet(x, y, "boss")
		return bullet

	def draw_health_bar(self, screen:Surface) -> None:
		pygame.draw.rect(screen, (255,0,0), pygame.Rect(125, 45, 200, 20), 2) # no color-filled inside
		pygame.draw.rect(screen, (255,0,0), pygame.Rect(125, 45, self.health_point, 20)) # color-filled inside
		# pass
	
	def detect_collision(self, bullet:Bullet, hero_spaceship) -> bool:
		if bullet.shape.colliderect(pygame.Rect(hero_spaceship.x, hero_spaceship.y, hero_spaceship.width, hero_spaceship.height)):
			return True
		else: 
			return False