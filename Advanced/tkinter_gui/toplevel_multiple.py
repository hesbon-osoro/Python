from tkinter import *
root = Tk()
root.title('Root Window')
root.geometry('450x300')

label1 = Label(root, text='This is the root Window')

# define a function for 2nd toplevel
# window which is not associated with
# any parent window
def open_Toplevel2():
    top2 = Toplevel()
    top2.title('Toplevel2')
    top2.geometry('200x100')
    label = Label(top2, text='This is a Toplevel2 Window')
    button = Button(top2, text='Exit', command=top2.destroy)
    label.pack()
    button.pack()
    top2.mainloop()
# define a function for 1st toplevel
# which is associated with root window.
def open_Toplevel1():
    top1 = Toplevel(root)
    top1.title('Toplevel1')
    top1.geometry('200x200')
    label = Label(top1, text='This is a Toplevel1 Window')
    button1 = Button(top1, text='Exit', command=top1.destroy)
    button2 = Button(top1, text='open toplevel2', command=open_Toplevel2)
    label.pack()
    button2.pack()
    button1.pack()
    top1.mainloop()

button = Button(root, text='open toplevel1', command=open_Toplevel1)
label1.pack()
button.place(x=155, y=50)
root.mainloop()