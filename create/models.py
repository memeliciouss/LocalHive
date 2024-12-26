from django.db import models

#register your model in app's admin.py 
#and then register your app in settings.py in installed apps
#then run makemigrations and migrate
# makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations

# Create your models here.
class Events(models.Model):
    eventName=models.CharField(max_length=64)
    sport=models.CharField(max_length=64)
    location=models.CharField(max_length=128)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.eventName+": "+self.sport