from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da empresa', verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
