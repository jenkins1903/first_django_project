from django.db import models

# Create your models here.
class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField() 
   description = models.TextField(default='') 
def __str__(self):
        return f"{self.name} ({self.brand}) - {self.count} шт."