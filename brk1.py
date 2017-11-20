import pygame
import time
import random
pygame.init()
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Breakout")
bar_length=50
bar_breadth=10
block_size=10
font=pygame.font.SysFont(None, 25)
white=(255,255,255)
black=(0,0,0)
green=(0,155,0)
red=(255,0,0)
fps=30
def message_to_screen(msg,color):
	screen_text=font.render(msg,True,color)
	gameDisplay.blit(screen_text,[display_width/2,display_height/2])
clock=pygame.time.Clock()
message_to_screen("Welcome to Breakout",green)
pygame.display.update()
time.sleep(2)
def gameloop():

	gameexit1=False
	gameover=False
	lead_x_bar=display_width/2 - bar_length/2
        lead_y_bar=display_height - bar_breadth
	lead_x=display_width/2 - block_size/2
	lead_y=display_height-block_size-bar_breadth
	block_y_change=-10
	block_x_change=-10
	while not gameexit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameexit1==True
		if(lead_x==0 or lead_x==display_width):
			block_x_change=-block_x_change
		if(lead_y==0 ):
			block_y_change=-block_y_change
		if(lead_y==display_height):
			gameexit1=True
		lead_x +=block_x_change
		lead_y +=block_y_change
		gameDisplay.fill(black)
		pygame.draw.rect(gameDisplay,red,[lead_x_bar,lead_y_bar,bar_length,bar_breadth])
		pygame.draw.rect(gameDisplay,green,[lead_x,lead_y,block_size,block_size])
		pygame.display.update()
		clock.tick(fps)
	pygame.quit()
	quit()
		
	
gameloop()
