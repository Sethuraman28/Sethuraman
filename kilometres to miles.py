print("-------------------------KILOMETER TO MILES------------------------")
def kilo_mile():
	kilometers = float(input("\nEnter value in kilometers: "))
	conv_fac = 0.621371
	miles = kilometers * conv_fac
	print('{0} kilometers is equal to {1} miles' .format(kilometers,miles))
	kilo_mile()
kilo_mile()
   