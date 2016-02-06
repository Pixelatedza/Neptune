from django.conf.urls import patterns, url
from nepcore import views

urlpatterns = patterns('',
	url(r'^index/$', views.IndexView.as_view(), name='index'),
)
