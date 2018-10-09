#!/usr/bin/env python3
# -*-coding: utf8-*-
from random import choice

class RandomWalk():

    def __init__(self, number_points=5000):
        self.number_points = number_points
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        while len(self.x_value) < self.number_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step==0:
                continue
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)
