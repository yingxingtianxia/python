#!/usr/bin/env python3
#__*__coding: utf8__*__
import tarfile

tar_file = 'nginx-1.12.2.tar.gz'
tar = tarfile.open(tar_file)
#tar.extractall('/tmp')
items = tar.getmembers()
for item in items:
    tar.extract(item,'/tmp')
tar.close()