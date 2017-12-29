from django.contrib import admin
from solo.admin import SingletonModelAdmin
from nepcore.models import NEPSiteConfig

admin.site.register(NEPSiteConfig, SingletonModelAdmin)
