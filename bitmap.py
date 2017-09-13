class isCarac:                                              #class
    def ispossible():                                       #method signature
        if len(a[0]) // k > 1:
            m = []
            for i in range(len(a)):
                for j in range(0, len(a[0]), k):
                    if len(set(a[i][j:j + k])) == 1:
                        m.append("0")
                    else:
                        m.append("1")
                        break
            if "1" in m:
                return ("Impossible")
            else:
                return ("Possible")
        else:
            return ("Impossible")
"""topcoder format"""

import sys
class image:
    def ispossible(self,image,k):
        n=len(image)
        m=len(image[0])
        for n in range(0,n,k):
            for m in range(0,m,k):
                for i in range(k):
                    for j in range(k):
                        if image[n][m]!=image[n+j][m+i]:
                            return "impossible"
                            sys.exit()
        return "possible"