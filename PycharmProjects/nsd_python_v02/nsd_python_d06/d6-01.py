#！/usr/bin/env python3
#--*--coding: utf8--*--
import sys

def unix2dos(filename, linesep='\r\n'):
    new_filename = filename + '.txt'
    src_fobj = open(filename)
    dst_fobj = open(new_filename, 'w')

    for line in src_fobj:
        new_line = line.rstrip('\r\n') + linesep
        dst_fobj.write(new_line)

    src_fobj.close()
    dst_fobj.close()

if __name__ == '__main__':
    unix2dos(sys.argv[1])     #unix2dos
    unix2dos(sys.argv[1], '\n')     #dos2unix