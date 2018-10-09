#!/bin/bash

rpm -i tar-1.23-15.el6_8.x86_64.rpm

pin(){
	install -d ./tmp
	tar xf $1 -C ./tmp 
	cd tmp/*
	python setup.py install
	cd ../..
	rm -fr ./tmp
}


pin setuptools-22.0.0.tar.gz 
pin Werkzeug-0.11.10.tar.gz 
pin MarkupSafe-0.23.tar.gz 
pin Jinja2-2.8.tar.gz
pin pytz-2016.6.1.tar.gz
pin Babel-2.3.4.tar.gz 
pin itsdangerous-0.24.tar.gz
pin click-6.6.tar.gz 
pin Flask-0.11.1.tar.gz  
pin Flask-Login-0.4.0.tar.gz
pin Django-1.9.6.tar.gz

pin pycurl-7.21.5.tar.gz
pin redis-2.10.5.tar.gz
pin xlrd-0.9.4.tar.gz
pin xlwt-1.0.0.tar.gz
pin xlutils-1.7.1.tar.gz

pin mysql-connector-2.1.3.tar.gz 
pin importlib-1.0.4.tar.gz 
pin gevent-1.2.0.tar.gz
pin gevent-websocket-0.9.5.tar.gz




