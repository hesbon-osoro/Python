import tkinter as tk
window = tk.Tk()
window.rowconfigure(0, minsize = 50)
window.columnconfigure([0, 1, 2, 3], minsize = 50)
label1 = tk.Label(text = "1", bg = "teal", fg = "white")
label2 = tk.Label(text = "2", bg = "teal", fg = "white")
label3 = tk.Label(text = "3", bg = "teal", fg = "white")
label4 = tk.Label(text = "4", bg = "teal", fg = "white")
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1, sticky = 'ew') #fill = tk.Y
label3.grid(row = 0, column = 2, sticky = 'ns') #fill = tk.X
label4.grid(row = 0, column = 3, sticky = 'nsew') #fill = tk.BOTH
window.mainloop()

