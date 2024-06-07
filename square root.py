def sqrt():
	import math
	a=float(input("\nEnter a number to find its square root:"))
	b=math.sqrt(a)
	print("The square root of entered number is ",b)
	sqrt()
sqrt()