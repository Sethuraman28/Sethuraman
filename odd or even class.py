x=int(input("Enter the number:"))
class odev:
	def check(self,num):
		if num%2==0:
			print(num,"is even")
		else:
			print(num,"is odd")
n=odev()
n.check(x)