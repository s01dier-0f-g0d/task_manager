from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Task(models.Model): 
    title = models.CharField(max_length=200) 
    description = models.CharField(max_length=500) 
    # priority = models.CharField(max_length=50) 
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='task')
    estimated_hours = models.IntegerField() 
    progress = models.IntegerField()  # 0-100% 
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title