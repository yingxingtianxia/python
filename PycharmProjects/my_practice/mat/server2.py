#!/usr/bin/env python3
# -*-coding: utf8-*-
from flask import Flask
app = Flask(__name__)

@app.route('/abc')
def aaaa():
    print('12')
    return 'hello 12'

if __name__ == '__main__':
    app.run()