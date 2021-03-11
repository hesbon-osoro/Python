from tkinter import *
root = Tk()
root.title('Paint App')
root.geometry('500x350')

#define function when mouse double click is enabled
def paint(event):
    #co-ordinates
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)

    #color
    colour = '#000fff000'
    #specify type of display
    w.create_line(x1, y1, x2, y2, fill=colour)

#create canvas widget
w = Canvas(root, width=400, height=250, cursor='dot')
#call function when double click is enabled
w.bind('<B1-Motion>', paint)
#create label
l = Label(root, text='Double Click and Drag to draw')
l.pack()
w.pack()
mainloop()