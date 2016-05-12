from django.conf.urls import patterns, url, include
from nepauth import views

urlpatterns = patterns('',
	url(r'^$', views.AuthView.as_view(), name='auth'),
)
