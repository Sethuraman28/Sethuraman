print("------------------------MULTIPLICATION TABLE-----------------------")
def multip_table():
	n=int(input("\nDisplay multiplication table of which number(Enter 0 to exit):"))
	if n==000:
		exit()
	print("Here is the multiplication table of {}..............".format(n))
	for num in range(1,21):
		print(n,"x","{:02d}".format(num),"=",n*num)
	multip_table()
multip_table()