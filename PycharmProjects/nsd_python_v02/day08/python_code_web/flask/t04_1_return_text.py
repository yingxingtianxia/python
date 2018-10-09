#!/bin/python
# coding=utf8

from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    xm = request.values.get("xm")
    if xm!="tom":
        msg = "<img src=/static/cry.jpg><br><span style='color:red;font-size:20px'>你的注册名称不对!<span>"
    else:
        msg = "<img src=/static/smile.jpg><span style='color:green;font-size:30px'>欢迎你!<span>"

    return msg


if __name__ == '__main__':
    app.run()
