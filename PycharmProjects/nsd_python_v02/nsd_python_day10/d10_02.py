#!/usr/bin/env python
#--coding: utf8--
import sys

print 'Welcome.'
print 'Please Input strings:'
sys.stdout.flush()


line = sys.stdin.readline(1024).strip()
print 'you entered %s' % line
print 'you entered %d characters' % len(line)

