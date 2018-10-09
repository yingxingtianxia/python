#!/usr/bin/env python3
# -*-coding: utf8-*-
from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist._title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = "Results"
hist._y_title = "Frequency of results"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')