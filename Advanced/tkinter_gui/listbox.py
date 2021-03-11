from  tkinter import *
top = Tk()
listbox = Listbox(top, height=10, width=15, bg='teal',
                  activestyle='dotbox',
                  font=('Helvetica', 12), fg='yellow')
top.geometry('300x250')
label = Label(top, text='FOOD ITEMS')
#insert elements by their index and names
listbox.insert(1, 'Nachos')
listbox.insert(2, 'Sandwich')
listbox.insert(3, 'Burger')
listbox.insert(4, 'Pizza')
listbox.insert(5, 'Burrito')

label.pack()
listbox.pack()

#Delete items from the list by specifying the index
'''listbox.delete(2)
label.pack()
listbox.pack()'''

top.mainloop()