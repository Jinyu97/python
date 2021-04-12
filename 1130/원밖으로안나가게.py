import turtle
import random

wn = turtle.Screen()
wn.title('Na turtle')
wn.setup(500,500) #창 크기

t1 = turtle.Turtle()

t1.penup()
t1.left(-90)
t1.forward(100)
t1.right(-90)
t1.pendown()
t1.circle(100)
t1.home()

while t1.distance(0,0)<=100:
    x1=random.randint(-50,50)
    x2=random.randint(-90,90)
    t1.right(x2)
    t1.forward(x1)
    if (t1.distance(0,0)>100):
        t1.undo() #바로 이전 행동을 되돌림(앞으로 x1만큼 가는 것)

wn.mainloop()
