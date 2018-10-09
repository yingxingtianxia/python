#!/bin/python
# coding=utf8

from flask import Flask
app=Flask(__name__)


@app.errorhandler(404)
def to404(e):
    return "Hi, I cannot find it!"

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()






