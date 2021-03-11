import tkinter as tk

#Create a new window with the title "Address Entry Form"
window =tk.Tk()
window.title("Address Entry Form")

#Create a new frame 'frame_form' to contain the Label and Entry
#widgets for entering address information.
frame_form = tk.Frame(relief = tk.SUNKEN, borderwidth = 3)
#pack the frame into the window
frame_form.pack()

#List of field labels
labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:"
]

#Lopo over the list of field labels
for idx, text in enumerate(labels):
    # Create a Label widget with the text from the labels list
    label = tk.Label(master=frame_form, text = text)
    #Create an Entry widget
    entry = tk.Entry(master=frame_form, width = 50)
    #Use the grid geometry manager to place the Label and
    #Entry widgets in the row whose index is idx
    label.grid(row = idx, column = 0, sticky = 'e')
    entry.grid(row = idx, column = 1)
#Create a new frame 'frame_buttons' to contain the Submit and Clear buttons.
#This frame fills the whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding
frame_buttons = tk.Frame()
frame_buttons.pack(fill = tk.X, ipadx = 5, ipady = 5)

#Create the 'Submit' buttons and pack it to the right side
#of 'frame_buttons'
btn_submit = tk.Button(master=frame_buttons, text = 'Submit')
btn_submit.pack(side=tk.RIGHT, padx = 10, ipadx = 10)

#Cleate the 'Clear' button and pack it to the right side of 'frame_buttons
btn_clear = tk.Button(master=frame_buttons, text = 'Clear')
btn_clear.pack(side = tk.RIGHT, ipadx = 10)

#Start the application
window.mainloop()