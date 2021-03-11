from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *
root = Tk()
root.geometry('250x150')
label_frame = LabelFrame(root, text = 'Label Frame')
label_frame.pack(expand = 'yes', fill = 'both')
#Buttons
btn1 = Button(label_frame, text = 'Button 1')
btn1.place(x = 30, y = 10)
btn2 = Button(label_frame, text = 'Button 2')
btn2.place(x = 130, y = 10)
#Checkbuttons
chkbtn1 = Checkbutton(label_frame, text = 'Checkbutton 1')
chkbtn1.place(x = 30, y = 50)
chkbtn2 = Checkbutton(label_frame, text = 'Checkbutton 2')
chkbtn2.place(x = 30, y = 80)

root.mainloop()