from LOADING import *
        #Speed Control Function - Slow block
def speedcontrol(speedtoggle,tc,lead_x_change,lead_y_change,lead_x,lead_y):
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
    return [tc,lead_x_change,lead_y_change]

            #Speed control function - Fast Block
def fspeedcontrol(speedtoggle,fc,lead_x_change,lead_y_change):
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
    return [fc,lead_x_change,lead_y_change]
