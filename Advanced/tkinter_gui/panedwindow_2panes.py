from tkinter import *
from tkinter import ttk
root = Tk()
pw = PanedWindow(orient='vertical')
top = ttk.Button(pw, text="Click Me !\nI'm a Button")
top.pack(side=TOP)
# This will add button widget to the panedwindow
pw.add(top)
#Checkbutton Widget
bot = Checkbutton(pw, text='Choose Me !')
bot.pack(side=TOP)
# This will add Checkbutton to panedwindow
pw.add(bot)
# expand is used so that widgets can expand
# fill is used to let widgets adjust itself
# according to the size of main window
pw.pack(fill=BOTH, expand=True)

# This method is used to show sash
pw.configure(sashrelief=RAISED)
# Infinite loop can be destroyed by
# keyboard or mouse interrupt
mainloop() 
