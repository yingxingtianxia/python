#!/usr/bin/env python
#--coding: utf8--
person = {'zhang':18, 'wang':45, 'li':22, 'zhao':66}
m = 'zhang'
for key in person.keys():
    if person[m] < person[key]:
        m = key

print '%s:%d' % (m, person[m])