from django.conf.urls import patterns, url, include
from item import views

urlpatterns = patterns('',
	url(r'^$', views.ItemView.as_view(), name='item_select'),
	url(r'^create/item-type/$', views.CreateItemTypeView.as_view(), name='item_type_create'),
	url(r'^get/item-type-fields/$', views.ItemTypeFields.as_view(), name='item_type_fields'),
	url(r'^create/$', views.CreateEditItemView.as_view(), name='item_create_post'),
	url(r'^create/(?P<itemTypePK>[\w\- ]+)$', views.CreateEditItemView.as_view(), name='item_create'),
	url(r'^create/(?P<itemTypePK>[\w\- ]+)/(?P<item>[\w\- ]+)$', views.CreateEditItemView.as_view(), name='item_edit'),
	url(r'^get/item/(?P<itemPK>[\w\- ]+)$', views.GetItemView.as_view(), name='item_get'),
	url(r'^delete/$', views.DeleteItemView.as_view(), name='item_delete'),
	url(r'^list/items/$', views.PagedItemView.as_view(), name='item_list'),
	url(r'^export/items/$', views.ExportItemView.as_view(), name='item_export'),
	url(r'^email/items/$', views.EmailItemView.as_view(), name='item_export'),
)
