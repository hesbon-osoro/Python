import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Tab Widget')
tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Tab 1')
tabcontrol.add(tab2,text='Tab 2')
tabcontrol.pack(expand=1, fill='both')
ttk.Label(tab1, text='Welcome to GeeksForGeeks'
          ).grid(column=0, row=0, padx=30, pady=30)
ttk.Label(tab2, text='Lets dive into the world of computers'
          ).grid(column=0, row=0, padx=30, pady=30)
root.mainloop()