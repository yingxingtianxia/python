#!/bin/python
# coding=utf8
import time

from flask import Flask
from flask import session

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"


@app.route('/set')
def myset():
    session["user"] = "tom %s" % str(time.time())
    return "没有值,现在设个值tom"


@app.route('/get')
def myget():
    return "值:" + session.get("user")


if __name__ == '__main__':
    app.run(debug=True)
