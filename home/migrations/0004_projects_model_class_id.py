# Generated by Django 4.0.1 on 2022-08-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_projects_model_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects_model',
            name='class_id',
            field=models.CharField(default='', max_length=20, verbose_name='ایدی جاوااسکریپت'),
            preserve_default=False,
        ),
    ]
