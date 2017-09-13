class Initials:
  def getInitials(self,name):
    if name=='':
      return  ''
    if name==' ':
      return ''
    name=' '+name
    ret=''
    flag=0
    for s in name:
      if flag==1:
        ret+=s
        flag=0
      if s==' ':
        flag=1
    return ret
ob=Initials()
m=ob.getInitials("s u r y a")
print(m)