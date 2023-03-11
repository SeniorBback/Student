from django.db import models


class AchievementType(models.Models):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


class Achievement(models.Models):
    type = models.ForeignKey(AchievementType, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class HistoryOfStudy(models.Models):
    date = models.DateField()
    school = models.ForeignKey(School,on_delete=models.SET_NULL)
    profile = models.ForeignKey(AchievementType, on_delete=models.SET_NULL)



