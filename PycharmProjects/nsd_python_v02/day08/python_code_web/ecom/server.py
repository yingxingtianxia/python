#!/bin/python
# coding=utf8

from flask import Flask
from modules.login import login
from modules.product import product
from modules.cart import cart
from modules.bill import bill

app = Flask(__name__, template_folder="views", static_url_path='', static_folder='')
app.config["SECRET_KEY"] = "test"

app.register_blueprint(login)
app.register_blueprint(product)
app.register_blueprint(cart)
app.register_blueprint(bill)

if __name__ == "__main__":
    app.run(debug=True)
