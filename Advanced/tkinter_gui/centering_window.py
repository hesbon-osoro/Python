from tkinter import Tk, BOTH, Label
from tkinter import Frame
class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Centered Window')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        label = Label(text='This window is centered in the screen')
        label.place(x=45, y=60)

    def centerWindow(self):
        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d'%(w, h, x, y))

def main():
    root = Tk()
    ex = Example()
    root.mainloop()

if __name__=='__main__':
    main()