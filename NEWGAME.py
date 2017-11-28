#BREAKOUT (BRICK BREAKER)

            #Importing modules
import pygame
import time

from LOADING import *

from MENU import *

from LEVEL import *



#Opens the 'PyGame' window at a specific position on the screencreen
window_posi_x = 400
window_posi_y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(window_posi_x, window_posi_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

#Variables Required

    #For game exit
gameexit=False
gameover=False

    #Position of ball
lead_x=display_width/2
lead_y=display_height/2

    #Size of ball
block_size=10

    #Position of bar
lead_x_bar=display_width/2
lead_y_bar=display_height-block_size

    #bar size
bar_size=150

    #Chage in position of ball
lead_x_change=4
lead_y_change=-4

    #Change in position of bar
leadbar_x_change=0

    #Frame rate
fps=60

    #Score
score=0

    #Ball Speed Control
speedtoggle=0
fspeedtoggle=0

    #Life
life=2

    #Quit control variables
play=False
quit1=False
quit2=False
quit3=False
quit4=False
quit5=False

    #Blast Time Animation Variables
blasttime1=0
blasttime2=0
blasttime21=0

    #Level Cntrol variables
levels=1

# Implementing mode 1 and mode 2 in game:-
mode = 2

           #List declaration for each row of Bricks
    #Level 1 Normal Bricks
l=[]
l1=[]
l2=[]
l3=[]
    #Level 1 Ice Bricks
tb=[]
tc=[]
    #Level 2 Normal Bricks
l21=[]
l22=[]
l23=[]
l24=[]
l25=[]
l26=[]
l27=[]
    #Level 2 Cosmic Bricks
fb=[]
fc=[]
    #Exploding Bricks
bb1=[]
bb2=[]

    #Restarter variable
rs=1


        #List initialization for bricks
            #Normal Bricks
for i in range(15):
    l.append(1)
    l1.append(1)
    l2.append(1)
    l3.append(1)

            #Normal Bricks Level 2
for i in range(15):
    l21.append(1)
for i in range(14):
    l22.append(1)
for i in range(13):
    l23.append(1)
for i in range(12):
    l24.append(1)
for i in range(11):
    l25.append(1)
for i in range(10):
    l26.append(1)
for i in range(9):
    l27.append(1)

            #Special Bricks
for i in range(2):
    fb.append(1)
    fc.append(500)
    bb1.append(1)
    bb2.append(1)
    tb.append(1)
    tc.append(500)

            #Clock Initialization
clock=pygame.time.Clock()

            #Brick Restart Function
def brickrestart():
    for i in range(15):
        l[i]=1
        l1[i]=1
        l2[i]=1
        l3[i]=1
    for i in range(15):
        if i>0:
            l21[i]=1
        else:
            l21[i]=0
    for i in range(14):
        if i>1:
            l22[i]=1
        else:
            l22[i]=0
    for i in range(13):
        if i>2:
            l23[i]=1
        else:
            l23[i]=0
    for i in range(12):
        if i>3:
            l24[i]=1
        else:
            l24[i]=0
    for i in range(11):
        if i>4:
            l25[i]=1
        else:
            l25[i]=0
    for i in range(10):
        if i>5:
            l26[i]=1
        else:
            l26[i]=0
    for i in range(9):
        if i>6:
            l27[i]=1
        else:
            l27[i]=0
    for i in range(2):
        fb[i]=1
        fc[i]=500
        bb1[i]=1
        bb2[i]=1
        tb[i]=1
        tc[i]=500

    global lead_x,lead_y,lead_x_bar,bar_size,lead_x_change,lead_y_change,life,score
    lead_x=200
    lead_y=400
    lead_x_bar=400-bar_size/2
    lead_x_change=4
    lead_y_change=-4
    life=2
    score=0

            #Main Loop Calling Function
def gameloop():

#Game Ending control Variables
    global gameexit,gameover
    gameexit=False
    gameover=False

    #Initializing Variables

#Ball
    global lead_x,lead_y

#Bar
    global lead_x_bar
    lead_x_bar=display_width/2

#Block Size
    global block_size

#Bar control change variable
    global leadbar_x_change
    leadbar_x_change=0

#Life Scoping
    global life
    life=2

#Level Initialization
    brickrestart()

#Quit control variables
    global quit1
    quit1=False
#Blast time Control
    global blasttime1,blasttime2,blasttime21
#Main Menu Screen
    if(play==False):
        global quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode
        quit1=False
        quit2=False
        quit3=False
        quit4=False
        quit5=False
        brickrestart()
        q=[play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode]
        play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode=mainmenu(q)

#Main Game Loop
    while (not gameexit) and play:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        quit4 =False
#Event Handling - Left,Right,Quiting of game,pausing
        z1=0
        z2=0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameexit=True
                if event.type ==pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                leadbar_x_change=-10
                                z1=1
                        if event.key == pygame.K_RIGHT:
                                leadbar_x_change=10
                                z2=1
                if event.type ==pygame.KEYUP:
                        leadbar_x_change=0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(mouse_x>770 and mouse_x<800 and mouse_y>0 and mouse_y<30):
                        global quit4
                        quit4=False
                        q=play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode,score,life,rs
                        play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode,score,life,rs=pausef(q)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        global quit4
                        quit4=False
                        q=play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode,score,life,rs
                        play,quit1,quit2,quit3,quit4,quit5,levels,bar_size,mode,score,life,rs=pausef(q)
        global rs
        if rs==1:
            brickrestart()
            rs=0
#Dividing bar in 3 parts, different reflection for each position
        if lead_x>=lead_x_bar and lead_x<(lead_x_bar+bar_size/3) and (lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar):
                if(lead_x_change>0):
                        lead_y_change=-lead_y_change
                        if (leadbar_x_change == 0 ):
                            lead_x_change=-lead_x_change
                        elif (leadbar_x_change > 0 and lead_x_change<=12):
                            lead_x_change = -(lead_x_change) + 2
                        elif (leadbar_x_change < 0):
                            lead_x_change = -(lead_x_change) - 2
                        pygame.mixer.Sound.play(bounce_sound)
                else:
                        lead_y_change=-lead_y_change
                        if (leadbar_x_change > 0):
                            lead_x_change += 2
                        elif (leadbar_x_change < 0):
                            lead_x_change -= 2
                        pygame.mixer.Sound.play(bounce_sound)
        if lead_x>=lead_x_bar+bar_size/3 and lead_x<(lead_x_bar+(bar_size*2)/3) and lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar:
                lead_y_change=-lead_y_change
                if (leadbar_x_change > 0):
                    lead_x_change += 2
                elif (leadbar_x_change < 0):
                    lead_x_change -= 2
                pygame.mixer.Sound.play(bounce_sound)
        if lead_x>=lead_x_bar+(bar_size*2)/3 and lead_x<=(lead_x_bar+bar_size) and lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar:
                if(lead_x_change<0):
                        lead_y_change=-lead_y_change
                        if (leadbar_x_change == 0):
                            lead_x_change=-lead_x_change
                        elif (leadbar_x_change > 0):
                            lead_x_change = -(lead_x_change) + 2
                        elif (leadbar_x_change < 0):
                            lead_x_change = -(lead_x_change) - 2
                        pygame.mixer.Sound.play(bounce_sound)
                else:
                        lead_y_change=-lead_y_change
                        if (leadbar_x_change > 0):
                            lead_x_change += 2
                        elif (leadbar_x_change < 0):
                            lead_x_change -= 2
                        pygame.mixer.Sound.play(bounce_sound)

#Reflection of ball at the edge of the screen
        global mode
        if (mode == 1):
            if lead_x+block_size>=display_width or lead_x<=0 :
                    lead_x_change=-lead_x_change
                    pygame.mixer.Sound.play(bounce_sound)
            if lead_y<=0:
                    lead_y_change=-lead_y_change
                    pygame.mixer.Sound.play(bounce_sound)
        elif (mode == 2):
            if (lead_x >= display_width):
                lead_x = 0
                pygame.mixer.Sound.play(whoosh_sound)
            elif (lead_x <= 0):
                lead_x = display_width
                pygame.mixer.Sound.play(whoosh_sound)
            if lead_y <= 0:
                lead_y_change =- lead_y_change
                pygame.mixer.Sound.play(bounce_sound)

#Game over when ball goes down under the screen and the bar misses
        if lead_y>display_height:
            if life==0:
                global bge
                gameDisplay.blit(bge,(0,0))
                x=pygame.transform.scale(text[1],(400,200))
                gameDisplay.blit(x,[200,200])
                pygame.mixer.Sound.play(lose_sound)
                pygame.display.update()
                time.sleep(4)
                gameover=True
            else:
                life=life-1
                lead_x=400
                lead_y=300
                lead_x_change=4
                lead_y_change=4
                time.sleep(1)
                pygame.mixer.Sound.play(life_sound)
                continue

#Replayability after death
        while gameover== True:
                gameDisplay.fill(black)
                mouse_x,mouse_y=pygame.mouse.get_pos()
                global white,bge,red,yellow,pause,pause1
                gameDisplay.blit(bge,(0,0))

                x=pygame.transform.scale(text[1],(400,200))
                gameDisplay.blit(x,[200,0])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360):
                    gameDisplay.blit(button,(300,300))
                    screen_text=font.render("PLAYAGAIN",True,red)
                else:
                    gameDisplay.blit(button1,(300,300))
                    screen_text=font.render("PLAYAGAIN",True,(0,255,255))
                x=pygame.transform.scale(text[10],(200,40))
                gameDisplay.blit(x,(325,310))
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                    gameDisplay.blit(button,(300,200))
                    screen_text=font.render("MAINMENU",True,red)
                else:
                    gameDisplay.blit(button1,(300,200))
                    screen_text=font.render("MAINMENU",True,(0,255,255))
                x=pygame.transform.scale(text[11],(200,40))
                gameDisplay.blit(x,(325,210))
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
                    gameDisplay.blit(button,(300,400))
                    screen_text=font.render("QUIT",True,red)
                else:
                    gameDisplay.blit(button1,(300,400))

                    screen_text=font.render("QUIT",True,(0,255,255))
                x=pygame.transform.scale(text[4],(200,40))
                gameDisplay.blit(x,(325,410))
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        gameexit=True
                                        gameover=False
                                if event.key == pygame.K_c:
                                        time.sleep(1)
                                        brickrestart()
                                        score=0
                                        gameloop()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360:
                                    brickrestart()
                                    score=0
                                    gameloop()
                                if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                                    gameexit=True
                                    gameover=False
                                if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                                    brickrestart()
                                    score=0
                                    global play
                                    play=False
                                    gameloop()


