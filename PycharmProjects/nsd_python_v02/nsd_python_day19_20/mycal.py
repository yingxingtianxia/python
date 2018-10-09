#!/usr/bin/env python3
#--*--coding: utf8--*--
act_count = 0
def cal(log):
    global act_count
    if log['act'] == 'play' and log['sdate'] == '2018-08-17':
        act_count = act_count + 1

    return act_count