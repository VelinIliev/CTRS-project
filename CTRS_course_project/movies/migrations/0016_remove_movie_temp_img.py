# Generated by Django 4.2.2 on 2023-07-16 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_alter_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='temp_img',
        ),
    ]
