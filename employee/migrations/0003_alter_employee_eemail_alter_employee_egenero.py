# Generated by Django 4.1.7 on 2023-03-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_eapellido_alter_employee_edireccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eemail',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='egenero',
            field=models.CharField(max_length=30),
        ),
    ]
