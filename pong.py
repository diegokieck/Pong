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

def moveBall(ball, ballDirX, ballDirY):
	ball.x+=ballDirX
	ball.y+=ballDirY
	return ball

def ballEdgeDetector(ball, ballDirX,ballDirY):
	if ball.top == LINETHICKNESS or ball.bottom == WINDOWHEIGHT - LINETHICKNESS:
		ballDirY = ballDirY*-1
	if ball.left ==LINETHICKNESS or ball.right ==WINDOWWIDTH -LINETHICKNESS:
		ballDirX = ballDirX*-1
	return ballDirX, ballDirY

def movePaddle(paddle, event):
	if(event>0):
		paddle.y+=1
	if(event<0):
		paddle.y-=1
	return paddle
def computerPaddle(ball, ballDirX, paddle):
	#after hiting the ball the paddle will move to the center of the screen
	if(ballDirX==-1):
		if(paddle.centery>WINDOWHEIGHT/2):
			paddle.y-=1
		if(paddle.centery<WINDOWHEIGHT/2):	
			paddle.y+=1
	if(ballDirX==1):
		if(paddle.centery>ball.centery):
			paddle.y-=1
		if(paddle.centery<ball.centery):	
			paddle.y+=1

	return paddle
def paddleDetection(ball, paddle1, paddle2):
	if(ball.x==LINETHICKNESS/2+PADDLEOFFSET and paddle1.top<ball.y<paddle1.bottom):
		return int(-1)
	elif(ball.x==WINDOWWIDTH- (LINETHICKNESS*1.5 +PADDLEOFFSET) and paddle2.top<ball.y<paddle2.bottom):
		return int(-1)
	else:
		return 1 
def scoring(ball):
	if
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

	#initial ballDir
	ballDirX=1
	ballDirY=1

	pygame.mouse.set_visible(0)
	while(True): #main game loop
		for event in pygame.event.get():
			if event.type ==QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type ==MOUSEMOTION:
				paddle1.y = event.pos[1]

		drawArena()
		drawPaddle(paddle1)
		drawPaddle(paddle2)
		ballDirX = ballDirX*paddleDetection(ball, paddle1, paddle2)
		ballDirX, ballDirY = ballEdgeDetector(ball, ballDirX, ballDirY)
		ball = moveBall(ball, ballDirX, ballDirY)
		paddle2 = computerPaddle(ball, ballDirX, paddle2)
		drawBall(ball)
		pygame.display.update()
		FPSCLOCK.tick(FPS)




if __name__=='__main__':
    main()