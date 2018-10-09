#!/bin/python
# coding=utf8

from flask import Blueprint, request, render_template, redirect

from cart_manager import cart_manager

cart = Blueprint('cart', __name__)


@cart.route('/cart/list')
def cart_list():
    cm = cart_manager()
    rows = cm.getItems()
    total = cm.total()
    return render_template("cart_list.html", rows=rows, total=total)


@cart.route('/cart/del')
def cart_del():
    pid = request.values.get("pid");
    cm = cart_manager()
    cm.del_product(pid)
    return redirect("/cart/list")


@cart.route('/cart/add')
def product_add_to_cart():
    pid = request.values.get("pid");
    pcount = request.values.get("pcount");
    cm = cart_manager()
    cm.add_product(pid, int(pcount));
    print cm.getItems()
    return cm.size()
