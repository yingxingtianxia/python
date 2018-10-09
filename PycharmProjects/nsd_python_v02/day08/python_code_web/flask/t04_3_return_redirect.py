#!/bin/python
# coding=utf8

from flask import request, redirect, url_for
from flask import Flask

app = Flask(__name__)

@app.route('/a')
def a():
    xm = request.values.get("xm")
    if xm == "tom":
        return redirect("/b")
    else:
        return redirect("/c")

@app.route('/b')
def b():
    return "this is b"

@app.route('/c')
def c():
    return "this is c"

if __name__ == '__main__':
    app.run(debug=True)
