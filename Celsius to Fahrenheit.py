print("------------------------CELSIUS TO FAHRENHEIT----------------------")
def cel_fah():
	celsius = float(input("\nEnter the celsius value:"))
	fahrenheit = (celsius * 1.8) + 32
	print("{0} degree Celsius is equal to {1} degree Fahrenheit".format(celsius,fahrenheit))
	cel_fah()
cel_fah()