# Author Cory Ingram

from tkinter import *
from tkinter import simpledialog
import goal
import os.path


class HomeUI:

    def __init__(self):
        
        # pointer to location in list
        self.lpointer = 0
        self.npointer = 0
        
        # initialize goal list
        self.goal_list = goal.GoalList("savefile.csv")
        if os.path.exists("files/savefile.csv"):
            self.goal_list.load()

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
        self.lframe.grid(row=1, column=0)
        
        # create list box
        self.sbar = Scrollbar(self.lframe, orient=VERTICAL)
        self.lbox = Listbox(self.lframe, yscrollcommand=self.sbar.set, height=10)
        self.sbar.config(command=self.lbox.yview)
        self.sbar.pack(side=RIGHT, fill=Y)
        self.lbox.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.lbox.bind("<<ListboxSelect>>", self.showdetails)


        # create button frame
        self.bframe = Frame(self.root)
        self.bframe.grid(row=2, column=0)
        
        # create add goal button
        self.button = Button(self.bframe, text="Add Goal +", command=self.add_goal)
        self.button.pack()
        
        # create other button frame
        self.eframe = Frame(self.root)
        self.eframe.grid(row=2, column=1)
        
        # create work on goal button
        self.ebutton = Button(self.eframe, text="Add Progress", command=self.add_progress)
        self.ebutton.pack()
        
        # create second list box
        self.lboxf = Frame(self.root)
        self.lboxf.grid(row=1, column=1)
        self.scbar = Scrollbar(self.lboxf, orient=VERTICAL)
        self.libox = Listbox(self.lboxf, yscrollcommand=self.scbar.set, height=10)
        self.scbar.config(command=self.libox.yview)
        self.scbar.pack(side=RIGHT, fill=Y)
        self.libox.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.libox.bind("<<ListboxSelect>>", self.show_note_details)

        # create details frame
        self.dframe = Frame(self.root)
        self.dframe.grid(row=0, column=0, sticky="n")
        self.dframe.grid_rowconfigure(0, weight=1)
        self.dframe.grid_columnconfigure(0, weight=1)

        # create details
        self.text0 = StringVar()
        self.text1 = StringVar()
        
        self.text0.set("                                                                       ")
        self.text1.set("Welcome to Personal Goal Tracker!")
        self.detail = Label(self.dframe, textvariable=self.text1).grid(row=0, column=0)
        self.windowstabilizer = Label(self.dframe, textvariable=self.text0).grid(row=1, column=0)
        
        # create note frame
        self.nframe = Frame(self.root)
        self.nframe.grid(row=1, column=2)
        self.ntext = StringVar()
        self.ntext.set("")
        self.nlabel = Label(self.nframe, textvariable=self.ntext)
        self.nlabel.pack()
        
        self.set_listbox()
        
        # main window loop initiation
        self.root.mainloop()
        
# -------------------------------------------------------------------------------

    def add_goal(self):
        newgoal = simpledialog.askstring("Input", "What goal would you like to begin tracking?", parent=self.root)
        if newgoal:
            goalamt = simpledialog.askinteger("Input", "What is your end goal amount?", parent=self.root, minvalue=1, maxvalue=1000000)
            if goalamt is None:
                goalamt = 1
            self.goal_list.goals.append(goal.Goal(newgoal,goalamt,0))
            self.goal_list.save()
            self.set_listbox()
            print(self.goal_list)
        
    def set_listbox(self):
        self.lbox.delete(0, END)
        for goalobj in self.goal_list.goals:
            self.lbox.insert(END, "{goalobj.name}".format(goalobj=goalobj))
            
    def showdetails(self, event):
        selection = self.lbox.curselection()
        if selection:
            self.lpointer = int(selection[0])
            self.text1.set("Working on %s\nProgress:\n%d/%d" %(self.goal_list.goals[self.lpointer].name, self.goal_list.goals[self.lpointer].progress, self.goal_list.goals[self.lpointer].finish))
            self.set_note_listbox()
            self.ntext.set("")
        
    def add_progress(self):
        selection = self.lbox.curselection()
        if selection:
            self.lpointer = int(selection[0])
            new_prog = simpledialog.askinteger("Input", "How much progress have you made?", parent=self.root, minvalue=1, maxvalue=(self.goal_list.goals[self.lpointer].finish - self.goal_list.goals[self.lpointer].progress))
            if new_prog:
                new_note = simpledialog.askstring("Input", "Any thoughts on this progress?", parent=self.root)
                self.goal_list.goals[self.lpointer].update(new_prog, new_note)
                print(self.goal_list.goals[self.lpointer])
                self.text1.set("Working on %s\nProgress:\n%d/%d" %(self.goal_list.goals[self.lpointer].name, self.goal_list.goals[self.lpointer].progress, self.goal_list.goals[self.lpointer].finish))
                self.set_note_listbox()
            
    def set_note_listbox(self):
        self.libox.delete(0,END)
        for node in self.goal_list.goals[self.lpointer].rec:
            self.libox.insert(END, "{node.time}".format(node=node))
            
    def show_note_details(self, event):
        note_select = self.libox.curselection()
        if note_select:
            self.npointer = int(note_select[0])
            self.ntext.set("%s" % (self.goal_list.goals[self.lpointer].rec[self.npointer].note))
            
            
            
           


# -------------------------------------------------------------------------------

if __name__ == '__main__':
    ui = HomeUI()

# -------------------------------------------------------------------------------
