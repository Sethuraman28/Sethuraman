def tan():
	import math
	print("\t\t\t  TAN CALCULATOR")
	a=float(input("\nEnter the number(in radians):"))
	print("The tangent value of entered number is ",math.tan(a))
tan()
n=int(input("If you want do want to return to menu press 1 or if you want to carry out the same operation press0"))
if n=1:
	sci_cal()
elif n=0:
	tan()
else:
	print("Enter a valid number!!")
	n=int(input("If you want do want to return to menu press 1 or if you want to carry out the same operation press0"))