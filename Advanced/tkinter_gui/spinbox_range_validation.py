from tkinter import *
#validating function
def validate(user_input):
    from tkinter.messagebox import showerror, showinfo
    if user_input.isdigit():
        #fetching minimum and maximum value of the spinbox
        minval = int(root.nametowidget(spinbox).config('from')[4])
        maxval = int(root.nametowidget(spinbox).config('to')[4])
        #check if the number is within the range
        if int(user_input) not in range(minval, maxval):

            showerror('Out of range')
            return False
        #printing the user input to the console
        showinfo('Message', 'You entered: '+user_input)
        return True
    #if input is blank
    elif user_input is "":
        showinfo('Message', "You didn't input anything")
        return True
    #return false if input is not numeric
    else:
        showerror('Message', 'Not numeric')
        return False
root = Tk()
root.geometry('300x300')
root.title('Spinbox Range Validation')

#creating spinbox
spinbox = Spinbox(root, from_=1, to=1000)
spinbox.pack()
range_validation = root.register(validate)

spinbox.config(validate = 'key', validatecommand=(range_validation, '% P'))
root.mainloop()