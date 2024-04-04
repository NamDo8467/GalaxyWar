import pygame
from src.colors import colors
from pygame import Surface
from .spaceships.spaceship_dimension import dimension
class Bullet:
	def __init__(self, spaceShipX:float, spaceShipY:float, name:str):
		self.x:float = spaceShipX + ( (dimension["hero"][0]/2-5) if name == "hero" else (dimension["enemy"][0]/2))
		self.y:float = spaceShipY - ( (dimension["hero"][0]/2-10) if name == "hero" else (dimension["enemy"][0]/2-15))
		self.width:float = 5
		self.height:float = 30
		self.color = colors["green"] if name == "hero" else colors["red"]
		# self.shape = pygame.Rect(self.x, self.y, 5, 15)
		if name == "hero":
			self.shape:Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/laserGreen13.png").convert_alpha(), (self.width,self.height)), 0)
		else:
			self.shape:Surface = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/laserRed13.png").convert_alpha(), (self.width,self.height)), 0)

	def draw(self, screen: Surface)->None:
		screen.blit(self.shape, (self.x, self.y))
		# pygame.draw.rect(screen, self.color, self.shape)