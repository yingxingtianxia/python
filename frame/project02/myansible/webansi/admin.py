from django.contrib import admin
from .models import Host, HostGroup, AnsibleModule, ModuleArg

# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ipaddr', 'hostgroup')
    list_filter = ('hostgroup',)


class HostGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)


class AnsibleModuleAdmin(admin.ModelAdmin):
    list_display = ('mod_name',)


class ModuleArgAdmin(admin.ModelAdmin):
    list_display = ('arg_text',)


admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup,HostGroupAdmin)
admin.site.register(AnsibleModule, AnsibleModuleAdmin)
admin.site.register(ModuleArg, ModuleArgAdmin)