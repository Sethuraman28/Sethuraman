def rand():
	import random
	n=int(input("\nEnter the maximum number till which you want the random number:"))
	a=random.randint(0,n)
	print("The random number is ",a)
	rand()
rand()