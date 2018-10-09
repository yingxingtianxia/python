#!/usr/bin/env python
#--*--coding: utf8--*--
from flask import Flask

app = Flask(__name__)

@app.route('/abc')
def aa():
    print('121')
    return '12'

if __name__ == '__main__':
    app.run()