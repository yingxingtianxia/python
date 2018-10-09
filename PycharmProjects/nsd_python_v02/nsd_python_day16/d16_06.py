#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def login_show():
    data = range(1,100)
    return render_template('list.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)