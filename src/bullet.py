import pygame
from src.colors import colors
from pygame import Surface
from .spaceships.spaceship_dimension import dimension
class Bullet:
	def __init__(self, spaceShipX:float, spaceShipY:float):
		self.x:float = spaceShipX + (dimension["hero"][0]/2-5)
		self.y:float = spaceShipY - (dimension["hero"][0]/2-10)
		self.color = list(colors.values())[0]# red
		self.shape = pygame.Rect(self.x, self.y, 5, 15)
	def draw(self, screen: Surface)->None:
		# print("Yes")
		# self.shape = pygame.Rect(spaceShipX + 20, spaceShipY - 23, 10, 10)
		pygame.draw.rect(screen, self.color, self.shape)