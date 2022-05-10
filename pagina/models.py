from django.db import models

class Hilo(models.Model):
    titulo = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    contenido = models.TextField()
    comision = models.IntegerField()
    creador = models.CharField(max_length=200)

    def __str__(self):
        return f"[{self.tema}] {self.titulo}"
