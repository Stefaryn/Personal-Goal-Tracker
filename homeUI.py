# Author Cory Ingram

from tkinter import *
import goal


class HomeUI:

    def __init__(self):
    
        # initialize goal list
        self.goal_list = goal.GoalList("savefile")

        # main window
        self.root = Tk()

        # create a menu bar
        menubar = Menu(self.root)

        # create file menu
        filemenu = Menu(menubar, tearoff=0)

        # add exit command
        filemenu.add_command(label="Exit", command=self.root.destroy)

        # display the menu
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

        # set name
        self.root.title("Personal Goal Tracker")

        # create frame
        self.frame = Frame(self.root)
        self.frame.pack()
        
        # create add goal button
        self.button = Button(self.frame, text="Add Goal +", command=self.add_goal)
        self.button.pack()


        # main window loop initiation
        self.root.attributes("-topmost", True)
        self.root.mainloop()
        
# -------------------------------------------------------------------------------

    def add_goal(self):
        self.goal_list.goals.append(goal.Goal("work",0,0))
        print(self.goal_list)


# -------------------------------------------------------------------------------

if __name__ == '__main__':
    ui = HomeUI()

# -------------------------------------------------------------------------------
