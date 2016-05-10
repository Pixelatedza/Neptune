from django.conf.urls import patterns, url, include
from item import views

urlpatterns = patterns('',
	url(r'^create/item-type/$', views.CreateItemTypeView.as_view(), name='item_type_create'),
	url(r'^get/item-type-fields/$', views.ItemTypeFields.as_view(), name='item_type_fields'),
	url(r'^create/(?P<itemName>[\w\- ]+)$', views.CreateItemView.as_view(), name='item_create'),
	url(r'^$', views.ItemView.as_view(), name='item_select'),
)
