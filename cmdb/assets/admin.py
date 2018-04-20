from django.contrib import admin
from assets.models import Host, Project
from dev.models import Dev_Script
from install.models import Install_List


admin.site.register(Host)
admin.site.register(Project)
admin.site.register(Dev_Script)
admin.site.register(Install_List)