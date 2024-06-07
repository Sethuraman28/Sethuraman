a=[]
print("Welcome!!!\nNow you are going to create a list!")
b=int(input("Enter the starting value of list:"))
c=int(input("Enter the ending value of list(It should be greater than starting value):"))
d=int(input("Enter the interval value:"))
for i in range(b,c,d):
	a.append(i)
print ("Here is your required list -----> ",a)