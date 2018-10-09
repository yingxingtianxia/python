#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from page1 import page1
from page2 import page2

app = Flask(__name__)
app.config['SECTET_KEY'] = 'TEST'

app.register_blueprint(page1)
app.register_blueprint(page2)

if __name__ == '__main__':
    app.run(debug=True)