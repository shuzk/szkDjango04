from django.db import models


# 定义地区模型类，存储省、市、区县信息
class AreaInfo(models.Model):
    atitle = models.CharField("标题", max_length=30)
    # atitle = models.CharField(max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 父级

    # 将方法作为列
    def title(self):
        return self.atitle
    title.admin_order_field = "atitle"

    title.short_description = "区域名称"

    def parent(self):
        if self.aParent is None:
            return ""
        return self.aParent.atitle
    parent.short_description = "父级区域名称"
