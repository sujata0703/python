from tkinter import *
#creating new window
mw = Tk()
def click():
    label1=Label(mw,text="I love python",font=('Arial',20))
    label1.pack(pady=10)
b1=Button(mw,text="clickme",command=click)
b1.pack()

a1=Entry(mw)
a1.pack()

mw.mainloop()

