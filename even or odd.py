def even_odd():
	x=int(input("\nEnter a number:"))
	if x%2==0:
		print(x,"is even!!!")
	else:
		print(x,"is odd!!!")
	even_odd()
even_odd()