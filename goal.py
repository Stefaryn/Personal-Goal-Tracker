#This is the prototype for the MVP of the goal module

#Currently written on ix-dev which uses python 3.7.3

class Goal:
    # I'm tempted to basically overload this init so that it can either take this info or a file name
    # But for now that would end up being harder to read so I will make a specific load function
    def __init__(self, name: str, finish: int, progress: int = 0):
        self.name = name
        self.finish = finish
        self.progress = progress

    def __repr__(self) -> str:
        return f"Goal: {self.name}, Finish: {self.finish}, Progress: {self.progress}"

    def update(self, change: int):
        self.progress += change

    # Note that load and save currently use everything from a <files> directory
    def load(self, filename: str):
        # TODO: Currently load crashed if the file is incorrect, we should decide on a file format and verify file input
        # Most of the error checking should probably happen on the user input side eventually and our files can just be reliable
        filename = "files/" + filename
        infile = open(filename, "r")

        # Strip to remove whitespace
        self.name = infile.readline().strip()
        # Convert to ints
        self.finish = int(infile.readline())
        self.progress = int(infile.readline())

        infile.close()

    def save(self, filename: str):
        # TODO: This does not save any sort of node progress, need to figure out how we want to do that, and also incorporate a time element of some sort
        # Note that this currently overwrites the file, so we should be careful with usage
        filename = "files/" + filename
        outfile = open(filename, "w")

        # Add newlines back and conver ints to strs
        outfile.write(self.name + "\n") 
        outfile.write(str(self.finish) + "\n")  
        outfile.write(str(self.progress) + "\n")

        outfile.close()

class GoalList:
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
                goal.load(goal.name + ".txt")
                    # ^this currently doesn't do anything new and we may move to not reading this
                    #  when it is used rather than on initialization
                
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
    g1 = Goal("Bad", 200)
    print(g1)

    g1.load("example.txt")
    print(g1)

    g1.update(1)
    print(g1)

    g1.save("example.txt")


    #GoalList save tests
    l1 = GoalList("list.txt")
    l1.add_goal(g1)
    print(l1)

    l1.save()

    #GoalList load tests
    l2 = GoalList("list.txt")
    l2.load()
    print(l2)

basic_test()
