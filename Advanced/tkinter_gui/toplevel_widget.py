from tkinter import *
root = Tk()
root.geometry('200x300')
root.title('Main')

label = Label(root, text='This is root window')

top = Toplevel()
top.geometry('180x100')
top.title('Toplevel')

label2 = Label(top, text='This is toplevel window')

label.pack()
label2.pack()

top.mainloop()