# Generated by Django 4.2.2 on 2023-06-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projection', '0002_rename_hall_id_projection_hall_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projection',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, unique=True),
        ),
    ]
