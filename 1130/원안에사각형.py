import turtle

wn = turtle.Screen()
wn.title('Na turtle')
wn.setup(500,500) #창 크기
t1 = turtle.Turtle()

t1.circle(100)
t1.goto(100,100)
t1.goto(0,200)
t1.goto(-100,100)
t1.goto(0,0)

wn.mainloop()
