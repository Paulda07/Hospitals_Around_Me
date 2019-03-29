

# Create your models here.
from __future__ import unicode_literals

from datetime import datetime



from django.db import models



class Find_Hosp(models.Model):

    title = models.CharField(max_length=200)

    text = models.TextField()



    def __str__(self):

        return self.title
    