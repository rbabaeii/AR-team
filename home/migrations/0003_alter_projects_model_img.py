# Generated by Django 4.0.1 on 2022-08-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_projects_model_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects_model',
            name='img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='عکس پروژه'),
        ),
    ]
