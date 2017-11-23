#BREAKOUT (BRICK BREAKER)

            #Importing modules
import pygame
import time
import random
import math
import os

            #Initializing pygame
pygame.init()

            #Colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)

        #Loading the sounds
background_music = pygame.mixer.music.load("background.mpeg")
hit_sound = pygame.mixer.Sound("brick_1.ogg")
bounce_sound = pygame.mixer.Sound("hit.ogg")
life_sound = pygame.mixer.Sound("life.ogg")
ice_sound = pygame.mixer.Sound("ice.ogg")
speed_sound = pygame.mixer.Sound("speedup.ogg")
pygame.mixer.music.play(-1)

        #Resoultion
display_width=800
display_height=600

        #Opens the 'PyGame' window at a specific position on the screencreen
window_posi_x = 400
window_posi_y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(window_posi_x, window_posi_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'
            #Defining display
gameDisplay=pygame.display.set_mode((display_width,display_height))

            #Set caption
pygame.display.set_caption("BREAKOUT")

        #Variables Required

            #For game exit
gameexit=False

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
fps=30

            #Score
score=0

            #Ball Speed Control
speedtoggle=0
fspeedtoggle=0

            #Life
life=0


        #Graphics Loading
            #Image Loading
bg= pygame.image.load("sk.png")
bg= pygame.transform.scale(bg,(display_width,display_height))
brick= pygame.image.load("brick.png")
brickgreen=pygame.image.load("gb1.jpg")
bge= pygame.image.load("bgexit.jpg")
bge= pygame.transform.scale(bge,(display_width,display_height))
iceball=pygame.image.load("iceball.jpg")
iceball=pygame.transform.scale(iceball,(10,10))
            #Font Loading
font=pygame.font.SysFont(None,50)


            #Message to Screen at Game Initialization -  Function
def message_to_screen(msg,color):
    screen_text =font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2-50,display_height/2-20])

            #Clock Initialization
clock=pygame.time.Clock()

            #Game Initialization Screen - Start Intro Screen
message_to_screen("Breakout!!",red)
pygame.display.update()
time.sleep(2)

            #Brick Creation Function
def block(blx,bly,bls,l,i):
    if (lead_x>blx and lead_x<blx+bls and lead_y+block_size>bly and lead_y<bly+block_size and l[i]==1):
        l[i]=0
        global lead_y_change
        lead_y_change=-lead_y_change
        global score
        score +=1
        pygame.mixer.Sound.play(hit_sound)
    if l[i]:
        pygame.draw.rect(gameDisplay,red,[blx,bly,bls,block_size])
        global brick
        brick=pygame.transform.scale(brick,(bls,block_size))
        gameDisplay.blit(brick,(blx,bly))

            #Time Block - Special
def timeblock(blx,bly,bls,l,i):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and tb[i]==1):
        tb[i]=0
        global lead_y_change
        lead_y_change=-lead_y_change
        global score
        global tc
        tc[i]-=1
        score +=2
        pygame.mixer.Sound.play(ice_sound)
    if tb[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(brickgreen,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))
        
def fastblock(blx,bly,bls,fb,i):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and tb[i]==1):
        fb[i]=0
        global lead_y_change
        lead_y_change=-lead_y_change
        hit_sound = pygame.mixer.Sound.play(speed_sound)
        global score
        global tc
        fc[i]-=1
        score +=2
    if fb[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(brickgreen,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))

            #List declaration for each row of Bricks
l=[]
l1=[]
l2=[]
l3=[]
tb=[]
tc=[]

l21=[]
l22=[]
l23=[]
l24=[]
l25=[]
l26=[]
l27=[]

fb=[]
fc=[]

        #List initialization for bricks
            #Normal Bricks    
for i in range(16):
    l.append(1)
    l1.append(1)
    l2.append(1)
    l3.append(1)

            #Time Bricks
for i in range(2):
    tb.append(1)
    tc.append(500)

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
for i in range(19):
    l27.append(1)

for i in range(2):
    fb.append(1)
    fc.append(500)

            #Level Creation Function 
def level():
    global lead_x_change
    global lead_y_change
        #Row creation for normal bricks
    for i in range(15):
        if l[i]==1:
            block(i*50,100,50,l,i)
    for i in range(15):
        if l1[i]==1:
            block(i*50,100+40,50,l1,i)
    for i in range(15):
        if l2[i]==1:
            block(i*50,100+80,50,l2,i)
    for i in range(15):
        if l3[i]==1:
            block(i*50,100+120,50,l3,i)

    for i in range(2):
        if tb[i]==1:
            timeblock(i*7/4+37,100+30*i,100,tb,i)
    global speedtoggle
    speedtoggle=0
    speedcontrol(speedtoggle) 

