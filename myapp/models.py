from django.db import models

# Create your models here.
# sample model
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class SignalModel(models.Model):
    description = models.CharField(max_length=100)