from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField(max_length =5000)
	upload_date = models.DateTimeField(default = timezone.now)

	def get_absolute_url(self):
		return '/%s/' % self.title

