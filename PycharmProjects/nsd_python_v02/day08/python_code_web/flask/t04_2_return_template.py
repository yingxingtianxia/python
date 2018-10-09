#!/bin/python
# coding=utf8

from flask import request, render_template
from flask import Flask

app = Flask(__name__)


# http://127.0.0.1:5000/test3_form.html

@app.route('/template1')
def test():
    return render_template("abc")


if __name__ == '__main__':
    app.run(debug=True)
