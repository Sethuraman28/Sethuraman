import math as m
def area():
	print("\nEnter the number of shape for which you wanna calculate the area")
	shape=int(input("1. Triangle\n2. Square\n3. Circle\n4. Rectangle\n5. Rhombus\n6. Parallelogram\n"))
	
	
	if shape==1:
		def tri():
			print("\nAREA OF TRIANGLE CALCULATOR")
			base=float(input("Enter base value:"))
			ht=float(input("Enter height value:"))
			area=(base*ht)/2
			print("The area of triangle is ",area," units")
		tri()
		while True:
			n=int(input("\nIf you wanna do the calculation again press 0 or if you wanna return to menu press 1:"))
			if n==0:
				tri()
			else:
				area()
	
	
	elif shape==2:
		def sq():
			print("\nAREA OF SQUARE CALCULATOR")
			a=float(input("Enter side length:"))
			area=a*a
			print("The area of square is ",area," units")	
		sq()
		while True:
			n=int(input("\nIf you wanna do the calculation again press 0 or if you wanna return to menu press 1:"))
			if n==0:    
				sq()
			else:
				area()
	elif shape==3:
		def cir():
			print("\nAREA OF CIRCLE CALCULATOR")
			r=float(input("Enter the radius value:"))
			area=m.pi*r*r
			print("The area of the circle is ",area,"units")
		cir()		
		while True:
			n=int(input("\nIf you wanna do the calculation again press 0 or if you wanna return to menu press 1:"))
			if n==0:
				cir()
			else:
				area()
	
	elif shape==4:
		def rec():
			print("\nAREA OF RECTANGLE CALCULATOR")
			l=float(input("Enter the length value:"))
			b=float(input("Enter the breadth value:"))
			area=l*b
			print("The area of the rectangle is ", area," units")	
		rec()	
		while True:
			n=int(input("\nIf you wanna do the calculation again press 0 or if you wanna return to menu press 1:"))
			if n==0:
				rec()
			else:
				area()
	
	elif shape==5:
		def rhom():
			print("\nAREA OF RHOMBUS CALCULATOR")
			p=float(input("Enter value of one diagonal:"))
			q=float(input("Enter value of another diagonal:"))
			area=(p*q)/2
			print("The area of rhombus is ",area," units")
		rhom()
		while True:
			n=int(input("\nIf you wanna do the calculation again press 0 or if you wanna return to menu press 1:"))
			if n==0:
				rhom()
			else:
				area()
	
	
	elif shape==6:
		def para():
			print("\nAREA OF PARALLELOGRAM CALCULATOR")
			b=float(input("Enter base length:"))
			h=float(input("Enter height value:"))
			area=b*h
			print("The area of parallelogram is ",area,"units")
		para()
		while True:
			n=int(input("\nIf you wanna do the calculation again press 0 or if you wanna return to menu press 1:"))
			if n==0:
				para()
			else:
				area()
	else:
		print("Enter a valid input!!")
		area()
area()
	
	