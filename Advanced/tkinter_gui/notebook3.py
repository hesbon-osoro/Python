import tkinter as tk
from tkinter import ttk
root = tk.Tk()
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='ws')
notebook = ttk.Notebook(root, style='lefttab.TNotebook')
frame1 = tk.Frame(notebook, bg='red', width=200, height=200)
frame2 = tk.Frame(notebook, bg='blue', width=200, height=200)
notebook.add(frame1, text='Frame 1')
notebook.add(frame2, text='Frame 2')
notebook.pack()
root.mainloop()