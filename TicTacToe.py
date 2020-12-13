import pygame

pygame.init()

win=pygame.display.set_mode((400, 250))
pygame.display.set_caption("Tic-Tac-Toe")
clock=pygame.time.Clock()
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
c=0

Font=pygame.font.SysFont("timesnewroman", 15)
text=Font.render("Enter player1 Name -",True, (255, 255, 255))
text2=Font.render("Enter player2 Name -",True, (255, 255, 255))
cursor=Font.render("|",True, (255, 255, 255))
draw=Font.render("Drawn the Game ",True, (255, 255, 255))
s1=Font.render("Submit", True, white)

player1=""
player2=""
run=True
active=False
active1=False
flag=0

def tictactoe(win, player1, player2):
    run=True
    c=0
    one, two, three, four, five, six, seven, eight, nine=0,0,0,0,0,0,0,0,0
    win.fill((0, 0, 0))
    up1,up2, down1, down2, left1,middlerow1, middlerow2, middlecolumn1, middlecolumn2 , left2, right1, right2, leftcross1, leftcross2, rightcross1, rightcross2=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    first = pygame.draw.rect(win, white, (10, 10, 50, 50), 0)
    second = pygame.draw.rect(win, white, (80, 10, 50, 50), 0)
    third = pygame.draw.rect(win, white, (150, 10, 50, 50), 0)

    fourth = pygame.draw.rect(win, white, (10, 80, 50, 50), 0)
    fifth = pygame.draw.rect(win, white, (80, 80, 50, 50), 0)
    sixth = pygame.draw.rect(win, white, (150, 80, 50, 50), 0)

    seventh = pygame.draw.rect(win, white, (10, 150, 50, 50), 0)
    eighth = pygame.draw.rect(win, white, (80, 150, 50, 50), 0)
    nineth = pygame.draw.rect(win, white, (150, 150, 50, 50), 0)

    win1 = Font.render(player1+" Wins the Game ", True, (255, 255, 255))
    win2 = Font.render(player2+" Wins the Game ", True, (255, 255, 255))

    flag=0
    while run:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return 0
            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                if(first.collidepoint(pos)):
                    if(one==0 and c%2==0):
                        pygame.draw.rect(win, blue, (20, 20, 30, 30), 0)
                        c+=1
                        up1+=1
                        leftcross1+=1
                        left1+=1
                        one=1
                    elif(one==0 and c%2==1):
                        pygame.draw.circle(win, red, [35, 35], 20, 0)
                        c+=1
                        up2 += 1
                        leftcross2 += 1
                        left2 += 1
                        one=1
                if (second.collidepoint(pos)):
                    if (two == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (90, 20, 30, 30), 0)
                        c += 1
                        up1+=1
                        middlecolumn1+=1
                        two = 1
                    elif (two == 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [105, 35], 20, 0)
                        c += 1
                        up2 += 1
                        middlecolumn2 += 1
                        two = 1
                if (third.collidepoint(pos)):
                    if (three == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (160, 20, 30, 30), 0)
                        c += 1
                        up1+=1
                        right1+=1
                        rightcross1+=1
                        three = 1
                    elif (three == 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [175, 35], 20, 0)
                        c += 1
                        up2 += 1
                        right2 += 1
                        rightcross2 += 1
                        three = 1
                if (fourth.collidepoint(pos)):
                    if (four == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (20, 90, 30, 30), 0)
                        c += 1
                        left1+=1
                        middlerow1+=1
                        four = 1
                    elif (four == 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [35, 105], 20, 0)
                        c += 1
                        left2 += 1
                        middlerow2 += 1
                        four = 1
                if (fifth.collidepoint(pos)):
                    if (five == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (90, 90, 30, 30), 0)
                        c += 1
                        leftcross1+=1
                        rightcross1+=1
                        middlerow1+=1
                        middlecolumn1+=1
                        five = 1
                    elif (five == 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [105, 105], 20, 0)
                        c += 1
                        leftcross2 += 1
                        rightcross2 += 1
                        middlerow2 += 1
                        middlecolumn2 += 1
                        five = 1
                if (sixth.collidepoint(pos)):
                    if (six == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (160, 90, 30, 30), 0)
                        c += 1
                        right1+=1
                        middlerow1+=1
                        six = 1
                    elif (six == 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [175, 105], 20, 0)
                        c += 1
                        right2 += 1
                        middlerow2 += 1
                        six = 1
                if (seventh.collidepoint(pos)):
                    if (seven == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (20, 160, 30, 30), 0)
                        c += 1
                        down1+=1
                        rightcross1+=1
                        left1+=1
                        seven = 1
                    elif (seven == 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [35, 175], 20, 0)
                        c += 1
                        down2+=1
                        left2+=1
                        rightcross2 += 1
                        seven = 1
                if (eighth.collidepoint(pos)):
                    if (eight == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (90, 160, 30, 30), 0)
                        c += 1
                        down1+=1
                        middlecolumn1+=1
                        eight = 1
                    elif (eight== 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [105, 175], 20, 0)
                        c += 1
                        down2 += 1
                        middlecolumn2 += 1
                        eight = 1
                if (nineth.collidepoint(pos)):
                    if (nine == 0 and c % 2 == 0):
                        pygame.draw.rect(win, blue, (160, 160, 30, 30), 0)
                        c += 1
                        right1+=1
                        down1+=1
                        leftcross1+=1
                        nine= 1
                    elif (nine== 0 and c % 2 == 1):
                        pygame.draw.circle(win, red, [175, 175], 20, 0)
                        c += 1
                        nine= 1
                        right2 += 1
                        down2 += 1
                        leftcross2 += 1
                if(flag==0 and (left1==3 or right1==3 or up1==3 or down1==3 or middlecolumn1==3 or middlerow1==3 or leftcross1==3 or rightcross1==3)):
                    print(left1, up1, rightcross1, right1, down1, leftcross1, middlerow1, middlecolumn1)
                    win.blit(win1, (220, 100))
                    flag=1
                elif(flag==0 and (left2==3 or right2==3 or up2==3 or down2==3 or middlecolumn2==3 or middlerow2==3 or leftcross2==3 or rightcross2==3)):
                    win.blit(win2, (220, 100))
                    flag=1
                elif(flag==0 and c==9):
                    win.blit(draw, (220, 100))
                    flag=1
        pygame.display.update()
