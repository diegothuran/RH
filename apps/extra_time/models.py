from django.db import models


class ExtraTime(models.Model):
    reason = models.CharField(max_length=100, verbose_name='Motivo')

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extra'
