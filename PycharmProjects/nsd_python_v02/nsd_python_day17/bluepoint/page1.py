#!/usr/bin/env python3
#--*--coding: utf8--*--

from flask import Blueprint

page1 = Blueprint('page1', __name__)

@page1.route('/')
@page1.route('/page1')
def index():
    return "这是首页，也是一个独立页面1 <br><a href=/page2>去page2</a>"
