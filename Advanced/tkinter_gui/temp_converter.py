import tkinter as tk

def fahrenheit_to_celcius():
    """Convert the value for Fahrenheit to Celsius and insert the
        result into lbl_result.
        """
    fahrenheit = ent_temperature.get()
    celcius = (5/9)*(float(fahrenheit)-32)
    lbl_result['text'] = f"{round(celcius, 2)} \N{DEGREE CELSIUS}"

#Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

#Create the Fahrenheit entry frame with an Entry widget and label in it
frame_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frame_entry, width = 10)
lbl_temp = tk.Label(master=frame_entry, text = "\N{DEGREE FAHRENHEIT}")

#Layout the temperature Entry and Label in frame_entry
#using the .grip() geometry manager
ent_temperature.grid(row = 0, column = 0, sticky = 'e')
lbl_temp. grid(row = 0, column = 1, sticky = 'w')

#Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    # text="\N{BLACK RIGHTWARDS ARROW}",
    text = u"\u27A1",
    command = fahrenheit_to_celcius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

#Set-up the layout using the .grid() geometry manager
frame_entry.grid(row = 0, column = 0, padx = 10)
btn_convert.grid(row = 0, column = 1, pady = 10)
lbl_result.grid(row = 0, column = 2, padx = 10)

#Run the application
window.mainloop()