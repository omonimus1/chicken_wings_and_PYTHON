# Author: Davide Pollicino
# Date: 21/12/2019
#!/usr/bin/env python

"""
    Application that calculates the distance between two
    points.
"""
import math


def get_coordinates():
    x1 = int(input('X of the first point: '))
    y1 = int(input('y of the first point: '))
    x2 = int(input('x of the second point: '))
    y2 = int(input('y of the first point: '))
    distance = calculate_distance(x1, y1, x2, y2)
    return distance


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))


distance = get_coordinates()
print("Distance: {0}".format(distance))