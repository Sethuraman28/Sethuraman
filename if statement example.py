def vote():
    age=int(input("Enter your age:"))
    if age>0 & age<18:
        print("You are a minor")
        vote()
    elif age<0:
        print("Enter valid number")
        vote()
    elif age<65:
        print("You are an adult")
        vote()
    elif age>=65:
        print("You are a senior")
        vote()
vote()