#!/bin/python
# coding=utf8

from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/testget', )
def test():
    xm = request.values.get("xm")
    return "你Post提交了:%s" % xm



if __name__ == '__main__':
    app.run()
