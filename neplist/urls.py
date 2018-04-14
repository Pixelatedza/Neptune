from django.conf.urls import url, include
from neplist import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='list'),
	url(r'^worklists$', views.WorklistsView.as_view(), name='worklists'),
	url(r'^checklist/(?P<checklist_pk>\d+)$', views.CheckListView.as_view(), name='check'),
	url(r'^check/save$', views.CheckView.as_view(), name='check'),
]
