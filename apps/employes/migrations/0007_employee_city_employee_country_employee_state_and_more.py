# Generated by Django 4.1 on 2022-09-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0006_alter_employee_departament'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='País'),
        ),
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='employee',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='employee',
            name='zipcode',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='CEP'),
        ),
    ]
