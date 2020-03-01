import graph
import goal





def init_goal():
	goalOne = goal.Goal("Horse Riding", 9)
	goalOne.progress = 0
	goalOne.time_rec = ['2020-02-10']
	goalOne.prog_rec = [0]
	goalOne.note_rec = ['goal created']
	graph.build_graph(goalOne)
	
def prog_one():
	goalOne = goal.Goal("Horse Riding", 9)
	goalOne.progress = 3
	goalOne.time_rec = ['2020-02-10','2020-02-20','2020-02-24','2020-02-27']
	goalOne.prog_rec = [0,1,2,3]
	goalOne.note_rec = ['goal created','groomed the horse','saddled the horse','horse jumping']
	
	graph.build_graph(goalOne)
	
	
def prog_two():
	goalOne = goal.Goal("Horse Riding", 9)
	goalOne.progress = 6
	goalOne.time_rec = ['2020-02-10','2020-02-13','2020-02-14','2020-02-19','2020-02-26','2020-02-29']
	goalOne.prog_rec = [0,1,2,3,4,5]
	goalOne.note_rec = ['goal created now lets see how the txt is formatted on screen','groomed the horse','saddled the horse','horse jumping','Replaced horse shoe','Beach riding']
	
	graph.build_graph(goalOne)
	
	


def main():
    init_goal()
    prog_one()
    prog_two()
	

if __name__ == '__main__':
	main()
