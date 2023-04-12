from django.contrib import admin
from apps.online_queue.models import New, NewPhoto, OnlineQueue, StudentPhoto, Student
from django.contrib.admin.options import TabularInline


class StudentPhotoAdminInline(TabularInline):
    extra = 1
    model = StudentPhoto
    max_num = 50


class NewPhotoAdminInline(TabularInline):
    extra = 1
    model = NewPhoto
    max_num = 50


@admin.register(New)
class NewPhotoAdmin(admin.ModelAdmin):
    inlines = (NewPhotoAdminInline, )


@admin.register(Student)
class StudentPhotoAdmin(admin.ModelAdmin):
    inlines = (StudentPhotoAdminInline,)


admin.site.register(OnlineQueue)
