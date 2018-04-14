from django.contrib import admin
from neplist.models import CheckListTemplate, Cron, CheckList, CheckTemplate, Check

@admin.register(CheckListTemplate)
class CheckListTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Cron)
class CronAdmin(admin.ModelAdmin):
    pass

@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    pass

@admin.register(CheckTemplate)
class CheckTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Check)
class Check(admin.ModelAdmin):
    pass