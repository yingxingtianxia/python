#!/usr/bin/env python3
#__*__coding: utf8__*__
from django.conf.urls import url
from .views import *

app_name = '[learning_logs]'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^topics/$', topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', topic, name='topic'),
    url(r'^new_topic/$', new_topic, name='new_topic'),
    url(r'^new_topic/(?P<topic_id>\d+)/$', new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', edit_entry, name='edit_entry'),
]
