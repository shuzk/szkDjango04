from django.contrib import admin
from booktest.models import *

# Register your models here.


# class AreaAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(AreaInfo, AreaAdmin)
admin.site.register(AreaInfo)


@admin.register(AreaInfo)
class AreaAdmin(admin.ModelAdmin):
    pass
