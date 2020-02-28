 
import matplotlib.pyplot as plt
import matplotlib.dates as plt_dates
from datetime import datetime, timedelta
import time


plt.style.use('seaborn')

def build_graph(goalObj):

	milestones = goalObj.prog_rec
	timestamps = []
	data_x = []
	data_y = []
	
	#takes the date stamps and add them to a list in python's datetime format
	for index in goalObj.time_rec:
		date_splitted = index.split('-')
		timestamps.append(datetime(int(date_splitted[0]),int(date_splitted[1]),int(date_splitted[2])))

	
	data_x.append(timestamps[0])
	data_y.append(milestones[0])
	print(data_x, data_y)

	fig = plt.figure(figsize=(8, 8))
	ax = fig.add_subplot(111)
	line, = ax.plot(data_x, data_y, '-o', picker=goalObj.finish)

	#initial display of graph's limits
	ax.set_ylim(-0.2, goalObj.finish+1)
	ax.set_xlim(timestamps[0] - timedelta(days=1), timestamps[-1] + timedelta(days=1))
	
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
		
		return formatted_txt
		
	def on_pick(event):
		line = event.artist
		ind = event.ind

		print("debug on pick event",ind)
		
		text = txt_format(str(goalObj.note_rec[ind[0]]))
		txt.set_text(text)
		fig.canvas.draw()
		fig.canvas.flush_events()
    

	#removes the message when mouse is outside the graph
	def on_leave(event):
		txt.set_text('')
		fig.canvas.draw()
		fig.canvas.flush_events()

	cid = fig.canvas.mpl_connect('pick_event', on_pick)
	fig.canvas.mpl_connect('figure_leave_event', on_leave)

	plt.show(False)

	for i in range(1, len(milestones) ):
		data_x.append(timestamps[i])
		data_y.append( milestones[i])
    
		line.set_xdata(data_x)
		line.set_ydata(data_y)
    
		fig.canvas.draw()
		fig.canvas.flush_events()
    
		print(data_x, data_y)
		time.sleep(.25)


	plt.show()
	
	
	
			
	
	
	

