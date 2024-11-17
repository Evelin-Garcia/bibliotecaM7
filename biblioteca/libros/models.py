import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(10000.99)])
    fecha_p = models.DateField(validators=[MinValueValidator(datetime.date(2000,1,1))])
    
    #Ejecuta validaciones antes de guardar
    def save(self, *arg, **kwargs):
        self.full_clean()
        super().save(*arg, **kwargs)
    
    def __str__(self):
        return self.titulo
    
class Analytics(models.Model):
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField(max_length=5)
    
    class Meta:
        managed = False
        db_table = 'analytics'
        
    def __str__(self):
        return f"{self.categoria} -- {self.cantidad}"