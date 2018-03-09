from django.contrib import admin
from solo.admin import SingletonModelAdmin
from nepcore.models import NEPSiteConfig, NEPMenu, NEPState

class NEPMenuInline(admin.StackedInline):
    model = NEPMenu
    extra = 1

@admin.register(NEPMenu)
class NEPMenuAdmin(admin.ModelAdmin):
    list_display = ('text', 'state', 'parent', 'icon', 'link')
    inlines = [NEPMenuInline]

@admin.register(NEPState)
class NEPStateAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'url', 'params')

admin.site.register(NEPSiteConfig, SingletonModelAdmin)