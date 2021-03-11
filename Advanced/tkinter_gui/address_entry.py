import tkinter as tk

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

#Create a new 'frame_form' to contain the Label and Entry
# widgets for entering address information.
frame_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg='teal')

#pack the frame into the window
frame_form.pack()

#create the Label and Entry widgets for "First Name"
lbl_first_name = tk.Label(master=frame_form, text = 'First Name:')
ent_first_name = tk.Entry(master=frame_form, width = 50)

#use the grid geometry manager to place the Label and
# Entry widgets in the first and second columns of the first row of the grid
lbl_first_name.grid(row = 0, column = 0, sticky = 'e')
ent_first_name.grid(row = 0, column = 1)

#Create the Label and Entry widgets for 'Last Name
lbl_last_name = tk.Label(master=frame_form, text = 'Last Name:')
ent_last_name = tk.Entry(master=frame_form, width = 50)

#Place the widgets in the second row of the grid
lbl_last_name.grid(row = 1, column = 0, sticky = 'e')
ent_last_name.grid(row = 1, column = 1)

#Create the Label and Entry widgets for 'Address Line 1'
lbl_address1 = tk.Label(master=frame_form, text = 'Address Line 1:')
ent_address1 = tk.Entry(master=frame_form, width = 50)

#Place the widgets in the third row of the grid
lbl_address1.grid(row = 2, column = 0, sticky = 'e')
ent_address1.grid(row = 2, column = 1)

#Create the Label and Entry widgets for 'Address Line 2'
lbl_address2 = tk.Label(master=frame_form, text = 'Address Line 2:')
ent_address2 = tk.Entry(master=frame_form, width = 50)

#Place the widgets in the fourth row of the grid
lbl_address2.grid(row = 3, column = 0, sticky = tk.E)
ent_address2.grid(row = 3, column = 1)

#Create the Label and Entry widgets for 'City'
lbl_city = tk.Label(master=frame_form, text = 'City:')
ent_city = tk.Entry(master=frame_form, width = 50)

#Place the widgets inn the fifth row of the grid
lbl_city.grid(row = 4, column = 0, sticky = tk.E)
ent_city.grid(row = 4, column = 1)

#Create the Label and Entry widgets for 'State/Province'
lbl_state = tk.Label(master=frame_form, text = 'State/Province:')
ent_state = tk.Entry(master=frame_form, width = 50)

#Place the widgets in the sixth row of the grid
lbl_state.grid(row = 5, column = 0, sticky = tk.E)
ent_state.grid(row = 5, column = 1)

#Create the Label and Entry widgets for 'Postal Code'
lbl_postal_code = tk.Label(master=frame_form, text = 'Postal Code:')
ent_postal_code = tk.Entry(master=frame_form, width = 50)

#Place the widgets in the seventh row of the grid
lbl_postal_code.grid(row = 6, column = 0, sticky =tk.E)
ent_postal_code.grid(row = 6, column = 1)

#Create the Label and Entry widgets for 'Country'
lbl_country = tk.Label(master=frame_form, text = 'Country:')
ent_country = tk.Entry(master=frame_form, width = 50)

#Place the widgets in the eighth row of the grid
lbl_country.grid(row = 7, column = 0, sticky = tk.E)
ent_country.grid(row = 7, column = 1)

#Create a new frame 'frame_buttons' to contain the Submit and Clear buttons.
#This frame fills the whole window in the horizontal direction and has
#5 pixels of horizontal and vertical padding
frame_buttons = tk.Frame(bg = 'green')
frame_buttons.pack(fill = tk.X, ipadx = 5, ipady = 5)

#Create the 'Submit button and pack it to the right side of 'frame_buttons'
btn_submit = tk.Button(master=frame_buttons, text = "Submit")
btn_submit.pack(side = tk.RIGHT, padx = 10, ipadx = 10)

#Create the 'Clear' button and pack it to the right side of 'frame_buttons'
btn_clear = tk.Button(master=frame_buttons, text = 'Clear')
btn_clear.pack(side = tk.RIGHT, ipadx = 10)

#Start the application
window.mainloop()