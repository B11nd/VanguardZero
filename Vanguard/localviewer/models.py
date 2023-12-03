from django.db import models

# Create your models here.
    
class fridge(models.Model):
    IngredientName = models.CharField(max_length=50)
    Protein = models.IntegerField()
    Carbs = models.IntegerField()
    Fats = models.IntegerField()
    Complete = models.IntegerField()
    Remaining = models.IntegerField()
    Portion = models.IntegerField()
    Price = models.IntegerField()

#class sensors(models.Model):
#    SensorId = models.AutoField()
#    OwnerId = models.AutoField()
#    type = models.PositiveSmallIntegerField()
#    payload = models.PositiveSmallIntegerField()
#    timestamp = models.DateTimeField()

class sensor(models.Model):
    SensorId = models.BigIntegerField(primary_key=True)
    OwnerId = models.BigIntegerField()
    type = models.SmallIntegerField()
    payload = models.SmallIntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.SensorId)
    
class plates(models.Model):
    PlateName = models.CharField(max_length=50) 
    Ingredients = models.CharField(max_length=50)
    CookingTime = models.IntegerField()
    Type = models.IntegerField()
