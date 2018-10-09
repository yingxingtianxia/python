#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def handler1():
    res = "<font color=red size=100>hello</font>"
    return res

@app.route('/score')
def handler2():
    score = request.values.get('score')
    n = int(score)
    if n < 60:
        return redirect("/static/flunk.html")
    elif n >= 60 and n< 80:
        return redirect("/static/normal.html")
    else:
        return redirect("/static/excellent.html")

@app.route('/form')
def handler3():
    name = request.values.get('name')
    if name:
        return "You submit: name = %s" % name
    else:
        return "<form>" \
               "name <input name=name>" \
               "<input type=submit value=go>" \
               "</from>"



if __name__ == '__main__':
    app.run()