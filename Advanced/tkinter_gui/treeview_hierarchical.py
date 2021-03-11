# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter

# Importing tkinter
from tkinter import *

#Importing ttk from tkinter
from tkinter import ttk

#Creating app window
app = Tk()

#Defining title of the app
app.title('GUI Application of Python')
# Defining label of the app and calling a geometry
# management method i.e, pack in order to organize
# widgets in form of blocks before locating them
# in the parent widget
ttk.Label(app, text='Treeview(hierarchical)').pack()

#Creating treeview window
treeview = ttk.Treeview(app)
#calling pack method on the treeview
treeview.pack()

# Inserting items to the treeview
# Inserting parent
treeview.insert('', '0', 'item1', text='GeeksForGeeks')
#inserting child
treeview.insert('', '1', 'item2', text='Computer Science')
treeview.insert('', '2', 'item3', text='Programming Languages')
treeview.insert('', 'end', 'item4', text='Python Programming')

#Inserting more than one attribute of an item
treeview.insert('item2', 'end', 'Algorithm', text='Algorithm')
treeview.insert('item2', 'end', 'Data Structures', text='Data Structures')

treeview.insert('item3', 'end', 'Python', text='Python')
treeview.insert('item3', 'end', 'Java', text='Java')
treeview.insert('item3', 'end', 'Go', text='Go')
treeview.insert('item3', 'end', 'Android', text='Android')
treeview.insert('item3', 'end', 'Swift', text='Swift')

treeview.insert('item4', 'end', 'paradigms', text='Multiple Programming Paradigms')
treeview.insert('item4', 'end', 'web', text='Web Testing')
treeview.insert('item4', 'end', 'mine', text='Data Extraction.')
treeview.insert('item4', 'end', 'ai', text='Artificial Intelligence')
treeview.insert('item4', 'end', 'ds', text='Data Science')
treeview.insert('item4', 'end', 'db', text='Database Easy Access')
treeview.insert('item4', 'end', 'sec', text='Cybersecurity')

#Placing each child items in parent widget
'''Comment the section below and observe the behavior'''
treeview.move('item2', 'item1', 'end')
treeview.move('item3', 'item1', 'end')
treeview.move('item4', 'item1', 'end')

app.mainloop()