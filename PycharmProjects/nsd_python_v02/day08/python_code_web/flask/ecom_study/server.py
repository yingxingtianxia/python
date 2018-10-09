#!/bin/python
# coding=utf8

from flask import Flask
from user import user
from product import product
from box import box

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(box)
app.config["SECRET_KEY"] = "test"

if __name__ == "__main__":
    app.run(debug=True)
