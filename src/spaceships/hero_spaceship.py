from .spaceship import Spaceship
from pygame import Surface
from src.bullet import Bullet
from .enemy_spaceship import EnemySpaceship
from .boss_spaceship import BossSpaceship
from .spaceship_dimension import dimension
from typing import Union
import pygame
class HeroSpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 420, name:str ="hero")->None:
		super().__init__(x,y,name)
		self.width:float = dimension["hero"][0]
		self.height:float = dimension["hero"][1]

	def draw(self, screen:Surface) -> None:
		super().draw(screen)

	def move(self, keys) -> None:
		if keys[pygame.K_RIGHT] and self.x < 450 - dimension["hero"][0]: # 450 is the SCREEN_WIDTH
			self.x += 10
		if keys[pygame.K_LEFT] and self.x > 0:
			self.x -= 10

	def fire(self) -> Bullet:
		return super().fire()
	
	def detect_collision(self, bullet:Bullet, enemy_fleet: list) -> Union[EnemySpaceship, BossSpaceship, None]: # or return a BossSpaceship
		for enemy in enemy_fleet:
			if bullet.shape.colliderect(pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)):
				return enemy
		return None