def cointoss():
	import random
	a=[ ]
	b=int(input("Enter the number of times you want to toss a coin:"))
	for i in range(0,b):
		c=random.randint(0,1)
		if c==0:
			a.append("Heads")
		else:
			a.append("Tails")
	print(a)
	print(a.count("Heads"), "Heads")
	print(a.count("Tails"), "Tails")
cointoss()