# Author Cory Ingram

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import goal
import os.path
graphok = 0
try:
    import graph
except ModuleNotFoundError:
    graphok = 1


class HomeUI:

    def __init__(self):
        
        # pointer to selected goal in list
        self.lpointer = 0
        # pointer to selected note in list
        self.npointer = 0
        
        # initialize goal list
        self.goal_list = goal.GoalList("savefile.csv")
        # if save data exists load it
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
        
        # create frame for list of goals
        self.lframe = Frame(self.root)
        self.lframe.grid(row=1, column=0)
        
        # create list box for list of goals
        self.sbar = Scrollbar(self.lframe, orient=VERTICAL)
        self.lbox = Listbox(self.lframe, yscrollcommand=self.sbar.set, height=10)
        self.sbar.config(command=self.lbox.yview)
        self.sbar.pack(side=RIGHT, fill=Y)
        self.lbox.pack(side=LEFT, fill=BOTH, expand=1)
        
        # create event when selecting a goal from the listbox
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
        
        # create add progress button
        self.ebutton = Button(self.eframe, text="Add Progress", command=self.add_progress)
        self.ebutton.pack()
        
        # create second listbox to hold progress notes
        self.lboxf = Frame(self.root)
        self.lboxf.grid(row=1, column=1)
        self.scbar = Scrollbar(self.lboxf, orient=VERTICAL)
        self.libox = Listbox(self.lboxf, yscrollcommand=self.scbar.set, height=10)
        self.scbar.config(command=self.libox.yview)
        self.scbar.pack(side=RIGHT, fill=Y)
        self.libox.pack(side=LEFT, fill=BOTH, expand=1)
        

        # create details frame for text messages
        self.dframe = Frame(self.root)
        self.dframe.grid(row=0, column=0, sticky="n")
        self.dframe.grid_rowconfigure(0, weight=1)
        self.dframe.grid_columnconfigure(0, weight=1)

        # create text variables
        self.text0 = StringVar()
        self.text1 = StringVar()
        
        # Large empty line to help prevent the window from constantly resizing
        self.text0.set("                                                                       ")
        self.text1.set("Welcome to Personal Goal Tracker!\n\n")
        self.detail = Label(self.dframe, textvariable=self.text1).grid(row=0, column=0)
        self.windowstabilizer = Label(self.dframe, textvariable=self.text0).grid(row=1, column=0)
        
        # create display buttons frame
        self.nframe = Frame(self.root)
        self.nframe.grid(row=1, column=2)
        
        # create additional buttons
        self.notebutton = Button(self.nframe, text="View Note", command=self.view_note)
        self.notebutton.grid(row=0, column=0)
        self.surveybutton = Button(self.nframe, text="View Survey", command=self.view_survey)
        self.surveybutton.grid(row=1, column=0)
        self.graphbutton = Button(self.nframe, text="View Graph", command=self.view_graph)
        self.graphbutton.grid(row=2, column=0)
        
        # display all goals in listbox
        self.set_listbox()
        
        # main window loop initiation
        self.root.mainloop()
        
