from django.db import models

# Create your models here.
class Task(models.Model):
    taskName = models.CharField(max_length=256)
    dateCreated = models.DateTimeField()
    dateCompleted = models.DateTimeField(blank=True,null=True)