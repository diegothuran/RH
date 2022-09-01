from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=100, help_text='Nome do Funcionario', verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
