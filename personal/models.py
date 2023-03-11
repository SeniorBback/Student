from django.db import models

from prof.models import Profile


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'


QUARTER_CHOICES = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Annual(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,verbose_name='субьект')
    quarter_1 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_1')
    quarter_2 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_2')
    quarter_3 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_3')
    quarter_4 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_4')
    quarter_final = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='итоговая')

    class Meta:
        verbose_name = 'Годовая'
        verbose_name_plural = 'Годовые'


class Grade(models.Model):
    grade = models.IntegerField(verbose_name='оценка')
    annual = models.ForeignKey(Annual, on_delete=models.CASCADE, verbose_name='годовая')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class PersonalFile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='профиль')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='оценка')

    class Meta:
        verbose_name = 'Личное дело'
        verbose_name_plural = 'Личное дело'
