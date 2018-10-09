#!/usr/bin/env python3
#--*--coding: utf8--*--
import hashlib
import tarfile
import time
import os
import pickle

def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def full_back(src_dir, dst_dir, md5file):
    #路径定义
    fname = os.path.basename(src_dir.rstrip('/'))
    date = time.strftime('%Y%m%d')
    fname = '%s_full_%s.tar.gz' % (fname, date)
    fname = os.path.join(dst_dir, fname)
    #完全备份
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()
    #记录md5值
    md5_dic = {}
    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            md5_dic[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5_dic, fobj, True)


def incr_back(src_dir, dst_dir, md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    date = time.strftime('%Y%m%d')
    fname = '%s_full_%s.tar.gz' % (fname, date)
    fname = os.path.join(dst_dir, fname)
    md5_dic = {}

    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            md5_dic[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5_dic, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in md5_dic:
        if old_md5.get(key) != md5_dic[key]:
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    src_dir = '/tmp/aa'
    dst_dir = '/tmp/bb'
    md5file = '/tmp/md5.data'
    day = time.strftime('%A')
    if day == 'Sunday':
        full_back(src_dir, dst_dir, md5file)
    else:
        incr_back(src_dir, dst_dir, md5file)