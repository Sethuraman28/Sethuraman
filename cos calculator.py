def cos():
	import math
	print("\t\t\tCOSINE CALCULATOR")
	a=float(input("\nEnter the number(in radians):"))
	print("The cos value of entered number is ",math.cos(a))
cos()
n=int(input("If you want do want to return to menu press 1 or if you want to carry out the same operation press0"))
if n=1:
	sci_cal()
elif n=0:
	cos()
else:
	print("Enter a valid number!!")
	n=int(input("If you want do want to return to menu press 1 or if you want to carry out the same operation press0"))