import pygame
from src.colors import colors
from pygame import Surface
class Bullet:
	def __init__(self, spaceShipX:int, spaceShipY:int):
		self.x = 0
		self.y = 0
		self.color = list(colors.values())[0]# red
		self.shape = pygame.Rect(spaceShipX + 20, spaceShipY - 23, 10, 10)

	def draw(self, screen: Surface):
		# print("Yes")
		# self.shape = pygame.Rect(spaceShipX + 20, spaceShipY - 23, 10, 10)
		pygame.draw.rect(screen, self.color, self.shape)