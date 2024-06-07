s=[]#list of entered values
x=[]#list of even numbers
for b in range(0,1000000):
    if b%2==0:
        x.append(b)

for i in range(10):
    a=int(input("Enter a number:"))
    s.append(a)

for j in s:
    if j in s and j in x:
        print('The list contains even numbers')
        break
    elif j in s and j not in x:
        print("The list does not contain even numbers")
        break