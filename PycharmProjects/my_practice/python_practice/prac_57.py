#!/usr/bin/env python
#--coding: utf8--
import turtle

def drawline(n=4):
    t = turtle.Pen()
    t.color(0.3, 0.8, 0.6)
    t.begin_fill()
    for i in range(n):
        t.forward(50)
        t.left(360/n)
    t.end_fill()

if __name__ == '__main__':
    drawline()