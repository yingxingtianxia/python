#!/data/python/frame/djenv/bin/python
#创建动态主机清单脚本
#该文件具有可执行权限
#执行结果以json的格式返回

#规划格式
# {
#     'group1': {'hosts': ['host1', 'host2',...]},
#     'group2': {'hosts': ['host1', 'host2',...]},
# }
#######################################
#此方法文件不能直接执行，放弃
# import json
# from webansi.models import HostGroup
#
# groups = HostGroup.objects.all()
#
# res = {}
#
# for group in groups:
#     res[group.group_name] = {}
#     res[group.group_name]['hosts'] = []
#     hosts = group.host_set.all()            #取出该组所有主机的实例
#
#     for host in hosts:
#         res[group.group_name]['hosts'].append(host.ipaddr)
#
# print(json.dumps(res))

###############################################################
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json

engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/myansi?charset=utf8',
    encoding='utf8'
)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(30), unique=True)

    def __str__(self):
        return self.group_name


class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(50), unique=True)
    ipaddr = Column(String(15))
    hostgroup_id = Column(Integer, ForeignKey('webansi_hostgruop.id'))

    def __str__(self):
        return "<%s: %s>" % (self.hostname, self.ipaddr)


if __name__ == '__main__':
    session = Session()
    groups = session.query(HostGroup.group_name, Host.ipaddr).join(Host,HostGroup.id==Host.hostgroup_id)

    res = {}
    for group, host in groups.all():
        if group not in res:
            res[group] = {}
            res[group]['hosts'] = [host]
        else:
            res[group]['hosts'].append(host)

    print(json.dumps(res))