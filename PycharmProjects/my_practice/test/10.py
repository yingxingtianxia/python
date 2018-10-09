#!/usr/bin/env python3
# -*-coding: utf8-*-
gs = {"x":10, "y":20}
ls = {"x":1, "y":2}
exec("z=x+y", gs, ls)
print(ls)
print()