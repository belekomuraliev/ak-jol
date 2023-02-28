# Generated by Django 3.2 on 2023-02-28 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ak_jol_user', '0001_initial'),
        ('pdd', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ak_jol_user.author'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/blog/'),
        ),
    ]