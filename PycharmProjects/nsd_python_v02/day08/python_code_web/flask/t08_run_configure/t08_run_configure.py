#!/bin/python
# coding=utf8

from flask import Flask,render_template

app = Flask(__name__, template_folder="views", static_url_path='/res', static_folder='http_resource')


@app.route('/')
def page1():
    return '<img src=/res/images/baby.jpg>'


@app.route('/b')
def page2():
    return render_template("tmp1.html")

@app.route("/long")
def long_fun():
    import time
    time.sleep(10)
    return "done, I finished a long task!"


if __name__ == '__main__':
    app.run(debug=True, port=4000, host="127.0.0.1", threaded=True)
