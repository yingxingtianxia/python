#!/usr/bin/env python3
#__*__coding: utf8__*__
from .views import *
from django.conf.urls import url
from django.contrib.auth.views import login


#app_name = '[users]'


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^register/$', register, name='register'),
]
