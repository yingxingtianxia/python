#!/usr/bin/env python3
#--*--coding: utf8--*--
import os
os.mkdir('/tmp/demo')
os.listdir('/tmp/demo')
os.symlink('/etc/hosts', '/tmp/demo/zhuji')
os.chdir('/tmp/demo/')
os.getcwd()
os.curdir