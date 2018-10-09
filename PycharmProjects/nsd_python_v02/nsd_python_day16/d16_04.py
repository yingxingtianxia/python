#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def login_show():
    return render_template('login1.html')

@app.route('/login/check')
def login_check():
    name = request.values.get('name')
    password = request.values.get('password')
    errormsg = ''

    if name == 'tom':
        if password == '123':
            return render_template('success.html', name=name)
        else:
            errormsg+='Password is wrong!'
    else:
        errormsg += 'Username is wrong!'

    return render_template('login1.html', name=name, msg=errormsg)

if __name__ == '__main__':
    app.run(debug=True)