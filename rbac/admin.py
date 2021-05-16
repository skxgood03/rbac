from django.contrib import admin

# Register your models here.

from . import models
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(models.Menu,MenuAdmin)
#定制admin
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title','url','name']
    list_editable = ['url','name'] #依赖上一步

admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Role)
admin.site.register(models.UserInfo)