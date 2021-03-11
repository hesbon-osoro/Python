import tkinter
top =  tkinter.Tk()
can = tkinter.Canvas(top, bg = 'teal', height = 250, width = 300)
coord = 10, 50, 240, 210
arc = can.create_arc(coord, start = 0, extent = 150, fill= 'yellow')
can.pack()
top.mainloop()