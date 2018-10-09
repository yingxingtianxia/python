#!/bin/python
# coding=utf8

from flask import Blueprint

page = Blueprint('product', __name__)


@page.route('/product/list')
def product_list():
    return "product list"


@page.route('/product/add_to_cart')
def product_add_to_cart():
    return "product_add_to_cart"

