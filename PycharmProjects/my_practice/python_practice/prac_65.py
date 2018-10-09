#!/usr/bin/env python
#--coding: utf8--
import math
from Tkinter import *

class PTS():
    def __init__(self):
        self.x = 0
        self.y = 0

points = []
def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w/2
    ycenter = h/2
    redius = (h-30) / (AspectRatio*2)-20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * redius)
        p.y = ycenter + int(math.sin(rads) * redius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(
        xcenter - redius, ycenter - redius,
        xcenter + redius, ycenter + redius
    )
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

    canvas.pack()
    mainloop()

if __name__ == '__main__':
    LineToDemo()