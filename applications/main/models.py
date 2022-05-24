from django.db import models
from applications.product.models import Product


class Student(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=60)
    username = models.CharField(verbose_name='Логин', max_length=30, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=150)

class St_Task(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.PROTECT)
    task = models.ForeignKey(Product, verbose_name='Задача', on_delete=models.PROTECT)
    point = models.SmallIntegerField()
