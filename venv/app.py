# Monte-Carlo Algorithm visualisation

# Imports:
import os
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


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

    np.savetxt('data100k.csv', results, delimiter=',')


def visualize():
    my_data = pd.read_csv('data.csv')
    plt.plot(my_data)
    pi = plt.axhline(y=3.14159)
    pi.set_color('red')
    plt.show()


# get_csv(100000)
visualize()

'''

SecureRandom random = new SecureRandom();

        double counter = 0;
        double totalPoints = 10000000;
        double ratio = 0;
        double x = 0;
        double y = 0;
        double pi = 0;

        for (int i = 0; i <= totalPoints; i++) {
            x = random.nextDouble();
            y = random.nextDouble();
            if((Math.pow(x, 2) + Math.pow(y, 2)) <= 1){
                counter++;
            }
        }

        ratio = counter / totalPoints;
        pi = ratio * 4;
        System.out.println(pi);

    '''
