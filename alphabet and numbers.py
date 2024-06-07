a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=[i for i in range(1,27) ]
a==b
while True:
    n=int(input("\nEnter the number:"))
    if n in b:
       print("The corressponding alphabet of the number ",n," is ",a[n-1])
    else:
       print("Enter valid number!")
       
       
  