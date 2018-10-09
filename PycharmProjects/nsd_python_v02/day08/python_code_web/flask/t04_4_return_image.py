#!/bin/python
# coding=utf8

from flask import request, redirect, url_for
from flask import Flask

app = Flask(__name__)


@app.route('/img')
def img():
    f = file("static/cry.jpg", "r")
    bytes = f.read()
    return bytes, 200, {'Content-Type': 'image/jpeg'}


if __name__ == '__main__':
    app.run(debug=True)
