from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

master = tk.Tk()
master.geometry('500x200')
def func():
    messagebox.showinfo('Hello enthusiast', 'Click on the tabs to view the content')

button1 = Button(master, text='Click me for next step', background='red',
                     fg='#000000', command=func)
button1.pack()
tc = ttk.Notebook(master)
t1 = ttk.Frame(tc)
t2 = ttk.Frame(tc)
tc.add(t1, text='Notebook 1')
tc.add(t2, text='Notebook 2')
tc.pack(expand=1, fill='both')
ttk.Label(t1, text='Hello Educba Technology Institute').grid(column=3, row=3)
ttk.Label(t2, text='Notebook widget demonstration').grid(column=3, row=3)
master.mainloop()