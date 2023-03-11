from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)

def __str__(self):
    return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=255)

def __str__(self):
    return f'{self.name}'


class District(models.Model):
    name = models.CharField(max_length=255)

def __str__(self):
    return f'{self.name}'


class School(models.Model):
    fullname = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

def __str__(self):
    return f'{self.fullname}'

class GoldenCertificate(models.Model):
    # student_fullname = models.OneToOneField(Student, max_length=50, on_delete=models.SET_NULL)
    school_fullname = models.ForeignKey(School, max_length=255, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()
    year = models.IntegerField()

class Olympiad(models.Model):
    # student_fullname = models.ForeignKey(max_length=255)
    school_fullname = models.ForeignKey(School, max_length=255, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()
    year = models.IntegerField()