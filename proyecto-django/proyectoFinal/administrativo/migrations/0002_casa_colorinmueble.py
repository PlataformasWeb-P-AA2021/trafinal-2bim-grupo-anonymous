# Generated by Django 3.2.4 on 2021-07-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='colorInmueble',
            field=models.CharField(default='N/A', max_length=100, verbose_name='Color del Inmueble'),
            preserve_default=False,
        ),
    ]
