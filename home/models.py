from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Projects_model(models.Model):
    title = models.CharField("عنوان پروژه", max_length=50)
    img = models.ImageField('عکس پروژه', blank = True)
    description = models.TextField('شرح پروژه')
    class_id = models.CharField("ایدی جاوااسکریپت" , max_length=20)