from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from asset.api import *

v1_api = Api(api_name='v1')
v1_api.register(DiagnosticMachineResource())
v1_api.register(DesktopComputerResource())
v1_api.register(NoteBookResource())
v1_api.register(PrinterResource())
v1_api.register(StorageResource())
v1_api.register(ServerResource())
v1_api.register(DisplayResource())
v1_api.register(SoftwareResource())
v1_api.register(ComponentResource())
v1_api.register(InputDeviceResource())
v1_api.register(PrinterConResource())
v1_api.register(AccessoryResource())
v1_api.register(NetworkDeviceResource())
v1_api.register(TabletResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'Neptune.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^nepcore/', include('nepcore.urls')),
    url(r'^api/', include(v1_api.urls)),
]
