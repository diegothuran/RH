from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da empresa', verbose_name='Nome')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
