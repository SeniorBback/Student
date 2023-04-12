from django.contrib import admin
from apps.prof.models import Achievement, AchievementType, Profile, HistoryOfStudy

admin.site.register(AchievementType)
admin.site.register(Achievement)
admin.site.register(Profile)
admin.site.register(HistoryOfStudy)


