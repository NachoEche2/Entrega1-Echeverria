# Generated by Django 4.1.2 on 2022-11-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0002_alter_autor_options_alter_pais_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pais",
            name="fechaindependencia",
        ),
        migrations.AddField(
            model_name="pais",
            name="fechaSalida",
            field=models.DateField(null=True),
        ),
    ]