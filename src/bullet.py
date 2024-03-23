import pygame
from src.colors import colors
from pygame import Surface
from .spaceships.spaceship_dimension import dimension
class Bullet:
	def __init__(self, spaceShipX:float, spaceShipY:float, name:str):
		self.x:float = spaceShipX + ( (dimension["hero"][0]/2-5) if name == "hero" else (dimension["enemy"][0]/2))
		self.y:float = spaceShipY - ( (dimension["hero"][0]/2-10) if name == "hero" else (dimension["enemy"][0]/2-15))
		self.color = colors["green"] if name == "hero" else colors["red"]
		self.shape = pygame.Rect(self.x, self.y, 5, 15)
	def draw(self, screen: Surface)->None:
		pygame.draw.rect(screen, self.color, self.shape)