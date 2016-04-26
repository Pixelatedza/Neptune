from django.conf.urls import patterns, url, include
from nepcore import views

urlpatterns = patterns('',

	url(r'^$', views.BaseView.as_view(), name='base'),
	url(r'^index/$', views.IndexView.as_view(), name='index'),
	url(r'^login/$', views.LoginView.as_view(), name='loginv'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logoutv'),
	url(r'^item/', include('item.urls')),
)
