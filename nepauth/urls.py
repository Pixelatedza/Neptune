from django.conf.urls import patterns, url, include
from nepauth import views

urlpatterns = patterns('',
	url(r'^$', views.AuthView.as_view(), name='auth'),
	url(r'^users/$', views.PagedUserView.as_view(), name='auth_user'),
	url(r'^users/edit/group/$', views.ChangeUserGroupView.as_view(), name='auth_user_edit_group'),
	url(r'^groups/$', views.GetGroupsView.as_view(), name='auth_get_groups'),
)