def level2():
    global lead_x_change
    global lead_y_change
    for i in range(15):
        if i>0:
            if l21[i]==1:
                block(i*50,100,50,l21,i)
    for i in range(14):
        if i>1:
            if l22[i]==1:
                block(i*50,110,50,l22,i)
    for i in range(13):
        if i>2:
            if l23[i]==1:
                block(i*50,120,50,l23,i)
    for i in range(12):
        if i>3:
            if l24[i]==1:
                block(i*50,130,50,l24,i)
    for i in range(11):
        if i>4:
            if l25[i]==1:
                block(i*50,140,50,l25,i)
    for i in range(10):
        if i>5:
            if l26[i]==1:
                block(i*50,150,50,l26,i)
    for i in range(9):
        if i>6:
            if l27[i]==1:
                block(i*50,160,50,l27,i)
    if fb[0]==1:
        fastblock(40,40,100,fb,0)
    if fb[1]==1:
        fastblock(280,700,100,fb,0)
    global fspeedtoggle
    fspeedtoggle=0
    fspeedcontrol(fspeedtoggle)

        #Speed Control Function
def speedcontrol(speedtoggle):
    global lead_x_change
    global lead_y_change
    global lead_x
    global lead_y

    for i in range(2):
        if tc[i]<500 and tc[i]>0:
            tc[i]-=1
            speedtoggle=1
            break
        elif tc[i]==0:
            speedtoggle=2
    if speedtoggle==1:
        gameDisplay.blit(iceball,(lead_x,lead_y))
        if lead_x_change<0:
            lead_x_change=-2
        else:
            lead_x_change=2
        if lead_y_change<0:
            lead_y_change=-2
        else:
            lead_y_change=2
    if speedtoggle==2:
        if lead_x_change>0:
            lead_x_change=4
        else:
            lead_x_change=-4
        if lead_y_change>0:
            lead_y_change=4
        else:
            lead_y_change=-4 

def fspeedcontrol(speedtoggle):
    global lead_x_change
    global lead_y_change
    for i in range(2):
        if fc[i]<500 and fc[i]>0:
            fc[i]-=1
            speedtoggle=1
            break
        elif fc[i]==0:
            speedtoggle=2
    if speedtoggle==1:
        if lead_x_change<0:
            lead_x_change=-8
        else:
            lead_x_change=8
        if lead_y_change<0:
            lead_y_change=-8
        else:
            lead_y_change=8
    if speedtoggle==2:
        if lead_x_change>0:
            lead_x_change=4
        else:
            lead_x_change=-4
        if lead_y_change>0:
            lead_y_change=4
        else:
            lead_y_change=-4 

def brickrestart():
    global l
    global l1
    global l2
    global l3
    for i in range(16):
        l[i]=1
        l1[i]=1
        l2[i]=1
        l3[i]=1
    for i in range(2):
        tb[i]=1
        tc[i]=500
    for i in range(15):
         l21[i]=1
    for i in range(14):
         l22[i]=1
    for i in range(13):
        l23[i]=1
    for i in range(12):
        l24[i]=1
    for i in range(11):
        l25[i]=1
    for i in range(10):
        l26[i]=1
    for i in range(9):
        l27[i]=1
    for i in range(2):
        fb[i]=1

            #Game Loop Function
