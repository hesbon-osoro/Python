import  tkinter as tk
window = tk.Tk()
window.title("Button Click Event")

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text = 'Click me !')
button.pack()
button.bind("<Button-1>", handle_click)
#"Button-1" left mouse button click
#"Button-2" middle mouse button click
#"Button-3" right mouse button click

window.mainloop()