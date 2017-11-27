import time
from LOADING import *
from SPEED import *
from BRICKS import *

            #Message to Screen at Game Initialization -  Function
def message_to_screen(msg,color):
    screen_text =font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2-50,display_height/2-20])

        #Level Creation Function
            #Level 1 Design
def level(v):
        #Row creation for normal bricks
    lead_x,lead_y,score,block_size,lead_x_change,lead_y_change,speedtoggle,l,l1,l2,l3,bb1,tb,tc,blasttime1,blasttime2=v
    for i in range(15):
        if l[i]==1:
            lead_x,lead_y,score,lead_y_change,l=block(i*50,100,50,l,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(15):
        if l1[i]==1:
            lead_x,lead_y,score,lead_y_change,l1=block(i*50,100+40,50,l1,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(15):
        if l2[i]==1:
            lead_x,lead_y,score,lead_y_change,l2=block(i*50,100+80,50,l2,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(15):
        if l3[i]==1:
            lead_x,lead_y,score,lead_y_change,l3=block(i*50,100+120,50,l3,i,lead_x,lead_y,block_size,score,lead_y_change)

    if bb1[0]:
        lead_x,lead_y,score,lead_y_change,bb1,l,l1,l2,l3,blasttime1,blasttime2=ExplodingBlock1(13*50,100+30,100,bb1,0,lead_x,lead_y,block_size,score,lead_y_change,l,l1,l2,l3,blasttime1,blasttime2)
    if bb1[1]:
        lead_x,lead_y,score,lead_y_change,bb1,l,l1,l2,l3,blasttime1,blasttime2=ExplodingBlock1(4*50,100+100,100,bb1,1,lead_x,lead_y,block_size,score,lead_y_change,l,l1,l2,l3,blasttime1,blasttime2)
    if tb[0]==1:
        lead_x,lead_y,score,lead_y_change,tb,tc=timeblock(40,100+30,100,tb,tc,0,lead_x,lead_y,block_size,score,lead_y_change)
    if tb[1]==1:
        lead_x,lead_y,score,lead_y_change,tb,tc=timeblock(500,165,100,tb,tc,1,lead_x,lead_y,block_size,score,lead_y_change)

    speedtoggle=0
    tc,lead_x_change,lead_y_change=speedcontrol(speedtoggle,tc,lead_x_change,lead_y_change,lead_x,lead_y)
    return [lead_x,lead_y,lead_x_change,lead_y_change,l,l1,l2,l3,bb1,tb,tc,blasttime1,blasttime2,score]

            #Level 2 Design
def level2(v):
    lead_x,lead_y,score,block_size,lead_x_change,lead_y_change,fspeedtoggle,l21,l22,l23,l24,l25,l26,l27,bb2,fb,fc,blasttime21=v
    for i in range(15):
        if i>0:
            if l21[i]==1:
                lead_x,lead_y,score,lead_y_change,l21=block(i*50,100,50,l21,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(14):
        if i>1:
            if l22[i]==1:
                lead_x,lead_y,score,lead_y_change,l22=block(i*50,110,50,l22,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(13):
        if i>2:
            if l23[i]==1:
                lead_x,lead_y,score,lead_y_change,l23=block(i*50,120,50,l23,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(12):
        if i>3:
            if l24[i]==1:
                lead_x,lead_y,score,lead_y_change,l24=block(i*50,130,50,l24,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(11):
        if i>4:
            if l25[i]==1:
                lead_x,lead_y,score,lead_y_change,l25=block(i*50,140,50,l25,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(10):
        if i>5:
            if l26[i]==1:
                lead_x,lead_y,score,lead_y_change,l26=block(i*50,150,50,l26,i,lead_x,lead_y,block_size,score,lead_y_change)
    for i in range(9):
        if i>6:
            if l27[i]==1:
                lead_x,lead_y,score,lead_y_change,l27=block(i*50,160,50,l27,i,lead_x,lead_y,block_size,score,lead_y_change)
    if fb[0]==1:
        lead_x,lead_y,score,lead_y_change,fb,fc=fastblock(40,40,100,fb,fc,0,lead_x,lead_y,block_size,score,lead_y_change)
    if fb[1]==1:
        lead_x,lead_y,score,lead_y_change,fb,fc=fastblock(280,200,100,fb,fc,1,lead_x,lead_y,block_size,score,lead_y_change)

    bb2[0]=1
    if bb2[1]==1:
        lead_x,lead_y,score,lead_y_change,bb2,l22,l23,l24,l25,l26,l27,blasttime21=ExplodingBlock2(350,150,100,bb2,1,lead_x,lead_y,block_size,score,lead_y_change,l22,l23,l24,l25,l26,l27,blasttime21)
    fspeedtoggle=0
    tc,lead_x_change,lead_y_change=fspeedcontrol(fspeedtoggle,fc,lead_x_change,lead_y_change)
    return [lead_x,lead_y,lead_x_change,lead_y_change,l21,l22,l23,l24,l25,l26,l27,bb2,fb,fc,blasttime21,score]


            #Game Over Checking Function
def gameo(l,l1,l2,l3,l21,l22,l23,l24,l25,l26,l27,tb,fb,bb1,bb2,score):
    def check(q):
        for x in range(len(q)):
            if(q[x]!=0):
                return 1
        return 0
    if(((check(l)+check(l1)+check(l2)+check(l3)+check(tb)+check(bb1))==0) or (check(l21)+check(l22)+check(l23)+check(l24)+check(l25)+check(l26)+check(l27)+check(fb)+check(bb2))==0):
                gameDisplay.blit(bge,(0,0))
                message_to_screen("Congrats! You Won",red)
                screen_text=font.render("Score: "+str(score),True,black)
                gameDisplay.blit(screen_text,(500,500))
                pygame.display.update()
                pygame.mixer.Sound.play(win_sound)
                time.sleep(5)
                return True
    return False
