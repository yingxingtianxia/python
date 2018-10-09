#!/usr/bin/env python
#--coding: utf8--
import Tkinter as tk
from functools import partial

root = tk.Tk()
mylabel = tk.Label(root, text='Welcome', font='Arial 20')
mybutton = partial(
    tk.Button,
    root,
    foreground='white',
    background='blue',
    font='Arial 20'
)
b1 = mybutton(text='Button1')
b2 = mybutton(text='Button2')
qb = mybutton(foreground='red', text='quit', command=root.quit)
mylabel.pack()
b1.pack()
b2.pack()
qb.pack()
root.mainloop()