#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask, request

app = Flask(__name__)

@app.route('/user/add', methods=['GET','POST'])
def user_add():
    name = request.args.get('name')
    age = request.args.get('age')
    res = "http get: name=%s,age=%s"%(name,age)

    return res

if __name__ == '__main__':
    app.run()