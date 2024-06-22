x=int(input("Enter the number:"))
class odev:
	def check(self,num):
		if num%2==0:
			if num>0:
				print(num,"is positive even")
			else:
				print(num,"is negative even")
		else:
			if num>0:
				print(num,"is positive odd")
			else:
				print(num,"is negative odd")
n=odev()
n.check(x)