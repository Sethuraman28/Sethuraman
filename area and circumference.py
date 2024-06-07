import math 
print("Welcome!!!")
pi=math.pi
def area_cir():
	def circle(r):
		return(pi*r*r,2*pi*r)
	radius=float(input("\nEnter the radius:"))
	(area,cir)=circle(radius)
	print("The area is ",area)
	print("The circumference is ",cir)
	area_cir()
area_cir()