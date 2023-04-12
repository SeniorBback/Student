from django.contrib import admin

# Register your models here.

from apps.personal.models import Subject, Annual, Grade, PersonalFile

admin.site.register(Subject)
admin.site.register(Annual)
admin.site.register(Grade)
admin.site.register(PersonalFile)
