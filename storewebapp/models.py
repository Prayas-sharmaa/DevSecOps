from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    role = models.CharField(max_length=10)
    shift = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name} ({self.role})"