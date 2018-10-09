#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def login_show():
    data = [
        {'name':'zhangsan', 'age':40},
        {'name':'lisi', 'age':50},
        {'name':'wangwu', 'age':60},
    ]
    return render_template('list1.html', data=data)

if __name__ == '__main__':
    app.run()