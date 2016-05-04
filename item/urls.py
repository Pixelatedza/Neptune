from django.conf.urls import patterns, url, include
from item import views

urlpatterns = patterns('',
	url(r'^create/item-type/$', views.CreateItemTypeView.as_view(), name='item_type_create'),
	url(r'^create/(?P<itemName>[\w\- ]+)$', views.CreateItemView.as_view(), name='item_create'),
	url(r'^select-type/$', views.SelectItemTypeView.as_view(), name='item_type_select'),
)
