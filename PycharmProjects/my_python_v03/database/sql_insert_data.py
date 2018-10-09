#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments
from my_python_v03.database.sql_orm import Empolyees
from my_python_v03.database.sql_orm import Salary
from my_python_v03.database.sql_orm import session
from datetime import datetime

#定义部门表实例
dep_hr = Departments(dep_name='人事部')
dep_dev = Departments(dep_name='开发部')
dep_ops = Departments(dep_name='运维部')
dep_inf = Departments(dep_name='财务部')
dep_sc = Departments(dep_name='市场部')
dep_sail = Departments(dep_name='销售部')
dep_xz = Departments(dep_name='行政部')
#定义员工表实例
emp_zhangsan = Empolyees(
    emp_name = '张三',
    gender = 'male',
    phone = '13999998888',
    email = 'zhangsan@tarena.cn',
    dep_id = 1
)

emp_lisi = Empolyees(
    emp_name = '李四',
    gender = 'male',
    phone = '13277889900',
    email = 'lisi@tarena.cn',
    dep_id = 1
)

emp_wangxiaowu = Empolyees(
    emp_name = '王小五',
    gender = 'female',
    phone = '15011223344',
    email = 'wangxiaowu@tarena.cn',
    dep_id = 2
)

emp_wangermazi = Empolyees(
    emp_name = '王二麻子',
    gender = 'male',
    phone = '15100998877',
    email = 'wangermazi@tarena.cn',
    dep_id = 3
)

emp_chendaxian = Empolyees(
    emp_name = '陈大仙',
    gender = 'male',
    phone = '15998766789',
    email = 'chendaxian@tarena.cn',
    dep_id = 2
)

emp_zhangdashen = Empolyees(
    emp_name = '张大神',
    gender = 'male',
    phone = '13888889999',
    email = 'zhangdashen@tarena.cn',
    dep_id = 3
)

emp_linmeimei = Empolyees(
    emp_name = '林妹妹',
    gender = 'female',
    phone = '18667899876',
    email = 'linmeimei@tarena.cn',
    dep_id = 4
)

emp_fangxiaojie = Empolyees(
    emp_name = '方小姐',
    gender = 'female',
    phone = '17719199191',
    email = 'fangxiaojie@tarena.cn',
    dep_id = 5
)

emp_geerdan = Empolyees(
    emp_name = '格尔但',
    gender = 'male',
    phone = '15533221199',
    email = 'geerdan@tarena.cn',
    dep_id = 6
)

emp_ayiguli = Empolyees(
    emp_name = '阿依古丽',
    gender = 'female',
    phone = '17867768998',
    email = 'ayiguli',
    dep_id = 7
)
#定义工资实例
sal_1 = Salary(
    date = datetime.date(datetime.now()),
    emp_id = 1,
    basic = 8000,
    award = 1000
)

sal_2 = Salary(
    date = datetime.date(datetime.now()),
    emp_id = 2,
    basic = 7000,
    award = 2000
)

sal_3 = Salary(
    date = datetime.date(datetime.now()),
    emp_id = 3,
    basic = 4000,
    award = 500
)

sal_4 = Salary(
    date = datetime.date(datetime.now()),
    emp_id = 4,
    basic = 5000,
    award = 4000
)

#提交部门表实例
session.add_all([dep_hr, dep_dev, dep_ops, dep_inf, dep_sc, dep_sail, dep_xz])
session.commit()
#提交员工表实例
session.add_all([emp_zhangsan, emp_lisi, emp_wangxiaowu, emp_wangermazi, emp_chendaxian,
                 emp_zhangdashen, emp_linmeimei, emp_fangxiaojie, emp_geerdan, emp_ayiguli])
session.commit()
#提交工资表实例
session.add_all([sal_1, sal_2, sal_3, sal_4])
session.commit()