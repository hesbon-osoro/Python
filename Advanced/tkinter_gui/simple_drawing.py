from tkinter import *
root = Tk()
c = Canvas(root, bg='yellow', height=250, width=300)
line = c.create_line(108, 120, 320, 40, fill='green')
arc = c.create_arc(180, 150, 80, 210, start=0, extent=220, fill='teal')
oval = c.create_oval(80, 30, 140, 150, fill='magenta')
c.pack()
root.mainloop()