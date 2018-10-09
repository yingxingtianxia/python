#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def login_show():
    return render_template('login2.html', msg={})

@app.route('/login/check')
def login_check():
    name = request.values.get('name')
    password = request.values.get('password')
    errormsg = {}

    if name != 'tom':
        errormsg['name'] = 'Username is wrong!'
    if password != '123':
        errormsg['password'] = 'Password is wrong!'

    if errormsg == {}:
        return render_template('success.html', name=name)
    else:
        return render_template('login2.html', name=name, password=password,msg=errormsg)


if __name__ == '__main__':
    app.run(debug=True)