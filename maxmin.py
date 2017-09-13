import random

import simplegui


cmpscore=0
humanscore=0
humanchoice=""
cmpchoice=""
def cn(c):
    return{'rock':0,'paper':1,'scissor':2}[c]
def nc(n):
    rps_dict={0:'rock',1:'paper',2:'scissor'}
    return rps_dict[n]
def ran():
    return random.c(['rock','paper', 'scissor'])
def choiceresult(humanchoice,cmpchoice):
    global cmpscore
    global humanscore
    hn=cn(humanchoice)
    cn=cn(cmpchoice)
    if(hn-cn)%3==1:
        cmpscore=cmpscore+1
    elif hn==cn:
        print("tie")
    else:
        humanscore=humanscore+1