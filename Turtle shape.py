import turtle as t
t.speed(13)
t.bgcolor("black")
t.color("cyan")
t.hideturtle()
t.penup()
t.goto(0,-1200)
t.pendown()
def c1():
    t.begin_fill()
    i=0
    while i<=5:
        t.circle(100,-180)
        t.circle(-100,-180)
        i+=1
    t.end_fill()
c1()
def c2():
    t.begin_fill()
    i=0
    while i<=6:
        t.circle(-100,-180)
        t.circle(100,-180)
        i+=1
    t.end_fill()
c2()
def t1():
    t.color("red")
    t.begin_fill()
    t.penup()
    t.goto(-400,0)
    t.pendown()
    for i in range(3):
        t.fd(100)
        t.lt(120)
    t.end_fill()
t1()
def t2():
    t.color("red")
    t.begin_fill()
    t.penup()
    t.goto(300,0)
    t.pendown()
    for i in range(3):
        t.fd(100)
        t.lt(120)
    t.end_fill()
t2()
def s1():
    for x in [800,-800]:
        t.penup()
        t.goto(-400,x)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.color("yellow")
            t.fd(100)
            t.rt(90)
        t.end_fill()
s1()
def s2():
    for x in [800,-800]:
        t.penup()
        t.goto(300,x)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.color("yellow")
            t.fd(100)
            t.rt(90)
        t.end_fill()
s2()
def trev1():
    t.color("red")
    t.begin_fill()
    t.penup()
    t.goto(-400,0)
    t.pendown()
    for i in range(3):
        t.fd(100)
        t.rt(120)
    t.end_fill()
trev1()
def trev2():
    t.color("red")
    t.begin_fill()
    t.penup()
    t.goto(300,0)
    t.pendown()
    for i in range(3):
        t.fd(100)
        t.rt(120)
    t.end_fill()
trev2()
t.done()