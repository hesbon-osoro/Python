import tkinter as tk
from tkinter.colorchooser import askcolor

def callback():
    result = askcolor(color='#6A9662', title="Bernd's Colour Chooser")

root = tk.Tk()
tk.Button(
    root,
    text='Choose Color',
    fg='darkgreen',
    command=callback
).pack(side=tk.LEFT, padx=10)
tk.Button(text='Quit',
          command=root.quit,
          fg='red').pack(side=tk.LEFT, padx=10)
tk.mainloop()