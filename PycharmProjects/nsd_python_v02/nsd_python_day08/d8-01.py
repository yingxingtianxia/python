#!/usr/bin/env python
#--coding: utf8--
import cPickle as p
import hashlib
import os
import tarfile
import time

def check_md5(fname):
    m = hashlib.md5()
    with open(fname) as fobj:
        while True:
            data = fobj.read(4096)
            if data == '':
                break
            m.update(data)

def full_backup(src_dir, dst_dir, md5_file):
    md5_dict = {}
    backup_name = '%s_full_%s.tar.gz' % (
        os.path.basename(src_dir.rstrip('/')),
        time.strftime('%Y%m%d')
    )
    full_backname = os.path.join(dst_dir, backup_name)
    tar = tarfile.open(full_backname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    for path, folder, files in os.walk(src_dir):
        for file in files:
            abs_path = os.path.join(path, file)
            md5_dict[abs_path] = check_md5(abs_path)

    with open(md5_file, 'w') as fobj:
        p.dump(md5_dict, fobj)

def incr_backup(src_dir, dst_dir, md5_file):
    new_md5 = {}
    backup_name = '%s_incr_%s.tar.gz' % (
        os.path.basename(src_dir.rstrip('/')),
        time.strftime('%Y%m%d')
    )
    incr_backname = os.path.join(dst_dir, backup_name)

    with open(md5_file) as fobj:
        old_md5 = p.load(fobj)

    for path, folder, files in os.walk(src_dir):
        for file in files:
            abs_path = os.path.join(path, file)
            new_md5[abs_path] = check_md5(abs_path)

    with open(md5_file, 'w') as fobj:
        p.dump(new_md5, fobj)

    tar = tarfile.open(incr_backname, 'w:gz')
    for key in new_md5:
        if new_md5[key] != old_md5[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src_dir = '/root/test/'
    dst_dir = '/tmp/backup/'
    md5_file = '/tmp/backup/md5.data'
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    if time.strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir)
    else:
        incr_backup(src_dir, dst_dir)