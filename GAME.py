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
whoosh_sound = pygame.mixer.Sound("whoosh.ogg")
win_sound = pygame.mixer.Sound("win.ogg")
lose_sound = pygame.mixer.Sound("gameover.ogg")
speed_sound = pygame.mixer.Sound("speedup.ogg")
blast_sound = pygame.mixer.Sound("Explosion.ogg")
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
quit3 = False
quit4=False
quit5=False

            #Blast Time Animation Variables
blasttime1=0
blasttime2=0
blasttime21=0

        #Graphics Loading
            #Image Loading
bg= pygame.image.load("background2.png")
bg= pygame.transform.scale(bg,(display_width,display_height))
brick= pygame.image.load("brick.png")
brickgreen=pygame.image.load("gb1.jpg")
bge= pygame.image.load("background3.jpg")
bge= pygame.transform.scale(bge,(display_width,display_height))
iceball=pygame.image.load("iceball.jpg")
iceball=pygame.transform.scale(iceball,(10,10))
blast=pygame.image.load("blast.png")
pause=pygame.image.load("pause.png")
pause=pygame.transform.scale(pause,(30,30))
pause1=pygame.image.load("pause1.png")
pause1=pygame.transform.scale(pause1,(30,30))
helping=pygame.image.load("Help.jpg")
helping=pygame.transform.scale(helping,(display_width,display_height))

            #Video Loading
text=[]
for x in range(1,18):
    b="text/text"+str(x)+".png"
    b1=pygame.image.load(b)
    text.append(b1)
frames=[]
for x in range(253,501):
    b="frames/scene00"+str(x)+".png"
    b1=pygame.image.load(b)
    b1=pygame.transform.scale(b1,(200,200))
    frames.append(b1)
frames1=[]
for x in range(181,501):
    b="frames2/scene00"+str(x)+".png"
    b1=pygame.image.load(b)
    b1=pygame.transform.scale(b1,(200,200))
    frames1.append(b1)
button=pygame.image.load("button.png")
button=pygame.transform.scale(button,(250,60))
button1=pygame.image.load("button1.png")
button1=pygame.transform.scale(button1,(250,60))
bomb=pygame.image.load("bomb.jpg")
blackbrick=pygame.image.load("blackbrick.png")
iceblock=pygame.image.load("iceblock.jpg")


            #Font Loading
font=pygame.font.SysFont(None,50)


            #Message to Screen at Game Initialization -  Function
def message_to_screen(msg,color):
    screen_text =font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2-50,display_height/2-20])

            #Clock Initialization
clock=pygame.time.Clock()


            #Brick Creation Function
def block(blx,bly,bls,l,i):
    if (lead_x>blx and lead_x<blx+bls and lead_y+block_size>bly and lead_y<bly+block_size and l[i]==1):
        l[i]=0
        global lead_y_change,score
        lead_y_change=-lead_y_change
        score +=1
        pygame.mixer.Sound.play(hit_sound)
    if l[i]:
        pygame.draw.rect(gameDisplay,red,[blx,bly,bls,block_size])
        global brick
        brick=pygame.transform.scale(brick,(bls,block_size))
        gameDisplay.blit(brick,(blx,bly))

            #Time Block creation function
def timeblock(blx,bly,bls,l,i):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and tb[i]==1):
        tb[i]=0
        global lead_y_change,score,tc
        lead_y_change=-lead_y_change
        tc[i]-=1
        score +=2
        pygame.mixer.Sound.play(ice_sound)
    if tb[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(iceblock,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))

            #Fast Block creation function
def fastblock(blx,bly,bls,fb,i):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and fb[i]==1):
        fb[i]=0
        global lead_y_change,score,tc
        lead_y_change=-lead_y_change
        hit_sound = pygame.mixer.Sound.play(speed_sound)
        fc[i]-=1
        score +=2
    if fb[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(blackbrick,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))


            #Exploding block creation function
def ExplodingBlock1(blx,bly,bls,bb1,i):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and bb1[i]==1):
        bb1[i]=0
        global lead_y_change,score,blasttime1,blasttime2
        lead_y_change=-lead_y_change
        score +=2
        if i==0:
            global l,l1,l2
            l[13]=0
            l[14]=0
            l[12]=0
            l1[12]=0
            l1[14]=0
            l1[13]=0
            l2[13]=0
            l2[14]=0
            l2[13]=0
            blasttime1=15
            pygame.mixer.Sound.play(blast_sound)
        if i==1:
            global l1,l2,l3
            l1[4]=0
            l1[3]=0
            l1[5]=0
            l2[4]=0
            l2[3]=0
            l2[5]=0
            l3[3]=0
            l3[4]=0
            l3[5]=0
            blasttime2=15
            pygame.mixer.Sound.play(blast_sound)

    if bb1[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(bomb,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))


            #Exploding Block creation function
