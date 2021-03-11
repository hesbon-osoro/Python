# Import only those methods
# which are mentioned below, this way of
# importing methods is efficient
from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *

# Creating tkinter window with fixed geometry
root = Tk()
root.geometry('250x150')
# This will create a LabelFrame
label_frame = LabelFrame(root, text = "This is a Label Frame")
label_frame.pack(expand = 'yes', fill = 'both')

label1 = Label(label_frame, text = '1. This is a Label.')
label1.place(x = 0, y = 5)
label2 = Label(label_frame, text = '2. This is another Label')
label2.place(x = 0, y = 35)
label3 = Label(label_frame, text = '3.We can add multiple widgets in it')
label3.place(x = 0, y = 65)
# This creates an infinite loop which generally
# waits for any interrupt (like keyboard or
# mouse) to terminate
mainloop()