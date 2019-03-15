from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#学习笔记主页
def index(request):

    return render(request, 'learning_logs/index.html')


#显示所有的主题
@login_required
def topics(request):
    #显示用户自己的主题
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    return render(request, 'learning_logs/topics.html', {'topics': topics})


#显示单个主题及其所有的项目
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    #确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('date_added')

    return render(request, 'learning_logs/topic.html', {'topic': topic, 'entries': entries})


#添加新主题
@login_required
def new_topic(request):
    if request.method != 'POST':
        #未提交数据，创建一个新的表单
        form = TopicForm()
    else:
        #通过表单post提交了数据，进行数据处理
        form = TopicForm(request.POST)
        if form.is_valid():
            #将新主题关联到用户
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return HttpResponseRedirect(reverse('learning_logs:topics'))

    return render(request, 'learning_logs/new_topic.html', {'form': form})


#添加新记录
@login_required
def new_entry(request, topic_id):
    #在指定主题下添加条目
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #未提交数据，创建一个空表单
        form = EntryForm()
    else:
        #post提交数据并进行数据处理
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    return render(request, 'learning_logs/new_entry.html', {'topic': topic, 'form': form})


#编辑已经存在的记录
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #保护编辑页面
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #首次提交为get请求，将已有记录展示
        form = EntryForm(instance=entry)
    else:
        #本此提交为post请求，处理post上来的数据
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)