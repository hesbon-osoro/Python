from tkinter import *
import tkinter
from tkinter import messagebox
top = tkinter.Tk()
checkVar1 = IntVar()
checkVar2 = IntVar()
box1 = Checkbutton(top, text = "Music", variable = checkVar1, onvalue = 1, \
                   offvalue = 0, height = 5, width = 20)
box2 = Checkbutton(top, text = "Video", variable = checkVar2, onvalue = 1, \
                   offvalue = 0, height = 5, width = 20)
box1.pack()
box2.pack()
top.mainloop()