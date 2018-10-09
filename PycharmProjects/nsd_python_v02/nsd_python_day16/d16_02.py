#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def handler():
    name = request.values.get("name")
    return render_template('a.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)