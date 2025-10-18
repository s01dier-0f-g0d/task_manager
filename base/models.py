from django.db import models

# Create your models here.

class Task(models.Model): 
    title = models.CharField(max_length=200) 
    description = models.CharField(max_length=500) 
    priority = models.CharField(max_length=50) 
    estimated_hours = models.IntegerField() 
    progress = models.IntegerField()  # 0-100% 