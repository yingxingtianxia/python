#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Blueprint
from nsd_python_v02.nsd_python_day18.mods.cart_box import *
from flask import session
from flask import request

blue_cart = Blueprint('blue_cart', __name__)

@blue_cart.route('/cart/add', methods=['GET', 'POST'])
def cart_add():
    pid = request.values.get('pid')
    pcount = request.values.get('pcount')
    c = session.get('cart')
    if c:
        c.add(pcount)
    else:
        c = Cart_Box()
        c.add(pcount)
    #session['cart'] = c
    return str(c.counts())