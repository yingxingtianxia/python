#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello to flask"

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')