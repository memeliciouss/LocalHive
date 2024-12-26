from django.db import models

# Create your models here.
class Events(models.Model):
    eventName=models.CharField(max_length=64)
    sport=models.CharField(max_length=64)
    location=models.CharField(max_length=128)
    desc=models.TextField()
    date=models.DateField()
    eventID=models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.eventName + ": " + self.sport