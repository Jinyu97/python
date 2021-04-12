from tkinter import *

wn=Tk()
b1=Button(wn,text=' Up ')
b2=Button(wn,text='Left')
b3=Button(wn,text='Right')
b4=Button(wn,text='Down')

b1.grid(row=0,column=0, columnspan=2)
b2.grid(row=1,column=0)
b3.grid(row=1,column=1)
b4.grid(row=2,column=0, columnspan=2)

wn.mainloop()