import turtle, random, time

wn = turtle.Screen()
wn.title('YoGGaJi')
knuTur = turtle.Turtle()
knuTur1 = turtle.Turtle()
knuTur2 = turtle.Turtle()
knuTur3 = turtle.Turtle()

knuTur.shape('turtle')
knuTur1.shape('turtle')
knuTur2.shape('turtle')
knuTur3.shape('turtle')

knuTur.color('green')

knuTur.forward(3)
knuTur2.forward(50)
knuTur3.forward(100)

knuTur.penup()

for i in range(-100,100):
    dist=random.randint(-20,20)
    gakdo=random.randint(-90,90)
    knuTur.forward(dist)
    time.sleep(0.1)
#knuTur.backward(100) #forward(-100)과 같은 의미
    knuTur.right(gakdo)
    time.sleep(0.1)
#knuTur.right(-180)

wn.mainloop()
