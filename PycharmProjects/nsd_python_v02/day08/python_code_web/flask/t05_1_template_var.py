#!/bin/python
# coding=utf8

from flask import Flask
from flask import render_template

app = Flask(__name__)


# http://127.0.0.1:5000/test3_form.html

@app.route('/test')
def test():
    msg="Tom"
    return render_template("template_var.html", msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
