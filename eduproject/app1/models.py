from django.db import models

class task(models.Model):
    index = models.IntegerField()
    task = models.CharField(max_length=300)
