from django.contrib import admin
from .models import switchhost
#from .models import Role
# Register your models here.
admin.site.register(switchhost)
class switchhostAdmin(admin.ModelAdmin):
 list_display = ['id','hostname','ipadd']
#ad min.site.register(Role)