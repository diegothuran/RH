from django.db import models
from django.shortcuts import reverse
from apps.employes.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100, verbose_name="Descricao", help_text='Documento')
    owner = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='documents')

    def get_absolute_url(self):
        return reverse('update_employee', args=[self.owner.id])

    def __str__(self):
        return self.description
