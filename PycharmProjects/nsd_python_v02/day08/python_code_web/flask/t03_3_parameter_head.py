#!/bin/python
# coding=utf8

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def showhead():
    print "method=" + request.method
    print "path=" + request.path
    print "host=" + request.host
    print "url=" + request.url
    print "remote_addr=" + request.remote_addr
    print "-----------------"
    print "headers=" + request.headers.__str__()  # 不是简单对象,需要这样转换为字符串
    print "cookies=" + request.cookies.__str__()
    return "done"


if __name__ == '__main__':
    app.run(debug=True)
