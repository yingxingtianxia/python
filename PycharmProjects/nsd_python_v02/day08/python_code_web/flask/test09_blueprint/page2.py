#!/bin/python
# coding=utf8

from flask import Blueprint

page2 = Blueprint('page2', __name__)


@page2.route('/page2')
def index():
    return u"这是一个独立页2"
