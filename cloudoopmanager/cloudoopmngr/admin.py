from django.contrib import admin
from cloudoopmngr.models import HD, Host, DataNode

# Register your models here.
admin.site.register(HD)
admin.site.register(Host)
admin.site.register(DataNode)