# Generated by Django 2.2.7 on 2019-11-26 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20191125_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='descricao_horario',
            field=models.CharField(max_length=150),
        ),
    ]
