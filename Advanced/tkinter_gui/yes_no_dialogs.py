from tkinter import messagebox
answer = messagebox.askokcancel('Question', "Do you want to open this file")
answer = messagebox.askretrycancel('Question', 'Do you want to try that again?')
answer = messagebox.askyesno('Question', 'Do you like Python?')
answer = messagebox.askyesnocancel('Question', 'Continue playing?')