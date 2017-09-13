n=int(input())
for i in range(n):
	x=int(input())
	def f(x):
		if x==1:
			return 1
		else:
			return f(x-1)+f(x-2)
	print(f(x))


"""import math
n=int(input())
for i in range(n):
	x=int(input())
	print(math.factorial(x))"""