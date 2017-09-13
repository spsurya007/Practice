import string
import random
def rp():
    c=string.ascii_lowercase+string.digits
    return "".join(random.choice(c) for x in range(0,9))
n=int(input())
for i in range(n):
    print(rp())