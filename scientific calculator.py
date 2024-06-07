print("------------------WELCOME TO SCIENTIFIC CALCULATOR-----------------")
print("\t\t      CREATED BY SETHURAMAN.M")
def sci_cal():
	s=input("1.   sin()\n2.   cos()\n3.   tan()\n4.   Convert radian to degree\n5.   Convert degree to radian\n6.   Ceil\n7.   Floor\n8.   log()\n9.   Greatest common divisor(GCD) of two numbers\n10.  Absolute value of a number\n11.  Factorial of a number\n12.  Square root of a number\n13.  Square of a number\n14.  x to the power y(x^y)\n\nEnter valid number:")

	if s=='1':
		def sin():
			import math
			print("\t\t\tSINE CALCULATOR")
			a=float(input("\nEnter the number:"))
			print("The sine value of entered number is ",math.sin(math.radians(a)))
		sin()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			sin()
		
				
	elif s=='2':
			def cos():
				import math
				print("\t\t\tCOSINE CALCULATOR")
				a=float(input("\nEnter the number:"))
				print("The cos value of entered number is ",math.cos(math.radians(a)))
			cos()
			n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
			if n=='1':
				sci_cal()
			else:
				cos()
			
			
	elif s=='3':
			def tan():
				import math
				print("\t\t\t  TAN CALCULATOR")
				a=float(input("\nEnter the number:"))
				print("The tangent value of entered number is ",math.tan(math.radians(a)))
			tan()
			n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
			if n=='1':
				sci_cal()
			else :
				tan()
				
				
	elif s=='4':
			def rad_deg():
				import math
				print("\t\t  CONVERTION OF RADIAN TO DEGREE")
				a=float(input(("\nEnter radian value:")))
				print(math.degrees(a))
			rad_deg()
			n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
			if n=='1':
				sci_cal()
			else:
				rad_dag()
				
				
	elif s=='5':
			def deg_rad():
				import math
				print("\t\t  CONVERTION OF DEGREE TO RADIAN")
				a=float(input(("\nEnter degree value:")))
				print(math.radians(a))
			deg_rad()
			n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
			if n=='1':
				sci_cal()
			else:
				deg_rad()
				
				
	elif s=='6':
		def ceil():
			import math
			print("\t\t\tCEIL CALCULATOR")
			a=float(input("Enter a number:"))
			print("The ceil of the entered number is ",math.ceil(a))
		ceil()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			ceil()
			
	elif s=='7':
		def floor():
			import math
			print("\t\t\tFLOOR CALCULATOR")
			a=float(input("Enter a number:"))
			print("The floor of the entered number is ",math.floor(a))
		floor()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			floor()
			
	elif s=='8':
			def log():
				import math
				print("\t\t\tLOGARITHM CALCULATOR")
				a=float(input("\nEnter a number to calculate its log value:"))
				print("The log value of the entered value is ",math.log10(a))
			log()
			n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
			if n=='1':
				sci_cal()
			else:
				log()
	
	elif s=='9':
		def gcd():
			import math
			print("\t\tGCD CALCULATOR")
			a=int(input("Enter a number:"))
			b=int(input("Enter another number:"))
			print("The GCD of the entered numbers is ",math.gcd(a,b))
		gcd()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			gcd()
			
	elif s=='10':
		def abs():
			import math
			print("\t\t    ABSOLUTE VALUE CALCULATOR")
			a=float(input("\nEnter a number to find its absolute value:"))
			print("The absolute value of the entered number is ",math.fabs(a))
		abs()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			abs()	
			
			
	elif s=='11':
		def fact():
			import math
			print("\t\t     FACTORIAL CALCULATOR")
			a=int(input("\nEnter a number to find its factorial:"))
			b=math.factorial(a)
			print("The factorial of the entered number is ",b)
		fact()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			fact()
			
	elif s=='12':
		def sqrt():
			import math
			print("\t\t\tSQUARE ROOT CALCULATOR")
			a=float(input("\nEnter a number to find its square root:"))
			b=math.sqrt(a)
			print("The square root of entered number is ",b)
		sqrt()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else:
			sqrt()
			
	elif s=='13':
	    def sq():
	        n=int(input("Enter a number to find its square:"))
	        a=n*n
	        print("The square of entered number is ",a)
	    sq()
	    n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
	    if n=='1':
	        sci_cal()
	    else :
	        sq()

	elif s=='14':
		def pow():
			import math
			print("\t\tPOWER CALCULATOR")
			a=int(input("Enter base number:"))
			b=int(input("Enter exponent:"))
			print("The value of {} to the power {} is {}".format(a,b,a**b))
		pow()
		n=input("\nIf you want to return to menu press 1 or if you want to carry out the same operation press any key:")
		if n=='1':
			sci_cal()
		else :
			pow()
			
	else:
		print("ENTER A VALID NUMBER!!!")
		sci_cal()
			
		
sci_cal()