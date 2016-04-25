from django.conf.urls import patterns, url, include
from item import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='item'),
)
