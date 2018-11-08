from django.contrib import admin
from booktest.models import *


# Register your models here.


# class AreaStackedInline(admin.StackedInline):
#     model = AreaInfo  # 关联子对象
#     extra = 2  # 额外编辑两个子对象


class AreaTabularInline(admin.TabularInline):
    model = AreaInfo  # 关联子对象
    extra = 2  # 额外编辑3个子对象


class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True

    list_display = ["id", "atitle", "title", "parent"]

    list_filter = ["atitle"]

    search_fields = ["atitle"]

    # fields = ["aParent", "atitle"]

    fieldsets = (
        ("基本", {"fields": ["atitle"]}),
        ("高级", {"fields": ["aParent"]})
    )

    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]


admin.site.register(AreaInfo, AreaAdmin)  #
# admin.site.register(AreaInfo)
#
#
# @admin.register(AreaInfo)
# class AreaAdmin(admin.ModelAdmin):
#     pass
