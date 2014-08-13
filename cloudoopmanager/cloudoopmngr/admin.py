from django.contrib import admin
from cloudoopmngr.models import HD, Host, DataNode, Rack

# Register your models here.
admin.site.register(HD)
admin.site.register(Host)
admin.site.register(DataNode)
admin.site.register(Rack)