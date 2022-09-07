from django.db import models
from apps.companies.models import Company
from django.shortcuts import reverse


class Departament(models.Model):

    name = models.CharField(max_length=100, help_text='Nome do Departamento', verbose_name='Nome')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list_departaments')

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