while run:
    win.fill((0, 0, 0)) # very import because when we backspace and it is used
    p1 = pygame.draw.rect(win, blue, (135, 2, 200, 20), 2)
    p2 = pygame.draw.rect(win, blue, (135, 30, 200, 20), 2)
    submit=pygame.draw.rect(win, green, (185, 85, 50, 20), 0)
    win.blit(text, (0, 0))
    win.blit(text2, (0, 30))
    for event in pygame.event.get():
        if(active and c>=0):
            c+=1
            win.blit(cursor, (138+text1.get_width(), 2))
        elif(active1 and c>=0):
            c+=1
            win.blit(cursor, (138 + text3.get_width(), 30))
        if active and event.type==pygame.KEYDOWN:
            if( event.key == pygame.K_BACKSPACE):
                player1 = player1[0:-1]
            else:
                player1 += event.unicode
        if active1 and event.type==pygame.KEYDOWN:
            if( event.key == pygame.K_BACKSPACE):
                player2 = player2[0:-1]
            else:
                player2 += event.unicode
        if(event.type==pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            if(p1.collidepoint(pos)):
                active=True
                active1=False
            elif(p2.collidepoint(pos)):
                active1=True
                active=False
            elif(submit.collidepoint(pos)):
                flag=tictactoe(win, player1, player2)
                if(flag==0):
                    run=False
        if event.type==pygame.QUIT:
            run=False
            break
    text1 = Font.render(player1, True, (255, 255, 255))
    text3 = Font.render(player2, True, (255, 255, 255))
    win.blit(s1, (188, 87))
    win.blit(text1, (137, 2))
    win.blit(text3, (137, 30))
    pygame.display.flip()
    if(c==3):
        c=-3
    c+=1
    clock.tick(60)
pygame.quit()