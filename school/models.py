from django.db import models

from online_queue.models import Student


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')

    class Meta:
        verbose_name = 'Область'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class District(models.Model):
    name = models.CharField(max_length=255, verbose_name='район')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Район'

    def __str__(self):
        return f'{self.name}'


class School(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='полное имя')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name='регион')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='город')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, verbose_name='район')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class GoldenCertificate(models.Model):
    student_fullname = models.OneToOneField(Student, max_length=50, on_delete=models.SET_NULL, verbose_name='имя студента')
    school_fullname = models.ForeignKey(School, max_length=255, on_delete=models.SET_NULL, null=True, verbose_name='название школы')
    points = models.IntegerField(verbose_name='оценки')
    year = models.IntegerField(verbose_name='год')

    class Meta:
        verbose_name = 'Золотой сертификат'
        verbose_name_plural = 'Золотые сертификаты'


class Olympiad(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, max_length=255, verbose_name='студент')
    school = models.ForeignKey(School, max_length=255, on_delete=models.SET_NULL, null=True, verbose_name='школа')
    points = models.IntegerField(verbose_name='оценки')
    year = models.IntegerField(verbose_name='год')

    class Meta:
        verbose_name = 'Олимпиада'
        verbose_name_plural = 'Олимпиады'
