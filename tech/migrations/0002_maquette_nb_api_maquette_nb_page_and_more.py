# Generated by Django 4.0.4 on 2022-11-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquette',
            name='nb_api',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maquette',
            name='nb_page',
            field=models.PositiveIntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maquette',
            name='pt_description',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
    ]