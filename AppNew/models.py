from django.db import models

class mascota (models.Model):
    nombre= models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)

class duenio(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    email= models.EmailField()

class paseo(models.Model):
    ultimo_paseo= models.DateField()
    realizado= models.BooleanField()
    nombre_del_paseo= models.CharField(max_length=100)