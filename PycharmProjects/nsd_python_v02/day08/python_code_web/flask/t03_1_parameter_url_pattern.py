#!/bin/python
# coding=utf8

from flask import render_template, request
from flask import Flask

app = Flask(__name__)


@app.route('/test/<a>/<b>')
def test1(a, b):
    print "result1=%s,%s" % (a, b)
    return "result1=%s,%s" % (a, b)


@app.route('/test/<a>,<b>')
def test2(a, b):
    print "result2=%s,%s" % (a, b)
    return "result2=%s,%s" % (a, b)


if __name__ == '__main__':
    app.run()
