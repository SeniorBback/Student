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


class Grade(models.Model):
    grade = models.IntegerField(verbose_name='класс')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='профиль', related_name='personalFile')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Annual(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,verbose_name='субьект')
    quarter_1 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_1')
    quarter_2 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_2')
    quarter_3 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_3')
    quarter_4 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_4')
    quarter_final = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='итоговая')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='годовая', related_name='annual')

    class Meta:
        verbose_name = 'Годовая'
        verbose_name_plural = 'Годовые'





class PersonalFile(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='оценка', related_name='grade_value')

    class Meta:
        verbose_name = 'Личное дело'
