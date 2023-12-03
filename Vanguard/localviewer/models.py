from django.db import models

# Create your models here.

class Calendar(models.Model):
    Name = models.CharField(max_length=50)
    
class Event(models.Model):
    Event = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    EventName = models.CharField(max_length=50)