def ExplodingBlock2(blx,bly,bls,bb2,i):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and bb2[i]==1):
        bb2[i]=0
        global lead_y_change,score,blasttime21
        lead_y_change=-lead_y_change
        score +=2
        if i==0:
            global l,l1,l2
            l22[1]=0
            l22[2]=0
            l22[3]=0
            l23[2]=0
            l23[3]=0
            l24[3]=0
            pygame.mixer.Sound.play(blast_sound) 
        if i==1:
            global l1,l2,l3
            l24[6]=0
            l24[7]=0
            l24[8]=0
            l25[5]=0
            l25[9]=0
            l25[6]=0
            l25[7]=0
            l25[8]=0
            l26[6]=0
            l26[7]=0
            l26[8]=0
            l27[7]=0
            l27[8]=0
            blasttime21=15
            pygame.mixer.Sound.play(blast_sound) 

    if bb2[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(bomb,(bls,block_size))
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

bb1=[]
bb2=[]

        #List initialization for bricks
            #Normal Bricks
for i in range(15):
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
for i in range(9):
    l27.append(1)

for i in range(2):
    fb.append(1)
    fc.append(500)
    bb1.append(1)
    bb2.append(1)

        #Level Creation Function
            #Level 1 Design
def level():
    global lead_x_change,lead_y_change,speedtoggle
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

    if bb1[0]:
        ExplodingBlock1(13*50,100+30,100,bb1,0)
    if bb1[1]:
        ExplodingBlock1(4*50,100+100,100,bb1,1)
    if tb[0]==1:
        timeblock(40,100+30,100,tb,0)
    if tb[1]==1:
        timeblock(500,165,100,tb,1)

    speedtoggle=0
    speedcontrol(speedtoggle)
    #gameo()

            #Level 2 Design
def level2():
    global lead_x_change,lead_y_change,fspeedtoggle
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
        fastblock(280,200,100,fb,1)

    bb2[0]=1
    if bb2[1]==1:
        ExplodingBlock2(350,150,100,bb2,1)
    fspeedtoggle=0
    fspeedcontrol(fspeedtoggle)
    #gameo()


        #Speed Control Function - Slow block
def speedcontrol(speedtoggle):
    global lead_x_change,lead_y_change,lead_x,lead_y

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

            #Speed control function - Fast Block
def fspeedcontrol(speedtoggle):
    global lead_x_change,lead_y_change
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

            #Brick Restart Function
def brickrestart():
    global l,l1,l2,l3,lead_x,lead_y,life,lead_x_change,lead_y_change
    for i in range(15):
        l[i]=1
        l1[i]=1
        l2[i]=1
        l3[i]=1
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
        fc[i]=500
        bb1[i]=1
        bb2[i]=1
        tb[i]=1
        tc[i]=500

    lead_x=200
    lead_y=400
    lead_x_bar=400-bar_size/2
    lead_x_change=4
    lead_y_change=-4
    life=2

            #Level control variable
levels=level

            #Game Over Checking Function
def gameo():
    global l,l1,l2,l3,tb,l21,l22,l23,l24,l25,l26,l27,fb,bb1,bb2
    def check(q):
        for x in range(len(q)):
            if(q[x]!=0):
                return 1
        return 0
    if(((check(l)+check(l1)+check(l2)+check(l3)+check(tb)+check(bb1))==0) or (check(l21)+check(l22)+check(l23)+check(l24)+check(l25)+check(l26)+check(l27)+check(fb)+check(bb2))==0):
                #global bge
                gameDisplay.blit(bge,(0,0))
                message_to_screen("Congrats! You Won",red)
                screen_text=font.render("Score: "+str(score),True,black)
                gameDisplay.blit(screen_text,(500,500))
                pygame.display.update()
                pygame.mixer.Sound.play(win_sound)
                time.sleep(5)
                return True
    return False


# Implementing mode 1 and mode 2 in game:-
mode = 2


            #Main Loop Calling Function
def gameloop():
       
#Game Ending control Variables
    gameexit=False
    gameover=False

    #Referencing global scope variables

#Ball 
    global lead_x
    global lead_y
    lead_x=display_width/2
    lead_y=display_height/2

#Bar
    global lead_x_bar
    global lead_y_bar
    lead_x_bar=display_width/2

#Block Size 
    global block_size
    block_size=10

#Ball Change 
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

#Life Scoping
    global life
    life=2

#Mouse Variables
    global z

#Level Initialization
    brickrestart()

#Quit control variables
    global bge
    quit1=False
    global play
    global quit1,quit4,quit5

#Mode level Screen
    def modes():
            global quit5 
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

#Pause level screen
    def pausef():
            global quit4
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
                            mainmenu()   
                        if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                            global quit4    
                            quit4=True

#Difficulty level screen 
    def difficultyselect():
        global quit3
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
                            modes()
                        if mouse_x>=300 and mouse_x<=520 and mouse_y>=400 and mouse_y<=460:
                            global bar_size,quit3
                            bar_size=50
                            quit3=True
                            modes()
                        if (mouse_x>=300 and mouse_x<=520 and mouse_y>=200 and mouse_y<=260):
                            global bar_size,quit3
                            bar_size=150
                            quit3=True
                            modes()
    
#Level Select screen
    def levelselect():
        global quit2
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
                        levels=level
                        global quit2
                        quit2=True
                    if mouse_x>=300 and mouse_x<=550 and mouse_y>=400 and mouse_y<=460:
                        levels=level2
                        global levels
                        levelsa=2
                        global quit2
                        quit2=True
        difficultyselect()

#Main Game Loop
    def mainmenu():
        global quit1,helping
        while not quit1:
            gameDisplay.fill(black)
            mouse_x,mouse_y=pygame.mouse.get_pos()
            global white,bge,red,yellow,button,button1
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
                        brickrestart()
                        score=0
                        global play
                        play=True
                        global quit1
                        quit1=True
                        levelselect()
                    elif mouse_x>=300 and mouse_x<=550 and mouse_y>=400 and mouse_y<=460:
                        gameexit=True     
                        gameover=False
                        global quit1
                        quit1=True
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


#Main Menu Screen
    if(play==False):
        global quit1,quit2,quit3,quit4
        quit1=False
        quit2=False
        quit3=False
        quit4=False
        quit5=False
        mainmenu()
            
#Main Game 
    while (not gameexit) and play:
        mouse_x,mouse_y=pygame.mouse.get_pos()
        global quit4
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
                        pausef()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        global quit4
                        quit4=False
                        pausef()
                        
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
        levels()
        gameover=gameo()

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
#Things to be done
#        First Priority
#  Help Screen
