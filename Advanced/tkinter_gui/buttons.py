import tkinter
# import tkMessageBox
from tkinter import messagebox
top = tkinter.Tk()


def helloCallBack():
     # tkMessageBox.showinfo("Hello Python","Hello World")
     messagebox.showinfo("Hello Python", "Hello World")


button = tkinter.Button(top, text = "Hello", command = helloCallBack())

button.pack()
top.mainloop()