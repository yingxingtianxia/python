#!/usr/bin/env python3
#--*--coding: utf8--*--
import tarfile

tar = tarfile.open('/tmp/aaa.tar.gz', 'w:gz')
tar.add('/etc/passwd')
tar.add('/etc/hosts')
tar.close()