# Python program to illustrate the usage of
# treeview scrollbars using tkinter
from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title('Treeview Demo')
window.resizable(width=1, height=1)
#using treeview widget
treev = ttk.Treeview(window, selectmode='browse')
#calling pack method w.r.to treeview
treev.pack(side='right')
# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(window, orient='vertical', command=treev.yview)
'''horscrlbar = ttk.Scrollbar(window, orient='horizontal', command=treev.xview)'''
# Calling pack method w.r.to verical
# scrollbar
verscrlbar.pack(side='right', fill='x')
'''horscrlbar.pack(side='left', fill='y')'''
# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)
'''treev.configure(yscrollcommand=horscrlbar.set)'''
# Defining number of columns
treev['columns'] = ['1', '2', '3']

# Defining heading
treev['show'] = 'headings'
# Assigning the width and anchor to  the
# respective columns
treev.column('1', width=90, anchor='c')
treev.column('2', width=90, anchor='se')
treev.column('3', width=90, anchor='se')
# Assigning the heading names to the
# respective columns
treev.heading('1', text='Name')
treev.heading('2', text='Sex')
treev.heading('3', text='Age')

# Inserting the items and their features to the
# columns built
treev.insert('', 'end', text='L1', values=('Wazimu', 'M', 21))
treev.insert('', 'end', text='L2', values=('Grace', 'F', 21))
treev.insert('', 'end', text='L3', values=('Mshamba', 'M', 22))
treev.insert('', 'end', text='L4', values=('John', 'M', 20))
treev.insert('', 'end', text='L5', values=('Ashley', 'F', 20))
treev.insert('', 'end', text='L6', values=('Divinah', 'F', 21))
treev.insert('', 'end', text='L7', values=('Decla', 'F', 20))
treev.insert('', 'end', text='L8', values=('Charles', 'F', 18))
treev.insert('', 'end', text='L9', values=('Duke', 'M', 12))
treev.insert('', 'end', text='L10', values=('Epidius', 'M', 7))
treev.insert('', 'end', text='L11', values=('Levis', 'M', 22))
treev.insert('', 'end', text='L12',  values=('Amira', 'F', 5))
window.mainloop()