# Generated by Django 3.2 on 2023-02-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionNamber',
            field=models.IntegerField(auto_created=True, unique=True),
        ),
    ]