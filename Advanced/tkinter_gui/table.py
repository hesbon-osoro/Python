from tkinter import *
class Table:
     def __init__(self, root):
         #code for creating table
         for i in range(total_rows):
             for j in range(total_columns):
                 self.e = Entry(root, width=10, fg='yellow', bg='teal',
                                font=('Consolas', 16, 'bold'))
                 self.e.grid(row=i, column=j)
                 self.e.insert(END, lst[i][j])

# take the data
lst = [(1, 'Wazimu', 'Juja', 21),
       (2, 'Namaiyian', 'Nairobi', 21),
       (3, 'Juliet', 'Nairobi', 24),
       (4, 'Grace', 'Westie', 21),
       (5, 'Sharon', 'Kilgoris', 22)]

#find total number of rows and columns in list
total_rows = len(lst)
total_columns = len(lst[0])

#create root window
root = Tk()
root.title('Table')
t = Table(root)
root.mainloop()
