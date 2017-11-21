import pygame
import time
import random
import math
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
#resoultion
display_width=800
display_height=600
#defining display
gameDisplay=pygame.display.set_mode((display_width,display_height))
# set caption
pygame.display.set_caption("BREAKOUT")
gameexit=False
#position of ball
lead_x=display_width/2
lead_y=display_height/2
#position of bar
lead_x_bar=display_width/2
#size of ball
block_size=10
lead_y_bar=display_height-block_size
#chage in position in ball
lead_x_change=5
lead_y_change=-5
#change in position in bar
leadbar_x_change=0
#farame rate
fps=30
#bar size
bar_size=150
score=0
bg= pygame.image.load("sk.png")
bg= pygame.transform.scale(bg,(display_width,display_height))
brick= pygame.image.load("brick.png")
brickgreen=pygame.image.load("gb1.jpg")
font=pygame.font.SysFont(None,50)
def message_to_screen(msg,color):
        screen_text =font.render(msg,True,color)
        gameDisplay.blit(screen_text,[display_width/2-50,display_height/2-20])
clock=pygame.time.Clock()
#starting screen
message_to_screen("Breakout!!",red)
pygame.display.update()
time.sleep(2)
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
z=500

timetoggle=False
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
l=[]
l1=[]
l2=[]
l3=[]
for i in range(16):#need a bvariable for number of blocks

    l.append(1)
    l1.append(1)
    l2.append(1)
    l3.append(1)
#print l
l4=[1,1,1,1,1]
l5=[1,1,1,1,1]
def level():
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
	 #timeblock(100,100+20,50,l4,0)
	 timeblock(200,100+20,50,l4,1)
         #timeblock(300,100+20,50,l4,2)
         #timeblock(400,100+20,50,l4,3)
         #timeblock(500,100+20,50,l4,4)
         #timeblock(100,100+100,50,l5,0)
         #timeblock(200,100+100,50,l5,1)
         #timeblock(300,100+100,50,l5,2)
         timeblock(400,100+100,50,l5,3)
         #timeblock(500,100+100,50,l5,4)

def gameloop():
	gameexit=False
	gameover=False

        global lead_x
        global lead_y
        lead_x=display_width/2
        lead_y=display_height/2
        global lead_x_bar
        lead_x_bar=display_width/2
        global block_size
        block_size=10
        global lead_y_bar
#        lead_y_bar=display_height-block_size
        global lead_x_change
        global lead_y_change
#        lead_x_change=5
#        lead_y_change=-5
        global leadbar_x_change
        leadbar_x_change=0
        global fps
#        fps=30
        global bar_size
#        bar_size=150
        global score
        global z
#        z=500
	global l
	global l1,l2,l3,l4,l5
	l=[]
	l1=[]
	l2=[]
	l3=[]
	for i in range(16):#need a bvariable for number of blocks
	    l.append(1)
	    l1.append(1)
	    l2.append(1)
	    l3.append(1)
	#print l
	l4=[1,1,1,1,1]
	l5=[1,1,1,1,1]


	while not gameexit:
		z1=0
		z2=0
		'''
		global lead_x
		global lead_y
#		lead_x=display_width/2
#		lead_y=display_height/2
		global lead_x_bar
#		lead_x_bar=display_width/2
		global block_size
#		block_size=10
		global lead_y_bar
#		lead_y_bar=display_height-block_size
		global lead_x_change
		global lead_y_change
#		lead_x_change=5
#		lead_y_change=-5
		global leadbar_x_change
#		lead_x_change=0
		global fps
#		fps=30
		global bar_size
#		bar_size=150
		global score
		global z
		'''
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
                    
        #dividing bar in 3 parts                        
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
#change in postion of ball
        	if lead_x+block_size>=display_width or lead_x<=0 :
			lead_x_change=-lead_x_change
		if lead_y<=0:
			lead_y_change=-lead_y_change	
#game over when ball goes down
        	if lead_y>display_height:
			message_to_screen("game over",red)
			pygame.display.update()
			time.sleep(2)
			gameover=True
		while gameover== True:
			gameDisplay.fill(black)
			global white
			screen_text =font.render("press q to x exit or c to play again",True,white)
        		gameDisplay.blit(screen_text,[display_width/2-400,display_height/2-20])
			pygame.display.update()
			for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                                gameexit=True
                                                gameover=False
                                        if event.key == pygame.K_c:
                                                gameloop()
  
			    
#checking bar edge	
		if(lead_x_bar<=display_width-bar_size and lead_x_bar>-1):
			lead_x_bar +=leadbar_x_change
	#else:
		if(lead_x_bar<=0):
			lead_x_bar=0
		if(lead_x_bar>=display_width-bar_size):
			lead_x_bar=display_width-bar_size
        	gameDisplay.fill(white)
		gameDisplay.blit(bg,(0,0))
		pygame.draw.rect(gameDisplay,red,[lead_x_bar,lead_y_bar,bar_size,block_size])
	#block(150,100,50,l)
#        for i in range(15):
#            if l[i]==1:
#                block(i*50,100,50,l,i)
#        if l[15]==1:
#            timeblock(250,150,250,l,15)
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

        	pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
		level()
		font1=pygame.font.SysFont(None,100)
		screen_text =font.render("score"+str(score),True,black)
        	gameDisplay.blit(screen_text,[0,0])
        	lead_x += lead_x_change
        	lead_y += lead_y_change
        	pygame.display.update()
        	clock.tick(2*fps)
	pygame.quit()
	quit()
gameloop()
