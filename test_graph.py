import graph
import goal

# class Goal:
    # def __init__(self, name: str, finish: int, progress: int = 0):
        # self.name = name
        # self.finish = finish
        # self.progress = progress
        # self.time_rec = []
        # self.prog_rec = []
        # self.note_rec = []


def init_goal():
	goalOne = goal.Goal("Horse Riding", 9)

def prog_one():
	goalOne = goal.Goal("Horse Riding", 9)
	goalOne.progress = 3
	goalOne.time_rec = ['2020-02-10','2020-02-20','2020-02-24','2020-02-27']
	goalOne.prog_rec = [1,2,3,4]
	goalOne.note_rec = ['goal created','groomed the horse','saddled the horse','horse jumping']
	
	graph.build_graph(goalOne)
	
	
def prog_two():
	goalOne = goal.Goal("Horse Riding", 9)
	goalOne.progress = 5
	goalOne.time_rec = ['2020-02-10','2020-02-20','2020-02-24','2020-02-27','2020-03-2','2020-03-5']
	goalOne.prog_rec = [1,2,3,4,5,6]
	goalOne.note_rec = ['goal created','groomed the horse','saddled the horse','horse jumping','Replaced horse shoe','Beach riding']
	
	graph.build_graph(goalOne)
	
	


def main():
	#init_goal()
	#prog_one()
	prog_two()
	

if __name__ == '__main__':
	main()