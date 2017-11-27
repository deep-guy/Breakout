import pygame
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

#Resoultion
display_width=800
display_height=600

        #Loading the sounds
background_music = pygame.mixer.music.load("./Sound/background.mpeg")
hit_sound = pygame.mixer.Sound("./Sound/brick_1.ogg")
bounce_sound = pygame.mixer.Sound("./Sound/hit.ogg")
life_sound = pygame.mixer.Sound("./Sound/life.ogg")
ice_sound = pygame.mixer.Sound("./Sound/ice.ogg")
whoosh_sound = pygame.mixer.Sound("./Sound/whoosh.ogg")
win_sound = pygame.mixer.Sound("./Sound/win.ogg")
lose_sound = pygame.mixer.Sound("./Sound/gameover.ogg")
speed_sound = pygame.mixer.Sound("./Sound/speedup.ogg")
blast_sound = pygame.mixer.Sound("./Sound/Explosion.ogg")
pygame.mixer.music.play(-1)


            #Defining display
gameDisplay=pygame.display.set_mode((display_width,display_height))

            #Set caption
pygame.display.set_caption("BREAKOUT")



        #Graphics Loading
            #Image Loading
bg= pygame.image.load("./Pictures/background2.png")
bg= pygame.transform.scale(bg,(display_width,display_height))
brick= pygame.image.load("./Pictures/brick.png")
brickgreen=pygame.image.load("./Pictures/gb1.jpg")
bge= pygame.image.load("./Pictures/background3.jpg")
bge= pygame.transform.scale(bge,(display_width,display_height))
iceball=pygame.image.load("./Pictures/iceball.jpg")
iceball=pygame.transform.scale(iceball,(10,10))
blast=pygame.image.load("./Pictures/blast.png")
pause=pygame.image.load("./Pictures/pause.png")
pause=pygame.transform.scale(pause,(30,30))
pause1=pygame.image.load("./Pictures/pause1.png")
pause1=pygame.transform.scale(pause1,(30,30))
helping=pygame.image.load("./Pictures/Help.jpg")
helping=pygame.transform.scale(helping,(display_width,display_height))

            #Video Loading
text=[]
for x in range(1,18):
    b="text/text"+str(x)+".png"
    b1=pygame.image.load(b)
    text.append(b1)
frames=[]
for x in range(253,501):
    b="./Pictures/frames/scene00"+str(x)+".png"
    b1=pygame.image.load(b)
    b1=pygame.transform.scale(b1,(200,200))
    frames.append(b1)
frames1=[]
for x in range(181,501):
    b="./Pictures/frames2/scene00"+str(x)+".png"
    b1=pygame.image.load(b)
    b1=pygame.transform.scale(b1,(200,200))
    frames1.append(b1)
button=pygame.image.load("./Pictures/button.png")
button=pygame.transform.scale(button,(250,60))
button1=pygame.image.load("./Pictures/button1.png")
button1=pygame.transform.scale(button1,(250,60))
bomb=pygame.image.load("./Pictures/bomb.jpg")
blackbrick=pygame.image.load("./Pictures/blackbrick.png")
iceblock=pygame.image.load("./Pictures/iceblock.jpg")


            #Font Loading
font=pygame.font.SysFont(None,50)
