from django.conf.urls import patterns, url
from nepcore import views

urlpatterns = patterns('',
	url(r'^index/$', views.IndexView.as_view(), name='index'),
	url(r'^hello/$', views.IndexView.as_view(), name='hello'),
	url(r'^child_1/$', views.IndexView.as_view(), name='child_1'),
	url(r'^child_2/$', views.IndexView.as_view(), name='child_2'),
	url(r'^other/$', views.IndexView.as_view(), name='other'),
	url(r'^other_child_2/$', views.IndexView.as_view(), name='other_child_2'),
	url(r'^lvl_1/$', views.IndexView.as_view(), name='lvl_1'),
	url(r'^hello_asset/$', views.IndexView.as_view(), name='hello_asset'),
	url(r'^child_1_asset/$', views.IndexView.as_view(), name='child_1_asset'),
	url(r'^child_2_asset/$', views.IndexView.as_view(), name='child_2_asset'),
	url(r'^other_child_2_asset/$', views.IndexView.as_view(), name='other_child_2_asset'),
)
