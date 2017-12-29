from django.db import models
from solo.models import SingletonModel

class NEPPermission(models.Model):
	""" This is a dummy model to register custom permissions """

	class Meta:
		permissions = (
			("test_perm","Test Permission"),
		)

class NEPSiteConfig(SingletonModel):
	site_name = models.CharField(max_length=255, default='Site Name')
	default_view = models.CharField(max_length=255, default='index')
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
