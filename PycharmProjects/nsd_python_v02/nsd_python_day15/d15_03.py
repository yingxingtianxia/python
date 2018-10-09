#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask

app = Flask(__name__)

@app.route('/user/add/<name>/<age>')
def user_add(name, age):
    res = "name=%s, age=%s" % (name, age)
    return res

if __name__ == '__main__':
    app.run()