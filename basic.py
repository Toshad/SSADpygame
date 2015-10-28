import pygame
pygame.init()
Display= pygame.display.set_mode((800,650))

class object():
	x=0
	y=0
	img=pygame.image.load('horizontal-line.png')
	width=0
	height=0
	def draw(self):
		Display.blit(self.img,(self.x,self.y));
	def getposition(self):
		return {'x':self.x,'y':self.y,'width':self.width,'height':self.height}

class movable(object):
	dx=0
	dy=0
	def updat(self):
		self.x+=self.dx
		self.y+=self.dy
