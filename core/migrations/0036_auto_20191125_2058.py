# Generated by Django 2.2.7 on 2019-11-25 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20191125_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turma',
            old_name='descricao_horário',
            new_name='descricao_horario',
        ),
    ]
