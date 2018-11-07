from django.contrib import admin
from booktest.models import *

# Register your models here.


class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True

    list_display = ["id", "atitle", "title", "parent"]

    list_filter = ["atitle"]





admin.site.register(AreaInfo, AreaAdmin)
# admin.site.register(AreaInfo)
#
#
# @admin.register(AreaInfo)
# class AreaAdmin(admin.ModelAdmin):
#     pass
