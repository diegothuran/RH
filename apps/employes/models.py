from django.db import models
from django.contrib.auth.models import User

from apps.companies.models import Company
from apps.departaments.models import Departament


class Employee(models.Model):

    name = models.CharField(max_length=100, help_text='Nome do Funcionario', verbose_name='Nome')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    street = models.CharField(max_length=200, verbose_name="Rua", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="Cidade", blank=True, null=True)
    state = models.CharField(max_length=500, verbose_name="Estado", blank=True, null=True)
    zipcode = models.CharField(max_length=15, verbose_name="CEP", blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name="País", blank=True, null=True)
    departament = models.ManyToManyField(Departament, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default=None,
                                null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
