from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *
root = Tk()
root.geometry('250x250')
label_frame = LabelFrame(root, text = 'Please Login')
label_frame.pack(fill = 'both')
username_label = Label(root, text = 'Username:')
user_entry = Entry(root)
username_label.place(x = 10, y = 50)
user_entry.place(x = 80, y = 50)

password_label = Label(root, text = 'Password:')
password_entry = Entry(root, show = '*')
password_label.place(x = 10, y = 70)
password_entry.place(x = 80, y = 70)

login_button = Button(root, text = "LOGIN")
login_button.place(x = 10, y = 100)
root.mainloop()
