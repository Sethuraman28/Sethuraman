try:
	a=10/0
except Exception as b:
	print(b)
else:
	print(a)
finally:
	print("Thank you")
try:
	a=10/5
except Exception as b:
	print(b)
else:
	print(a)
finally:
	print("Thanks")
	