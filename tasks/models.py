from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.TextField()
    status = models.CharField(max_length=30)
    date = models.DateField()