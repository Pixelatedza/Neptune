from django.db import models

class NEPPermission(models.Model):
	""" This is a dummy model to register custom permissions """

	class Meta:
		permissions = (
			("test_perm","Test Permission"),
		)
