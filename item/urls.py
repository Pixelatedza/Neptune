from django.conf.urls import patterns, url, include
from item import views

urlpatterns = patterns('',
	url(r'^$', views.ItemTypeView.as_view(), name='item'),
	url(r'temp/^$', views.ItemView.as_view(), name='item1'),
)
