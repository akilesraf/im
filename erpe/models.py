import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    cliente_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.cliente_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    
    
 
   


class Informe(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    informe_Producto = models.CharField(max_length=200)
    
    
    Domicilio_Instalacion = models.CharField(max_length=200)
    Emil = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=50)
    Unidades = models.IntegerField(default=0)
    Importe_Sesenta=  models.IntegerField(default=0)
    Importe_Treinta =  models.IntegerField(default=0)
    Importe_diez=  models.IntegerField(default=0)
    Nazani =  models.IntegerField(default=0)
    Importacion = models.IntegerField(default=0)
    Mosquitero = models.IntegerField(default=0)
    Vidrios = models.IntegerField(default=0)
    Albanil = models.IntegerField(default=0)
    Instalacion = models.IntegerField(default=0)
    Extras = models.IntegerField(default=0)
    Total_gastos = models.IntegerField(default=0)
    Beneficios = models.IntegerField(default=0)
    Pendientes = models.IntegerField(default=0), models.CharField(max_length=200)
    def __str__(self):
        return self.informe_Producto




