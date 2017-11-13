### First round of trying to make a search bar

from tkinter import *

class Application(Frame):
    def say_hi(self):
        print( "hi there, everyone!")

    def createWidgets(self):
        # User entry bar here
        Label(self, text = "Entry: ").grid(row=1)
        self.search_bar = Entry(self, bd = 5)
        self.search_bar.grid(row=1, column=1)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
