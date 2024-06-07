def fact():
	import math
	a=int(input("\nEnter a number to find its factorial:"))
	b=math.factorial(a)
	print("The factorial of the entered number is ",b)
	fact()
fact()