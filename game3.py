import pygame
import time
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
green=(0,155,0)
red=(255,0,0)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("slither")
block_size=10
fps=30
font=pygame.font.SysFont(None,25)
def message_to_screen(msg,color):
        screen_text =font.render(msg,True,color)
        gameDisplay.blit(screen_text,[display_width/2,display_height/2])
clock=pygame.time.Clock()
def gameloop():
        gameexit=False
        gameover=False
        lead_x=display_width/2
        lead_y=display_height/2
        lead_x_change=0
        lead_y_change=0
	apple_x=round(random.randrange(0,display_width-block_size)/10.0)*10.0
	apple_y=round(random.randrange(0,display_width-block_size)/10.0)*10.0
        while not gameexit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameexit=True
                        if event.type ==pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        lead_x_change =-block_size
                                        lead_y_change=0
                                if event.key == pygame.K_RIGHT:
                                        lead_x_change =block_size
                                        lead_y_change=0
                                if event.key ==pygame.K_UP:
                                        lead_y_change=-block_size
                                        lead_x_change=0
                                if event.key ==pygame.K_DOWN:
                                        lead_y_change=block_size
                                        lead_x_change=0

                if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y <=0:
                    gameover=True
                lead_x += lead_x_change
                lead_y += lead_y_change
                gameDisplay.fill(white)
                pygame.draw.rect(gameDisplay,green,[apple_x,apple_y,block_size,block_size])
		pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])
		if(lead_x==apple_x and lead_y==apple_y):
			apple_x=round(random.randrange(0,display_width-block_size)/10.0)*10.0
		        apple_y=round(random.randrange(0,display_width-block_size)/10.0)*10.0

                pygame.display.update()
                clock.tick(fps)
        	while gameover==True:
                	gameDisplay.fill(black)
                	message_to_screen("gameover,press c to play again or q to exit",white)
                	pygame.display.update()
                	for event in pygame.event.get():
                        	if event.type == pygame.KEYDOWN:
                                	if event.key == pygame.K_q:
                                        	gameexit=True
                                        	gameover=False
                                	if event.key == pygame.K_c:
                                        	gameloop()

        pygame.quit()
        quit()
if __name__=='__main__':
	gameloop()
           
