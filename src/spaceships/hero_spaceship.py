from .spaceship import Spaceship
from pygame import Surface
import pygame
class HeroSpaceship(Spaceship):
	def __init__(self, x:float = 0, y:float = 420, name:str ="hero")->None:
		super().__init__(x,y,name)
		# self.spaceship_surface: Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_yellow.png").convert_alpha(), (50, 50)), 180)


	def draw(self, screen:Surface) -> None:
		super().draw(screen)

	def move(self, keys) -> None:
		if keys[pygame.K_RIGHT] and self.x < 400 - 50: # 400 is the SCREEN_WIDTH and 50 is the width of the spaceship
			self.x += 10
		if keys[pygame.K_LEFT] and self.x > 0:
			self.x -= 10
