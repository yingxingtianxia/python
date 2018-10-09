#!/usr/bin/env python3
#--*--coding: utf8--*--
import tkinter
from functools import partial

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='hello world!', font='Helvetica 32 bold italic')
mybutton = partial(tkinter.Button, root, bg='blue', fg='white')
b1 = mybutton(text='Button1')
b2 = mybutton(text='Button2')
b3 = mybutton(text='QUIT', command=root.quit)

lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()