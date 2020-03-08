import goal

def init_goal():
    
    goalOne = goal.Goal("Horse Riding1", 9)

    goalOne.update(1,"rode a pony", ["a", "b", "c", "d", "e"])
    goalOne.update(1,"it kicked me", ["aa", "bb", "cc", "dd", "ee"])

    goalOne.save()
    print(goalOne.rec[0].time.month)
    print(goalOne.rec[0].survey)
    
    goalTwo = goal.Goal("Horse Riding1", 9)
    goalTwo.load()
    print(goalTwo.rec[0].time)
    print(goalTwo.rec[0].survey)

def read_goal():

    test = goal.Goal("testGoal", 10)

    test.load("files/testGoal.csv")
    for t in test.rec:
        print(t.time)
        print(t.progress)
        print(t.note)

def main():
    #uncomment to test save

    init_goal()
    read_goal()
#    prog_one()
#    prog_two()

    # test_load_one()
    # test_load_two()
    # test_load_three()

    
if __name__ == '__main__':
	main()
