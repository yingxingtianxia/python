#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask

app = Flask(__name__)

my = []
@app.route('/')
def a():
    my.append('test')
    return str(my)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, processes=3)