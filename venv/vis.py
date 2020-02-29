import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import csv

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], '-')

with open('data1k.csv', newline='') as f:
    reader = csv.reader(f)
    my_data = list(reader)


def convert(frame):
    y_value = my_data[int(frame)][0]
    return float(y_value[:20])


def init():
    ax.set_xlim(0, 1000)
    ax.set_ylim(2, 4.5)
    pi = plt.axhline(y=3.14159)
    pi.set_color('red')
    return ln,


def update(frame):
    xdata.append(frame)
    ydata.append(convert(frame))
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=990,
                    init_func=init, blit=True)
plt.show()

ani.save('vis.mp4', writer=writer)
