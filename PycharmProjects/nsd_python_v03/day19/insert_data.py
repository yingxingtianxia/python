from myorm import Departments, Employees, Salary, session
from datetime import datetime

dep_hr = Departments(dep_name='人事部')
dep_dev = Departments(dep_name='开发部')
emp_bob = Employees(
    emp_name='bob',
    gender='male',
    phone='13355667788',
    email='bob@tedu.cn',
    dep_id=1
)
sal_bob_201803 = Salary(
    emp_id = 1,
    date=datetime.date(datetime.now()),
    basic=10000,
    award=5000
)
session.add_all([dep_hr, dep_dev])
session.commit()
session.add(emp_bob)
session.commit()
session.add(sal_bob_201803)
session.commit()


