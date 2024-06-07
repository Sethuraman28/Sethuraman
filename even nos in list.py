from random import *
a=[x for x in range(0,10)]
b=[]
i=0
while i<9:
    c=choice(a)
    if c %2==0:
        if c not in b:
            b.append(c)
    else:
        pass
    i+=1
print(b)

