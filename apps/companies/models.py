from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da empresa', verbose_name='Nome')
    street = models.CharField(max_length=200, verbose_name="Rua", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Cidade", blank=True, null=True)
    state = models.CharField(max_length=500, verbose_name="Estado", blank=True, null=True)
    zipcode = models.CharField(max_length=15, verbose_name="CEP", blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name="País", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
