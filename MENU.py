from LOADING import *


#Mode level Screen
def modes(q):
    global quit5
    play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode=q
    i1=0
    i2=0
    while not quit5:
        gameDisplay.fill(black)
        mouse_x,mouse_y=pygame.mouse.get_pos()
        global white,bge,red,yellow
        gameDisplay.blit(bge,(0,0))
        if(i1>248*4-3):
            i1=0
        gameDisplay.blit(frames[i1/4],(320,1))
        i1=i1+1
        if(i2>319*4-3):
            i2=0
        gameDisplay.blit(frames1[i2/4],(320,300))
        i2=i2+1
        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
            gameDisplay.blit(button,(300,200))
            screen_text=font.render("resume",True,red)
        else:
            gameDisplay.blit(button1,(300,200))
            screen_text=font.render("resume",True,(0,255,255))
        x=pygame.transform.scale(text[15],(200,40))
        gameDisplay.blit(x,(320,210))
        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=500 and mouse_y<=560):
            gameDisplay.blit(button,(300,500))
            screen_text=font.render("hard",True,red)
        else:
            gameDisplay.blit(button1,(300,500))
            screen_text=font.render("HARD",True,(0,255,255))
        x=pygame.transform.scale(text[16],(200,40))
        gameDisplay.blit(x,(320,510))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x>=300 and mouse_x<=520 and mouse_y>=500 and mouse_y<=560:
                    global quit1,quit2,quit3,quit4,play,mode
                    mode=1
                    quit5=True
                if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                    global quit4,mode
                    mode=2
                    quit5=True
    q=[play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode]
    return q

#Difficulty level screen
def difficultyselect(q):
    global quit3
    play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode=q
    while not quit3:
        gameDisplay.fill(black)
        mouse_x,mouse_y=pygame.mouse.get_pos()
        global white,bge,red,yellow
        gameDisplay.blit(bge,(0,0))
        screen_text=font.render("BREAKOUT",True,red)
        x=pygame.transform.scale(text[0],(400,200))
        gameDisplay.blit(x,[200,0])
        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360):
            gameDisplay.blit(button,(300,300))
            screen_text=font.render("MEDIUM",True,red)
        else:
            gameDisplay.blit(button1,(300,300))
            screen_text=font.render("MEDIUM",True,(0,255,255))
        x=pygame.transform.scale(text[9],(200,40))
        gameDisplay.blit(x,(320,310))

        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
            gameDisplay.blit(button,(300,200))
            screen_text=font.render("EASY",True,red)
        else:
            gameDisplay.blit(button1,(300,200))
            screen_text=font.render("EASY",True,(0,255,255))
        x=pygame.transform.scale(text[7],(200,40))
        gameDisplay.blit(x,(320,210))
        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
            gameDisplay.blit(button,(300,400))
            screen_text=font.render("HARD",True,red)
        else:
            gameDisplay.blit(button1,(300,400))
            screen_text=font.render("HARD",True,(0,255,255))
        x=pygame.transform.scale(text[8],(200,40))
        gameDisplay.blit(x,(320,410))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360:
                    global bar_size,quit3
                    bar_size=100
                    quit3=True
                    q=play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode
                    q=modes(q)
                if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                    global bar_size,quit3
                    bar_size=50
                    quit3=True
                    q=play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode
                    q=modes(q)
                if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                    global bar_size,quit3
                    bar_size=150
                    quit3=True
                    q=play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode
                    q=modes(q)
    return q

#Level Select screen
def levelselect(q):
    # global quit2
    play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode=q
    while not quit2:
        gameDisplay.fill(black)
        mouse_x,mouse_y=pygame.mouse.get_pos()
        global white,bge,red,yellow
        gameDisplay.blit(bge,(0,0))
        gameDisplay.blit(bge,(0,0))
        x=pygame.transform.scale(text[0],(400,200))
        gameDisplay.blit(x,[200,0])
        if not(mouse_x>=300 and mouse_x<=550 and mouse_y>=300 and mouse_y<=360):
            gameDisplay.blit(button,(300,300))
            screen_text=font.render("L=1",True,red)

        else:
            gameDisplay.blit(button1,(300,300))
            screen_text=font.render("L=1",True,(0,255,255))
        x=pygame.transform.scale(text[5],(200,40))
        gameDisplay.blit(x,(320,310))
        if not(mouse_x>=300 and mouse_x<=550 and mouse_y>=400 and mouse_y<=460):
            gameDisplay.blit(button,(300,400))
            screen_text=font.render("L=2",True,red)
        else:
            gameDisplay.blit(button1,(300,400))
            screen_text=font.render("L=2",True,(0,255,255))
        x=pygame.transform.scale(text[6],(200,40))
        gameDisplay.blit(x,(320,410))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                global levels
                if mouse_x>=300 and mouse_x<=550 and mouse_y>=300 and mouse_y<=360:
                    levels=1
                    global quit2
                    quit2=True
                if mouse_x>=300 and mouse_x<=550 and mouse_y>=400 and mouse_y<=460:
                    levels=2
                    global levels
                    # levelsa=2
                    global quit2
                    quit2=True
    q=difficultyselect([play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode])
    return q

