# Generated by Django 2.1.2 on 2018-12-09 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascensor', '0003_remove_registrocliente_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocliente',
            name='fecha_publicacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
