from django.db import models

from online_queue.models import Student
from school.models import School


class GoldenCertificate(models.Model):
    student_fullname = models.OneToOneField(Student, max_length=50, on_delete=models.SET_NULL, null=True)
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
