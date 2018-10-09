#!/bin/python
# coding=utf8

from flask import session
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"

uname = 'taa'


@app.route('/page1/<m>')
def page1(m):
    global uname
    uname = m
    return u"设个值 %s"% m


@app.route('/page2')
def page2():
    global uname
    return u"取值" + uname


if __name__ == '__main__':
    app.run(debug=True)
