 
import matplotlib.pyplot as plt
import matplotlib.dates as plt_dates
from datetime import datetime, timedelta

import time
import numpy as np

plt.style.use('seaborn')


milestones = [0,1,2,3,4,5]
	
	
timestamps = []
#this would be the initial date
timestamps.append(datetime(2019,1,18))
for x in range(5):
	timestamps.append(timestamps[x] + timedelta(days=10))
	
'''

	
axes = plt.gca()
axes.set_xlim([timestamps[0],timestamps[4]])
axes.set_ylim([milestones[0],milestones[4]])
plt.plot_date(timestamps[0],milestones[0])
plt.plot_date(timestamps[1],milestones[1])

#format the date to (Month name, day, year) instead of YYYY-MM-DD
'''

data_x = np.array(timestamps[:1])
data_y = np.array(milestones[:1])
print(data_x, data_y)

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
line, = ax.plot(data_x[:1], data_y[:1], '-o', picker=5)

ax.set_ylim([milestones[0], milestones[4]])
ax.set_xlim([timestamps[0], timestamps[4]])
#'get current figure' to show dates slanted
plt.gcf().autofmt_xdate()


ax.set_title('Goal Name')
ax.set_ylabel('Milestones')
ax.set_xlabel('Dates')
plt.tight_layout()

txt = ax.text(timestamps[1], milestones[3], '', va="center",fontsize=16,
        bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
        )
#displays the message of the plot
def on_pick(event):
    line = event.artist
    xdata, ydata = line.get_data()
    ind = event.ind
    print('DEBUG:on pick line:', np.array([xdata[ind], ydata[ind]]).T)
    
    x = xdata[ind]
    y = ydata[ind]
    
    txt.set_text('This message wil hopefully display \nsomething related to this \ncoordinates {0}, {1}'.format(x, y))
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
    data_x = np.append(data_x, timestamps[i])
    data_y = np.append(data_y, milestones[i])
    
    line.set_xdata(data_x)
    line.set_ydata(data_y)
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    print(data_x, data_y)
    time.sleep(.25)

plt.show()

