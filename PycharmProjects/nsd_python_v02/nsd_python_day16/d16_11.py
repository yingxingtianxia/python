#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ABC'

@app.route('/')
def login_show():
    return render_template('login.html')

@app.route('/login/check')
def login_check():
    name = request.values.get('name')
    password = request.values.get('password')
    if name == 'tom' and password == '123':
        session['aa'] = '1'
        return redirect('/email/look')
    else:
        return redirect('/')

@app.route('/email/look')
def email_look():
    login_ed = session.get('aa')
    if login_ed == '1':
        return 'this is email!'
    else:
        return redirect('/')

@app.route('/email/detail')
def email_detail():
    if session.get('aa') == '1':
        return "Email-25: How are you"
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)