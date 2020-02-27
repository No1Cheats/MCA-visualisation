import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')
my_list = [4, 3, 4, 3.4, 3, 3.1]


def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(2, 6)
    return ln,


def update(frame):
    xdata.append(frame)
    ydata.append(my_list[frame])
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=5, init_func=init, blit=True)
plt.show()

#ani.save('vis.mp4', writer=writer)
