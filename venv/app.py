# Monte-Carlo Algorithm visualisation

# Imports:
import os
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import csv


# Functions:
def calc_pi(points):
    counter = 0
    total_points = points
    ratio = 0
    x = 0
    y = 0
    pi = 0

    for i in range(0, total_points):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            counter += 1
            ratio = counter / total_points

    ratio = counter / total_points
    pi = ratio * 4
    return pi


def get_csv(amount_of_iterations):
    results = []
    for i in range(1, amount_of_iterations):
        results.append(calc_pi(i))

    np.savetxt('data10k.csv', results, delimiter=',')


def visualize_static():
    my_data = pd.read_csv('data.csv')
    plt.plot(my_data)
    pi = plt.axhline(y=3.14159)
    pi.set_color('red')
    plt.show()

get_csv(10000)
#visualize_static()