#Checking bar edge so that it doesn't go off screen
        if(lead_x_bar<=display_width-bar_size and lead_x_bar>-1):
                lead_x_bar +=leadbar_x_change
        if(lead_x_bar<=0):
                lead_x_bar=0
        if(lead_x_bar>=display_width-bar_size):
                lead_x_bar=display_width-bar_size

#Getting the screen ready
        gameDisplay.fill(white)
        gameDisplay.blit(bg,(0,0))
        pygame.draw.rect(gameDisplay,red,[lead_x_bar,lead_y_bar,bar_size,block_size])

#Drawing the ball
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
        if(mouse_x>770 and mouse_x<800 and mouse_y>0 and mouse_y<30):
                gameDisplay.blit(pause1,(770,0))
        else:
                    gameDisplay.blit(pause,(770,0))

#Drawing the level
        global l,l1,l2,l3,bb1,tb,tc,blasttime1,blasttime2,l21,l22,l23,l24,l25,l26,l27,fb,fc,bb1,bb2,blasttime21
        global lead_x,lead_y,lead_x_change,lead_y_change,score
        if levels==1:
            lead_x,lead_y,lead_x_change,lead_y_change,l,l1,l2,l3,bb1,tb,tc,blasttime1,blasttime2,score=level([lead_x,lead_y,score,block_size,lead_x_change,lead_y_change,speedtoggle,l,l1,l2,l3,bb1,tb,tc,blasttime1,blasttime2])
        else:
            lead_x,lead_y,lead_x_change,lead_y_change,l21,l22,l23,l24,l25,l26,l27,bb2,fb,fc,blasttime21,score=level2([lead_x,lead_y,score,block_size,lead_x_change,lead_y_change,speedtoggle,l21,l22,l23,l24,l25,l26,l27,bb2,fb,fc,blasttime21])
        gameover=gameo(l,l1,l2,l3,l21,l22,l23,l24,l25,l26,l27,tb,fb,bb1,bb2,score)

