from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    web = models.CharField(max_length=200)
    descripcion = models.TextField()
    comision = models.IntegerField()

    def __str___(self):
        return f"[Profe]{self.nombre} {self.apellido}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    web = models.CharField(max_length=200)
    descripcion = models.TextField()
    comision = models.IntegerField()