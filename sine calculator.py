def sin():
	import math
	print("\t\t\tSINE CALCULATOR")
	a=float(input("\nEnter the number(in radians):"))
	b=math.radians(a)
	print("The sine value of entered number is ",math.sin(b))
sin()
n=int(input("If you want do want to return to menu press 1 or if you want to carry out the same operation press0"))
if n==1:
	sci_cal()
elif n==0:
	sin()
else:
	print("Enter a valid number!!")
	n=int(input("If you want do want to return to menu press 1 or if you want to carry out the same operation press0"))