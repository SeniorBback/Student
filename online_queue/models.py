from django.db import models

from school.models import School


class StudentPhoto(models.Model):
    photo = models.ImageField(upload_to='student/')

    class Meta:
        verbose_name = 'Фотография студента'
        verbose_name_plural = 'Фотографии студента'


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.ForeignKey(StudentPhoto, on_delete=models.SET_NULL)
    school = models.ForeignKey(School, on_delete=models.SET_NULL)
    grade = models.IntegerField()
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class OnlineQueue(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sms = models.TextField()

    class Meta:
        verbose_name = 'Онлайн очередь'

