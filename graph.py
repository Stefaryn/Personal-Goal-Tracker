 
#try:
import matplotlib.pyplot as plt
import matplotlib.dates as plt_dates
import matplotlib.dates as mdates
#except ModuleNotFoundError:
#    print("\nMatplotlib is not installed please refer to the user installation document.\n")
#    exit(1)

from datetime import datetime, timedelta, date
import time


plt.style.use('seaborn')

def build_graph(goalObj):
    '''
	This function is called in homeUI.py with a goal's object to display
	a graphical representation of a goal for the user.
	
	Args:
	goalObj: an object of goal class
	milestones: a list of integers that represents the progress steps of a goal
	timestamps: a list of dates that corresponds to the milestones
	notes: a list of strings that corresponds to the milestones

        '''

    milestones = []
    timestamps = []
    notes = []

    # checks if the object contains data

    if len(goalObj.rec) < 1:
    	print("DEBUG: no progress found in this goal")
    	return

    # iterates through the nodes in the object and add its data to the lists

    for node in goalObj.rec:
        print("GRAPH DEBUG:",node.time)
        node_time = str(node.time)
        date_splitted = node_time.split('-')
        timestamps.append(datetime(int(date_splitted[0]),int(date_splitted[1]),int(date_splitted[2])))
        
        notes.append(node.note)
        milestones.append(int(node.progress))
	



    print("milestones:",milestones)
    print("timestamps:",timestamps)
    print("Finish",goalObj.finish)

    # sets the defualt display size of the graph

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)

    # plots the first data of the goal, sets the graph to be lines and clickable points
    line, = ax.plot(timestamps, milestones, '-o', picker=goalObj.finish)

    #set default y axis limit
    ax.set_ylim(-0.2, goalObj.finish)

    # Get the range of the dates
    # this handles the formatting of the x axis of the graph to be more presentable in different cases
    date_range = timestamps[-1] - timestamps[0]
    print(date_range)
    days_padding = (5 - date_range.days)
    days_padding = max(1, days_padding)

    start_date = timestamps[0] - timedelta(days=1)
    end_date = timestamps[-1] + timedelta(days=days_padding)

	#set default x axis limit 
    ax.set_xlim(start_date, end_date)

    #format the dates to (month name day, year) 
    date_fmt = mdates.DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(date_fmt)
	
    #gcf stands for 'get current figure' to show dates slanted
    plt.gcf().autofmt_xdate()

    #graph's labels
    ax.set_title(goalObj.name)
    ax.set_ylabel('Milestones')
    ax.set_xlabel('Dates')
	
    #lets the graph use the whole window
    plt.tight_layout()

    #displays the notes when called, always exist but its empty when not triggered
    txt = ax.text(timestamps[0], goalObj.finish-(1/10*goalObj.finish), '', va="center",fontsize=16,
                  bbox=dict(boxstyle='round', color='lightskyblue')
                  )


    #formats the message of the plot
    def txt_format(txt_str):
        #every 4th space is \n
        formatted_txt = ""
       	space_count = 0
       	for char in txt_str:
            if char == ' ':
                space_count += 1
            if space_count == 4:
                space_count = 0
                char = '\n'
            formatted_txt += char
        print("return text:",formatted_txt)
        return formatted_txt
	

	#event action when a plot is clicked
    def on_pick(event):
        line = event.artist
        ind = event.ind
        
        print("debug on pick event",ind)
        print("DEBUG notes:",notes[ind[0]])
        text = txt_format(notes[ind[0]])
        
        print("DEBUG text:",text)
        txt.set_text(str(text))
        fig.canvas.draw()
        fig.canvas.flush_events()
    

	#removes the message when mouse is outside the graph
    def on_leave(event):
        txt.set_text('')
        fig.canvas.draw()
        fig.canvas.flush_events()


    #listens for actions
    cid = fig.canvas.mpl_connect('pick_event', on_pick)
    fig.canvas.mpl_connect('figure_leave_event', on_leave)
        

    

    plt.show(block=False)
	
	
	
			
	
	
	

