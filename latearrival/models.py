from django.db import models
from apprentice.models import Apprentice

# Create your models here.
class LateArrival(models.Model):
    #date_arrival = models.DateField(auto_now_add = True, auto_now=False, editable=False)
    date_arrival = models.DateField() 
    observations = models.CharField(null=True, blank=True, default='NINGUNA', max_length = 60)    
    document_apprentice = models.ForeignKey(
        Apprentice,
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.document_apprentice.full_name +" "+ str(self.date_arrival)