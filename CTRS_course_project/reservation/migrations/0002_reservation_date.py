# Generated by Django 4.2.2 on 2023-06-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateField(default='2023-06-25'),
            preserve_default=False,
        ),
    ]
