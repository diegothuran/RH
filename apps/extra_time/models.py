from django.db import models
from apps.employes.models import Employee


class ExtraTime(models.Model):
    reason = models.CharField(max_length=100, verbose_name='Motivo')
    employee = models.ForeignKey(Employee, models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extra'
