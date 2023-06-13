from django.db import models

# Create your models here.

class paciente(models.Model):
    nombre=models.CharField(max_length=80)
    dni=models.CharField(max_length=9)
    usuario=models.CharField(max_length=16)
    password=models.CharField(max_length=16)
    
class medico(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    dni=models.CharField(max_length=9)
    usuario=models.CharField(max_length=16)
    password=models.CharField(max_length=16)
    especialidad=models.CharField(max_length=100)
    
class administrador(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    dni=models.CharField(max_length=9)
    usuario=models.CharField(max_length=16)
    password=models.CharField(max_length=16)
    
class cita(models.Model):
    especialidad=models.CharField(max_length=100)
    dni_paciente=models.CharField(max_length=9)
    nombre_medico=models.CharField(max_length=50)
    dni_medico=models.CharField(max_length=9, default='')
    fecha_hora=models.DateTimeField()
    
class ficha_medica(models.Model):
    nombre_paciente=models.CharField(max_length=50) 
    dni_paciente=models.CharField(max_length=9)
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=10)
    peso=models.IntegerField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=9)
    observaciones=models.CharField(max_length=10000, default='')
    



    
    
    
    