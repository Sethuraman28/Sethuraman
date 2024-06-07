def name():
	x=input("Enter a name:")
	if x=='sethu':
		for i in range(-1000,1000,1):
			print('hello sethu')
	else:
		print("Enter sethu to see the magic")
		name()
name()