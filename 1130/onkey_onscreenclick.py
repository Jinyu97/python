import turtle

wn = turtle.Screen()
wn.title('Na turtle')
wn.setup(500,500) #창 크기

def test():
    t1.forward(100)

t1 = turtle.Turtle()

wn.onkey(test, 'Up') #up 키 누르면 test 함수 돌림
wn.listen()

wn.onscreenclick(t1.goto) #클릭한 위치로 이동

wn.mainloop()
