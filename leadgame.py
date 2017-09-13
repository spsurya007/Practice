"""
def leadgame():
    p1=0
    p2=0
    lead=0
    maxlead=0
    lp=0
    winner=0
    x = int(input("enter the no of games"))
    while(x):
        a, b = [input("enter").split()]
        p1=p1+a
        p2=p2+b
        lead=p1-p2
        lp=1
        x=x-1
        if(lead<0):
            lead=p2-p1
            lp=2
        elif (lead>maxlead):
            maxlead=lead
            winner=lp
    print(winner,maxlead)
leadgame()"""
t = int(input())
i = 0
player_1 = []
player_2 = []
difference = []
sump1 = 0
sump2 = 0
while i < t:
    play1, play2 = map(int, input().split())
    player_1.append(play1)
    player_2.append(play2)
    sump1 = sum(player_1)
    sump2 = sum(player_2)
    difference.append(sump1 - sump2)
    i = i + 1
val = max(difference, key=abs)
if val > 0:
    print("1 " + str(abs(val)))
else:
    print("2 " + str(abs(val)))
