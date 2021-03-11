import random
import tkinter as tk

def roll():
    lbl_result['text'] = str(random.randint(1,6))

window = tk.Tk()
window.title("Roll the Die!")
window.columnconfigure(0, minsize = 150)
window.rowconfigure([0, 1], minsize = 50)

btn_roll = tk.Button(text = 'Roll', command = roll, bg = 'lightgreen')
lbl_result = tk.Label(bg = 'green')

btn_roll.grid(row = 0, column = 0, sticky = 'nsew')
lbl_result.grid(row = 1, column = 0)

window.mainloop()