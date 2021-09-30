from django.db import models
from django.db.models.fields.related import ForeignKey

class User(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        nombre_completo = self.nombres + ' ' + self.apellidos
        return nombre_completo


class PreguntaBeck(models.Model):
    enunciado = models.TextField()
    imagen = models.ImageField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.enunciado

class RespuestaBeck(models.Model):
    pregunta_beck = ForeignKey(PreguntaBeck, on_delete=models.CASCADE)
    respuesta = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField()
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.respuesta)

class ResultadoBeck(models.Model):
    puntaje = models.IntegerField()
    resumen = models.TextField()

    def __str__(self) -> str:
        return self.puntaje



