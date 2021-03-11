from tkinter import *
from tkinter import ttk
root = Tk()
pw = PanedWindow(orient='vertical')
# pw = PanedWindow(orient='horizontal')
top = ttk.Button(pw, text="Click Me !\nI'm a Button")
top.pack(side=TOP)
pw.add(top)
bot = Checkbutton(pw, text='Choose Me !')
bot.pack(side=TOP)
pw.add(bot)
label = Label(pw, text="I'm a Label")
label.pack(side=TOP)
pw.add(label)
string = StringVar()
entry = Entry(pw, textvariable=string, font=('arial', 15, 'bold'))
entry.pack()
# Focus force is used to focus on particular
# widget that means widget is already selected for operations
entry.focus_force()
pw.add(entry)

# expand is used so that widgets can expand
# fill is used to let widgets adjust itself
# according to the size of main window
pw.pack(fill=BOTH, expand=True)

# This method is used to show sash
pw.configure(sashrelief=RAISED)

# Infinite loop can be destroyed by
# keyboard or mouse interrupt
mainloop()