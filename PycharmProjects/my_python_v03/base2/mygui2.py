#!/usr/bin/env python3
#--*--coding: utf8--*--
import tkinter
from functools import partial

# def hello():
#     lb1.config(text='hello tedu')
#
# def welcome():
#     lb1.config(text='hello tarena')

def say_hi(word):
    def hi():
        lb1.config(text='hello %s' % word)
    return hi

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='hello world!', font='Helvetica 32 bold italic')
mybutton = partial(tkinter.Button, root, bg='blue', fg='white')
# b1 = mybutton(text='Button1', command=hello)
# b2 = mybutton(text='Button2', command=welcome)
b1 = mybutton(text='Button1', command=say_hi('tedu'))
b2 = mybutton(text='Button2', command=say_hi('tarena'))
b3 = mybutton(text='QUIT', command=root.quit)

lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()