play=False
quit1=False
quit2=False
quit3 = False
levels=level
def gameloop():
        #Game Ending control Variables
    gameexit=False
    gameover=False

    #Referencing global scope variables

        #Ball Initialization
    global lead_x
    global lead_y
    lead_x=display_width/2
    lead_y=display_height/2

        #Bar initialization
    global lead_x_bar
    global lead_y_bar
    lead_x_bar=display_width/2

        #Block Size Initialization
    global block_size
    block_size=10

        #Ball Change Initialization
    global lead_x_change
    global lead_y_change

        #Bar control change variable
    global leadbar_x_change
    leadbar_x_change=0

        #FPS (Frames per second)
    global fps

        #Bar size
    global bar_size

        #Score
    global score
        
        #Brick Row initialization
    global l
    global l1,l2,l3,l4,l5

        #Life Scoping
    global life
    life=2
        #Unknown Variables
    global z
    brickrestart()        
        #Broken Time loop list , I think
    #l4=[1,1,1,1,1]
    #l5=[1,1,1,1,1]
    global bge
    #quit1=False
    global play
    global quit1
    def difficultyselect():
        global quit3
        while not quit3:
                gameDisplay.fill(black)
                mouse_x,mouse_y=pygame.mouse.get_pos()
                global white,bge,red,yellow
                gameDisplay.blit(bge,(0,0))
                screen_text=font.render("BREAKOUT",True,red)
                gameDisplay.blit(screen_text,[350,0])
                #screen_text =font.render("Press 'q' to exit the game  or 'c' to play again",True,white)
                #gameDisplay.blit(screen_text,[0,display_height/6])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360):
                    pygame.draw.rect(gameDisplay,yellow,[300,300,220,60])
                    screen_text=font.render("MEDIUM",True,red)
                else:
                    pygame.draw.rect(gameDisplay,(0,0,255),[300,300,220,60])
                    screen_text=font.render("MEDIUM",True,(0,255,255))
                gameDisplay.blit(screen_text,[310,300])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                    pygame.draw.rect(gameDisplay,yellow,[300,200,220,60])
                    screen_text=font.render("EASY",True,red)
                else:
                    pygame.draw.rect(gameDisplay,(0,0,255),[300,200,220,60])
                    screen_text=font.render("EASY",True,(0,255,255))
                gameDisplay.blit(screen_text,[310,200])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
                    pygame.draw.rect(gameDisplay,yellow,[305,400,200,60])
                    screen_text=font.render("HARD",True,red)
                else:
                    pygame.draw.rect(gameDisplay,(0,0,255),[305,400,200,60])
                    screen_text=font.render("HARD",True,(0,255,255))
                gameDisplay.blit(screen_text,[350,400])
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360:
                                    global bar_size,quit3
                                    bar_size=100
                                    quit3=True
                                if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                                    global bar_size,quit3
                                    bar_size=50
                                    quit3=True
                                if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                                        global bar_size,quit3
                                        bar_size=150
                                        quit3=True

    #Main Game Loop
    def levelselect():
        while not quit2:	
            gameDisplay.fill(black)
            mouse_x,mouse_y=pygame.mouse.get_pos()
            global white,bge,red,yellow
            gameDisplay.blit(bge,(0,0))
            screen_text=font.render("BREAKOUT",True,red)
            gameDisplay.blit(screen_text,[350,0])
            #screen_text =font.render("Press 'q' to exit the game  or 'c' to play again",True,white)
            #gameDisplay.blit(screen_text,[0,display_height/6])
            if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360):
                pygame.draw.rect(gameDisplay,yellow,[300,300,220,60])
                screen_text=font.render("L=1",True,red)
            else:
                pygame.draw.rect(gameDisplay,(0,0,255),[300,300,220,60])
                screen_text=font.render("L=1",True,(0,255,255))
            gameDisplay.blit(screen_text,[310,300])
            if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
                pygame.draw.rect(gameDisplay,yellow,[305,400,200,60])
                screen_text=font.render("L=2",True,red)
            else:
                pygame.draw.rect(gameDisplay,(0,0,255),[305,400,200,60])
                screen_text=font.render("L=2",True,(0,255,255))
            gameDisplay.blit(screen_text,[350,400])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    global levels
                    if mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360:
                        levels=level
                        global quit2
                        quit2=True
                    if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                        levels=level2
                        global quit2
                        quit2=True
        difficultyselect()

    def mainmenu():
        while not quit1:	
            gameDisplay.fill(black)
            mouse_x,mouse_y=pygame.mouse.get_pos()
            global white,bge,red,yellow
            gameDisplay.blit(bge,(0,0))
            screen_text=font.render("BREAKOUT",True,red)
            gameDisplay.blit(screen_text,[350,0])
            #screen_text =font.render("Press 'q' to exit the game  or 'c' to play again",True,white)
            #gameDisplay.blit(screen_text,[0,display_height/6])
            if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360):
                pygame.draw.rect(gameDisplay,yellow,[300,300,220,60])
                screen_text=font.render("PLAY",True,red)
            else:
                pygame.draw.rect(gameDisplay,(0,0,255),[300,300,220,60])
                screen_text=font.render("PLAY",True,(0,255,255))
            gameDisplay.blit(screen_text,[310,300])
            if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
                pygame.draw.rect(gameDisplay,yellow,[305,400,200,60])
                screen_text=font.render("QUIT",True,red)
            else:
                pygame.draw.rect(gameDisplay,(0,0,255),[305,400,200,60])
                screen_text=font.render("QUIT",True,(0,255,255))
            gameDisplay.blit(screen_text,[350,400])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360:
                        brickrestart()
                        score=0
                        global play
                        play=True
                        global quit1
                        quit1=True
                        levelselect()
                    if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                        gameexit=True
                        gameover=False
                        global quit1
                        quit1=True
    if(play==False):
        global quit1,quit2
        quit1=False
        quit2=False
        mainmenu()
    while (not gameexit) and play:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        #Event Handling - Left,Right,Quiting of game
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
            
        #Dividing bar in 3 parts, different reflection for each position                       
        if lead_x>=lead_x_bar and lead_x<(lead_x_bar+bar_size/3) and (lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar):
                if(lead_x_change>0):
                        lead_y_change=-lead_y_change
                        lead_x_change=-lead_x_change
                        pygame.mixer.Sound.play(bounce_sound)
                else:
                        lead_y_change=-lead_y_change
                        pygame.mixer.Sound.play(bounce_sound)
        if lead_x>=lead_x_bar+bar_size/3 and lead_x<(lead_x_bar+(bar_size*2)/3) and lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar:
                lead_y_change=-lead_y_change
                pygame.mixer.Sound.play(bounce_sound)
        if lead_x>=lead_x_bar+(bar_size*2)/3 and lead_x<=(lead_x_bar+bar_size) and lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar:
                if(lead_x_change<0):
                        lead_y_change=-lead_y_change
                        lead_x_change=-lead_x_change
                        pygame.mixer.Sound.play(bounce_sound)
                else:
                        lead_y_change=-lead_y_change
                        pygame.mixer.Sound.play(bounce_sound)

        #Reflection of ball at the edge of the screen
        if lead_x+block_size>=display_width or lead_x<=0 :
                lead_x_change=-lead_x_change
                pygame.mixer.Sound.play(bounce_sound)
        if lead_y<=0:
                lead_y_change=-lead_y_change
                pygame.mixer.Sound.play(bounce_sound)

        #Game over when ball goes down under the screen and the bar misses
        if lead_y>display_height:
            if life==0:
                global bge
                gameDisplay.blit(bge,(0,0))
                message_to_screen("game over",red)
                pygame.display.update()
                time.sleep(2)
                gameover=True
            else:
                life=life-1
                lead_x=400
                lead_y=400
                time.sleep(1)
                pygame.mixer.Sound.play(life_sound)
                continue

        #Replayability after death 
        while gameover== True:
                gameDisplay.fill(black)
                mouse_x,mouse_y=pygame.mouse.get_pos()
                global white,bge,red,yellow
                gameDisplay.blit(bge,(0,0))
                screen_text=font.render("GAMEOVER",True,red)
                gameDisplay.blit(screen_text,[350,0])
                #screen_text =font.render("Press 'q' to exit the game  or 'c' to play again",True,white)
                #gameDisplay.blit(screen_text,[0,display_height/6])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=300 and mouse_y<=360):
                    pygame.draw.rect(gameDisplay,yellow,[300,300,220,60])
                    screen_text=font.render("PLAYAGAIN",True,red)
                else:
                    pygame.draw.rect(gameDisplay,(0,0,255),[300,300,220,60])
                    screen_text=font.render("PLAYAGAIN",True,(0,255,255))
                gameDisplay.blit(screen_text,[310,300])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                    pygame.draw.rect(gameDisplay,yellow,[300,200,220,60])
                    screen_text=font.render("MAINMENU",True,red)
                else:
                    pygame.draw.rect(gameDisplay,(0,0,255),[300,200,220,60])
                    screen_text=font.render("MAINMENU",True,(0,255,255))
                gameDisplay.blit(screen_text,[310,200])
                if not(mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460):
                    pygame.draw.rect(gameDisplay,yellow,[305,400,200,60])
                    screen_text=font.render("QUIT",True,red)
                else:
                    pygame.draw.rect(gameDisplay,(0,0,255),[305,400,200,60])
                    screen_text=font.render("QUIT",True,(0,255,255))
                gameDisplay.blit(screen_text,[350,400])
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

        #Drawing the level
        #level()
        #level2()
        levels()

        #Displaying the score
        font1=pygame.font.SysFont(None,100)
        screen_text =font.render("Score "+str(score),True,black)
        gameDisplay.blit(screen_text,[0,0])
        screen_text=font.render("Life "+str(life),True,black)
        gameDisplay.blit(screen_text,[540,0])
        for i in range(2):
            if tc[i]>0 and tc[i]<500:
                screen_text=font.render("Time "+str(tc[i]),True,black)
                gameDisplay.blit(screen_text,[(i+1)*200,0])

        #Changing the ball position for the next loop
        lead_x += lead_x_change
        lead_y += lead_y_change

        #Updating the display
        pygame.display.update()

        #Controlling the Frames per second (FPS) //60 For Now
        clock.tick(2*fps)
    
    #Ending Pygame

    pygame.quit()
    quit()

#Calling the Function which runs all the Code for the game
gameloop()
#Things to be done
#        First Priority
# Reflection Sounds
# Choice of level in main menu
#        Second Priority
# Fireball powerup from top?
# Fast Ball Brick Image
# level 1 slight redesign
# the time counter overlaps with life counter
# Modes (Reflection/no side reflection) implementation
# Exploding brick
# Time Reset Function
