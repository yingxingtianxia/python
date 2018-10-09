#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
import time

app = Flask(__name__, template_folder='view',
            static_url_path='/res',
            static_folder='http_resource')

@app.route('/')
def page1():
    return '<img src=/res/images/baby.jpg>'

@app.route('/b')
def page2():
    return render_template("tmp1.html")

@app.route('/long')
def long_fun():
    time.sleep(10)
    return "done, I finished a long task"

if __name__ == '__main__':
    app.run(debug=True, port=4000, host="0.0.0.0", threaded=True)