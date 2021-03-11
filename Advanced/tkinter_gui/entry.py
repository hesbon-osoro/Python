from tkinter import *
top = Tk()
label1 = Label(top, text = "Username")
label1.pack(side = LEFT)
entry1 = Entry(top, bd = 5)
entry1.pack(side = RIGHT)

# label12 = Label(top, text = "Password")
# label12.pack(side = LEFT)
# entry2 = Entry(top, show = "*", bd = 2)
# entry2.pack(side = RIGHT)
top.mainloop()