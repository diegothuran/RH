from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=100, verbose_name="Descricao", help_text='Documento')

    def __str__(self):
        return self.description
