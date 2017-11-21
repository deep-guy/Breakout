#BREAKOUT (BRICK BREAKER)

            #Importing modules
import pygame
import time
import random
import math

            #Initializing pygame
pygame.init()

            #Colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)

            #Resoultion
display_width=800
display_height=600

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
lead_x_change=5
lead_y_change=-5

            #Change in position of bar
leadbar_x_change=0

            #Frame rate
fps=30

            #Score
score=0

            #Unknown Variable
z=500
timetoggle=False


        #Graphics Loading
            #Image Loading
bg= pygame.image.load("sk.png")
bg= pygame.transform.scale(bg,(display_width,display_height))
brick= pygame.image.load("brick.png")
brickgreen=pygame.image.load("gb1.jpg")

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
	if l[i]:
		pygame.draw.rect(gameDisplay,red,[blx,bly,bls,block_size])
		global brick
		brick=pygame.transform.scale(brick,(bls,block_size))
		gameDisplay.blit(brick,(blx,bly))

'''
def timeblock(blx,bly,bls,l,i):
    if (lead_x>blx and lead_x<blx+bls and lead_y+block_size>bly and lead_y<bly+block_size and l[i]==1):
        l[i]=0
        global lead_y_change
        global lead_x_change
        lead_y_change=-lead_y_change
        if lead_x_change<0:
            lead_x_change=-5/2
        else:
            lead_x_change=5/2
        if lead_y_change<0:
            lead_y_change=-5/2
        else:
            lead_y_change=5/2                    
    if l[i]:
            pygame.draw.rect(gameDisplay,green,[blx,bly,bls,block_size])
	    global brickgreen
	    brickgreen=pygame.transform.scale(brickgreen,(bls,block_size))
	    gameDisplay.blit(brickgreen,(blx,bly))
            timetoggle=False
'''
            #List declaration for each row of Bricks
l=[]
l1=[]
l2=[]
l3=[]


            #List initialization for each row of Bricks
'''
for i in range(16):
    l.append(1)
    l1.append(1)
    l2.append(1)
    l3.append(1)
'''

            #Broken Time Block List
l4=[1,1,1,1,1]
l5=[1,1,1,1,1]

            #Level Creation Function 
def level():
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

            #Broken Time Block functions
	 #timeblock(200,100+20,50,l4,1)
         #timeblock(400,100+100,50,l5,3)

            #Game Loop Function
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

            #Unknown Variables
        global z
        '''
	l=[]
	l1=[]
	l2=[]
	l3=[]
        '''
            #List for Row of Brick creation Intialization
	for i in range(16):
	    l.append(1)
	    l1.append(1)
	    l2.append(1)
	    l3.append(1)
            #Broken Time loop list , I think
	l4=[1,1,1,1,1]
	l5=[1,1,1,1,1]

        #Main Game Loop

	while not gameexit:

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
			else:
				lead_y_change=-lead_y_change
		if lead_x>=lead_x_bar+bar_size/3 and lead_x<(lead_x_bar+(bar_size*2)/3) and lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar:
                	lead_y_change=-lead_y_change
		if lead_x>=lead_x_bar+(bar_size*2)/3 and lead_x<=(lead_x_bar+bar_size) and lead_y>=(lead_y_bar-block_size) and lead_y<=lead_y_bar:
                	if(lead_x_change<0):
				lead_y_change=-lead_y_change
				lead_x_change=-lead_x_change
			else:
				lead_y_change=-lead_y_change

                #Reflection of ball at the edge of the screen
        	if lead_x+block_size>=display_width or lead_x<=0 :
			lead_x_change=-lead_x_change
		if lead_y<=0:
			lead_y_change=-lead_y_change	

                #Game over when ball goes down under the screen and the bar misses
        	if lead_y>display_height:
			message_to_screen("game over",red)
			pygame.display.update()
			time.sleep(2)
			gameover=True
		while gameover== True:
			gameDisplay.fill(black)
			global white
			screen_text =font.render("Press 'q' to exit the game  or 'c' to play again",True,white)
        		gameDisplay.blit(screen_text,[0,display_height/6])
			pygame.display.update()
			for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                                gameexit=True
                                                gameover=False
                                        if event.key == pygame.K_c:
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
        	
                #Broken Time Brick Code
                if z>0 and l[15]==0:
            		z-=1
        	if z==0:
            		if lead_x_change<0:
                		lead_x_change=-5
            		else:
               			lead_x_change=5
            	if lead_y_change<0:
                	lead_y_change=-5
           	else:
                	lead_y_change=5

                #Drawing the ball
        	pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])

                #Drawing the level
		level()

                #Displaying the score
		font1=pygame.font.SysFont(None,100)
		screen_text =font.render("score"+str(score),True,black)
        	gameDisplay.blit(screen_text,[0,0])

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
