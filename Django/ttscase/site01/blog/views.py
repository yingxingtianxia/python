from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):

    listPost = Post.objects.all()

    return render(request, 'index.html', {'listPost': listPost})

def test(request):
    a = [1,2,3,4,5]
    b = 'hello'
    posts = Post.objects.all()

    return render(request, 'test.html', {
        'a':a,
        'b':b,
        'posts': posts,
    })

def showList(request):
    posts = Post.objects.all()

    return render(request, 'list.html', {
        'posts': posts,
    })

def add(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.desc = request.POST.get('desc')
        post.author = request.POST.get('author')
        post.content = request.POST.get('content')
        post.save()

        return HttpResponseRedirect('/blog/show')
    else:
        return render(request, 'edit.html', {
            'action': '/blog/add',
        })

def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.desc = request.POST.get('desc')
        post.author = request.POST.get('author')
        post.content = request.POST.get('content')
        post.save()

        return HttpResponseRedirect('/blog/show')
    else:
        return render(request, 'edit.html', locals())


def delete(request):
    id = request.GET.get('id')
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/blog/show')


def ajaxDel(request):
    return JsonResponse({
        'code':0,
        "msg":"删除成功",
    })