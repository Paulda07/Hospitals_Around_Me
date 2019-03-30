

# Create your models here.
from __future__ import unicode_literals

from datetime import datetime



from django.db import models



class Find_Hosp(models.Model):

	latitude = models.FloatField(default = 0)
	longitude = models.FloatField(default = 0)
	name = models.CharField(max_length=200)
	address = models.TextField()
	contact = models.CharField(max_length= 20)


	def __str__(self):

		return self.name
    