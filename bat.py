import random as r
n=int(input("Enter the score till you wanna play:"))
i=0
while i<n:
    if i>=0:
        a=r.randint(1,10)
        b=int(input("Enter:"))
        print(a,b)
        if b!=a:
            i+=b
        elif b==a:
            print(f"You got out at {i}!")
            break
print("YAY!!! You have won the game!!!")
