print("------------------------MULTIPLICATION TABLE-----------------------")
def multip_table():
	n=int(input("\nDisplay multiplication table of which number:"))
	print("Here is the multiplication table of {}..............".format(n))
	for num in range(0,21):
		print(n,"x",num,"=",n*num)
	multip_table()
multip_table()