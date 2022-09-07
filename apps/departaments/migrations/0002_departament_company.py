# Generated by Django 4.1 on 2022-09-07 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company_city_company_country_company_state_and_more'),
        ('departaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='companies.company'),
            preserve_default=False,
        ),
    ]
