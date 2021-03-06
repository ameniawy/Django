from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField(max_length = 20000)

	def get_absolute_url(self):
		return '/%s/' % self.title
