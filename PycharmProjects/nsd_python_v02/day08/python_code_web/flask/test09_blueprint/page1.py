#!/bin/python
# coding=utf8

from flask import Blueprint

page1 = Blueprint('page1', __name__)


@page1.route('/')
@page1.route('/page1')
def index():
    return u"这是首页,也是一个独立页1 <br><a href=/page2>去第2页</a>"
