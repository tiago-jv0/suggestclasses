# Generated by Django 3.0.6 on 2020-05-13 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_auto_20200513_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Departamento'),
        ),
    ]
