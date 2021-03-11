import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

#create the root window
root = tk.Tk()
root.title('Tkinter MessageBox')
root.resizable(False, False)
root.geometry('300x150')

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text='Error Message',
    command=lambda: showerror(
        title='Error',
        message='This is an error message.')
).pack(**options)

ttk.Button(
    root,
    text='Information Message',
    command=lambda: showinfo('Information', 'This is an information message')
).pack(**options)

ttk.Button(
    root,
    text='Warning Message',
    command=lambda: showwarning('Warning', 'This is a warning message.')
).pack(**options)

#run the app
root.mainloop()