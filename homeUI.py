# Author Cory Ingram

from tkinter import *


class HomeUI:

    def __init__(self):

        # main window
        self.main = Tk()

        # create a menu bar
        menubar = Menu(self.main)

        # create file menu
        filemenu = Menu(menubar, tearoff=0)

        # add exit command
        filemenu.add_command(label="Exit", command=self.main.destroy)

        # display the menu
        menubar.add_cascade(label="File", menu=filemenu)
        self.main.config(menu=menubar)

        # set name
        self.main.title("Personal Goal Tracker")

        # create frame
        self.frame1 = Frame(self.main, borderwidth=2, relief="solid")


        # main window loop initiation
        self.main.attributes("-topmost", True)
        self.main.mainloop()


# -------------------------------------------------------------------------------

if __name__ == '__main__':
    Gui = HomeUI()

# -------------------------------------------------------------------------------
