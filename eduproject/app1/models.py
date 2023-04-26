from django.db import models

class task(models.Model):
    id = models.IntegerField(primary_key=int)
    name = models.CharField(max_length=20)
    task_text = models.CharField(max_length=300)
