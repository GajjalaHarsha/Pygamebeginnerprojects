import pygame
pygame.init()
win=pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Traffic")
Font=pygame.font.SysFont('timesnewroman',  30)
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 0)
orange=(255, 100, 0)
black=(0, 0, 0)
red=(255, 0, 0)
text=Font.render("G0", True, orange)
text1=Font.render("STOP", True, orange)
done=True
click=0
click1=0
def drawrect(win, x, y, w, h, outline, color, text):
    pygame.draw.rect(win, outline, (x-2, y-2, w+4, h+4), 2)
    pygame.draw.rect(win, color, (x, y, w, h))
    win.blit(text, (x + (w - text.get_width()) / 2, y + (h - text.get_height()) / 2))
    return x, y, w, h
while done:
    win.fill((255, 255, 255))
    x, y, w, h=605, 235, 90, 30
    x1, y1, w1, h1= 705, 235, 90, 30
    drawrect(win, 605, 235, 90, 30, black, green, text)
    drawrect(win, 705, 235, 90, 30, black, red, text1)
    image = pygame.image.load("bg1.png")
    win.blit(image, (0, 0))
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            done=False
            break
        if(event.type==pygame.MOUSEBUTTONDOWN):
            pos=pygame.mouse.get_pos()
            if(click==0 and pos[0]>x and pos[0]<x+w and pos[1]>y and pos[1]< y+h):
                click1=0
                click+=1
                print(click)
                start_time=pygame.time.get_ticks()
                while(pygame.time.get_ticks()-start_time < 500):
                    image = pygame.image.load("bg4.png")
                    win.blit(image, (0, 0))
                    pygame.display.update()
            elif(click1==0 and pos[0]>x1 and pos[0]<x1+w1 and pos[1]>y1 and pos[1]< y1+h1):
                click=0
                click1+=1
                print(click1)
                start_time = pygame.time.get_ticks()
                while (pygame.time.get_ticks() - start_time < 500):
                    image = pygame.image.load("bg4.png")
                    win.blit(image, (0, 0))
                    pygame.display.update()
        if(click>=1):
            image = pygame.image.load("bg3.png")
            win.blit(image, (0, 0))
        if (click1 >= 1):
            image = pygame.image.load("bg2.png")
            win.blit(image, (0, 0))
        pygame.display.update()
pygame.quit()