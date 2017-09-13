"""N=int(input())
mod=10**9+7
for i in range(N):
    n=int(input())
    a=[int(i) for i in input().split()]
    sum=0
    for k in range(n):
        for l in range(k+1,n+1):
            if k>0:
                sum+=(a[k]*a[l]*(2**k)*(2**(n-l)))
            else:
                sum += (a[k] * a[l] * (2) * (2 ** (n - l)))

    sum=sum%mod
    print(sum)"""

m = 10**9 + 7
for i in range(int(input().strip())):
	input()
	a = list(map(int, input().strip().split()))
	s,x,p = 0,a[0],1
	for i in range(1,len(a)):
		s = (2*(s + x*a[i]))
		x += (p*a[i])
		p = (p*2)
	print(s%m)