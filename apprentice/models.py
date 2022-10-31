from django.db import models
from course.models import Course

# Create your models here.
class Apprentice(models.Model):
    document = models.BigIntegerField(primary_key=True)
    full_name = models.CharField(max_length = 100) 
    email = models.EmailField(max_length = 100, null=True, blank=True)    
    id_course = models.ForeignKey(
        Course,
        on_delete = models.CASCADE,
    )
    
    def __str__(self):
        return self.full_name
