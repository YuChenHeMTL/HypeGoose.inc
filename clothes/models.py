from django.db import models

# Create your models here.

class Clothes(models.Model):
    clothesID = models.IntegerField(primary_key = True)
    clotheGenres = models.CharField(max_length=50)
    clotheName = models.CharField(max_length=100)
    def __str__(self):
        return self.clotheName
    
