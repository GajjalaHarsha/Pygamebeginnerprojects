import pygame
pygame.init()
win=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Scrolling Text")
Font=pygame.font.SysFont('timesnewroman',  30)
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
done=False
text1=Font.render("P", True, orange, yellow)
text2=Font.render("R", False, orange, green)
text3=Font.render("A", False, orange, yellow)
text4=Font.render("D", False, orange, green)
text5=Font.render("E", False, orange, yellow)
text6=Font.render("E", False, orange, green)
text7=Font.render("P", False, orange, yellow)
i=0
c=1
while not done:
    if(i>=820):
        i=0
        c+=1
        pygame.time.wait(500)
    win.fill((255, 255, 255))
    if(c%6==0):
        win.blit(text1, (662-i, -162+i))
        win.blit(text2, (639-i, -139+i))
        win.blit(text3, (608-i, -108+i))
        win.blit(text4, (579-i, -79+i))
        win.blit(text5, (552-i, -52+i))
        win.blit(text6, (529-i, -29+i))
        win.blit(text7, (500 -i, 0 + i))
        i+=80
    if(c%6==5):
        win.blit(text1, (-162+i, -162+i))
        win.blit(text2, (-135+i, -135+i))
        win.blit(text3, (-110+i, -110+i))
        win.blit(text4, (-79+i, -79+i))
        win.blit(text5, (-52+i, -52+i))
        win.blit(text6, (-27+i, -27+i))
        win.blit(text7, (0 + i, 0 + i))
        i+=80
    if(c%6==4):
        win.blit(text1, (480, -180 + i))
        win.blit(text2, (480, -150 + i))
        win.blit(text3, (480, -120 + i))
        win.blit(text4, (480, -90+ i))
        win.blit(text5, (480, -60+i))
        win.blit(text6, (480, -30+i))
        win.blit(text7, (480, 0 + i))
        i +=80
    if(c%6==3):
        win.blit(text1, (0, -180+i))
        win.blit(text2, (0, -150+i))
        win.blit(text3, (0, -120+i))
        win.blit(text4, (0, -90+i))
        win.blit(text5, (0, -60 + i))
        win.blit(text6, (0, -30 + i))
        win.blit(text7, (0, 0 + i))
        i+=80
    if(c%6==1):
        win.blit(text1, (-124 + i, 0))
        win.blit(text2, (-102 + i, 0))
        win.blit(text3, (-82 + i, 0))
        win.blit(text4, (-58+ i, 0))
        win.blit(text5, (-40+i, 0))
        win.blit(text6, (-19+i, 0))
        win.blit(text7, (0 + i, 0))
        i +=80
    if(c%6==2):
        win.blit(text1, (-124 + i, 470))
        win.blit(text2, (-102 + i, 470))
        win.blit(text3, (-82 + i, 470))
        win.blit(text4, (-58+ i, 470))
        win.blit(text5, (-40 + i, 470))
        win.blit(text6, (-19+i, 470))
        win.blit(text7, (0 + i, 470))
        i+=80
    pygame.display.update()
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            done=True
    pygame.time.wait(500)
pygame.quit()