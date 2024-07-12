from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=64)
    edad = models.IntegerField()
    
    def _str_(self):
        return self.nombre