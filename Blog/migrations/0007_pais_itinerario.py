# Generated by Django 4.1.2 on 2022-11-16 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0006_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="pais",
            name="itinerario",
            field=models.CharField(default=11, max_length=1000),
            preserve_default=False,
        ),
    ]
