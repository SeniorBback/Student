from django.db import models

# from online_queue.models import Student


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Область'

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
    longitude = models.IntegerField(verbose_name='долгота', null=True)
    latitude = models.IntegerField(verbose_name='широта',null=True)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
    
    def __str__(self):
        return self.fullname


