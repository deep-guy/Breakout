from LOADING import *
            #Brick Creation Function
def block(blx,bly,bls,l,i,lead_x,lead_y,block_size,score,lead_y_change):
    global brick
    if (lead_x>blx and lead_x<blx+bls and lead_y+block_size>bly and lead_y<bly+block_size and l[i]==1):
        l[i]=0
        lead_y_change=-lead_y_change
        score +=1
        pygame.mixer.Sound.play(hit_sound)
    if l[i]:
        pygame.draw.rect(gameDisplay,red,[blx,bly,bls,block_size])
        brick=pygame.transform.scale(brick,(bls,block_size))
        gameDisplay.blit(brick,(blx,bly))
    return [lead_x,lead_y,score,lead_y_change,l]

            #Time Block creation function
def timeblock(blx,bly,bls,tb,tc,i,lead_x,lead_y,block_size,score,lead_y_change):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and tb[i]==1):
        tb[i]=0
        lead_y_change=-lead_y_change
        tc[i]-=1
        score +=2
        pygame.mixer.Sound.play(ice_sound)
    if tb[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(iceblock,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))
    return [lead_x,lead_y,score,lead_y_change,tb,tc]

            #Fast Block creation function
def fastblock(blx,bly,bls,fb,fc,i,lead_x,lead_y,block_size,score,lead_y_change):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and fb[i]==1):
        fb[i]=0
        lead_y_change=-lead_y_change
        hit_sound = pygame.mixer.Sound.play(speed_sound)
        fc[i]-=1
        score +=2
    if fb[i]:
        pygame.draw.rect(gameDisplay,blue,[blx,bly,bls,block_size])
        brick1=pygame.transform.scale(blackbrick,(bls,block_size))
        gameDisplay.blit(brick1,(blx,bly))
    return [lead_x,lead_y,score,lead_y_change,fb,fc]


            #Exploding block creation function
def ExplodingBlock1(blx,bly,bls,bb1,i,lead_x,lead_y,block_size,score,lead_y_change,l,l1,l2,l3,blasttime1,blasttime2):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and bb1[i]==1):
        bb1[i]=0
        lead_y_change=-lead_y_change
        score +=2
        if i==0:
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
    return [lead_x,lead_y,score,lead_y_change,bb1,l,l1,l2,l3,blasttime1,blasttime2]

            #Exploding Block creation function
def ExplodingBlock2(blx,bly,bls,bb2,i,lead_x,lead_y,block_size,score,lead_y_change,l22,l23,l24,l25,l26,l27,blasttime21):
    if (lead_x>blx and lead_x<blx + bls and lead_y+block_size>bly and lead_y<bly+block_size and bb2[i]==1):
        bb2[i]=0
        lead_y_change=-lead_y_change
        score +=2
        if i==0:
            l22[1]=0
            l22[2]=0
            l22[3]=0
            l23[2]=0
            l23[3]=0
            l24[3]=0
            pygame.mixer.Sound.play(blast_sound)
        if i==1:
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
    return [lead_x,lead_y,score,lead_y_change,bb2,l22,l23,l24,l25,l26,l27,blasttime21]
