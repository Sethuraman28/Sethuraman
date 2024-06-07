import turtle as t
t.hideturtle()
t.speed(0)
t.bgcolor("black")
c=["green","white","orange"]
j=0
for i in (0,100,200):
    t.color(c[j])
    t.begin_fill()
    t.penup()
    t.goto(0,i)
    t.pendown()
    t.fd(300)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(600)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(300)
    t.end_fill()
    j+=1
    
t.color("blue")
t.penup()
t.goto(0,120)
t.pendown()
t.pensize(2)
t.circle(30)
t.lt(90)

t.penup()
t.goto(0,120)
t.pendown()
t.fd(60)

t.penup()
t.lt(90)#turn
t.goto(30,150)
t.pendown()
t.fd(60)

t.penup()
t.rt(45)#turn
t.goto(20,130)
t.pendown()
t.fd(60)

t.penup()
t.rt(90)#turn
t.goto(-20,130)
t.pendown()
t.fd(60)


t.done()