#!/bin/python
# coding=utf8

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/testpost', methods=['GET', 'POST'])
def test():
    xm = request.values.get("xm")
    return "你输入了:%s" % xm


if __name__ == '__main__':
    app.run()
