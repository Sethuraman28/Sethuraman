def posi_nega():
	x=float(input("\nEnter a value:"))
	if x<0:
		print(x,"is negative")
	elif x==0:
		print(x,"is equal to 0")
	else:
		print(x,"is positive")
	posi_nega()
posi_nega()