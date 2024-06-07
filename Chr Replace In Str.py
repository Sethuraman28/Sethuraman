str=input("Enter a string:")
a=int(input("If the string you entered is okay press 1 or if you want to change any character press 0:"))
if a==0:
	x=input("Enter the character you want to change:")
	y=input("Enter new character:")
	print(str.replace(x,y))
else:
	print(str)