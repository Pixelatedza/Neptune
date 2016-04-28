from django.conf.urls import patterns, url, include
from item import views

urlpatterns = patterns('',
	url(r'^create/item-type/$', views.CreateItemTypeView.as_view(), name='item'),
	url(r'^create/$', views.CreateItemView.as_view(), name='item1'),
)
