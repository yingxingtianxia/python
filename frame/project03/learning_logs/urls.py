#定义learning_logs的urls文件
from django.conf.urls import url
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
    #主题页
    url(r'^topics/$', views.topics, name='topics'),
    #详细信息页
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #添加主题页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #添加记录页
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #修改记录页
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]