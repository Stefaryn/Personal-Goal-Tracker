 
import matplotlib.pyplot as plt
import matplotlib.dates as plt_dates
import matplotlib.dates as mdates

from datetime import datetime, timedelta, date
import time


plt.style.use('seaborn')

def build_graph(goalObj):

    milestones = [] #goalObj.prog_rec
    timestamps = []
    notes = []
    data_x = []
    data_y = []
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
    data_x.append(timestamps[0])
    data_y.append(milestones[0])
    print(data_x, data_y)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    line, = ax.plot(timestamps[0], milestones[0], '-o', picker=goalObj.finish)

    #initial display of graph's limits
    ax.set_ylim(-0.2, goalObj.finish)

    # Get the range of the dates
    date_range = timestamps[-1] - timestamps[0]
    print(date_range)
    days_padding = (5 - date_range.days)
    days_padding = max(1, days_padding)

    start_date = timestamps[0] - timedelta(days=1)
    end_date = timestamps[-1] + timedelta(days=days_padding)
    ax.set_xlim(start_date, end_date)

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
    txt = ax.text(timestamps[0], goalObj.finish-1, '', va="center",fontsize=16,
                  bbox=dict(boxstyle='round', color='lightskyblue')
                  )


    #displays the message of the plot
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

    for i in range(1, len(milestones)):
        data_x.append(timestamps[i])
        data_y.append( milestones[i])

        line.set_xdata(data_x)
        line.set_ydata(data_y)

        fig.canvas.draw()
        fig.canvas.flush_events()

        print(data_x, data_y)
        time.sleep(.25)

    cid = fig.canvas.mpl_connect('pick_event', on_pick)
    fig.canvas.mpl_connect('figure_leave_event', on_leave)
        
    plt.show(False)
    

    plt.show()
	
	
	
			
	
	
	

