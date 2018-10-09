#!/usr/bin/env python3
# -*-coding: utf8-*-
from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run()