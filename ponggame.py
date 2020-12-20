import pygame
import random
import time
pygame.init()

win=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong Game")

white=(255, 255, 255)
red  =(255, 0, 0)
green=(0, 255, 0)
blue =(0, 0, 255)

class paddle:
    def __init__(self, win, width, height, posX, posY):
        self.height=height
        self.win=win
        self.width=width
        self.posX=posX
        self.posY=posY
    def draw(self):
        pygame.draw.rect(win, blue, (self.posX, self.posY, self.width, self.height), 0, 5)
    def moveLeft(self):
        if(self.posX-20>0):   # As if pos -20 <0, paddle would disappear hence made pos=0 if pos-20<0
            self.posX-=20
        else:
            self.posX=0
        return  self.posX+35  # returning position of paddle +width/2 so that ball will be at middle of paddle if not playing
    def moveRight(self):
        if(self.posX+70<500):  #If pos+70 greater than 500 means next position would be greater then 500 which is right boundary and hence assign position to 420
            self.posX+=20
        else:
            self.posX=430
        return self.posX+35  # returning position of paddle +width/2 so that ball will be at middle of paddle if not playing

class ball:
    def __init__(self, win, radius, posX, posY):
        self.win=win
        self.radius=radius
        self.posX=posX
        self.dx=0
        self.dy=0
        self.posY=posY
    def draw(self):
        pygame.draw.circle(win, white, (self.posX, self.posY), 10)
    def ballStartMoves(self):
        self.dx=random.uniform(0.1, 0.3)
        self.dy=random.uniform(0.1, 0.2)
    def ballMoving(self):
        self.posX-=self.dx
        self.posY-=self.dy
    def topCollisionChangeBallMotion(self):
        self.dy=-self.dy
    def leftrightwallCollisionChangeBallMotion(self):
        self.dx=-self.dx
    def ballpaddlecollision(self):
        self.dx+=0.0001
        self.dy=-self.dy-0.0001

class collisionManager:
    def topCollision(self, ball):
        if(ball.posY<0):
            return True
    def leftrightwallCollision(self, ball):
        if(ball.posX<0 or ball.posX+ball.radius>500):
            return True
    def downCollision(self, ball):
        if(ball.posY>500):
            return True
    def ballandpaddleCollision(self, b1, p1):
        if (b1.posY >= 470 and b1.posY <= 480):
            if (b1.posX >= p1.posX+1 and b1.posX < p1.posX + p1.width-1): #Whenver The ball hits on top of paddle, it return true
                return True
            if (b1.posX >= p1.posX+p1.width-1 and b1.posX <= p1.posX + p1.width): # whenever the ball hits on edge of the paddle if we increment and change the ball position in range (0.1, 0.3) not sufficientto change position as height is 10 and so we wxpilicitly written the code
                b1.dy = -b1.dy
                b1.posY-=b1.dy+10
            if (b1.posX >= p1.posX and b1.posX <= p1.posX + 1):
                b1.dy = -b1.dy
                b1.posY -= b1.dy + 10
        return False

run=True
playing=False
left=False
right=False

def initialSetUp():
    win.fill((0, 0, 0))
    p1 = paddle(win, 70, 10, (500 / 2 - 70 / 2), (480))  # x-coordinate:(width of screen/2 - width of paddle/2 , y-coordinate: height of screen-20
    b1 = ball(win, 10, (500 / 2 ), (480 - 10))  # x-coordinate:width of screen/2, y-coordinate:y-coordinate of paddle-height of paddle
    c1 = collisionManager()
    p1.draw()
    b1.draw()
    return p1, b1, c1

p1, b1, c1=initialSetUp()

while run:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            run=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                win.fill((0, 0, 0))
                mouseposition=p1.moveLeft()
                p1.draw()
                if(playing==False):
                    b1.posX=mouseposition
                    b1.draw()
            if(event.key==pygame.K_RIGHT):
                win.fill((0, 0, 0))
                mouseposition=p1.moveRight()
                p1.draw()
                if (playing == False):
                    b1.posX=mouseposition
                    b1.draw()
            if(event.key==pygame.K_UP and playing==False):
                playing=True
                b1.ballStartMoves()
    if(playing):
        win.fill((0, 0, 0))
        b1.ballMoving()
        b1.draw()
        p1.draw()
        if(c1.topCollision(b1)):
            b1.topCollisionChangeBallMotion()
        if(c1.leftrightwallCollision(b1)):
            b1.leftrightwallCollisionChangeBallMotion()
        if(c1.downCollision(b1)):
            playing=False
            initialSetUp()
            b1.posX, b1.posY, p1.posX, p1.posY=(500 / 2), (480 - 10), (500 / 2 - 70 / 2), (480) #After losinng game, initial setup start
        if(c1.ballandpaddleCollision(b1, p1)):
            b1.ballpaddlecollision()

    pygame.display.update()
pygame.quit()
