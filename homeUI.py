# Author Cory Ingram

from tkinter import *
from tkinter import simpledialog
import goal


class HomeUI:

    def __init__(self):
    
        # bool to check for second window
        self.secondw = 0
        
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
        
        # create list frame
        self.lframe = Frame(self.root)
        self.lframe.grid(row=0, column=0)
        
        # create list box
        self.sbar = Scrollbar(self.lframe, orient=VERTICAL)
        self.lbox = Listbox(self.lframe, yscrollcommand=self.sbar.set, height=10)
        self.sbar.config(command=self.lbox.yview)
        self.sbar.pack(side=RIGHT, fill=Y)
        self.lbox.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.lbox.bind("<<ListboxSelect>>", self.showdetails)


        # create button frame
        self.bframe = Frame(self.root)
        self.bframe.grid(row=1, column=0)
        
        # create add goal button
        self.button = Button(self.bframe, text="Add Goal +", command=self.add_goal)
        self.button.pack()
        
        # create other button frame
        self.eframe = Frame(self.root)
        self.eframe.grid(row=1, column=1)
        
        # create work on goal button
        self.ebutton = Button(self.eframe, text="Work on Goal", command=self.edit_goal)
        self.ebutton.pack()

        # create details frame
        self.dframe = Frame(self.root, width=200, height=200)
        self.dframe.grid(row=0, column=1, sticky="n")
        self.dframe.grid_rowconfigure(0, weight=1)
        self.dframe.grid_columnconfigure(0, weight=1)

        # create details
        self.text0 = StringVar()
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text3 = StringVar()
        self.text4 = StringVar()
        
        self.text0.set("                                                                       ")
        self.text1.set("Welcome to Personal Goal Tracker!")
        
        self.windowstabilizer = Label(self.dframe, textvariable=self.text0).grid(row=0, column=0)
        self.goalnameheader = Label(self.dframe, textvariable=self.text1).grid(row=1, column=0)
        self.goalname = Label(self.dframe, textvariable=self.text2).grid(row=2, column=0)
        self.goalprogheader = Label(self.dframe, textvariable=self.text3).grid(row=3, column=0)
        self.goalprog = Label(self.dframe, textvariable=self.text4).grid(row=4, column=0)
        
        # main window loop initiation
        self.root.attributes("-topmost", True)
        self.root.mainloop()
        
# -------------------------------------------------------------------------------

    def add_goal(self):
        print("hello")
        newgoal = simpledialog.askstring("Input", "What goal would you like to begin tracking?", parent=self.root)
        self.goal_list.goals.append(goal.Goal(newgoal,0,0))
        self.set_listbox()
        print(self.goal_list)
        
    def set_listbox(self):
        self.lbox.delete(0, END)
        for goalobj in self.goal_list.goals:
            self.lbox.insert(END, "{goalobj.name}".format(goalobj=goalobj))
            
    def showdetails(self, event):
        selection = self.lbox.curselection()
        if selection:
            i = int(selection[0])
            self.text1.set("Goal:")
            self.text2.set("%s" % (self.goal_list.goals[i].name))
            self.text3.set("Progress:")
            self.text4.set("%d" % (self.goal_list.goals[i].progress))
            
    def edit_goal(self):
        selection = self.lbox.curselection()
        if self.secondw == 0:
            if selection:
                self.secondw = 1
                i = int(selection[0])
                editwindow = Toplevel(self.root)
                editwindow.bind("<Destroy>", self.close_second_win)
                gname = StringVar()
                gname.set("working on %s" % (self.goal_list.goals[i].name))
                swheader = Label(editwindow, textvariable=gname)
                swheader.pack()
            else:
                print("No goal selected")
        else:
            print("Second window already active")

    def close_second_win(self, event):
        self.secondw = 0
           


# -------------------------------------------------------------------------------

if __name__ == '__main__':
    ui = HomeUI()

# -------------------------------------------------------------------------------
