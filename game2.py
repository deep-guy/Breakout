import pygame
import time
import random
import math
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
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
font=pygame.font.SysFont(None,50)
def message_to_screen(msg,color):
        screen_text =font.render(msg,True,color)
        gameDisplay.blit(screen_text,[display_width/2,display_height/2])
clock=pygame.time.Clock()
#starting screen
message_to_screen("breakout",red)
pygame.display.update()
time.sleep(2)
tt=0
def block(blx,bly,bls,l):
	global tt
	if (lead_x>blx and lead_x<blx+bls and lead_y>bly and lead_y<bly+block_size and tt==0):
		l[0]=0
		tt=tt+1
		global lead_y_change
		lead_y_change=-lead_y_change
	if l[0]:
		pygame.draw.rect(gameDisplay,red,[blx,bly,bls,block_size])
	

l=[1]
l=[(200,200)]	

while not gameexit:
	z1=0
	z2=0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameexit=True
                if event.type ==pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				leadbar_x_change=-5
				z1=1
			if event.key == pygame.K_RIGHT:
				leadbar_x_change=5
				z2=1
		if event.type ==pygame.KEYUP:
			leadbar_x_change=0
                    
        #deviding bar in 3 parts                        
        if lead_x>=lead_x_bar and lead_x<=(lead_x_bar+bar_size/3) and lead_y==(lead_y_bar-block_size):
		if(lead_x_change>0):
			lead_y_change=-lead_y_change
			lead_x_change=-lead_x_change
		else:
			lead_y_change=-lead_y_change
	if lead_x>lead_x_bar+bar_size/3 and lead_x<=(lead_x_bar+(bar_size*2)/3) and lead_y==(lead_y_bar-block_size):
                lead_y_change=-lead_y_change
	if lead_x>=lead_x_bar+(bar_size*2)/3 and lead_x<=(lead_x_bar+bar_size) and lead_y==(lead_y_bar-block_size):
                if(lead_x_change<0):
			lead_y_change=-lead_y_change
			lead_x_change=-lead_x_change
		else:
			lead_y_change=-lead_y_change
#change in postion of ball
        if lead_x==display_width or lead_x==0 :
		lead_x_change=-lead_x_change
	if lead_y==0:
		lead_y_change=-lead_y_change	
#game over when ball goes down
        if lead_y>=display_height:
		message_to_screen("game over",red)
		pygame.display.update()
		time.sleep(2)
		gameexit=True      
#checking bar edge	
	if(lead_x_bar<=display_width-bar_size and lead_x_bar>-1):
		lead_x_bar +=leadbar_x_change
	#else:
	if(lead_x_bar<=0):
		lead_x_bar=0
	if(lead_x_bar>=display_width-bar_size):
		lead_x_bar=display_width-bar_size

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay,red,[lead_x_bar,lead_y_bar,bar_size,block_size])
	block(150,100,50,l)
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])

        pygame.display.update()
        clock.tick(2*fps)
pygame.quit()
quit()

