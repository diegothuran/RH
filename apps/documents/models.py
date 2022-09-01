from django.db import models
from apps.employes.models import Employee
class Document(models.Model):
    description = models.CharField(max_length=100, verbose_name="Descricao", help_text='Documento')
    owner = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description
