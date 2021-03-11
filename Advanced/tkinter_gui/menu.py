from tkinter import *

#creating tkinter window
root = Tk()

#set geometry
root.geometry('400x400')

#Add title
root.title('Menu Demonstration')

#Creating Menubar
menubar = Menu(root)

#Creating File Menu and Submenus
file = Menu(menubar, tearoff = 0)
'''Comment out tearoffs and note the changes'''
menubar.add_cascade(label='File', menu=file)
file.add_command(label = 'New File')
file.add_command(label = 'Open...')
file.add_command(label = 'Save')

#Adding Edit and SubMenus
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = edit)
edit.add_command(label = 'Cut')
edit.add_command(label = 'Copy')
edit.add_command(label = 'Paste')
edit.add_command(label = 'Select All')

#Adding Help Menu and SubMenus
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = help_)
help_.add_command(label = 'Tk Help')
help_.add_command(label = 'Demo')

#display Menu
root.config(menu = menubar)

#Execute Tkinter
root.mainloop()