#Displaying the score
        font1=pygame.font.SysFont(None,100)
        screen_text =font.render("Score "+str(score),True,black)
        gameDisplay.blit(screen_text,[0,0])
        screen_text=font.render("  Life "+str(life),True,black)
        gameDisplay.blit(screen_text,[540,0])
        for i in range(2):
            if tc[i]>0 and tc[i]<500:
                screen_text=font.render("Time "+str(tc[i]),True,black)
                gameDisplay.blit(screen_text,[(i+1)*200,0])
            if fc[i]>0 and fc[i]<500:
                screen_text=font.render("Time "+str(fc[i]),True,black)
                gameDisplay.blit(screen_text,[(i+1)*200,0])

#Changing the ball position for the next loop
        lead_x += lead_x_change
        lead_y += lead_y_change
        global blasttime1,blasttime2,blasttime21
        if(blasttime1>0):
            global blast
            x=12*(60-blasttime1)
            blast1=pygame.transform.scale(blast,(x,x))
            gameDisplay.blit(blast1,(625-(x/2),115-(x/2)))
            blasttime1=blasttime1-1
        if(blasttime2>0):
            global blast
            x=12*(60-blasttime2)
            blast1=pygame.transform.scale(blast,(x,x))
            gameDisplay.blit(blast1,(175-(x/2),175-(x/2)))
            blasttime2=blasttime2-1
        if(blasttime21>0):
            global blast
            x=12*(60-blasttime21)
            blast1=pygame.transform.scale(blast,(x,x))
            gameDisplay.blit(blast1,(325-(x/2),125-(x/2)))
            blasttime21=blasttime21-1

#Updating the display
        pygame.display.update()

#Controlling the Frames per second (FPS) //60 For Now
        clock.tick(fps)

#Ending Pygame
    global quit4
    pygame.quit()
    quit()

#Calling the Function which runs all the Code for the game
gameloop()

# X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
