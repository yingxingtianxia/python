#!/usr/bin/env python3
#__*__coding: utf8__*__
import tarfile

# tar = tarfile.open('tar_if.tar.gz','w:gz')
# tar.add('if1.py',arcname='if_1.py')
# tar.add('/etc/httpd/')
# # tar.close()
#
# tar = tarfile.open('tar_if.tar.gz')
# members = tar.getmembers()
# for item in members:
#     print(item)

tar_file = "nginx-1.12.2.tar.gz"
tar = tarfile.open(tar_file)
# tar.extractall('/media')
items = tar.getmembers()
for item in items:
    tar.extract(item,'/media')
tar.close()