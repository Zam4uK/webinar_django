# Generated by Django 2.2 on 2022-12-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='blog'),
            preserve_default=False,
        ),
    ]