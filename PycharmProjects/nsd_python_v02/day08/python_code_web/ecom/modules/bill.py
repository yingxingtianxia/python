#!/bin/python
# coding=utf8
import time

from flask import Blueprint, request, session

from DB import query, getMaxId
from cart_manager import cart_manager

bill = Blueprint('bill', __name__)


@bill.route('/bill/add')
def cart_list():
    cm=cart_manager()
    return cm.bill()


@bill.route('/bill/list')
def bill_list():
    return "bill_list"
