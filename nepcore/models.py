from django.db import models
from solo.models import SingletonModel
from django.utils import text
from channels.binding.websockets import WebsocketBinding

class NEPPermission(models.Model):
	""" This is a dummy model to register custom permissions """

	class Meta:
		permissions = (
			("test_perm","Test Permission"),
		)

class NEPSiteConfig(SingletonModel):
	site_name = models.CharField(max_length=255, default='Site Name')
	default_view = models.CharField(max_length=255, default='nep_index')
	maintenance_mode = models.BooleanField(default=False)

	@property
	def short_site_name(self):
		short = ""
		for word in self.site_name.split(" "):
			short += word[0]
		return short

	def __unicode__(self):
		return u"Site Configuration"

	class Meta:
		verbose_name = "Site Configuration"
		
#class NEPMenus(SingletonModel()):
#	pass

class NEPMenu(models.Model):
	text = models.CharField(max_length=100)
	state = models.ForeignKey('NEPState', on_delete=models.DO_NOTHING, null=True, blank=True)
	icon = models.CharField(max_length=50, null=True, blank=True)
	link = models.CharField(max_length=150, null=True, blank=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="menus", related_query_name='menu', null=True, blank=True)
	
	def __unicode__(self):
		return self.text
	
	def __str__(self):
		return self.__unicode__()
	
	class Meta:
		verbose_name = "Menu"

# 	def save(self,*args,**kwargs):
# 		if self.state == None:
# 			self.state = 
# 		super(NEPMenu, self).save(*args, **kwargs)
	
class NEPState(models.Model):
	name = models.CharField(max_length=100)
	link = models.CharField(max_length=150)
	url = models.CharField(max_length=100, null=True, blank=True)
	params = models.BooleanField()
	
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.__unicode__()
	
	class Meta:
		verbose_name = "State"
		
		
class NEPMenuBinding(WebsocketBinding):
	model = NEPMenu
	stream = 'menu'
	fields = ['text', 'state', 'icon', 'link']
	
	@classmethod
	def group_names(cls, *args, **kwargs):
		return ['menu-updates']
	
	def has_permission(self, user, action, pk):
		return True

	
	
	
