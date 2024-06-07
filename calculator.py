print("\t\t\t    CALCULATOR")
def calc():
	x=float(input("\nEnter a value:"))
	y=float(input("Enter another value:"))
	print("What arithmetic operation do you want to carry out with these numbers?\n1.Addition\n2.Subtraction\n3 Multiplication\n4.Division")
	
	def cal():
		z=int(input())
		if z==1:
			print(x+y)
		elif z==2:
			print(x-y)
		elif z==3:
			print(x*y)
		elif z==4:
			print(x/y)
		else:
			print("ENTER A VALID NUMBER!!!\nWhat arithmetic operation do you want to carry out with these numbers?\n1.Addition\n2.Subtraction\n3 Multiplication\n4.Division")
			cal()
	cal()
	calc()
calc()