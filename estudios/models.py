from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt


class Tema(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, verbose_name="Título")
    sesion = models.SmallIntegerField(verbose_name="Sesión")
    dias_numero = models.CharField(max_length=19, null=True, blank=True, verbose_name="Días número")
    detalles = models.TextField(null=True, blank=True, verbose_name="Detalles")

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.titulo

class F_inicio(models.Model):
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha inicio ciclos")

    class Meta:
        verbose_name = 'Fecha inicio ciclos'
        verbose_name_plural = 'Fecha inicio ciclos'

    def __str__(self):
        return dt.strftime(self.fecha_inicio, "%d-%m-%Y")