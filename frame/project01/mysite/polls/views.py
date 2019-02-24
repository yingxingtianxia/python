from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

#request bixu tigong biaoshi yonghu qingqiu
def index(request):
    return HttpResponse('<h1>Polls OK</h1>')