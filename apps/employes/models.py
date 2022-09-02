from django.db import models
from django.contrib.auth.models import User

from apps.companies.models import Company
from apps.departaments.models import Departament


class Employee(models.Model):

    name = models.CharField(max_length=100, help_text='Nome do Funcionario', verbose_name='Nome')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departament = models.ManyToManyField(Departament, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default=None,
                                null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
