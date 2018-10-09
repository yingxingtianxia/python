#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Blueprint

page2 = Blueprint('page2', __name__)

@page2.route('/page2')
def index():
    return "这是一个独立页面2"
