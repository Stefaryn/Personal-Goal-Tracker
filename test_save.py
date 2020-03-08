
import goal
import graph
from datetime import date, timedelta, datetime

class Node:
    '''
        
        '''
    def __init__(self, progress: int, time: date, note: str):
        self.progress = progress
        self.time = time
        self.note = note



def init_goal():
	goalOne = goal.Goal("Horse Riding1", 9)
	goalOne.progress = 1
	goalOne.time_rec = ['2020-02-10']
	goalOne.prog_rec = [0]
	goalOne.note_rec = ['goal created']

	goalOne.save("Horse Riding1")
def prog_one():
	goalOne = goal.Goal("Horse Riding2", 9)
	goalOne.progress = 3
	goalOne.time_rec = ['2020-02-10','2020-02-20','2020-02-24','2020-02-27']
	goalOne.prog_rec = [0,1,2,3]
	goalOne.note_rec = ['goal created','groomed the horse','saddled the horse','horse jumping']
	goalOne.save("Horse Riding2")
    #graph.build_graph(goalOne)
	
	
def prog_two():
	goalOne = goal.Goal("Horse Riding3", 9)
	goalOne.progress = 5
    
	for i in range(goalOne.progress):
		goalOne.rec.append(Node(i,date.today()- timedelta(days=i*3),"note number"+str(i)))
        
#    goalOne.time_rec = ['2020-02-10','2020-02-20','2020-02-24','2020-02-27','2020-03-2','2020-03-5']
#    goalOne.prog_rec = [0,1,2,3,4,5]
#    goalOne.note_rec = ['goal created now lets see how the txt is formatted on screen','groomed the horse','saddled the horse','horse jumping','Replaced horse shoe','Beach riding']

    #graph.build_graph(goalOne)
	goalOne.save("Horse Riding3")
	
def test_load_one():
    obj = goal.Goal("Horse Riding1", 9)
    obj.load("Horse Riding1")
    print("TEST: load progress\n",obj.prog_rec)
    print("TEST: load timestamps\n",obj.time_rec)
    print("TEST: load notes list\n",obj.note_rec)
    print("TEST: progress --->",obj.progress)
    print()

def test_load_two():
    obj = goal.Goal("Horse Riding2", 9)
    obj.load("Horse Riding2")
    print("TEST: load progress\n",obj.prog_rec)
    print("TEST: load timestamps\n",obj.time_rec)
    print("TEST: load notes list\n",obj.note_rec)
    print("TEST: progress --->",obj.progress)
    print()
def test_load_three():
    obj = goal.Goal("Horse Riding3", 9)
    obj.load("Horse Riding3")
    graph.build_graph(obj)
    print()

def main():

#uncomment to test save

#    init_goal()
#    prog_one()
    #prog_two()

#    test_load_one()
#    test_load_two()
    test_load_three()





if __name__ == '__main__':
	main()