# -------------------------------------------------------------------------------

    def add_goal(self):
        '''
        Creates a new goal object and adds it to the goal list.
        Saves the new goal list to the save file.
        Updates the listbox display.
        '''
        newgoal = simpledialog.askstring("Input", "What goal would you like to begin tracking?", parent=self.root)
        # if nothing is entered then do nothing else
        if newgoal:
            goalamt = simpledialog.askinteger("Input", "What is your end goal amount?", parent=self.root, minvalue=1, maxvalue=1000000)
            # if no amount is entered default to 1
            if goalamt is None:
                goalamt = 1
            self.goal_list.goals.append(goal.Goal(newgoal,goalamt,0)) # add goal to goal list
            self.goal_list.goals[-1].update(0, "Goal Created")
            self.goal_list.save() # updates save data
            self.set_listbox() # updates listbox display
            print(self.goal_list)
        
    def set_listbox(self):
        '''
        updates goal listbox display.
        '''
        self.lbox.delete(0, END) # clears listbox
        for goalobj in self.goal_list.goals:
            self.lbox.insert(END, "{goalobj.name}".format(goalobj=goalobj)) # refills listbox with name of each goal
            
    def showdetails(self, event):
        '''
        Updates display to show details on highlighted listbox entry.
        '''
        selection = self.lbox.curselection() # gets position of highlighted listbox entry
        # if nothing selected then do nothing else
        if selection:
            self.lpointer = int(selection[0]) # sets the pointer in the goal list to be the same as the highlighted listbox entry
            self.text1.set("Working on %s\nProgress:\n%d/%d" %(self.goal_list.goals[self.lpointer].name, self.goal_list.goals[self.lpointer].progress, self.goal_list.goals[self.lpointer].finish))
            self.set_note_listbox() # update display on note listbox to notes of the selected goal
        
    def add_progress(self):
        selection = self.lbox.curselection()
        note_select = self.libox.curselection()
        if selection:
            self.lpointer = int(selection[0])
            if (self.goal_list.goals[self.lpointer].finish - self.goal_list.goals[self.lpointer].progress) > 0:
                new_prog = simpledialog.askinteger("Input", "How much progress have you made?", parent=self.root, minvalue=1, maxvalue=(self.goal_list.goals[self.lpointer].finish - self.goal_list.goals[self.lpointer].progress))
                if new_prog:
                    new_note = simpledialog.askstring("Input", "Any thoughts on this progress?", parent=self.root)
                    # add survey
                    self.goal_list.goals[self.lpointer].update(new_prog, new_note)
                    print(self.goal_list.goals[self.lpointer])
                    self.text1.set("Working on %s\nProgress:\n%d/%d" %(self.goal_list.goals[self.lpointer].name, self.goal_list.goals[self.lpointer].progress, self.goal_list.goals[self.lpointer].finish))
                    self.set_note_listbox()
                    self.goal_list.save() # updates save data
            else:
                messagebox.showwarning("Warning", "Goal already completed")
        else:
            if note_select:
                if (self.goal_list.goals[self.lpointer].finish - self.goal_list.goals[self.lpointer].progress) > 0:
                    new_prog = simpledialog.askinteger("Input", "How much progress have you made?", parent=self.root, minvalue=1, maxvalue=(self.goal_list.goals[self.lpointer].finish - self.goal_list.goals[self.lpointer].progress))
                    if new_prog:
                        new_note = simpledialog.askstring("Input", "Any thoughts on this progress?", parent=self.root)
                        # add survey
                        self.goal_list.goals[self.lpointer].update(new_prog, new_note)
                        print(self.goal_list.goals[self.lpointer])
                        self.text1.set("Working on %s\nProgress:\n%d/%d" %(self.goal_list.goals[self.lpointer].name, self.goal_list.goals[self.lpointer].progress, self.goal_list.goals[self.lpointer].finish))
                        self.set_note_listbox()
                        self.goal_list.save() # updates save data
                else:
                    messagebox.showwarning("Warning", "Goal already completed")
            else:
                messagebox.showwarning("Warning", "No goal selected")
            
    def set_note_listbox(self):
        '''
        Updates note listbox display
        '''
        self.libox.delete(0,END) # clear current listbox
        for node in self.goal_list.goals[self.lpointer].rec:
            self.libox.insert(END, "{node.time}".format(node=node)) # refill list box with each node in selected goal
            
            
    def view_note(self):
        '''
        Displays text for a selected note
        '''
        note_select = self.libox.curselection() # gets position of highlighted listbox entry
        if note_select:
            self.npointer = int(note_select[0]) # set pointer in node list to the same as highlighted listbox entry
            messagebox.showinfo("note", self.goal_list.goals[self.lpointer].rec[self.npointer].note) # display note text
        else:
            messagebox.showwarning("Warning", "No note selected")
        
    def view_survey(self):
        print("Survey")
        
    def view_graph(self):
        if graphok == 0:	    
            selection = self.lbox.curselection()
            note_select = self.libox.curselection()
            if selection:
                self.lpointer = int(selection[0])
                graph.build_graph(self.goal_list.goals[self.lpointer])
            else:
                if note_select:
                    graph.build_graph(self.goal_list.goals[self.lpointer]) # if cursor is on a note then a goal must have already been selected and lpointer already set.
                else:
                    messagebox.showwarning("Warning", "No goal selected")
        else:
            messagebox.showwarning("Warning", "Matplotlib is not installed please refer to the user installation document.")
        
            
        
           


# -------------------------------------------------------------------------------

if __name__ == '__main__':
    ui = HomeUI()

# -------------------------------------------------------------------------------
