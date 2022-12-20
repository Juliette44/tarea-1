from django.db import models

class Mascota (models.Model):
    nombre= models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} + {self.tipo}"

class Duenio(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f"{self.nombre} + {self.apellido} + {self.edad} + {self.email}"

class Chequeo(models.Model):
    nombre_del_chequeo= models.CharField(max_length=100)
    ultimo_chequeo= models.DateField()
    realizado= models.BooleanField()

    def __str__(self):
        return f"{self.nombre_del_chequeo} + {self.ultimo_chequeo} - {self.realizado}"
    