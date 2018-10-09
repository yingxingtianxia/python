#!/usr/bin/env python3
# -*-coding: utf8-*-
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.number_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk?(y/n)')
    if keep_running == 'n':
        break