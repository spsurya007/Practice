class ud:
    def maxh(self , n , a , b):
        currenth = 0
        for i in range(n):
            cangoup=(n-(i+1))*b > currenth
            if cangoup:
                currenth += min(a ,(n-(i+1))*b-currenth)
            else:
                break
        return currenth
object=ud()
m=object.maxh(3,7,10)
print(m)