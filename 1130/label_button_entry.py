from tkinter import *

wn=Tk()
wn.title("Na Tkinter")
#wn.geometry('500x500')

def test():
    l1.configure(text=e1.get()) #l1의 text를 entry에 입력한 글로 바꿈

l1= Label(wn, text='Test ida')
#btn1=Button(wn,text='Okay', command=test)
btn1=Button(wn,text='Okay', command=quit) #창 꺼짐
e1=Entry(wn)
l1.pack()
btn1.pack()
e1.pack()

wn.mainloop()