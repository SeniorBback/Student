from django.db import models


class StudentPhoto(models.Model):
    photo = models.ImageField(upload_to='student/')


class Student(models.Model):
    fullname = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.ForeignKey(StudentPhoto, on_delete=models.SET_NULL)
    school = models.ForeignKey(School, on_delete=models.SET_NULL)
    grade = models.IntegerField()
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)


class OnlineQueue(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sms = models.TextField()
