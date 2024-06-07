import random as r
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"
d="@#₹&_-*!?:"
A=r.choice(a)
B=r.choice(b)
C=r.choice(c)
D=r.choice(d)
all=A+B+C+D
print("    ",all)