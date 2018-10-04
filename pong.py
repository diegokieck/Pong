import pygame, sys
from pygame.locals import *

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 200

WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

#Colors
BLACK= (0,0,0) 
WHITE = (255, 255, 255)

def drawArena():
	#create surface
	DISPLAYSURF.fill((0,0,0))
	#draw borders
	pygame.draw.rect(DISPLAYSURF,WHITE, ((0,0), (WINDOWWIDTH, WINDOWHEIGHT)), LINETHICKNESS*2)
	#draw center of coart
	pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0), ((WINDOWWIDTH/2), WINDOWHEIGHT), (LINETHICKNESS/4))



def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)

#draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)


def main():
	pygame.init()
	global DISPLAYSURF
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 

	pygame.display.set_caption('Pong')

	#Initial positions of objects:
	ballX =WINDOWWIDTH/2 - LINETHICKNESS/2
	ballY =WINDOWHEIGHT/2 - LINETHICKNESS/2

	playerOnePosition=(WINDOWHEIGHT - PADDLESIZE)/2
	playerTwoPosition=(WINDOWHEIGHT - PADDLESIZE)/2

	#Creates Rectangles for ball and paddles 
	paddle1 = pygame.Rect(PADDLEOFFSET, playerOnePosition, LINETHICKNESS,  PADDLESIZE)
	paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerOnePosition, LINETHICKNESS,  PADDLESIZE)
	ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

	#draw objects
	drawArena()
	drawPaddle(paddle1)
	drawPaddle(paddle2)
	drawBall(ball)


	while(True): #main game loop
		for event in pygame.event.get():
			if event.type ==QUIT:
				pygame.quit()
				sys.exit()
			print(event)

		#drawArena()
		#drawPaddle(paddle1)
		#drawPaddle(paddle2)
		#drawBall(ball)
		pygame.display.update()
		FPSCLOCK.tick(FPS)




if __name__=='__main__':
    main()