from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#注销用户
def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('learning_logs:index'))


#注册用户
def register(request):
    if request.method != 'POST':
        #首次请求为get，创建空表单
        form = UserCreationForm()
    else:
        #处理post上来的数据
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登陆，重定向到主页
            authenticated_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
            )
            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('learning_logs:index'))

    return render(request, 'users/register.html', {'form': form})