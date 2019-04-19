#!/bin/bash
s_time=`date -d "$(mysql -uroot -p123456 tedu -e "select ts from password order by id DESC limit 1" | tail -1)" +%s`
n_time=`date +%s`

r_time=`echo "${n_time} - ${s_time}" | bc`
if [ ${r_time} -gt 1800 ];then
    echo "yes"
else
    echo "no"
fi 
