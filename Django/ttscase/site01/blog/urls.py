#!/usr/bin/env python3
#__*__coding: utf8__*__
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^test', test),
    url(r'^show', showList),
    url(r'^add', add),
    url(r'^edit/(?P<id>\d+)$', edit),
    url(r'^del', delete),
    url(r'^ajaxdel', ajaxDel)
]