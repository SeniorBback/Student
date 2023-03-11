from django.db import models

from online_queue.models import Student


class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Область'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class District(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Район'

    def __str__(self):
        return f'{self.name}'


class School(models.Model):
    fullname = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class GoldenCertificate(models.Model):
    student_fullname = models.OneToOneField(Student, max_length=50, on_delete=models.SET_NULL)
    school_fullname = models.ForeignKey(School, max_length=255, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        verbose_name = 'Золотой сертификат'
        verbose_name_plural = 'Золотые сертификаты'


class Olympiad(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, max_length=255)
    school = models.ForeignKey(School, max_length=255, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        verbose_name = 'Олимпиада'
        verbose_name_plural = 'Олимпиады'
