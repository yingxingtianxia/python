#!/usr/bin/env python3
#__*__coding: utf8__*__
import tarfile

tar = tarfile.open('tar_if.tar.gz','w:gz')
tar.add('if1.py',arcname='if_1.py')
tar.add('if2.py')
tar.add('/etc/httpd')
tar.close()