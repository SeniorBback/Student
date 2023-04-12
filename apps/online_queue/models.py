from django.db import models
from django.utils import timezone
from apps.school.models import School


class Student(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='фио')
    pin = models.CharField(max_length=255, verbose_name='пин')
    birthdate = models.DateField(verbose_name='дата рождения')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, verbose_name='школа', null=True)
    grade = models.IntegerField(verbose_name='класс')
    father = models.CharField(max_length=255, verbose_name='отец')
    mother = models.CharField(max_length=255, verbose_name='мать')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class StudentPhoto(models.Model):
    photo = models.ImageField(upload_to='student/', verbose_name='фото')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, verbose_name='фото', null=True)

    class Meta:
        verbose_name = 'Фотография студента'
        verbose_name_plural = 'Фотографии студента'


class OnlineQueue(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='школа', related_name='queue')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент')
    sms = models.TextField(verbose_name='смс')

    class Meta:
        verbose_name = 'Онлайн очередь'
        verbose_name_plural = 'Онлайн очередь'


class New(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    text = models.CharField(max_length=255, verbose_name='текст')
    date = models.DateTimeField(verbose_name='дата', default=timezone.now)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewPhoto(models.Model):
    photo = models.ImageField(upload_to='new_photo/', verbose_name='фото')
    news_photo = models.ForeignKey(New, on_delete=models.CASCADE, verbose_name='фото новостей')

    class Meta:
        verbose_name = 'Новое фото'
        verbose_name_plural = 'Новые фото'