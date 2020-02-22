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

	def save(self, filename: str):
		# TODO: This does not save any sort of node progress, need to figure out how we want to do that, and also incorporate a time element of some sort
		# Note that this currently overwrites the file, so we should be careful with usage
		filename = "files/" + filename
		outfile = open(filename, "w")

		# Add newlines back and conver ints to strs
		outfile.write(self.name + "\n")	
		outfile.write(str(self.finish) + "\n")	
		outfile.write(str(self.progress) + "\n")	

class GoalList:
	def __init(self, goals: list, savefile: str):
		self.goals = goals
		self.savefile = savefile

	# TODO: These will eventually be in charge of most of the loading and saving probably, and I think Leonie wanted to use
	# Sort of saved info file with the names of all the goals, for now I am leaving this empty
	def load(self):
		pass

	def save(self):
		pass

# Eventually this and other tests should be moved to a unittest file but for now I just left them in here as an example of usage
def basic_test():
	g1 = Goal("Bad", 200)
	print(g1)

	g1.load("example.txt")
	print(g1)

	g1.update(1)
	print(g1)

	g1.save("example.txt")

basic_test()
