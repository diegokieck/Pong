import pygame, sys
from pygame.locals import *

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 200

WINDOWWIDTH = 400
WINDOWHEIGHT = 300

def main():
	pygame.init()
	global DISPLAYSURF
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 

	pygame.display.set_caption('Pong')

	while(True): #main game loop
		for event in pygame.event.get():
			if event.type ==QUIT:
				pygame.quit()
				sys.exit()

			pygame.display.update()
			FPSCLOCK.tick(FPS)




if __name__=='__main__':
    main()