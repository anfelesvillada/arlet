from django.db import models
#from django.urls import reverse

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    career = models.CharField(max_length = 100)    
    
    def __str__(self):
        return self.career

    