from django.db import models

from online_queue.models import Student
from school.models import School


class AchievementType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Тип достижений'
        verbose_name_plural = 'Типы достижений'

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Студент')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Achievement(models.Model):
    type = models.ForeignKey(AchievementType, on_delete=models.SET_NULL, verbose_name='Тип', null=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    date = models.DateField(verbose_name='Дата')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль', related_name='achievement')

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class HistoryOfStudy(models.Model):
    date = models.DateField(verbose_name='Дата')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, verbose_name='Школа', null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name='Профиль', null=True, related_name='history')

    class Meta:
        verbose_name = 'История обучения'
        verbose_name_plural = 'История обучения'

