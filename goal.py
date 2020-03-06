#This is the prototype for the MVP of the goal module
# written by Stephan Fields and Leonie Way

#Currently written on ix-dev which uses python 3.7.3

from datetime import datetime,date, timedelta
import os
import csv

class Node:
    '''

    '''
    def __init__(self, progress: int, time: date, note: str):
        self.progress = progress
        self.time = time
        self.note = note



class Goal:
    '''

    '''
    # I'm tempted to basically overload this init so that it can either take this info or a file name
    # But for now that would end up being harder to read so I will make a specific load function
    def __init__(self, name: str, finish: int, progress: int = 0):
        self.name = name
        self.finish = finish
        self.progress = progress

        #initialize lists for update tracking,
        self.rec = [Node(0, date.today(), "goal created")]


    def __repr__(self) -> str:
        return f"Goal: {self.name}, Finish: {self.finish}, Progress: {self.progress}"

    def update(self, change: int, note: str = ""):
        self.progress += change

        #record goal update for graphing

        self.rec.append( Node(self.progress, date.today(), note) )

    def getFilename(self):
        filename = self.name.replace(" ","_")
        filename = "files/" + filename + ".csv"
        return filename

    def load(self,filename: str = 0):

        if(not filename):
            filename = self.getFilename()
        
        if os.path.exists(filename):
            with open(filename,"r") as csvfile:
                #skips first row
                csv_reader = csv.reader(csvfile, delimiter=",")
                next(csvfile)
                for row in csv_reader:
                    self.rec.append(Node(row[0], date.fromordinal(int(row[1])), row[2]))

                    
            csvfile.close()
            #self.progress = len(self.time_rec)

        else:
            print("DEBUG: {} file not found".format(filename))


    def save(self, filename: str = 0):
        # in this version im assuming we could pass the goal name through home ui
        # and we could create a .csv file using that name, same goes to loading it

        if(not filename):
            filename = self.getFilename()

        with open(filename,'w') as csvfile:
            filewriter = csv.writer(csvfile, lineterminator='\n')
            #column names
            filewriter.writerow(["Progress","Date","Note"])

            for p in self.rec:
                filewriter.writerow([p.progress, p.time.toordinal(), p.note])
        csvfile.close()
        



class GoalList:
    '''

    '''
    def __init__(self, savefile: str):
        self.goals = []
        self.savefile = savefile

    # TODO: These will eventually be in charge of most of the loading and saving probably, and I think Leonie wanted to use
    # Sort of saved info file with the names of all the goals, for now I am leaving this empty

    def load(self):
        # read in and reinitialize all saved goals adding them to goals
        filename = "files/" + self.savefile
        infile = open(filename, "r")

        for l in infile.readlines():
            f = l.strip().split(",")
            if(len(f) >= 3):
                #initialize goal
                goal = Goal(f[0], int(f[1]), int(f[2]))
                goal.load() # load goal progress
                
                self.add_goal(goal)

        infile.close()
        

    def save(self):
        #write rudementary info about goals in from a comma separated file
        
        filename = "files/" + self.savefile
        outfile = open(filename, "w")
          
        for g in self.goals:
            outfile.write(g.name + ",")
            outfile.write(str(g.finish) + ",")  
            outfile.write(str(g.progress) + "\n")
            #save g to (g.name).txt
            g.save()

        outfile.close()
            
    def is_new_goal(self, name:str):
        # checks to see if goal with same name as another goal already exists.
        # returns false if a goal with name name is already in the list

        for g in self.goals:
            if (g.name == name):
                return False

        # no goal had name name.
        return True
        
    
    def add_goal(self, g:Goal):
        #adds a goal to the list
        #TODO: ensure that no duplicate 
        self.goals.append(g)

    def __str__(self):
        #TODO: update to display better if we ever need that
        return '{self.goals}'.format(self=self)


