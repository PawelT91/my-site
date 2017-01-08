from django.db import models


class Organization(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32, blank=True)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    url = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    activity = models.TextField(verbose_name='Сфера деятельности', blank=True)


class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация', null=True)
    D = models.CharField(verbose_name='Должность', max_length=16)
    ob = models.TextField(verbose_name='Обязанности')
    time_st = models.DateField(verbose_name='Начало работы', max_length=32, blank=True)
    time_end = models.DateField(verbose_name='Конец работы', max_length=32, blank=True)


class Hobby(models.Model):
    name = models.CharField(verbose_name='Хобби', max_length=32)
    url = models.CharField(verbose_name='Картинка', max_length=32)


class StPlace(models.Model):
    name = models.CharField(verbose_name='Университет', max_length=32)
    url = models.CharField(verbose_name='Сайт', max_length=64)
    sp = models.CharField(verbose_name='Специальность', max_length=32)
    Level = models.CharField(verbose_name='Уровень образования', max_length=16, blank=True)
    dip = models.CharField(verbose_name='Тема выпускной работы', max_length=32, blank=True)
    time_st = models.DateField(verbose_name='Начало обучения', max_length=32)
    time_end = models.DateField(verbose_name='Конец обучения', max_length=32)


class Course(models.Model):
    org = models.CharField(verbose_name='Организация', max_length=32, blank=True)
    url = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    sp = models.CharField(verbose_name='Специальность', max_length=32, blank=True)
    Data = models.CharField(verbose_name='Год обучения', max_length=16, blank=True)


class Task(models.Model):
    url_pi = models.CharField(verbose_name='Иконка', max_length=32, blank=True)
    url_text = models.CharField(verbose_name='Задача', max_length=64, blank=True)
    url_sov = models.CharField(verbose_name='Решение', max_length=64, blank=True)
    category = models.CharField(verbose_name='Тип задачи', max_length=16, blank=True)
