from django.shortcuts import render
from django.shortcuts import redirect
from .models import Host, HostGroup, AnsibleModule, ModuleArg

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants  as C


# Create your views here.

def index(request):
    return render(request, 'index.html')

#使用ansible-cmdb生成所有主机信息的页面，然后在mainpage中直接render
#为了使页面中的数据是时时的，可以把生成ansible-cmdb页面的语句放到计划任务
# ansible all -m setup --tree out/
# ansible-cmdb out/ > ../webansi/templates/mywebansi/mainpage.html
def mainpage(request):

    return render(request, 'mywebansi/mainpage.html')

#页面上边是添加主机信息部分，下边是主机和主机组的列表
#判断页面方法，如果是get从数据库查询列表并返回前端，如果是post，则提取出来post上来的
#参数，然后写入数据库，写入数据动作完成后重定向到get页面
def addhosts(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        ip = request.POST.get('ip')
        group = request.POST.get('group')

        delhost = request.POST.get('delhost')

        delgroup = request.POST.get('delgroup')

        if host and ip and group:
            g = HostGroup.objects.get_or_create(group_name=group)[0]
            g.host_set.get_or_create(hostname=host, ipaddr=ip)

            return redirect(addhosts)

        elif delhost:
            dh = Host.objects.filter(hostname=delhost)
            if dh:
                dh.delete()

                return redirect(addhosts)

        elif delgroup:
            dg = HostGroup.objects.filter(group_name=delgroup)
            if dg:
                dg.delete()

                return redirect(addhosts)


    groups = HostGroup.objects.all()

    return render(request, 'mywebansi/addhosts.html', {'groups': groups})



def addmodules(request):
    if request.method == 'POST':
        mod = request.POST.get('mod_name')
        arg = request.POST.get('arg')

        delmod = request.POST.get('delmod')

        delarg = request.POST.get('delarg')

        if mod and arg:
            m = AnsibleModule.objects.get_or_create(mod_name=mod)[0]
            m.modulearg_set.get_or_create(arg_text=arg)

            return redirect(addmodules)

        elif delmod:
            dm = AnsibleModule.objects.filter(mod_name=delmod)
            if dm:
                dm.delete()

                return redirect(addmodules)

        elif delarg:
            da = ModuleArg.objects.filter(arg_text=delarg)
            if da:
                da.delete()

                return redirect(addmodules)

    mods = AnsibleModule.objects.all()

    return render(request, 'mywebansi/addmodules.html', {'mods': mods})


def exec_task(servers, mod, arg):
    Options = namedtuple(
        'Options',[
            'connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'
        ]
    )
    options = Options(
        connection='smart',
        module_path=['/to/mymodule'],
        forks=10,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False
    )
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader,sources=['ansicfg/dhosts.py'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source = dict(
        name = "Ansible Play",
        hosts = servers,
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module=mod, args=arg), register='shell_out'),
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    tqm = None

    try:
        tqm = TaskQueueManager(
            inventory = inventory,
            variable_manager = variable_manager,
            loader = loader,
            options = options,
            passwords = passwords,
        )
        result = tqm.run(play)

    finally:
        if tqm is not None:
            tqm.cleanup()

        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


def tasks(request):
    if request.method == 'POST':
        server = request.POST.get('ip')
        if not server:
            server = request.POST.get('group')

        mod = request.POST.get('mod')
        arg = request.POST.get('arg')
        exec_task(server, mod, arg)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    mods = AnsibleModule.objects.all()

    return render(request, 'mywebansi/tasks.html', {'hosts':hosts, 'groups':groups, 'mods':mods })


def rmarg(request, arg_id):
    a = ModuleArg.objects.get(id=arg_id)
    if a:
        a.delete()

        return redirect(addmodules)


def rmmod(request, mod_id):
    m = AnsibleModule.objects.get(id=mod_id)
    if m:
        m.delete()

        return redirect(addmodules)


def rmhost(request, host_id):
    h = Host.objects.get(id=host_id)
    if h:
        h.delete()

        return redirect(addhosts)


def rmgroup(request, group_id):
    g = HostGroup.objects.get(id=group_id)
    if g:
        g.delete()

        return redirect(addhosts)