#Import tkinter package
from tkinter import *
root  =Tk()
#define a labelframe
label_frame = LabelFrame(root, text='Welcome to Python Programming', labelAnchor='center')
label_frame.pack(fill='both', expand='yes')
#define a child frame
left1 = Label(label_frame, text='Python is an easy language')
#to show the content in the window
left1.pack()
root.mainloop()