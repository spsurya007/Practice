s=input().strip()
k=int(input())
def uniq(s,k):
    start,end=0,0
    maxsize,maxstart=1,0
    c=[0]*len(set(s))
    c[ord(s[0])-ord('a')]+=1