#!/usr/bin/env python
#--coding: utf8--
import Tkinter as tk
from functools import partial

def say_hello(word):
    def say_hi():
        mylabel.config(text='Hello %s' % word)
    return say_hi

root = tk.Tk()
mylabel = tk.Label(root, text='Welcome', font='Arial 20')
mybutton = partial(
    tk.Button,
    root,
    foreground='white',
    background='blue',
    font='Arial 20'
)
b1 = mybutton(text='Button1', command=say_hello('World'))
b2 = mybutton(text='Button2', command=say_hello('China'))
qb = mybutton(foreground='red', text='quit', command=root.quit)
mylabel.pack()
b1.pack()
b2.pack()
qb.pack()
root.mainloop()