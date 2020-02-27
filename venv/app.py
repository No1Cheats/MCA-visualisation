#Monte-Carlo Algorithm visualisation

#Imports:
import os
import random
import numpy as np

#Funcations:
def calc_pi(points):

    counter = 0
    total_points = points
    ratio = 0
    x = 0
    y = 0
    pi = 0

    for i in range(0,total_points):
        x = random.random()
        y = random.random()
        if(x**2 + y**2 <= 1):
            counter += 1
            ratio = counter / total_points

    ratio = counter / total_points
    pi = ratio * 4
    return pi



def visualisze(amount_of_iterations):
    results = []
    for i in range (1,amount_of_iterations):
        results.append(calc_pi(i))

    np.savetxt('data.csv', (results), delimiter=',')

visualisze(1000)








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