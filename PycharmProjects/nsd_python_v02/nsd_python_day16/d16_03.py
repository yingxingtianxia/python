#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def login_show():
    return render_template('login.html')

@app.route('/login/check/')
def login_check():
    name = request.values.get('name')
    password = request.values.get('password')
    if name == 'tom' and password == '123':
        return render_template('success.html', name=name)
    else:
        return render_template('failed.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)