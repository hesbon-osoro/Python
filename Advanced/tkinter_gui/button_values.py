import tkinter as tk

#my methods to decrease and increase the value in the label
def increase():
    value = int(lbl_value["text"])
    lbl_value['text'] = f'{value + 1}'
def decrease():
    value = int(lbl_value['text'])
    lbl_value['text'] = f"{value - 1}"

window = tk.Tk()
window.geometry('250x50')
window.title("Button Click Event")

window.rowconfigure(0, minsize = 50, weight = 1)
window.columnconfigure([0, 1, 2], minsize = 50, weight = 1)

btn_decrease = tk.Button(master=window, text = '-', command = decrease, bg = 'red')
btn_decrease.grid(row = 0, column =  0, sticky = 'nsew')

lbl_value = tk.Label(master=window, text = '0', bg = 'gold')
lbl_value.grid(row = 0, column = 1)

btn_increase = tk.Button(master=window, text = '+', command = increase, bg = 'green')
btn_increase.grid(row = 0, column = 2, sticky = 'nsew')


window.mainloop()