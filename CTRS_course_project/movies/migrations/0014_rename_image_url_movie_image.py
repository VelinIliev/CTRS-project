# Generated by Django 4.2.2 on 2023-07-15 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_alter_movie_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image_url',
            new_name='image',
        ),
    ]