#Main menu screen
def mainmenu(q):
    play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode=q
    # global quit1,helping
    while not quit1:
        gameDisplay.fill(black)
        mouse_x,mouse_y=pygame.mouse.get_pos()
        # global white,bge,red,yellow,button,button1
        gameDisplay.blit(bge,(0,0))
        x=pygame.transform.scale(text[0],(400,200))
        gameDisplay.blit(x,[200,0])
        if not(mouse_x>=300 and mouse_x<=550 and mouse_y>=300 and mouse_y<=360):
            gameDisplay.blit(button,(300,300))
        else:
            gameDisplay.blit(button1,(300,300))
            screen_text=font.render("PLAY",True,(0,255,255))
        x=pygame.transform.scale(text[3],(200,40))
        gameDisplay.blit(x,(325,310))
        if not(mouse_x>=300 and mouse_x<=550 and mouse_y>=400 and mouse_y<=460):
            gameDisplay.blit(button,(300,400))
        else:
            gameDisplay.blit(button1,(300,400))
        x=pygame.transform.scale(text[4],(150,40))
        gameDisplay.blit(x,(340,410))
        screen_text=font.render("Press H for help",True,(0,0,0))
        gameDisplay.blit(screen_text,(450,550))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x>=300 and mouse_x<=550 and mouse_y>=300 and mouse_y<=360:
                    global play
                    play=True
                    global quit1
                    quit1=True
                    q=[play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode]
                    q=levelselect(q)
                elif mouse_x>=300 and mouse_x<=550 and mouse_y>=400 and mouse_y<=460:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    gameDisplay.fill(black)
                    gameDisplay.blit(helping,(0,0))
                    pygame.display.update()
                    quitz=False
                    while not quitz:
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_q:
                                    quitz=True
    return q

#Pause level screen
def pausef(q):
    global quit4
    play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode,score,life,rs=q
    while not quit4:
        gameDisplay.fill(black)
        mouse_x,mouse_y=pygame.mouse.get_pos()
        global white,bge,red,yellow
        gameDisplay.blit(bge,(0,0))
        screen_text=font.render("BREAKOUT",True,red)
        x=pygame.transform.scale(text[0],(400,200))
        gameDisplay.blit(x,[200,0])
        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
            gameDisplay.blit(button,(300,200))
            screen_text=font.render("resume",True,red)
        else:
            gameDisplay.blit(button1,(300,200))
            screen_text=font.render("resume",True,(0,255,255))
        x=pygame.transform.scale(text[14],(200,40))
        gameDisplay.blit(x,(320,210))
        if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
            gameDisplay.blit(button,(300,400))
            screen_text=font.render("hard",True,red)
        else:
            gameDisplay.blit(button1,(300,400))
            screen_text=font.render("HARD",True,(0,255,255))
        x=pygame.transform.scale(text[11],(200,40))
        gameDisplay.blit(x,(320,410))
        font1=pygame.font.SysFont(None,100)
        screen_text =font.render("Score "+str(score),True,black)
        gameDisplay.blit(screen_text,[0,0])
        screen_text=font.render("       Life "+str(life),True,black)
        gameDisplay.blit(screen_text,[540,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                    global quit1,quit2,quit3,quit4,quit5,play
                    quit1=False
                    quit2=False
                    quit3=False
                    quit5=False
                    quit4=True
                    play=False
                    rs=1
                    play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode=mainmenu([play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode])
                if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                    global quit4
                    quit4=True
    q=play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode,score,life,rs
    return q
