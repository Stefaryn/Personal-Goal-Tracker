#This is the prototype for the MVP of the goal module
# written by Stephan Fields and Leonie Way

#Currently written on ix-dev which uses python 3.7.3

from datetime import datetime,date, timedelta

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
        # TODO: no system of saving and loading back in
        self.time_rec = []
        self.prog_rec = []
        self.note_rec = []

    def __repr__(self) -> str:
        return f"Goal: {self.name}, Finish: {self.finish}, Progress: {self.progress}"

    def update(self, change: int, note: str = ""):
        self.progress += change

        #record goal update for graphing
        self.time_rec.append(date.today())
        self.prog_rec.append(self.progress)
        self.note_rec.append(note)

    # Note that load and save currently use everything from a <files> directory
    def load(self, filename: str):
        '''
        TODO: Currently load crashed if the file is incorrect,
        we should decide on a file format and verify file input

        Most of the error checking should probably happen on the
        user input side eventually and our files can just be reliable

        TODO: maybe change format of file because currently notes that
        contain "," will not be read back in properly
        '''
        filename = "files/" + filename
        infile = open(filename, "r")

        #read in time_rec
        line = infile.readline().strip(",\n")
        breakline = line.split(",")
        for t in breakline:
            self.time_rec.append(datetime.strptime(t, "%a %b %d %H:%M:%S %Y"))

        #read in prog_rec
        line = infile.readline().strip(",\n")
        breakline = line.split(",")
        for p in breakline:
            self.prog_rec.append(int(p))

        #read in note_rec
        line = infile.readline().strip(",\n")
        breakline = line.split(",")
        for n in breakline:
            self.note_rec.append(n)


        infile.close()

    def save(self, filename: str):
        # Note that this currently overwrites the file, so we should be careful with usage
        filename = "files/" + filename
        outfile = open(filename, "w")

        for rec in self.time_rec:
            outfile.write(rec.ctime() + ",")
        outfile.write("\n")

        for rec in self.prog_rec:
            outfile.write(str(rec) + ",")
        outfile.write("\n")

        for rec in self.note_rec:
            outfile.write(rec + ",")
        outfile.write("\n")
        
        outfile.close()

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
                #goal.load(goal.name + ".txt")
                    # ^this currently is broken because I changed what is being saved
                    #  when fixed should maybe be called later than it is 
                
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
            g.save(g.name + ".txt")

        outfile.close()
            
        
    def add_goal(self, g:Goal):
        #adds a goal to the list
        #TODO: ensure that no duplicate 
        self.goals.append(g)

    def __str__(self):
        #TODO: update to display better if we ever need that
        return '{self.goals}'.format(self=self)

# Eventually this and other tests should be moved to a unittest file but for now I just left them in here as an example of usage
def basic_test():
    #Goal Tests
    '''
    #broken by update of goal saving
    g1 = Goal("Bad", 200)
    print(g1)

    g1.load("example.txt")
    print(g1)

    g1.update(1, "eat a goat")
    print(g1)

    #g1.save("example.txt")
    '''

    #GoalList save tests
    '''
    l1 = GoalList("list.txt")
    l1.add_goal(g1)
    print(l1)

    print(g1.time_rec)
    print(g1.prog_rec)
    print(g1.note_rec)
    
    l1.save()
    '''
    #GoalList load tests
    l2 = GoalList("list.txt")
    l2.load()
    print(l2)

    print(l2.goals[0].time_rec)
    print(l2.goals[0].prog_rec)
    print(l2.goals[0].note_rec)

if __name__ == '__main__':
    basic_test()
