from django.db import models


class Departament(models.Model):

    name = models.CharField(max_length=100, help_text='Nome do Departamento', verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
